import polars as pl


def batch_handler(src_language_df: pl.DataFrame, dst_language: str) -> pl.DataFrame:
    print(src_language_df)
