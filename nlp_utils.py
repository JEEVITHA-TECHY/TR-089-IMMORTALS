import re

def extract_patient_info(text):
    data = {}

    # Age
    age_match = re.search(r'(\d{2})', text)
    if age_match:
        data['age'] = int(age_match.group(1))

    # Disease
    if "diabetes" in text.lower():
        data['disease'] = "diabetes"
    if "bp" in text.lower() or "hypertension" in text.lower():
        data['bp'] = "high"

    return data