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

## Details

###Multiple alignments

You will now be working with the sequences you have collected last time. This also means that the results will depend on your selection. An outcome of today could also be that you decide to replace certain sequences as the alignment indicates some issues with them (e.g. they are not covering the full length or seem to show many mismatches/gaps). **During this session, we only perform the alignments, if you decide that you need to replace or add sequences, you can discuss that with the TAs

#### Step a: Align the Cox1 sequences

Start by login into Solander.

Finally, we will start by aligning your **COX1 and cytB** sequences! We are going to use a software called `mafft`. 

Aligning this set of mitochondrial genomes is a computationally intensive task. 

In order to execute MAFFT, just type `mafft`. 
You will be asked several questions, among others: 
- the input file name (type in the fasta file you prepared),
- the output file name (type in the name of the fasta file you want to be called after alignment and include the file extension, `.fasta` in this case),
- output file format (sorted fasta),
- algorithm (choose `FFT-NS-1 (fast)`).

Once you have chosen all the options, the corresponding command will be printed on the screen.

**Question 1. Write down the command.**

Now, launch the alignment. It will take a while (maybe not as these computers are new). In the meantime, you can work on the next step on another terminal window, which is another alignment, of a single gene.

#### Step b: Align the sequences for the cytochrome B gene (cytB)


*Cytochrome b* and *COX1* are genes found in the mitochondria of eukaryotic cells. In *Cytochrome b*, the protein is part of the respiratory chain complex III, making it an essential part of the energy metabolism. Since all eukaryotes should have *cytB*, the gene can be used for species identification, and is often used to assess phylogenetic relationships between organisms

Proceed to the alignment with `mafft`. You can take the same command as the one you created when aligning for the COX1.

We are using the tool `AliView` to view the alignment. In "File", choose "Open File" and choose your alignment. Can you make sense of what you see? What do you think the window shows?

**Question 2. Visually inspect your alignment. Do you notice anything odd? Does any sequence stand out visually (e.g. the outgroup)?**


**Question 3. Show your new alignment to a teaching assistant. If you cannot show it, submit the corresponding alignment file (.fasta).**

The main take-home message from this step is that it is important to examine your alignments well. Sometimes some sequences will genuinely be longer or shorter than other sequences; however, it might also be due to some errors!

#### Back to Step a


By now the alignment of the COX1 should be ready for you to look at! Open it with `AliView`. What do you see?

**Question 4. Visually inspect the alignment of the COX1 gene the same way you did for cytB in Q2-4. What do you notice? Are the same species standing out?**

---
## REPORT

Multiple alignment: submit answers to questions 1 through 4. For Question 2 and 4, it can be useful to include a screenshot of what you saw. Only submit the alignment (FASTA file) if you cannot show it to a teaching assistant.


---
