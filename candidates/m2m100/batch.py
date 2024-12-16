import time
import polars as pl
from tqdm import tqdm

from utils import progressbar


def translate(model, text: str) -> str:
    time.sleep(0.001)
    return "done"

def batch_handler(src_language_df: pl.DataFrame, dst_language: str) -> pl.DataFrame:
    pbar = tqdm(total=len(src_language_df), desc="translation")

    src_language_df.with_columns(
        pl.col("text").map_elements(progressbar.w_pbar(pbar, lambda x: (translate("", x))), return_dtype=pl.String)
    )
