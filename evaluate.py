import os
import json
import argparse

from typing import Dict
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


def main():
    # batch.nllb_batch_handler(["ace"], "deu")

    config = load_settings_json("settings.json")

    print(config)


if __name__ == "__main__":
    main()
