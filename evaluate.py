import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", type=str, help="")
parser.add_argument("-t", "--translation", type=str, help="")
parser.add_argument("-r", "--reference", type=str, help="")
args = parser.parse_args()

def main():
    pass


if __name__ == "__main__":
    main()