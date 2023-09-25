import argparse

parser = argparse.ArgumentParser(prog='ProgramName', description='What the program does', epilog='Text at the bottom of help')

parser.add_argument('file', nargs='+')

if __name__ == '__main__':
    args = parser.parse_args()
    for f in args.file:
        print(f)
