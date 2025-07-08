class EthicalCore:
    @staticmethod
    def evaluate(intent):
        goal = str(intent.get("ЦЕЛЬ", "")).lower()
        if "обман" in goal or "вред" in goal:
            return 0
        return 100
