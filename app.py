from fastapi import FastAPI, UploadFile
import json
from matcher import match_patient_to_trial
from nlp_utils import extract_patient_info
from voice import voice_to_text

app = FastAPI()

# Load trials
with open("sample_data/trials.json") as f:
    trials = json.load(f)

@app.post("/match/text")
async def match_text(text: str):
    patient = extract_patient_info(text)

    results = []
    for trial in trials:
        score, explanation = match_patient_to_trial(patient, trial)
        results.append({
            "trial": trial["name"],
            "score": score,
            "explanation": explanation
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results

@app.post("/match/voice")
async def match_voice(file: UploadFile):
    with open("temp.wav", "wb") as f:
        f.write(await file.read())

    text = voice_to_text("temp.wav")
    patient = extract_patient_info(text)

    results = []
    for trial in trials:
        score, explanation = match_patient_to_trial(patient, trial)
        results.append({
            "trial": trial["name"],
            "score": score
        })

    return results