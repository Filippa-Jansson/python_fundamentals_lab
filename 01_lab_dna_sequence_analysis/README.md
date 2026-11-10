# DNA Sequence Analysis

A Python notebook that reads raw DNA sequence data, counts how often each DNA letter appears in every sequence and visualizes the result. Built as part of the Python programming course in the Data Engineering program at STI.

## Background

DNA can be written as a sequence of four letters: A (adenine), T (thymine), C (cytosine) and G (guanine). Counting letter frequencies is an early step in processing genetic data. The data in this lab is a simplified version of real sequence data.

## Input format

`dna_raw.txt` contains several sequences. Each sequence takes two lines: an ID starting with `>` and the sequence itself, in mixed upper and lower case.

```
>seq1
cGTAaccaataaaaaaacaagcttaacctaattc
```

## What the notebook does

1. Reads the file and pairs each ID with its sequence
2. Cleans the data by removing the `>` sign and newlines and converting all letters to uppercase
3. Counts each letter per sequence with a dictionary
4. Plots one bar chart per sequence, with the letters in the same order for easy comparison

Example output:

```
seq1: {'C': 8, 'G': 2, 'T': 7, 'A': 17}
```

Sequence 3 also contains the letter `N`, which is used in DNA data for a base that could not be identified. The notebook counts it like any other letter.

## How to run

Requires Python 3 and matplotlib.

```bash
pip install matplotlib
```

Open `dna_analysis.ipynb` in VS Code or Jupyter and run all cells.

## Possible improvements

- Wrap the logic in a reusable function that takes any file path
- Support sequences that are split over multiple lines