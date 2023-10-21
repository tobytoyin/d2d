import argparse

from d2d.api import UploaderAPI

parser = argparse.ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)


parser.add_argument("--src")  # source
parser.add_argument("--dst")  # destination
parser.add_argument("--files", nargs="+")  # files from the source

if __name__ == "__main__":
    args = parser.parse_args()
    UploaderAPI(source=args.src, destination=args.dst, files=args.files).upload()
