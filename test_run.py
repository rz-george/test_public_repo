import argparse

def main():
    parser = argparse.ArgumentParser(description="Hello World Script")

    parser.add_argument("--name", required=True, help="Name parameter")
    parser.add_argument("--message", default="Hello World", help="Message parameter")

    args = parser.parse_args()

    print(f"{args.message}, {args.name}!")

if __name__ == "__main__":
    main()