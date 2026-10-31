import hashlib
import uuid
import json
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization


def generate_prescription_hash(medications_data):
    """
    Génère un condensat SHA-256 unique à partir des lignes de prescription.
    """
    serialized_data = json.dumps(medications_data, sort_keys=True)
    return hashlib.sha256(serialized_data.encode('utf-8')).hexdigest()


def sign_hash_with_private_key(sha256_hash, private_key_pem):
    """
    Chiffre l'empreinte SHA-256 avec la clé privée du médecin.
    """
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode('utf-8'),
        password=None
    )
    signature = private_key.sign(
        sha256_hash.encode('utf-8'),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return signature.hex()


def verify_signature_with_public_key(sha256_hash, signature_hex, public_key_pem):
    """
    Vérifie la signature numérique à l'aide de la clé publique du médecin.
    """
    try:
        public_key = serialization.load_pem_public_key(public_key_pem.encode('utf-8'))
        public_key.verify(
            bytes.fromhex(signature_hex),
            sha256_hash.encode('utf-8'),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False