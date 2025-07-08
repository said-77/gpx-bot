class CXVision:
    def __init__(self, goals):
        self.goals = goals

    def extract(self):
        # Имитирует извлечение смысловых блоков на основе целей
        return [{"topic": goal, "weight": 1.0} for goal in self.goals if isinstance(goal, str)]
