# fah 1.1.0-dev0

Simple toolkit for working with sequences in fasta format.

## Tools

### `fah cat`

```
fah cat [-h] [-C {upper,lower}] [-w WIDTH] [infile]
```

Read sequence data in fasta format, write to stdout. By default sequences are written
as a single header line and a single line of sequence text.

```
positional arguments:
  infile                read from INFILE, default stdin

options:
  -h, --help            show this help message and exit
  -C {upper,lower}, --to-case {upper,lower}
                        force the case of sequence text
  -w WIDTH, --width WIDTH
                        width of sequence text, default written as a single line
```

### `fah chunkify`

Split sequences into chunks.

```
fah chunkify [-h] [-a] [-s CHUNK_SIZE] [-t TAG] [infile]
```

```
positional arguments:
  infile

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             Write all chunks, including short ones.
  -s CHUNK_SIZE, --chunk-size CHUNK_SIZE
                        Partition a sequence into chunks of size CHUNK_SIZE, default 1000
  -t TAG, --tag TAG     Prefix each new seqid with TAG

```

Split input sequences into chunks of size CHUNK_SIZE. The final chunk might not be
full length; if it's shorter than CHUNK_SIZE/2 it's not printed unless --all is specified.

### `fah cull`

```
fah cull [-h] [-m MIN_LENGTH] [-M MAX_LENGTH] [infile]
```

```
Read sequence data in fasta format, conditionally remove sequences.

positional arguments:
  infile                read from INFILE, default stdin

optional arguments:
  -h, --help            show this help message and exit
  -m MIN_LENGTH, --min-length MIN_LENGTH
                        minimum sequence length to retain, default 0
  -M MAX_LENGTH, --max-length MAX_LENGTH
                        maximum sequence length to retain, default no limit
```

### `fah longest`

```
fah longest [-h] [-n N] [infile]
```

Read sequence data in fasta format, write the N longest sequences to stdout.

```
positional arguments:
  infile       read from INFILE, default stdin

options:
  -h, --help   show this help message and exit
  -n N, --n N  write the N longest sequences to stdout, default 10
```

### `fah random`

```
fah [-h] [-L LABEL] [-l LEN] [-n NUM] [-N NOISE] [-r] [-s SEED] [--shuffle]
           [-t {DNA,RNA,PEPTIDE}]
           [infile]
```

Generate random sequences in fasta format.

```
positional arguments:
  infile                file to shuffle when using --shuffle, default stdin.

optional arguments:
  -h, --help            show this help message and exit
  -L LABEL, --label LABEL
                        prefix for the sequence ids
  -l LEN, --len LEN     mean length of output sequences, default 100
  -n NUM, --num NUM     number of sequences to generate, default 1
  -N NOISE, --noise NOISE
                        noise percentage, default 0.0
  -r, --rand            sequences have random length with mean LEN
  -s SEED, --seed SEED  random number generator seed
  --shuffle             read sequences from a file, print a shuffled version of each,
                        all other options except --label are ignored.
  -t {DNA,RNA,PEPTIDE}, --type {DNA,RNA,PEPTIDE}
                        type of sequence(s) to generate, default DNA
```

Standard mode generates random sequences de novo, specify SEED to generate the same
sequences. Shuffle mode (--shuffle) shuffles the characters in an input set of
sequences; the composition of each input sequence remains the same but the character
order changes.

### `fah relabel`

```
fah relabel [-h] [-M SEQID_MAPS] [infile]
```

Read sequence data in fasta format, selectively change seqids.

```
positional arguments:
  infile                read from INFILE, default stdin

optional arguments:
  -h, --help            show this help message and exit
  -M SEQID_MAPS, --seqid-maps SEQID_MAPS
                        File with original-to-new seqid maps, tab-separated
```

### `fah select`

```
fah select [-h] [-i ID] [-f FILE] [infile]
```

Select sequences by id.

```
positional arguments:
  infile                read from INFILE, default stdin

options:
  -h, --help            show this help message and exit
  -i ID, --id ID        id of sequence to select, can appear multiple times
  -f FILE, --file FILE  file with ids of sequences to select, one per line
```

### `fah uniq`

```
fah uniq [-h] [-p PREFIX] [infile]
```

Read sequence data in fasta format, write unique sequences to stdout.

```
positional arguments:
  infile                read from INFILE, default stdin

optional arguments:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        prefix for sequence ids
```

## Installing

```
python -m pip install git+https://github.com/crowja/fah.git
```
