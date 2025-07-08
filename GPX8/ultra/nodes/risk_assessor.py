class RiskAssessor:
    def __init__(self, logic):
        self.logic = logic

    def evaluate(self):
        # Имитирует оценку риска: чем больше узлов — тем выше риск
        return min(len(self.logic) * 5, 100)
