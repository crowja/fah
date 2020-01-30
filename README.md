# fah 1.1.0-dev0.

Helpers for working with files and streams in FASTA format. All read from a file
or stdin and write to stdout. Requires Python 3, Bio.SeqIO, NumPy, heapq.

*   fah cat. Write the input to stdout. All internal newlines removed from the
    sequence.
*   fah fragger. Randomly fragment the input. Specify the average fragment size
    and coverage.
*   fah longest. Write the N longest sequences from the input.
*   fah select. Write a specified set of of sequences to stdout.
*   fah summarize. Summary statistics of the input.
*   fah tidy. Tidy the input.
