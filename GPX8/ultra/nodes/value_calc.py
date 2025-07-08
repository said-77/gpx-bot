class ValueCalc:
    def __init__(self, logic):
        self.logic = logic

    def evaluate(self):
        # Пример простого подсчёта ценности на основе количества узлов
        return len(self.logic) * 10
