import os
import polars as pl

DATA_DIR = "data"
SPLITS = {"dev": "dev/*.parquet", "devtest": "devtest/*.parquet"}


def load_data(split: str):
    df = pl.read_parquet("hf://datasets/openlanguagedata/flores_plus/" + SPLITS[split])
    df = df.drop("id")

    for iso_code, language_df in df.group_by("iso_639_3"):
        language_df = language_df.rename(mapping={"text": "src"})
        language_df.write_parquet(
            os.path.join(DATA_DIR, f"{iso_code[0]}_{split}.parquet")
        )


def main():
    load_data("dev")


if __name__ == "__main__":
    main()
