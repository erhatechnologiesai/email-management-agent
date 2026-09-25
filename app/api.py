from fastapi import FastAPI
from app.config import settings
from app.models import IncomingEmail, TriageResult
from app.services.triage_service import triage_email

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/triage", response_model=TriageResult)
def triage(email: IncomingEmail):
    cat, prio, actions, reply = triage_email(email)
    return TriageResult(
        category=cat,
        priority_level=prio,
        extracted_action_items=actions,
        suggested_reply=reply
    )
