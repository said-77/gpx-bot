class MetaLogicExplainer:
    @staticmethod
    def annotate(logic):
        for node in logic:
            node["explanation"] = "Авто-аннотировано GPX"
        return logic
