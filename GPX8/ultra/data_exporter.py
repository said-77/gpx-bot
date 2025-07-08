import io
import pandas as pd

class DataExporter:
    @staticmethod
    def to_excel(data):
        df = pd.DataFrame([data])
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        return output.getvalue()
