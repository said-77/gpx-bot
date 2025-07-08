class IntentAnalytics:
    _log = []

    @staticmethod
    def track(intent):
        IntentAnalytics._log.append(intent)

    @staticmethod
    def get_stats():
        return {"total": len(IntentAnalytics._log)}
