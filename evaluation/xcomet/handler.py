import polars as pl
from comet import download_model, load_from_checkpoint

from typing import List


def init_evaluation_model():
    model_path = download_model("Unbabel/wmt22-cometkiwi-da")
    model = load_from_checkpoint(model_path)

    return model

def create_evaluation_data(df: pl.DataFrame) -> List:
    return df.to_dicts()

def evaluate(df: pl.DataFrame) -> pl.DataFrame:
    model = init_evaluation_model()

    data = create_evaluation_data(df)
    model_output = model.predict(data, batch_size=8, gpus=1)
    df = df.with_columns(
        scores=pl.Series(model_output["scores"])
    )

    return df