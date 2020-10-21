# fah 1.5.0-dev0.

Helpers for working with files and streams in FASTA format. All read from a file
or stdin and write to stdout. Requires Python 3, Bio.SeqIO, NumPy, heapq.

*   fah cat [ARGS]. Read a fasta file or stream, write to stdout.
*   fah fragger [ARGS]. Read a fasta file or stream, write each fragmented seq
    to stdout.
*   fah longest [ARGS]. Read a fasta file or stream, write the longest sequence
    to stdout.
*   fah random [ARGS]. Generate a stream of random sequences in fasta format.
*   fah select [ARGS]. Read a fasta file or stream, write selected sequences to
    stdout.
*   fah summarize [ARGS]. Read a fasta file or stream, write a summary to
    stdout.
*   fah tidy [ARGS]. Read a fasta file or stream, write a tidy version to
    stdout.
*   fah wc [ARGS]. Read a fasta file or stream, write kmer counts.
*   fah wcontext [ARGS]. Read a fasta file or stream, write sequence flanking a
    specified word.
