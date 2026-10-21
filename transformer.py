
import argparse


def transform_upper(text):
    """Return the string in uppercase."""
    return text.upper()


def transform_lower(text):
    """Return the string in lowercase."""
    return text.lower()


def get_word_count(text):
    """Return the number of words in the string."""
    return len(text.split())


def filter_short(text, min_length):
    """Return the string if it is longer than min_length; otherwise return None."""
    if len(text) > min_length:
        return text
    else:
        return None


def main():
    """Parse command-line arguments and process the strings."""
    parser = argparse.ArgumentParser(
        description="Transform and filter a list of strings."
    )

    parser.add_argument(
        "--action",
        choices=["upper", "lower", "count", "filter"],
        required=True,
        help="Action to perform: upper, lower, count, or filter"
    )

    parser.add_argument(
        "--data",
        required=True,
        help="Comma-separated strings to process"
    )

    parser.add_argument(
        "--min-length",
        type=int,
        default=3,
        help="Minimum character length for filtering (default: 3)"
    )

    args = parser.parse_args()

    data_list = args.data.split(",")

    for item in data_list:
        text = item.strip()

        if args.action == "upper":
            result = transform_upper(text)

        elif args.action == "lower":
            result = transform_lower(text)

        elif args.action == "count":
            result = get_word_count(text)

        elif args.action == "filter":
            result = filter_short(text, args.min_length)

        if result is not None:
            print(result)


if __name__ == "__main__":
    main()
