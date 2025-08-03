import fitz

def extract_policy_identifier(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    for page in doc:
        text = page.get_text()
        for line in text.split('\n'):
            if "Policy Number:" in line:
                return line.split(":")[1].strip()
    return ""
