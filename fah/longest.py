import argparse
import sys
import fah.utils as futils


def main():
    ap = argparse.ArgumentParser(
        prog="fah longest",
        description="""
        Read sequence data in fasta format, write the k longest sequences to stdout.
        """,
    )
    ap.add_argument(
        "-n",
        "--n",
        type=int,
        default=10,
        help="write the N longest sequences to stdout, default 10",
    )
    ap.add_argument(
        "infile", nargs="?", default=False, help="read from INFILE, default stdin"
    )
    args = ap.parse_args()

    pq = futils.PriorityQueue(max_capacity=args.n)

    try:
        for seq in futils.fasta_reader(args.infile):
            pq.put(-len(seq[1]), seq)
    except Exception as e:
        print("BARF", e)  # TODO
        pass

    while pq.len() > 0:
        _, seq = pq.get()
        futils.print_as_fasta(header=seq[0], seqtxt=seq[1])


if __name__ == "__main__":
    ##sys.argv.insert(1, 'cat')
    ##print(sys.argv)
    main()
