class ReportBuilder:
    @staticmethod
    def build(summary):
        lines = [f"{k}: {v}" for k, v in summary.items()]
        return "\n".join(lines)
