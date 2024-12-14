import argparse

from candidates.nllb import batch

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", type=str, help="")
parser.add_argument("-r", "--reference", type=str, help="")
args = parser.parse_args()


def main():
    batch.nllb_batch_handler(["ace"], "deu")


if __name__ == "__main__":
    main()
