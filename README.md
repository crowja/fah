# fah 1.0.1-dev0

Simple toolkit for working with sequences in fasta format.

```
fah cat [-h] [-C {upper,lower}] [-w WIDTH] [infile]
```

Read sequence data in fasta format, write to stdout. By default sequences are written as a single
header line and a single line of sequence text.

```
fah longest [-h] [-n N] [infile]
```

Read sequence data in fasta format, write the N longest sequences to stdout.

```
fah select [-h] [-i ID] [-f FILE] [infile]
```

Select sequences by id.


