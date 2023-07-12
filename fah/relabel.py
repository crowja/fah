import argparse
import sys
import fah.utils as futils


def read_seqid_maps(infile):
    maps = {}

    if not infile:
        return maps

    with open(infile, "r") as infh:
        for line in infh:
            text = line.strip()
            if not text or text.startswith("#"):
                continue
            vals = text.split("\t")
            maps[vals[0]] = "_".join(vals[1].split())  # replace ws with single _
    return maps


def main():
    ap = argparse.ArgumentParser(
        prog="fah relabel",
        description="""
        Read sequence data in fasta format, selectively change seqids.
        """,
    )
    ap.add_argument(
        "-M",
        "--seqid-maps",
        default=False,
        help="File with original-to-new seqid maps, tab-separated",
    )
    ap.add_argument(
        "infile", nargs="?", default=False, help="read from INFILE, default stdin"
    )
    args = ap.parse_args()

    maps = read_seqid_maps(args.seqid_maps)

    try:
        for seq in futils.fasta_reader(args.infile):
            seqid, desc = futils.split_header(seq[0])
            h = f"{maps[seqid]} {desc}" if seqid in maps else seq[0]
            futils.print_as_fasta(header=h, seqtxt=seq[1])
    except Exception as e:
        print("BARF", e)  # TODO
        pass


if __name__ == "__main__":
    ##sys.argv.insert(1, 'cat')
    ##print(sys.argv)
    main()
