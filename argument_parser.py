#we can copy file from source to destination
import argparse
import shutil


parser = argparse.ArgumentParser()
parser.add_argument('source', help="source file path")
parser.add_argument('desti', help="show verbose output")
args = parser.parse_args()

print(f"Copying {args.source} to {args.desti}")
shutil.copy2(args.source, args.desti)
