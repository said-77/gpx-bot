class AIClassifier:
    def classify(self, intent, logic):
        goal = intent.get("ЦЕЛЬ", "").lower()
        if "анализ" in goal:
            return "Аналитика"
        if "бизнес" in goal:
            return "Бизнес"
        if "обучение" in goal:
            return "Образование"
        return "Общее"
