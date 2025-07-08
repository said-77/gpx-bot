class FilterSimulation:
    def __init__(self, nodes):
        self.nodes = nodes

    def apply(self):
        # Удаляет фейковые или неполные элементы
        return [n for n in self.nodes if isinstance(n, dict) and "topic" in n]
