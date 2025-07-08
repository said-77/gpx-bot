class IntentGuard:
    @staticmethod
    def validate(intent):
        text = str(intent.get("ЦЕЛЬ", "")).lower()
        if any(x in text for x in ["убить", "взорвать", "обман", "наркотик"]):
            return False
        return True
