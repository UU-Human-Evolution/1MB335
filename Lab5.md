# Session 5 - Phylogenetic Analysis

## Background information/Refresher for Alignments
If you remember, we ran multiple alignments in lab 3. While we are not aligning in this session, it could be useful information to know about pairwise alignnment as well as you may need it in the future.

## The Basics of Sequence Alignment
At the core of sequence analysis lies **sequence alignment**, a method for arranging DNA, RNA, or protein sequences to identify regions of similarity. These similarities may indicate functional, structural, or evolutionary relationships between the sequences. The two main types of sequence alignment are:

- Pairwise Alignment: Compares two sequences directly to determine their similarity.
- Multiple Sequence Alignment (MSA): Aligns multiple sequences to identify conserved regions across species or genes.

## Pairwise alignment can be performed using two main approaches:
- Global Alignment (Needleman-Wunsch algorithm) – Aligns sequences from start to end, best suited for highly similar sequences of roughly equal length.
- Local Alignment (Smith-Waterman algorithm) – Finds the most similar subsections of two sequences, making it useful for sequences with only partial similarity.

## Introduction to BLAST

As genomic data exploded, researchers needed efficient ways to compare new sequences against existing databases. This led to the development of BLAST (Basic Local Alignment Search Tool), one of the most widely used bioinformatics tools. BLAST works by quickly **identifying local similarities** between a query sequence and sequences in a large database. Unlike traditional alignment methods that perform an exhaustive comparison, BLAST employs heuristics to speed up the process while maintaining accuracy. The main types of BLAST include:

- BLASTN – Compares a nucleotide query sequence to a nucleotide database.
- BLASTP – Compares a protein query sequence to a protein database.
- BLASTX – Translates a nucleotide query into proteins and compares it to a protein database.
- TBLASTN – Compares a protein query sequence to a translated nucleotide database.
- TBLASTX – Translates both query and database sequences and compares them at the protein level.

## Applications of BLAST and Pairwise Alignment

Sequence alignment and BLAST are indispensable in modern biology, with applications such as:
- Gene and protein identification: Determining the function of an unknown sequence by finding similar known sequences.
- Evolutionary studies: Investigating how genes and proteins have evolved across species.
- Medical and agricultural research: Identifying mutations, disease-associated genes, and antibiotic resistance genes.
- Forensics and environmental studies: Comparing unknown biological samples to known species.
  
## An Introduction to Phylogenetics
Since the eve of Biology as a field of Science, one of the key questions has been how do the different organisms we see today relate to each other, and how they evolved. In the old days, we used anatomical similarities (also known as [homologies](https://en.wikipedia.org/wiki/Homology_(biology))) and dissimilarities to try to reconstruct their evolutionary history. 
![Example of Homologies](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Homology_vertebrates-en.svg/1280px-Homology_vertebrates-en.svg.png)

With the dawn of genetic sequencing and the genomic era, we can now establish those relationships with quite more certainty and in a less biased way. The practice of using genetic data to infer these relationships is known as Phylogenetics, and it is the "gold-standard" for establishing the relationship between modern species. 

### The Base of Phylogenetic Analysis 
The basic idea behind it all is quite simple: as species diverge over time, they accumulate mutations that the other groups don't share. So, when comparing several sequences, the bigger the number of differences between them, the larger the time since their common ancestor. However, this simple idea gets complicated quite soon, as we are working with really long sequences and, in some cases, long periods of time. This means that we will need to use robust statistical modeling in order to infer these relationships, which we will represent as a [phylogenetic tree](https://en.wikipedia.org/wiki/Phylogenetic_tree).

![Phylogenetic tree from Ersmark et al. 2016](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Phylogenetic_tree_for_wolves.jpg/468px-Phylogenetic_tree_for_wolves.jpg)

*Phylogenetic tree from Ersmark et al. 2016: https://doi.org/10.3389/fevo.2016.00134*

Each tree is a hypothesis of the relationship between our sequences, and our goal is to identify (from all the possible trees), the one that is most likely to be a true tree, according to our data. This may vary depending on the region you are looking at, the models you are using or how you preprocess and align your sequences. 

### Bootstrapping 

Bootstrap resampling in phylogenetics works by randomly resampling columns (sites) from the multiple sequence alignment with replacement to generate new datasets. Then, a phylogenetic tree is reconstructed for each resampled dataset.

What this practically represents:
- Take your original alignment (e.g., 1000 nucleotide positions).
- Randomly sample columns from this alignment, with replacement, until you generate a new alignment of the same length (1000 positions).
- Some sites will be selected multiple times.
- Some sites will be omitted in a given resampled dataset.
- Build a phylogenetic tree from this new dataset.
- Repeat this process many times (typically 100 or 1000 replicates).
- Count how often each branch appears across all replicates.

If a branch appears in 90% of the bootstrap replicates, it gets a bootstrap support value of 90.
If it appears in only 54% of the replicates, it gets a bootstrap support value of 54.

So, with all of the above in mind, let's get going... 

## Goals
+ Test which substitution model works best with our data;
+ Work with IQTree and learn how to extract information from its output;
+ Create a phylogenetic tree that is meaningful for our project's question;

## Input
+ Fasta sequences of **CytB** and **Cox1** that we aligned in Lab 4

## Output(s)
+ IQTree file with relevant info on our tree
+ Tree file
+ Image files of your trees

## Tools
+ Maximum Likelihood  program: [IQTree](http://www.iqtree.org/)
+ FigTree, a phylogenetic tree visualization software

## Details

For this Session, we will use the files we created in the previous labs. Please make sure you follow the instructions properly and that you have all the files you need. 
#We will be using the fasta files with short name here

Since we have produced an alignment in the previous session, we can proceed to infer **which tree, of all the possible trees, is the most likely one**. There are several methods to do this:

+ [Parsimony](https://www.mun.ca/biology/scarr/2900_Parsimony_Analysis.htm): "**the simplest explanation that can explain the data is to be preferred**", so the hypothesis with the smallest number of changes is the most likely. 
 However, this method has plenty of assumptions that we know are false, so it is not used anymore.
+ [Neighbour-joining](https://academic.oup.com/mbe/article/4/4/406/1029664): A slightly more refined version of parsimony in which we chose the best tree by **minimizing branch lengths** in the tree. More computationally intensive than parsimony, but still something that a modern computer can do fairly quickly.
+ [Maximum Likelihood](http://ib.berkeley.edu/courses/ib200a/lect/ib200a_lect11_Will_likelihood.pdf): "Likelihood is defined to be a quantity proportional to the probability of observing the data given the model". This means that, **by providing a model of how DNA sequences change, we can determine which tree is the most probable to be true**. 
+ [Bayesian Inference](https://www.sciencemag.org/site/feature/data/1050262.pdf): This method uses Bayesian Statistics to combine **prior information** that we know about our data (also known as Prior Probability Distribution) **with the likelihood**, in order to transform it into a more accurate probability distribution, known as the **Posterior**.
  
![](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5624502/bin/emss-73449-f001.jpg)

*Prior, likelihood and posterior distribution for a two-parameter phylogenetic example in Nascimento et al. 2017: https://dx.doi.org/10.1038%2Fs41559-017-0280-x*

The last two are the state-of-the-art methods for phylogenetic analysis, and have become more and more popular as computing power has increased, as both methods are very demanding in that regard. 

For our project, we are going to use: 
- an implementation of the Maximum Likelihood approach called [IQ-TREE](http://www.iqtree.org/doc/Tutorial#first-running-example) 

As we mentioned earlier, any Maximum Likelihood approach is **based on a model**. In phylogenetics, this model **describes the probability of each substitution to happen**. [Here](http://evomics.org/resources/substitution-models/nucleotide-substitution-models/) you can find a list of the more common models, and [here](http://www.iqtree.org/doc/Substitution-Models) the ones that are implemented in IQ-TREE. 
![Substitution model representation](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fnrg3186/MediaObjects/41576_2012_Article_BFnrg3186_Fig1_HTML.jpg?as=webp)

*Graphical representation of some substitution models from Yang & Rannala, 2012. Nature Reviews Genetics: https://doi.org/10.1038/nrg3186*

## IQ-Tree -- Generating Maximum Likelihood trees

Now that we have a general picture of what we are doing, let's start working with IQ-TREE. The basic syntax for this software is:

```
iqtree -s ALIGNMENT -o OUTGROUP -m MODEL -pre SOME_OUTPUT_PREFIX -bb 1000
```
Replace the capitalized variables with your choices, e.g. replace `ALIGNMENT` with the name of your aligned FASTA file for the cytB gene.

Under OUTGROUP you should put the **name of your outgroup** as they appear in the alignment file. 
If you have multiple outgroups you can separate them with a comma (**make sure to have no spaces as separators!**) eg;

```
-o c_Vurs,H_sap

```

Now run IQ-TREE in your open terminal with the CytB data, and set your model to *-m MFP*. 
- *MFP* stands for ModelFinder Plus, and is an algorithm that automatically considers a list of substitution models & estimates which model is the one that fits our data better. 
- *-bb 1000* means that we want our algorithm to use [bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)). 

## FigTree -- Create a visual representation of your Maximum Likelihood trees

In the .iqtree file, you have a representation of the trees. However, it is an unrooted tree. You can root the tree, and do many other things, with the program FigTree.

*If you can't get FigTree to work in a terminal you can try downloading it from https://github.com/rambaut/figtree/releases and installing it locally on your computer. It's very simple to run and even recommendable*
  
When you call FigTree, a ***visual interface will open***. In `File`, choose `Open` and select one of your Maximum Likelihood trees. If the software asks you to select a name for the labels on the tree, you can keep the default or choose a keyword, for example `bootstrap`. **Note that you do *not* want the `.iqtree`, that file is more of a logfile than an actual tree.**

The three important things you have to do are:
  
  1. Root the tree with your outgroup (select the branch and then select `Reroot`)
  2. Show the bootstrap values (using `Branch labels` or `Node labels` and selecting the right value to display)
  3. Make sure the tree can be easily understood. 

Once you are done with those, you can play around with the other options (for example Rotate and different type of trees).
Before you export your tree, think about what else you can do to show your results better. Look on Google for actually published trees, like the ones shown below
 
<p float ="left">
	<img src="./Figures/Phylogenetic-analysis-of-orchids-The-phylogenetic-tree-was-based-on-the-chloroplast.png" width="500">
	<img src="./Figures/Phylogenetic-tree-of-the-species-used-for-the-evolutionary-analysis-of-Hox-genes.png" width="500">
	<img src="./Figures/fig-3-corrected.png" width="500">
	<img src="./Figures/41598_2020_70287_Fig1_HTML.png" width="500">
</p>	


**Do not forget to export your trees as image files. You will have to show them during the presentation.**


**Question 1:** 
**Which files do IQ-TREE output? Explain briefly what each of them is.**

IQ-TREE creates several types of trees (e.g. a Neighbour Joining tree saved as .bionj file and an ML tree saved as .treefile). In order to properly visualize your tree, you'll need to use specific software, as trees are not represented in a way we can easily understand in our files. In order to plot them, we are going to use [FigTree](SRC/FigTree_v1.4.4). Download it onto your computer and start it. 

**Question 2:**
**Which model did ModelFinder choose? From all the criteria calculated by this software, which was used to determine the best-fitting model?** (Hint: you can check the log file to find out, scroll a bit to find out)

**Question 3:**
**Briefly explain the best-fitting model.** (you can simply google it or find it on IQtree website)

**Question 4:**
**In your tree, you can see a number at the base of each branch. That is the number of iterations that supported that branching during bootstrapping. Which is your least supported branch? What does that mean to your question i.e. are the groups that you need to answer your question not supported?** 

**Repeat these steps for the Cox1 alignments. Remember to adapt the command above to run IQ-TREE and be careful to not over-write your files. (to be safe, work in a separate folder)** 

**Question 5:**
**Are the trees similar for CytB and Cox1, if not what's the difference?**

**Question 6:**
**Can you compare your CytB tree generated by IQtree to the one that you generated in the last lab in ITOL? Do they differ a lot? Which of the two do you trust more?**

# REPORT

Submit a file with the answers to all the questions and the *.iqtree* file for the CytB run.

---

This is the end of the lab, please make sure that you completed and wrote down the answers to all of the questions.
Upload the **scripts** (code) that you were asked to submit to Studium **in the original format** (i.e. .py or .sh), no `pdf` or word files! Any answers that are not code should, of course, be in text formats such as `.pdf, .txt & .docx`.
Also, make sure to delete any files that you no longer need - you can copy them somewhere else if you want to keep them.
