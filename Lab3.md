# Session 3 - Alignments of mitochondrial sequences

## Introduction / Background information to Session 3

In this session, you will focus on alignments. As you have seen in the lecture, you can align two sequences (pairwise alignment) or multiple sequences (multiple alignments). Here, you will do a bit of both. For the pairwise alignment part, you will follow a tutorial that was developed by Rasmus Wernersson. For the multiple alignment part, you will continue to work with the mitochondrial genomes from the previous sessions. Obtaining a good alignment of your sequences will be essential for answering your groups question.

## Goals

  + Perform local and global pairwise alignments with different algorithms
  + Explore parameters of pairwise alignments
  + Perform multiple alignments and visualize them
  + Manipulate files

## Input(s)

  + complete mitochondrial genomes
  + sequences for cytB

## Output(s)

  + An alignment of mitochondrial genomes
  + An alignment of cytB

## Tools

  + [Online alignment tools](https://www.ebi.ac.uk/Tools/psa/)
  + [Online tool to randomly shuffle a protein sequence](http://www.bioinformatics.org/sms2/shuffle_protein.html)
  + Alignment program: [mafft](https://mafft.cbrc.jp/alignment/software/)
  + Alignment visualization program: clustalw / clustalx

    **ARE WE ACTUALLY USING ALL OF THESE TOOLS? WHAT ABOUT JALVIEW**

## Steps

  + Step 1: Pairwise alignment exercise
  + Step 2: Multiple alignment exercise

## Details

### Step 1: Pairwise alignment

Please go through the tutorial on [this page](https://teaching.healthtech.dtu.dk/22111/index.php/ExPairwiseAlignment).

Questions are numbered from 1 to 14. Submit answers to all the questions (you can number them 1-1, 1-2, etc to distinguish them from the answers to the next part).

### Step 2: Multiple alignments

You will now be working with the sequences you have collected last time. This also means that the results will depend on your selection. An outcome of today could also be that you decide to replace certain sequences as the alignment indicates some issues with them (e.g. they are not covering the full length or seem to show many mismatches/gaps). **During this session, we only perform the alignments, if you decide that you need to replace or add sequences, we will do that as part of Lab 4.**

#### Step 2a: Align the entire mitochondria

Start by login into Solander.

Finally, we will start by aligning your **full mitochondrial** genomes! We are going to use a software called `mafft`. 

Aligning this set of mitochondrial genomes is a computationally intensive task. 

In order to execute MAFFT, just type `mafft`. You will be asked several questions, among others: the input file name, the output file name (include the file extension, `.clustal` in this case), output file format, algorithm. For the output file format, choose `clustal` (sorted). For the algorithm, choose `FFT-NS-1 (fast)`.

Once you have chosen all the options, the corresponding command-line will be printed on the screen.

**Question 2-1. Write down the command.**

Now, launch the alignment. It will take a while. In the meantime, you can work on the next step on another terminal window, which is another alignment, of a single gene. It is also a good time to take a break!

#### Step 2b: Align the sequences for the cytochrome B gene (cytB)

Nowadays there is an abundance of genomic data available, for organelles and entire genomes, for a large number of species. This is why in this session and the bioinformatics project, you are aligning the entire mitochondria. However, for a long time, it was more common to work with alignments of single genes (and in some cases, for instance when exploring the diversity in a given environment, it is still a common approach). Aligning single genes might also be a good approach when working with diverse species. And of course, it is much faster!

**ADD SOME BIOLOGY ABOUT cytB**

Proceed to the alignment with `mafft`. You can take the same command as the one you created when aligning for the entire genome.

Once it has finished, look at the output file (the .clustal). Do you understand the format?

**why jalview here and clustalx later???**

To have a better overview of the alignment, we are going to use the `JalView` program. In order to avoid having to download and install the program locally (which can be done following the [instructions](https://www.jalview.org/download/)), we are going to use [JalViewJS](https://www.jalview.org/jalview-js/JalviewJS/), a JavaScript implementation of the program that allows us to use it from our browsers. 

In "File", choose "Load Sequences" and choose your alignment. Can you make sense of what you see? What do you think the bottom window shows?

**Question 2-2. Visually inspect your alignment. Do you notice anything odd? Does any sequence stand out visually (e.g. the outgroup)?**


**Question 2-3. Show your new alignment to a teaching assistant. If you cannot show it, submit the corresponding alignment file (.clustal).**

The main take-home message from this step is that it is important to examine your alignments well. Sometimes some sequences will genuinely be longer or shorter than other sequences; however, it might also be due to some errors!

#### Back to Step 2a

**why clustalx here and jalview earlier???**


By now the alignment of the entire mitochondria should be ready for you to look at! Open it with `clustalx` (see Step 2f). What do you see?

**Question 2-4. Visually inspect the alignment of the full mitochondrial genome the same way you did for cytB in Q2-4. What do you notice? Are the same species standing out?**

---
## REPORT

Pairwise alignment tutorial: submit answers to all questions (you can number them 1-1, 1-2, etc).

Multiple alignment: submit answers to questions 2-1 through 2-4. For Question 2-2 and 2-4, it can be useful to include a screenshot of what you saw. Only submit the alignment (clustal file) if you cannot show it to a teaching assistant.

**SHOULD WE MAKE THEM PRODUCE FASTA FILES HERE OR ARE THEY ALIGNING THEM AGAIN IN LAB 5? DO WE ACTUALLY NEED CLUSTAL AND FASTA OR CAN WE USE FASTA FOR EVERYTHING?**

---
