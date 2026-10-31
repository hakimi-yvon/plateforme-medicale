from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Microservice IA & Temps Réel - Plateforme Médicale",
    version="1.0.0",
    description="Inférence IA pour le pré-diagnostic et alertes d'urgence pour le don de sang"
)

# --- Modèles de données Pydantic ---
class EmergencyAlertRequest(BaseModel):
    hospital_name: str
    blood_group: str
    city: str
    neighborhood: str
    urgency_level: str  # HIGH, CRITICAL

class PreDiagnosisRequest(BaseModel):
    patient_age: int
    gender: str
    symptoms: List[str]


# --- Endpoints FastAPI ---
@app.get("/")
def health_check():
    return {"status": "FastAPI service active", "engine": "Python FastAPI"}


@app.post("/ai/v1/pre-diagnosis/")
def ai_pre_diagnosis(payload: PreDiagnosisRequest):
    """
    Collecte interactive et triage IA des symptômes.
    """
    # Logique simplifiée de démonstration (à relier à un modèle NLP / LLM)
    recommended_specialty = "Médecine Générale"
    urgency = "NORMALE"

    if any(s.lower() in ["douleur poitrine", "difficulté respiratoire", "évanouissement"] for s in payload.symptoms):
        recommended_specialty = "Cardiologie / Urgences"
        urgency = "IMMEDIATE"

    return {
        "urgency_level": urgency,
        "recommended_specialty": recommended_specialty,
        "summary": f"Symptômes analysés pour un patient de {payload.patient_age} ans.",
        "disclaimer": "Cet avis est une aide à l'orientation et ne remplace pas un diagnostic médical."
    }


@app.post("/ai/v1/blood-donation/emergency-alert/", status_code=status.HTTP_200_OK)
def trigger_blood_emergency_alert(payload: EmergencyAlertRequest):
    """
    Déclenche une alerte massive push/SMS vers les donneurs compatibles géolocalisés.
    """
    # En production, ce service interroge la BDD / Redis et pousse les tâches vers Celery
    return {
        "status": "ALERT_DISPATCHED",
        "hospital": payload.hospital_name,
        "target_blood_group": payload.blood_group,
        "location": f"{payload.city}, {payload.neighborhood}",
        "message": f"Alerte critique émise pour le groupe {payload.blood_group}. Notifications diffusées."
    }