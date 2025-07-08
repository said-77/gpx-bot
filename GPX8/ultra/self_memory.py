class SelfMemory:
    _memory = []

    @staticmethod
    def log_intent(intent):
        SelfMemory._memory.append(intent)
        if len(SelfMemory._memory) > 5:
            SelfMemory._memory.pop(0)

    @staticmethod
    def recall():
        return SelfMemory._memory
