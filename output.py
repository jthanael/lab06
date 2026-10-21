import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--Output", help="Show output message")
parser.add_argument("-d", "--date", help="Show current date")
args = parser.parse_args()

if args.Output:
    print("Output:", args.Output)

if args.date:
    print("Current date:", args.date)