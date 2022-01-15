import argparse


def main():
    ap = argparse.ArgumentParser(prog="fah XXX")  # TODO
    ap.add_argument(
        "-o", "--outfile", default=False, help="Output file name, default stdout"
    )
    args = ap.parse_args()

    # TODO now get up and do what needs to be done ...


if __name__ == "__main__":
    main()
