import argparse
import sys
import fah.utils as futils


def main():
    ap = argparse.ArgumentParser(
        prog="fah cat",
        description="""
        Read sequence data in fasta format, write to stdout. By default sequences
        are written as a single header line and a single line of sequence text.
        """,
    )
    ap.add_argument(
        "-C",
        "--to-case",
        choices=("upper", "lower"),
        default=False,
        help="force the case of sequence text",
    )
    ap.add_argument(
        "-w",
        "--width",
        type=int,
        default=0,
        help="width of sequence text, default written as a single line",
    )
    ap.add_argument(
        "infile", nargs="?", default=False, help="read from INFILE, default stdin"
    )
    args = ap.parse_args()

    try:
        for seq in futils.fasta_reader(args.infile):
            print(f"***DEBUG IN cat: {seq}")
            if args.to_case == "upper":
                futils.print_as_fasta(
                    header=seq[0], seqtxt=seq[1].upper(), width=args.width
                )
            elif args.to_case == "lower":
                futils.print_as_fasta(
                    header=seq[0], seqtxt=seq[1].lower(), width=args.width
                )
            else:
                futils.print_as_fasta(header=seq[0], seqtxt=seq[1], width=args.width)
    except Exception as e:
        print("BARF", e)  # TODO
        pass


if __name__ == "__main__":
    ##sys.argv.insert(1, 'cat')
    ##print(sys.argv)
    main()
