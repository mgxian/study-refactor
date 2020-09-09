def score(candidate, medicalExam, scoringGuide):
    Scorer(candidate, medicalExam, scoringGuide).execute()


class Scorer:
    def __init__(self, candidate, medicalExam, scoringGuide):
        self._candidate = candidate
        self._medicalExam = medicalExam
        self._scoringGuide = scoringGuide

    def execute(self):
        result = 0
        healthLevel = 0
        highMedicalRiskFlag = False

        if self.medicalExam.isSmoker:
            healthLevel += 10
            highMedicalRiskFlag = True

        certificationGrade = "regular"
        if self.scoringGuide.stateWithLowCertification(self._candidate.originState):
            certificationGrade = "low"
            result -= 5

        # lots more code like this
        result -= max(healthLevel - 5, 0)
        return result
