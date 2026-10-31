import hmac
import hashlib
import json
from django.core.cache import cache
from django.conf import settings

LOCK_EXPIRE_SECONDS = 300  # Créneau verrouillé pendant 5 minutes


def lock_appointment_slot(doctor_id, slot_datetime):
    """
    Verrouille temporairement un créneau horaire dans Redis pour éviter la double réservation.
    """
    lock_key = f"lock:appointment:{doctor_id}:{slot_datetime}"
    # setnx (set if not exists) via le cache Redis
    is_acquired = cache.add(lock_key, "LOCKED", timeout=LOCK_EXPIRE_SECONDS)
    return is_acquired, lock_key


def release_appointment_slot(lock_key):
    """Libère le verrou Redis en cas d'annulation ou d'échec de paiement."""
    cache.delete(lock_key)


def verify_mobile_money_webhook_signature(payload_bytes, received_signature, secret_key):
    """
    Vérifie l'authenticité de la notification Webhook reçue de l'opérateur Mobile Money (HMAC-SHA256).
    """
    computed_signature = hmac.new(
        secret_key.encode('utf-8'),
        payload_bytes,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(computed_signature, received_signature)