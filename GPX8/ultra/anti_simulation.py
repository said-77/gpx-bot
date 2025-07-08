class AntiSimulation:
    @staticmethod
    def validate(intent):
        goal = intent.get("ЦЕЛЬ", "").lower()
        return "тест" not in goal and "симуляция" not in goal
