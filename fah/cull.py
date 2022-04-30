import argparse
import sys
import fah.utils as futils


def main():
    ap = argparse.ArgumentParser(
        prog="fah cull",
        description="""
        Read sequence data in fasta format, conditionally remove sequences.
        """,
    )
    ap.add_argument(
        "-m",
        "--min-length",
        type=int,
        default=0,
        help="minimum sequence length to retain, default 0",
    )
    ap.add_argument(
        "-M",
        "--max-length",
        type=int,
        default=False,
        help="maximum sequence length to retain, default no limit",
    )
    ap.add_argument(
        "infile", nargs="?", default=False, help="read from INFILE, default stdin"
    )
    args = ap.parse_args()

    try:
        for seq in futils.fasta_reader(args.infile):
            if len(seq[1]) < args.min_length:
                continue
            if args.max_length and len(seq[1]) > args.max_length:
                continue
            futils.print_as_fasta(header=seq[0], seqtxt=seq[1])
    except Exception as e:
        print("BARF", e)  # TODO
        pass


if __name__ == "__main__":
    ##sys.argv.insert(1, 'cat')
    ##print(sys.argv)
    main()
