class ScenarioBuilder:
    def build(self, intent, logic):
        return {
            "шаг_1": "Подготовка",
            "шаг_2": f"Анализ {len(logic)} элементов",
            "шаг_3": "Генерация результата"
        }
