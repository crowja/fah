import argparse
import re
import sys
import fah.utils as futils

'''
ET217190.1	100	200	+	info about ET217190
seq1	3	5
'''

def read_file_of_ids(infile):
    ids = {}
    if infile:
        with open(infile, "r") as infh:
            for line in infh:
                text = line.strip()
                if not text or line.startswith("#"):
                    continue
                vals = text.split("\t")
                seqid = vals[0]
                if seqid not in ids:
                    ids[seqid] = []
                if len(vals) < 1:
                    continue
                elif len(vals) < 2:
                    start0 = int(vals[0]) ## TODO
                    end0 = -1
                ids[seqid].append(vals[1:-1])
    return ids

def main():
    ap = argparse.ArgumentParser(
        prog="fah select", description="Select sequences by id."
    )
    ap.add_argument(
        "-i",
        "--id",
        action="append",
        help="id of sequence to select, can appear multiple times",
    )
    ap.add_argument(
        "-f",
        "--file",
        default=False,
        help="file with ids of sequences to select, one per line",
    )
    ap.add_argument(
        "infile", nargs="?", default=False, help="read from INFILE, default stdin"
    )
    args = ap.parse_args()

    # Get ids specified in an external file.
    print(f"Reading from {args.file}")
    ids = read_file_of_ids(args.file)
    ##print(ids)


    # Include any ids specified at the command line.
    if args.id:
        ##ids.update(set(args.id))
        pass

    try:
        for seq in futils.fasta_reader(args.infile):
            hh = futils.split_header(seq[0])
            ##print(f"***{hh}***")
            if hh[0] and hh[0] in ids:
                # Figure out what range to use and which strand ...
                futils.print_as_fasta(header=seq[0], seqtxt=seq[1])
    except Exception as e:
        print("BARF", e)  # TODO
        pass


if __name__ == "__main__":
    ##sys.argv.insert(1, 'cat')
    ##print(sys.argv)
    main()

