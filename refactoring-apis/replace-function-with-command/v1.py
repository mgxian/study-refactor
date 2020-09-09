def score(candidate, medicalExam, scoringGuide):
    result = 0
    healthLevel = 0
    highMedicalRiskFlag = False

    if medicalExam.isSmoker:
        healthLevel += 10
        highMedicalRiskFlag = True

    certificationGrade = "regular"
    if scoringGuide.stateWithLowCertification(candidate.originState):
        certificationGrade = "low"
        result -= 5

    # lots more code like this
    result -= max(healthLevel - 5, 0)
    return result
