# Session 2 - Database search

Mitochondria are present in all eukaryotic cells (for a review, see 'Origin and diversification of mitochondria', Roger et al.), where among many other functions it supplies the cells with chemical energy (ATP). Here, we will focus on the genes present in mitochondria; mitochondrial genomes present the advantage of being relatively small compared to nuclear genomes (e.g. 16,000 base pairs in humans), thus facilitating bioinformatic operations in the labs. They are also present in many copies in the cells, thus they are relatively easy to sequence even in extreme cases where DNA is often limited such as environmental DNA or ancient DNA studies. Although mitochondrial genomes can take many different forms depending on the species, they all contain a series of conserved protein-coding genes as well as rRNA and tRNA; this makes mitochondrial genomes good candidates for comparative analyses between different species.

## General introduction to sessions 2 to 6

![](Figures/Mitochondrion_structure.svg)


**Figure 1: Simplified structure of a mitochondrion.** 
*By Kelvinsong; modified by Sowlos - Own work based on: Mitochondrion mini.svg, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=27731882*

For the remaining labs you will work in groups on a bioinformatics project where you will try to answer one of the evolutionary biology questions below, using bioinformatic methods. You will be randomly assigned one of the questions and a group. Over the coming sessions, you will gather the data necessary to answer this question, format and align it in order to finally analyze it and present your results to the entire class.

We (the lab assistants) will help and guide you through this project, but ultimately the decisions are yours and you will need to consider the potential downstream effects of your choices. 

We made a checklist to help you when a command does not do what you expect it to do [here](Troubleshooting_checklist.md). It includes instructions to use `SFTP` to transfer files to and from Solander.


## Questions:
1. Are bats more closely related to horses than to cows?

2. Both whales and sea cows originate from land-living animals. Do they have a common ancestor that transitioned from land-to-water or has this transition occurred twice independently?

3. Are salamanders more closely related to frogs than to lizards?

4. What are the closest relatives of octopuses and squids?

5. Is the guinea pig more closely related to rats than to pigs?

6. What other cat-like animal is most closely related to the cheetah?

7. Are egg-laying mammals (platypus and echidna) more closely related to birds than to placental mammals?

8. Are moose more closely related to reindeer than to other deer species?

9. Describe the phylogeny of primates!

10. What type of wolves is the ancestor of domestic dogs?

11. Are Porcupines closer to pigs or to hedgehogs?

## Session 2

In this session, you will collect your data to work with during the coming sessions. For collecting your sequences you need to think about what species you want to test/compare. Your question does not include a particular species but rather groups of species, so you will need to collect multiple sequences per group. In addition to the species directly connected to your question, you should include one distantly related species to all of them (a so-called "outgroup") which is required for later analyses. The picture below helps to understand the concept of "ingroup" and "outgroup", we will get back to this in the phylogenetics part of the course: 

![](Figures/Outgroup.jpg)
_By Ngilbert202 - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=63950569_

The test in the above figure would have been to see if `C` is more related to `B` or to `D`, and the answer would then be that `C` is closer to`D` (they share one more common ancestor). 

If you are unsure what would be an appropriate outgroup for your question, ask us!
*Hint! - Look at the phylogenetic tree. The outgroup should be outside of the group you are comparing (or the question you are answering) but you don't need to go too far. For example, if you are comparing cats and dogs, you could use a platypus as an outgroup. (the more distant your outgroup is, the longer some bioinformatic analyses will take)*

**N.B.** Since you are going to produce quite a lot of files, try to use self-explanatory files names and a good structure of folders. It will make your work easier. It might be a good idea to write a short description about how the archive is organized and where the files are (trees, scripts, alignments and so forth).


## Gathering your data

First start by actually selecting what species you should use. Discuss about what species you need to answer the question and what could be a good outgroup. 
If you have a hard time coming up with good candidate species you can use the [NCBI taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Root).

In the end, you should have around 15-20 species in your dataset. 

**Question 1**: Write down a few sentences on the selection of species and outgroup in your dataset. Which species did you choose and why?

**Comment**: it is possible that you do not find data for some of the species. In that case, update your answer accordingly and add more species if needed.

This will help you later to reflect upon the question and your results. It also help us (the teaching assistants) to check that you will be able to answer the question you were given.


## Getting the sequences

Your task is to gather the full **mitochondrial** genome sequences for your species as well as the gene **CytB** (Cytochrome b). You should thus have two fasta files per species!

#### Collecting sequences from Genbank

* Go to NCBI Genbank [here](https://www.ncbi.nlm.nih.gov/nucleotide/).

* Search for your species of interest.

* On the left under *Genetic compartments* select `mitochondrion`. You will find all entries of mitochondrial sequences for that species.

* First, to obtain full mitochondrial genome sequences look for an entry listed as `complete genome` which should be around 17000 bp long.

* Click on the entry, then *FASTA* and download the fasta file for the entry to your computer.

* Repeat the last two steps for *cytB*.
  * One option is to search for entries called `cytochrome b` and `complete cds`.
  * The second option is to take a full mitochondrial genome sequence that is annotated (scroll down and see if there are genes and coding sequences listed). Search for "cytB", right click on the link "gene" and choose "open link in new tab". It opens a separate Genbank page specific to your gene of interest which you can then download as described above.

**Save your files with clever, distinguishable names.**

#### If you cannot find the two sequences (entire mitochondria and *cytB*) for some species

Preferably you should get the two types of sequences for all species in your dataset. It might be that you decided to include a species but could not find both sequences for it. In that case, try again with a close relative. If it is really difficult for you to find enough species with the two sequences for your dataset, ask a teaching assistant and we will look for a solution together. In a later session, we will also try a different strategy for obtaining additional sequences.

#### Create fasta files for the entire dataset

Once you found all the sequences for your dataset, you will need to put them together in a single fasta file (OBS! One fasta file for the entire mitochondria and one for *cytB*) using the `cat` command for example.

## Create a name conversion file.

Create two different files (one for the mitochondrial sequences and one for *cytB*). Both files are to be **tab-separated** into three columns. 
(I.e. there should be a tab charachter `\t` between each column.) 

The files should contain one row for each sequence in your data set, including: 

 * a maximum 8-character short-name (enough for you to identify it: e.g. c\_Vurs or mt\_Vurs)
 * an easy-readable name (good for presentation to others: e.g. cytB\_Vombat\_ursinus mitoc\_Vombat\_ursinus)
 * The header you got when dowloading it from NCBI (or if you have changed it already your own long header)
  `MN443013.1 Providencia stuartii strain PS11 subclass B1 metallo-beta-lactamase NDM-1 (blaNDM) gene, blaNDM-1 allele, partial cds`
  
  ```
c_Vurs	cytB_Vombat_ursinus	NC_003322.1 Vombatus ursinus mitochondrion, complete genome
H_sapiens	cytb_Homo_Sapiens	NC_003562.2 Homo Sapiens mitochondrion, complete genome
N_nean	cytB_Homo_Neanderthalensis	NC_004571.2 Homo Neanderthalensis mitochondrion, complete genome	
  ```


**Question 2** Now you should create a Python script that: 
- takes one of your merged fasta file as input (which at that point has one of the three types of headers in the conversion table);
- uses your conversion table;
- and has the option to switch between the three different header types, depending on your choice (short name/easy name/full header). It should be able to change which types of header is saved by an **option from the user**, from one to another and back again; 
- your script should be able to change the original file you send in and should not create a new fasta file!

**Hints**: 
- When your script is reading the table **remember that your columns are tab separated**, you can use that to differentiate between your different columns. 
- Remember that you can `sys.argv` to get inputs from the command line.
- *chatGPT* and other AI tools based on LLMs are very useful for writing such scripts -- feel free to use them but make sure to test the script so it does what you think it should. Also instruct the AI to *not* use any extra libraries/packages (e.g. BioPython) for this task.

*Hint* It's probably a good idea to create a mock fasta file and a mock conversion table, on which you can test your code. Something that is short and simple to analyze.

Submit the script, the two conversion tables and the fasta files for *cytB* and the full mitogenome.


## REPORT

Please submit the answer to Question 1 (text) and to Question 2 (a Python script, two conversion tables and the merged FASTA files). Please indicate whether you have used an AI tool for writing the script and what prompts you have used.

---

This is the end of the lab, please make sure that you completed and wrote down the answers to all of the questions.
Upload the **scripts** (code) that you were asked to submit to studium **in the original format** (i.e. .py or .sh), no `pdf` or word files! Any answers that are not code should of course be in text formats such as `.pdf, .txt & .docx`.
Also, make sure to delete any files that you no longer need - you can copy them somewhere else if you want to keep them. This goes for both the Unix computers and Solander.

