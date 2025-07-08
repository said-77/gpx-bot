class NameGenerator:
    def suggest(self, intent, logic):
        base = str(intent.get("ЦЕЛЬ", "Идея")).split()[0]
        return f"GPX-{base[:8].upper()}-{len(logic)}"
