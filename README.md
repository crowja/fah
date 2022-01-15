# fah 1.0.1-dev0

Simple toolkit for working with sequences in fasta format.

### `fah cat`

```
fah cat [-h] [-C {upper,lower}] [-w WIDTH] [infile]
```

Read sequence data in fasta format, write to stdout. By default sequences are written as a single
header line and a single line of sequence text.

    positional arguments:
      infile                read from INFILE, default stdin

    options:
      -h, --help            show this help message and exit
      -C {upper,lower}, --to-case {upper,lower}
                            force the case of sequence text
      -w WIDTH, --width WIDTH
                            width of sequence text, default written as a single line

### `fah longest`

```
fah longest [-h] [-n N] [infile]
```

Read sequence data in fasta format, write the N longest sequences to stdout.

    positional arguments:
      infile       read from INFILE, default stdin

    options:
      -h, --help   show this help message and exit
      -n N, --n N  write the N longest sequences to stdout, default 10


### `fah select`

```
fah select [-h] [-i ID] [-f FILE] [infile]
```

Select sequences by id.

    positional arguments:
      infile                read from INFILE, default stdin

    options:
      -h, --help            show this help message and exit
      -i ID, --id ID        id of sequence to select, can appear multiple times
      -f FILE, --file FILE  file with ids of sequences to select, one per line




