
# Session 6 - Wrap up the bioinformatics project

## Introduction / Background information to session 6

This is the last session of the bioinformatics project (and of the course). You will wrap up the project and present your results to the teaching assistants (details below).

## Goals

  + Further your understanding of your results
  + Plot trees with a visualization software
  + Answer the question you were given in Session 2
  
## Input(s)

  + The alignment for the mitochondria from session 3/5
  + The trees generated in Sessions 5
  + The name conversion tables generated in Session 2

## Output(s)

  + .pdf files of your trees

## Tool(s)
  + IQ-TREE
  + FigTree, a phylogenetic tree visualization software

## Details

### Step 1: Examine the IQTree output for the mitochondria

In Session 5 you performed a Maximum Likelihood  on two alignments: *cytB* and entire *mitochondria*. You answered  questions concerning the *cytB* run. Now, answer these same questions for the mitochondria run. You might be asked about these during the presentation.

**Question 1: Which files do IQ-TREE output? Explain briefly what each of them is.**

IQ-TREE creates several types of trees (e.g. a Neighbour Joining tree saved as .bionj file and an ML tree saved as .treefile). In order to properly visualize your tree, you'll need to use specific software, as trees are not represented in a way we can easily understand in our files. In order to plot them, we are going to use [FigTree](SRC/FigTree_v1.4.4). Download it onto your computer and start it. 

**Question 2: Compare the *.bionj* tree with the ML tree. Are there any differences? If so, explain what they are and why do you believe they are there.**

Now let's look at the .iqtree file.

#####Question 3:
1. **Which model did ModelFinder choose? From all the criteria calculated by this software, which was used to determine the best-fitting model?**

2. **Briefly explain the best-fitting model.**

#####Question 4:
1. **Now look at both your Maximum Likelihood tree and Consensus Tree. Are they the same? If not, where do they differ?**

2. **In both trees you can see a number at the base of each branch. That is the number of iterations that supported that branching during bootstrapping. Which is your least supported branch? What does that mean to your question?**

### Step 2: Create a visual representation of your Maximum Likelihood trees

In the .iqtree file, you have a representation of the trees. However, it is an unrooted tree. You can root the tree, and do many other things, with the program FigTree.

*If you can't get FigTree to work in a terminal you can try downloading it from https://github.com/rambaut/figtree/releases and installing it locally on your computer.*
  
When you call FigTree, a visual interface will open. In `File`, choose `Open` and select one of your Maximum Likelihood trees. If the software asks you to select a name for the labels on the tree, you can keep the default or choose a keyword, for example `bootstrap`. **Note that you do *not* want the `.iqtree`, that file is more of a logfile than an actual tree.**

The three important things you have to do are:
  
  1. Root the tree with your outgroup (select the branch and then select `Reroot`)
  2. Show the bootstrap values (using `Branch labels` or `Node labels` and selecting the right value to display)
  3. Make sure the tree can be easily understood. For example, you might need to change the name of the species, if you are using the short names that you created in [Session 2](Lab2.md). 

You can use the script you created in Session 2 to change the names in your treefiles.
Once you are done with those, you can play around with the other options (for example Rotate and different type of trees).

Before you export your tree, think about what else you can do to show your results better. Look on Google for actually published trees, like the ones shown below
 
<p float ="left">
	<img src="./Figures/Phylogenetic-analysis-of-orchids-The-phylogenetic-tree-was-based-on-the-chloroplast.png" width="500">
	<img src="./Figures/Phylogenetic-tree-of-the-species-used-for-the-evolutionary-analysis-of-Hox-genes.png" width="500">
	<img src="./Figures/fig-3-corrected.png" width="500">
	<img src="./Figures/41598_2020_70287_Fig1_HTML.png" width="500">
</p>	


**Do not forget to export your trees as image files. You will have to show them during the presentation.**



### Step 3: Reflect on your results

By now you have assembled a dataset to answer the question from Session 2; you collected *cytB* sequences and entire mitochondrial genomes for all species in the dataset; you aligned the species; you performed phylogenetic analysis and looked at some aspects of it, for example the model chosen; and you obtained a visual representation of your rooted trees.

Now it is time to reflect on all that you have done and to answer your phylogenetic question. The preferred method for that is to do it orally during Session 6. If for some reason this is not feasible, you will have to do it in a written form (details for the format are below).

At this stage, you should have two sets of trees: one for *cytB* and one for the entire mitochondria. To prepare for the presentation, think about:

- What is the answer to the question given by these trees?

- Do the different trees give the same answer? If not, what could be the explanation?

- Which tree(s) do you think are most supported? What does the bootstrap analysis tell?

- Are the substitution models different for *cytB* and the entire mitochondria? If yes, what could be an explanation?

- Do you think your choice of species (including the outgroup) was appropriate to answer the question? If you were to redo the analysis, would you change something?


We will also expect you to remind us briefly of the question you worked with, and list which species you chose to include and why, so take a moment to prepare that too.


---
## Presentation

Once you feel like you are ready to present (and not later than one hour before the end of the session), write your names on the board so the teaching assistants can come to listen to you. The presentation will last 5-10 minutes, at your desk.

You do not have to submit anything for this session (if you present orally).

---
## Back-up submission: Written report

In case you cannot finish in time, please let the teaching assistants know and submit a written document with your trees (the ones you made with FigTree) and 15-30 lines (or more if you are inspired) answering the questions. Do not forget to indicate which question you worked with and which species were included in the dataset. Exceptionally one submission by group is allowed - but remember to state the people involved.

---

This is the end of the lab, please make sure that you completed and wrote down the answers to all of the questions.
Also, make sure to delete any files that you no longer need - you can copy them somewhere else if you want to keep them.

 **Obs!** As this is the last session, this step is extra important. We won't delete anything before the end of the semester, but afterwards we do not guarantee that the data will be kept. 
