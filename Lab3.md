# Session 3 - Alignments of mitochondrial sequences

## Introduction / Background information to Session 3

In this session, you will focus on alignments. As you have seen in the lecture, you can align two sequences (pairwise alignment) or multiple sequences (multiple alignments). You will align your COX1 and CytB sequences using multiple alignments. Obtaining a good alignment of your sequences will be essential for answering your groups question.

## Goals
  + Perform multiple alignments and visualize them
  + Manipulate files

## Input(s)

  + COX1 sequences
  + cytB sequences

## Output(s)

  + An alignment of Cox1 sequences
  + An alignment of cytB sequences

## Tools
  + Alignment program: [mafft](https://mafft.cbrc.jp/alignment/software/)
  + Alignment visualization program: AliView

## Steps
 Multiple alignment exercise and visualisation

## Multiple alignments

You will now be working with the sequences you have collected last time. This also means that the results will depend on your selection. An outcome of today could also be that you decide to replace certain sequences as the alignment indicates some issues with them (e.g. they are not covering the full length or seem to show many mismatches/gaps). **During this session, we only perform the alignments, if you decide that you need to replace or add sequences, you can discuss that with the TAs

Both *Cytochrome b* and *COX1* are genes found in the mitochondria of eukaryotic cells. In *Cytochrome b*, the protein is part of the respiratory chain complex III, making it an essential part of the energy metabolism. Since all eukaryotes should have *cytB*, the gene can be used for species identification, and is often used to assess phylogenetic relationships between organisms

## Software we are using in this lab
### 1. MAFFT (Multiple Alignment using Fast Fourier Transform) 

MAAFT is a software tool used to align multiple sequences (DNA, RNA, or proteins) simultaneously. It offers various algorithms that balance speed and accuracy, making it especially useful for large datasets. Each algorithm is tuned for different scenarios, so your choice will depend on the characteristics of your sequences and the precision required for your analysis.

MAAFT is broadly used to:
- Find similarities and differences: By aligning sequences, scientists can identify conserved regions, mutations, or functional domains.
- Study evolution and function: Sequence alignments help in building phylogenetic trees and understanding evolutionary relationships.
- Prepare data for further analysis: Accurate alignments are a key starting point for many bioinformatics analyses, such as structure prediction or comparative genomics.

Some examples of the algorithms it offers are:
```
- FFT-NS-1 (Fast):
What It Does: Uses Fast Fourier Transform (FFT) to quickly perform a one-cycle progressive alignment without iterative refinement.
Why You’d Pick It: Ideal for very large datasets or when you need a quick, rough alignment. The trade-off is that it may be less accurate than slower methods.
- FFT-NS-2:
What It Does: Similar to FFT-NS-1 but adds one round of iterative refinement.
Why You’d Pick It: Offers a bit more accuracy than FFT-NS-1 while still being relatively fast. It’s a good middle-ground when you need slightly improved quality without a huge increase in computation time.
- L-INS-i:
What It Does: Incorporates local pairwise alignments along with iterative refinement, focusing on aligning conserved regions within otherwise variable sequences.
Why You’d Pick It: Best when your sequences have conserved motifs amid variable regions. It is slower but tends to be more accurate for complex alignments.
- G-INS-i:
What It Does: Uses global pairwise alignment information with iterative refinement, considering the entire sequence for alignment.
Why You’d Pick It: Ideal when your sequences are overall similar (global homology) and you need high accuracy, though at the cost of increased computation time.
- E-INS-i:
What It Does: Designed for sequences that include long unalignable regions or large insertions, using a consistency-based approach with iterative refinement.
Why You’d Pick It: Best for sequences with multiple conserved domains separated by long gaps. It’s slower but can handle complex insertions and variable regions effectively.
```
OBS! Choosing an Algorithm:
Speed vs. Accuracy: If you’re working with a large dataset or need a fast result, **FFT-NS-1 might be best, which is why we are using this one today**.
Sequence Complexity: For sequences with significant variability or long gaps, methods like L-INS-i, G-INS-i, or E-INS-i are more appropriate despite being slower, because they provide more reliable alignments.

#### 2. AliView

AliView is a lightweight, fast, and user-friendly software tool designed for viewing and editing multiple sequence alignments. It is generally used to:

- Inspect alignments: Quickly browse through large alignment files to check for errors or areas that might need manual adjustment.
- Edit alignments: Make corrections or refinements to automatically generated alignments (for example, those produced by MAFFT) to ensure the data is accurate.
- Work efficiently with big datasets: Its speed and simplicity make it ideal for handling large alignment files without performance issues.

#### Step a: Align the Cox1 sequences

Start by logging into Solander.

Since our datasets for each gene are now complete (Lab2) we will start by aligning your **COX1 and cytB** sequences. 
We are going to start by using the software called `mafft`. 

Aligning this set of mitochondrial genomes is a computationally intensive task. 

In order to execute MAFFT, just type `mafft`. 
You will be asked several questions, among others: 
- the input file name (type in the fasta file you prepared),
- the output file name (type in the name of the fasta file you want to be called after alignment and include the file extension, `.fasta` in this case),
- output file format (sorted fasta),
- algorithm (choose `FFT-NS-1 (fast)`).

Once you have chosen all the options, the corresponding command will be printed on the screen.

**Question 1. Write down the command.**

Now, launch the alignment. It will take a while (maybe not as these computers are new).

We are using the tool `AliView` to view the alignment. In "File", choose "Open File" and choose your alignment. Can you make sense of what you see? What do you think the window shows?

**Question 2. Visually inspect your alignment. Do you notice anything odd? Does any sequence stand out visually (e.g. the outgroup)?**

**Question 3. Show your new alignment to a teaching assistant. If you cannot show it, submit the corresponding alignment file (.fasta).**

The main take-home message from this step is that it is important to examine your alignments well. Sometimes some sequences will genuinely be longer or shorter than other sequences; however, it might also be due to some errors!


#### Step b: Align the sequences for the cytochrome B gene (cytB)

Proceed to the alignment with `mafft`. You can take the same command as the one you created when aligning for the COX1.

Open it with `AliView` and visualise the alignment. 

**Question 4. Visually inspect the alignment of the for cytB, the same that you did for COX1 gene in Q2-4. What do you notice? Are the same species standing out?**

---
## REPORT

Multiple alignment: submit answers to questions 1 through 4. For Question 2 and 4, it can be useful to include a screenshot of what you saw. Only submit the alignment (FASTA file) if you cannot show it to a teaching assistant.


---
