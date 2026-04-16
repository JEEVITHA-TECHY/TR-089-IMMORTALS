def match_patient_to_trial(patient, trial):
    score = 0
    total = 0
    explanation = []

    # Inclusion check
    for rule in trial["inclusion"]:
        total += 1
        if rule == "diabetes" and patient.get("disease") == "diabetes":
            score += 1
            explanation.append(f"{rule} → matched")
        else:
            explanation.append(f"{rule} → not matched")

    # Exclusion check
    for rule in trial["exclusion"]:
        total += 1
        if rule == "heart":
            if patient.get("heart") == True:
                explanation.append("heart → excluded ❌")
                return 0, explanation
            else:
                score += 1

    return score / total, explanation