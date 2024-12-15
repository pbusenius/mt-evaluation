import os
import json
import argparse
import polars as pl

from utils import dataset
from typing import Dict, List
from candidates.nllb import batch

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", type=str, help="")
parser.add_argument("-r", "--reference", type=str, help="")
args = parser.parse_args()


def load_settings_json(file: str) -> Dict:
    if not os.path.exists(file):
        return {}

    with open(file) as config_file:
        config = json.load(config_file)

    return config


def load_source_language_data(language_codes: List[str]) -> pl.DataFrame:
    src_dataframes = []
    for src_language in language_codes:
        tmp_df = dataset.load_language(src_language)
        src_dataframes.append(tmp_df)
    
    return pl.concat(src_dataframes)


def main():
    # batch.nllb_batch_handler(["ace"], "deu")

    config = load_settings_json("settings.json")

    src_language_df = load_source_language_data(config["source_languages"])
    dst_language_df = dataset.load_language(config["destination_language"])

    print(src_language_df)
    print(dst_language_df)


if __name__ == "__main__":
    main()
