import requests
from app.core.config import settings

def fetch_policy_text(policy_id: str) -> str:
    response = requests.get(f"{settings.POLICY_API_URL}?policy_id={policy_id}")
    response.raise_for_status()
    return response.json().get("policy_text", "")
