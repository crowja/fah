import argparse
import re
import sys
import fah.utils as futils


def main():
    ap = argparse.ArgumentParser(
        prog="fah uniq",
        description="""
        Read sequence data in fasta format, write unique sequences to stdout.
        """,
    )
    ap.add_argument("-p", "--prefix", default="", help="prefix for sequence ids.")
    ap.add_argument(
        "infile", nargs="?", default=False, help="read from INFILE, default stdin"
    )
    args = ap.parse_args()
    prefix = re.sub(r"\s+", "_", args.prefix)
    ##print(f"args.prefix {args.prefix} prefix {prefix}")
    ##exit(0)

    seqs_by_seqtxt = {}

    try:
        for seq in futils.fasta_reader(args.infile):
            seqid, desc = futils.split_header(seq[0])
            seqtxt = seq[1].upper()
            if seqtxt not in seqs_by_seqtxt:
                seqs_by_seqtxt[seqtxt] = set()
            if not seqid:
                seqid = "."
            seqs_by_seqtxt[seqtxt].add(seqid)

        group_counter = 0

        for seqtxt in seqs_by_seqtxt:
            group_counter += 1
            new_desc = ";".join(seqs_by_seqtxt[seqtxt])
            new_header = f"{prefix}{group_counter} ids={new_desc}"
            futils.print_as_fasta(header=new_header, seqtxt=seqtxt)

    except Exception as e:
        print("BARF", e)  # TODO
        pass


if __name__ == "__main__":
    ##sys.argv.insert(1, 'cat')
    ##print(sys.argv)
    main()
