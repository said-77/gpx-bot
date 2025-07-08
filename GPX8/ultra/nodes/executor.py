class Executor:
    def __init__(self, context, logic, value, risk, interpreted):
        self.context = context
        self.logic = logic
        self.value = value
        self.risk = risk
        self.intent = interpreted

    def finalize(self):
        summary = {
            "intent_id": self.intent.get("INTENT_ID", "unknown"),
            "logic_nodes": len(self.logic),
            "value_score": self.value,
            "risk_score": self.risk,
            "goals": self.intent.get("ЦЕЛЬ", "(не указано)"),
        }
        return {
            "summary": summary,
            "result": f"Решение построено из {len(self.logic)} узлов с оценкой {self.value}"
        }
