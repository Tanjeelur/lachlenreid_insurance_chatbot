import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

def call_gpt(user_query: str, policy_text: str) -> dict:
    prompt = f"""User Query: {user_query}
Policy Document:
{policy_text}

Return a JSON like:
{{
  "verdict": "Likely | Highly Unlikely | etc.",
  "score": 0–100,
  "explanation": "Short explanation"
}}"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    output = response['choices'][0]['message']['content']
    return eval(output)
