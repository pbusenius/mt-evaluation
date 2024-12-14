import os
import polars as pl

DATA_DIR = "data"

def load_language(iso_code: str, split: str = "dev") -> pl.DataFrame:
    language_file = os.path.join(DATA_DIR, f"{iso_code}_{split}.parquet")

    if not os.path.exists(language_file):
        return pl.DataFrame()

    df = pl.read_parquet(language_file)

    return df