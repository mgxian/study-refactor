def score(candidate, medicalExam, scoringGuide):
    Scorer(candidate, medicalExam, scoringGuide).execute()


class Scorer:
    def __init__(self, candidate, medicalExam, scoringGuide):
        self._candidate = candidate
        self._medicalExam = medicalExam
        self._scoringGuide = scoringGuide

    def execute(self):
        self.result = 0
        self.healthLevel = 0
        self.highMedicalRiskFlag = False

        self.scoreSmoking()
        certificationGrade = "regular"
        if self.scoringGuide.stateWithLowCertification(self._candidate.originState):
            certificationGrade = "low"
            self.result -= 5

        # lots more code like this
        self.result -= max(self.healthLevel - 5, 0)
        return self.result

    def scoreSmoking(self):
        if self.medicalExam.isSmoker:
            self.healthLevel += 10
            self.highMedicalRiskFlag = True
