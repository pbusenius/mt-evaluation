import polars as pl

from typing import List
from utils import dataset

def nllb_batch_handler(src_languages: List[str], dst_language: str) -> pl.DataFrame:
    for src_language in src_languages:
        src_df = dataset.load_language(src_language)

        print(src_df)