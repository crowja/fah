import argparse
import re
import sys

import fah.utils as futils


def print_chunks(args):

    count = 0
    width = args.chunk_size

    try:
        for seq in futils.fasta_reader(args.infile):
            seqid, desc = futils.split_header(seq[0])
            seqlen = len(seq[1])
            if seqlen == 0:
                continue
            for start0 in range(0, seqlen, width):
                end0 = min(start0 + width, seqlen)
                if end0 - start0 < width / 2 and not args.all:
                    break
                count += 1
                new_seqid = f"{args.tag}chunk{count}"
                if seqid:
                    new_desc = f'src="{seqid}" start0="{start0}" end0="{end0}" {desc}'
                else:
                    new_desc = desc

                futils.print_as_fasta(
                    header=f"{new_seqid} {new_desc}", seqtxt=seq[1][start0:end0]
                )

    except Exception as e:
        print("BARF", e)  # TODO
        pass


"""
        if seqtxt:
            print(f">{header}", file=outfh)
            for chunk in [seqtxt[i : i + width] for i in range(0, len(seqtxt), width)]:
                print(chunk, file=outfh)
"""


def main():
    ap = argparse.ArgumentParser(
        prog="fah chunkify",
        epilog="""
            Split input sequences into chunks of size CHUNK_SIZE. The final chunk might
            not be full length; if it's shorter than CHUNK_SIZE/2 it's not printed unless
            --all is specified.
            """,
    )
    ap.add_argument(
        "-a",
        "--all",
        default=False,
        action="store_true",
        help="Write all chunks, including short ones.",
    )
    ap.add_argument(
        "-s",
        "--chunk-size",
        type=int,
        default=1000,
        help="Partition a sequence into chunks of size CHUNK_SIZE, default 1000",
    )
    ap.add_argument("-t", "--tag", default="", help="Prefix each new seqid with TAG")
    ap.add_argument("infile", nargs="?", default=False)

    args = ap.parse_args()
    args.tag = args.tag.replace(" ", "")

    print_chunks(args)


if __name__ == "__main__":
    main()
