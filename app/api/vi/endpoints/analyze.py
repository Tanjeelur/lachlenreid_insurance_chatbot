from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from app.services.pdf_parser import extract_policy_identifier
from app.services.policy_client import fetch_policy_text
from app.core.gpt_service import call_gpt
from app.utils.file_utils import save_temp_file, delete_file

router = APIRouter()

@router.post("/")
async def analyze(user_query: str = Form(...), file: UploadFile = File(...)):
    file_path = save_temp_file(file)

    try:
        policy_id = extract_policy_identifier(file_path)
        if not policy_id:
            return JSONResponse({"error": "Policy ID not found"}, status_code=400)

        policy_text = fetch_policy_text(policy_id)
        result = call_gpt(user_query, policy_text)
        return result

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

    finally:
        delete_file(file_path)
