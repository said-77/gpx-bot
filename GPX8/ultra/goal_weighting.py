class GoalWeighting:
    def __init__(self, interpreted):
        self.goals = interpreted.get("goals", [])

    def apply(self):
        return [{"goal": g, "weight": 1.0} for g in self.goals]
