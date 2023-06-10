#! /usr/bin/env python3

import argparse
import math
import random
import re
import sys

import fah.utils as futils


def main_shuffle(prefix, args):
    """ Generate random sequences by shuffling input sequences """

    count = 0
    try:
        for seq in futils.fasta_reader(args.infile):
            count += 1
            s = list(seq[1])
            random.shuffle(s)
            ##futils.print_as_fasta(header=seq[0], seqtxt="".join(s))
            print(f">{prefix}{count} {seq[0]}\n{''.join(s)}")
    except Exception as e:
        print("BARF", e)  # TODO
        pass


def main_generate(prefix, args):
    """ Generate de novo random sequences """

    # Character sets for sequence types. Noise symbol X/N needs to be final character.
    charset = {
        "DNA": [c for c in "ACGTN"],
        "PEPTIDE": [c for c in "ACDEFGHIKLMNPQRSTVWYX"],
        "RNA": [c for c in "ACGUN"],
    }

    if args.noise < 0 or args.noise > 100:
        print(
            f"[ERROR] noise percentage needs to be between 0 and 100, specified {args.noise}",
            file=sys.stderr,
        )
        exit(1)

    if args.len < 1:
        print(
            f"[ERROR] target sequence length needs to be greater than 0, specified {args.len}",
            file=sys.stderr,
        )
        exit(1)

    w0 = (100.0 - args.noise) / (len(charset[args.type]) - 1)
    weights = [w0 for _ in range(len(charset[args.type]))]
    weights[-1] = args.noise
    ##print(weights); exit(0)

    if args.seed:
        random.seed(a=args.seed)

    for i in range(args.num):
        if args.rand:
            ##seqlen = max(1, np.random.poisson(args.len))
            z = (random.random() + random.random() + random.random()) / 3  # Bates
            seqlen = max(1, int(2 * args.len * z))
        else:
            seqlen = args.len

        chars = random.choices(charset[args.type], weights=weights, k=seqlen)
        ##chars = np.random.choice(charset[args.type], size=seqlen, p=probs,)
        print(f">{prefix}{i + 1}")
        print(f"{''.join(chars)}")


def main():
    ap = argparse.ArgumentParser(
        description="Generate random sequences in fasta format.",
        epilog="""
        Standard mode generates random sequences de novo, specify SEED to generate
        the same sequences. Shuffle mode (--shuffle) shuffles the characters in an
        input set of sequences; the composition of each input sequence remains the
        same but the character order changes.
        """,
    )
    ap.add_argument("-L", "--label", default=False, help="prefix for the sequence ids")
    ap.add_argument(
        "-l",
        "--len",
        type=int,
        default=100,
        help="mean length of output sequences, default 100",
    )
    ap.add_argument(
        "-n",
        "--num",
        type=int,
        default=1,
        help="number of sequences to generate, default 1",
    )
    ap.add_argument(
        "-N", "--noise", type=float, default=0.0, help="noise percentage, default 0.0"
    )
    ap.add_argument(
        "-r",
        "--rand",
        action="store_true",
        default=False,
        help="sequences have random length with mean LEN",
    )
    ap.add_argument(
        "-s", "--seed", type=int, default=False, help="random number generator seed"
    )
    ap.add_argument(
        "--shuffle",
        action="store_true",
        default=False,
        help="""
        read sequences from a file, print a shuffled version of each, all other
        options except --label are ignored.
        """,
    )
    ap.add_argument(
        "-t",
        "--type",
        choices=["DNA", "RNA", "PEPTIDE"],
        default="DNA",
        help="type of sequence(s) to generate, default DNA",
    )
    ap.add_argument(
        "infile",
        nargs="?",
        default=False,
        help="file to shuffle when using --shuffle, default stdin.",
    )
    args = ap.parse_args()

    prefix = ""
    if args.label:
        tmp = re.sub(r"\W+", "_", args.label.strip())
        if tmp:  # skip if args.label was all whitespace.
            prefix = tmp

    if args.shuffle:
        main_shuffle(prefix, args)
    else:
        main_generate(prefix, args)


if __name__ == "__main__":
    main()
