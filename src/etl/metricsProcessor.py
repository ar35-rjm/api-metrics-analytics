import pandas as pd
import json

class MetricsProcessor:
    def __init__(self, log_path: str = "data/metrics.log"):
        self.log_path = log_path

    def process_and_clean(self) -> pd.DataFrame:
        records = []
        with open(self.log_path, "r") as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line.strip()))
        
        df = pd.DataFrame(records)
        
        df["is_error"] = df["status_code"].apply(lambda x: 1 if x >= 400 else 0)
        return df

    def calculate_kpis(self, df: pd.DataFrame):
        summary = df.groupby(["path", "method"]).agg(
            avg_latency_ms=("latency_ms", "mean"),
            total_requests=("latency_ms", "count"),
            error_count=("is_error", "sum")
        ).reset_index()
        
        return summary