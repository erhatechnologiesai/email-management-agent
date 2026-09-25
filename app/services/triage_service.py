def triage_email(email):
    text = (email.subject + " " + email.body).lower()
    
    if any(w in text for w in ["invoice", "payment", "charge", "refund", "receipt"]):
        cat = "BILLING"
        prio = "P2_MEDIUM"
        reply = "Thank you for contacting Erha Billing. We are reviewing your payment ledger and will follow up shortly."
    elif any(w in text for w in ["down", "outage", "broken", "critical", "error 500"]):
        cat = "URGENT_SUPPORT"
        prio = "P1_HIGH"
        reply = "Our Site Reliability Engineering team has been alerted to your incident report. We are actively investigating."
    elif any(w in text for w in ["demo", "pricing", "hire", "consulting", "enterprise"]):
        cat = "SALES_INQUIRY"
        prio = "P1_HIGH"
        reply = "Thank you for your interest in Erha AI solutions! Our enterprise team would love to schedule a demo call."
    else:
        cat = "GENERAL"
        prio = "P3_LOW"
        reply = "Thank you for reaching out to Erha Technologies. We have received your message and will respond within 24 hours."

    actions = [f"Follow up with {email.sender}", f"Log {cat} ticket in CRM"]
    return cat, prio, actions, reply
