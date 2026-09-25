from pydantic import BaseModel
from typing import List, Optional

class IncomingEmail(BaseModel):
    sender: str
    subject: str
    body: str

class TriageResult(BaseModel):
    category: str # URGENT_SUPPORT, SALES_INQUIRY, BILLING, GENERAL
    priority_level: str # P1_HIGH, P2_MEDIUM, P3_LOW
    extracted_action_items: List[str]
    suggested_reply: str
