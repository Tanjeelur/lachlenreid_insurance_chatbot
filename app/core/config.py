import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    POLICY_API_URL: str = os.getenv("POLICY_API_URL")

settings = Settings()
