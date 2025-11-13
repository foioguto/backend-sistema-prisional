import pandas as pd

def read_csv(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path, sep=",", encoding="utf-8")
    
    except Exception as e:
        print(f"Error to read the archive {path}: {e}")
        return pd.DataFrame()
    