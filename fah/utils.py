#! /usr/bin/env python3

import re
import sys

# Have a look at https://www.programiz.com/python-programming/generator to see a few examples.

# Also for the ransom option https://www.geeksforgeeks.org/python-random-uppercase-in-strings/#:~:text=Method%20%231%20%3A%20Using%20join%20%28%29%20%2B%20choice,perform%20task%20of%20uppercasing%20and%20lowercasing%20characters%20respectively.


class FastaReader:
    def __init__(self, infile=False):
        self.infile = infile


class PriorityQueue:
    def __init__(self, max_capacity=0):
        self.max_capacity = max_capacity
        self.sorted_list = []

    def len(self):
        return len(self.sorted_list)

    def get(self):
        if self.len() > 0:
            return self.sorted_list.pop(0)
        else:
            raise queue.Empty("fah.util.PriorityQueue is empty")

    def put(self, priority, item=False):
        if item:
            self.sorted_list.append((priority, item))
            self.sorted_list.sort(key=lambda x: x[0])
            if self.max_capacity > 0 and len(self.sorted_list) == self.max_capacity:
                self.sorted_list.pop()


def fasta_reader(infile=False):
    header = ""
    seqtxt = ""
    state = "AT_START"

    with open(infile, "r") if infile else sys.stdin as infh:
        for line in infh:
            text = line.strip()

            if not text:
                continue

            if state == "AT_START":
                if text.startswith(">"):
                    header = re.sub(r"^[>\s]+", "", text)
                    seqtext = ""
                    state = "IN_HEADER"
                else:
                    seqtxt = re.sub(r"\s", "", text)
                    state = "IN_SEQTEXT"

            elif state == "IN_HEADER":
                if text.startswith(">"):
                    yield header, seqtxt
                    header = re.sub(r"^[>\s]+", "", text)
                    seqtxt = ""
                else:
                    seqtxt = seqtxt + re.sub(r"\s", "", text)
                    state = "IN_SEQTEXT"

            elif state == "IN_SEQTEXT":
                if text.startswith(">"):
                    yield header, seqtxt
                    header = re.sub(r"^[>\s]+", "", text)
                    seqtxt = ""
                    state = "IN_HEADER"
                else:
                    seqtxt = seqtxt + re.sub(r"\s", "", text)
            else:
                pass

    if header or seqtxt:
        yield header, seqtxt


def print_as_fasta(outfh=sys.stdout, header=False, seqtxt=False, width=0):
    if width < 1:
        if seqtxt:
            print(f">{header}\n{seqtxt}", file=outfh)
        else:
            print(f">{header}", file=outfh)
    else:
        if seqtxt:
            print(f">{header}", file=outfh)
            for chunk in [seqtxt[i : i + width] for i in range(0, len(seqtxt), width)]:
                print(chunk, file=outfh)
        else:
            print(f">{header}", file=outfh)


def split_header(h):
    # Splits a valid header line into id and description.
    return re.split(r"\s+", h, maxsplit=1)


if __name__ == "__main__":
    """
    for x in fasta_reader("test.fa"):
        print(x)
    """

    pq = PriorityQueue(max_capacity=4)
    pq.put(3, "cat")
    pq.put(4, "dog")
    pq.put(1, "ant")
    pq.put(5, "ent")
    pq.put(8, "hap")
    pq.put(2, "bee")
    pq.put(6, "fly")
    pq.put(7, "gad")
    while pq.len() > 0:
        priority, animal = pq.get()
        print(f"{priority} --> {animal}")
