import sys


def usage():
    print(f"Usage: {sys.argv[0]} [N]", file=sys.stderr)


def sequence_length():
    if len(sys.argv) > 2:
        usage()
        sys.exit(1)
    elif len(sys.argv) == 1:
        return 10
    else:
        try:
            n = int(sys.argv[1])
            if n <= 0:
                usage()
                sys.exit(1)
            return n
        except ValueError:
            usage()
            raise


def main() -> None:
    print(f"n = {sequence_length()}")


if __name__ == "__main__":
    main()
