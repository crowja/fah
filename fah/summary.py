import argparse
import sys
import fah.utils as futils


def simple_stats(x):
    """
    Compute summary stats n, mean, min, max
    lens is expected to have already been sorted in acending order.
    """

    if len(x) == 0:  # quick return
        return 0, 0.0, 0.0, 0.0

    longest = -sys.float_info.max
    shortest = sys.float_info.max
    s = 0.0
    for i in range(len(x)):
        s += x[i]
        longest = max(longest, x[i])
        shortest = min(shortest, x[i])

    return (len(x), s / len(x), shortest, longest)


def npctlen(lens, pct=50):
    """
    lens is expected to have already been sorted in acending order.
    """

    if pct <= 0.0 or pct >= 100.0:
        raise ValueError("fah.summary invalid percentage specified")

    # Figure out the total number of characters.
    s_all = 0
    for i in range(len(lens)):
        s_all += lens[i]

    # Now figure out where the percentile lies.
    if len(lens) == 0:  # quick return
        return 0
    if len(lens) == 1:  # quick return
        return lens[0]
    s = 0
    for i in range(len(lens)):
        s += lens[i]
        if s > s_all * pct / 100.0:
            return (lens[i] + lens[i - 1]) / 2
    print("DEBUG2")
    return lens[-1]


def main():
    ap = argparse.ArgumentParser(
        prog="fah summary",
        description="""
        Write a summary of an input fasta file/stream to stdout.
        """,
    )
    ap.add_argument(
        "-S",
        "--sizes",
        default=False,
        action="store_true",
        help="write seqid and size to stdout",
    )
    ap.add_argument(
        "infile", nargs="?", default=False, help="read from INFILE, default stdin"
    )
    args = ap.parse_args()

    total_seqs = 0
    total_chars = 0
    lens = []

    try:
        for seq in futils.fasta_reader(args.infile):
            ##print(f"***DEBUG IN cat: {seq}")
            if args.sizes:
                id, _ = futils.split_header(seq[0])
                if id:
                    print(f"{id}\t{len(seq[1])}")
            else:
                l = len(seq[1])
                total_seqs += 1
                total_chars += l
                if l > 0:
                    lens.append(l)

    except Exception as e:
        print("BARF", e)  # TODO
        pass

    lens.sort()
    count, mean, shortest, longest = simple_stats(lens)
    print(f"total-seqs\t{total_seqs}")
    print(f"total-seqs-nonzero\t{count}")
    print(f"total-seqs-zero\t{total_seqs - count}")
    print(f"longest\t{longest}")
    print(f"shortest-nonzero\t{shortest}")
    print(f"total-chars\t{total_chars}")

    n = min(10, len(lens))
    longest_lens = [lens[len(lens) - 1 - i] for i in range(n)]
    tmp = "\t".join([str(x) for x in longest_lens])
    print(f"longest\t{tmp}")
    print(f"n50\t{npctlen(lens, pct=50)}")
    print(f"n80\t{npctlen(lens, pct=80)}")


if __name__ == "__main__":
    ##sys.argv.insert(1, 'cat')
    ##print(sys.argv)
    main()
