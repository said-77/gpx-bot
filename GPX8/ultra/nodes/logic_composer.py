class LogicComposer:
    def __init__(self, nodes):
        self.nodes = nodes

    def compose(self):
        # Имитирует сборку логической структуры из узлов
        logic = []
        for i, node in enumerate(self.nodes):
            logic.append({
                "id": f"logic_{i}",
                "data": node,
                "link": f"next_{i+1}" if i + 1 < len(self.nodes) else None
            })
        return logic
