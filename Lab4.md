# Session 4 -  Distance Matrix & Manual Tree Construction**  

During the last sessions, you collected and aligned mitochondrial sequences, COX1 and CytB, from databases that you will be using for the remaining sessions. Today, you will generate a **distance matrix** from your multiple sequence alignment and manually construct a phylogenetic tree using iTOL. You will also learn about **Newick format**, which is used to represent tree structures.  

## **Goals**  
+ Learn how to compute a **distance matrix** from a multiple sequence alignment.  
+ Interpret **genetic relationships** based on sequence similarity.  
+ Become familiar with the **Newick format** for phylogenetic trees.  
+ Construct a **phylogenetic tree manually** in iTOL.
+ Visualize the tree in iTOL and analyze sister relationships.  

## **Input(s)**  
+ Aligned mitochondrial sequences from the previous lab.  
+ Online distance matrix calculation tools.  

## **Output(s)**  
+ Distance matrix of mitochondrial sequences.  
+ A manually constructed phylogenetic tree in **Newick format**.  
+ A visualization of the tree using **iTOL**.  

## **Tools**  
+ **EMBOSS DistMat** ([https://www.bioinformatics.nl/cgi-bin/emboss/distmat](https://www.bioinformatics.nl/cgi-bin/emboss/distmat))  
+ **iTOL (Interactive Tree of Life)** ([https://itol.embl.de](https://itol.embl.de))  

---  

## **Generating a Distance Matrix**  

A **distance matrix** is a table that quantifies the genetic distances between sequences. A smaller distance means the sequences are more closely related.  
In this lab, it is generated from a multiple sequence alignment (MSA) using tools like EMBOSS DistMat. 

EMBOSS DistMat is an online bioinformatics tool that calculates pairwise genetic distances from a multiple sequence alignment (MSA). It supports different distance metrics, such as Kimura, Tamura, Jukes-Cantor etc, to measure sequence similarity. 

Very shortly: 
- the Kimura model accounts for mutations occurring more than once at the same position, giving a more refined estimate of genetic distance.
- The Jukes-Cantor model does not take into account that transition rates between purines (A-G exchanges and between pyrimidines (C-T exchanges) are different from transversions rates between purines and pyrimidines (A<->C, A<->T, C<->G, G<->T). The Kimura model corrects for this effect.
- 'Percent Identity' is a straightforward method that calculates the percentage of identical bases or amino acids between sequences, providing a basic measure of similarity.

This matrix helps determine evolutionary relationships by identifying closely related sequences. Using these distances, species with the smallest values are grouped first in a Newick format tree, which is then manually constructed and visualized in iTOL. This process allows for interpreting evolutionary relationships and identifying sister species.

Let's try the **EMBOSS DistMat** tool:  

### **Steps:**  

1. Upload your **aligned FASTA file** from the previous lab.
2. Select a distance calculation method, for example **Kimura**.
3. You can leave the other options as they are/empty.  

### **Question 1:**  

- Which species have the **smallest** distance (most similar)?  
- Which species are the **most distant** from each other?  
- Do you see anything unusual with the distance matrix? 

---

## **Understanding the Newick Format**  

The **Newick format** is a simple way to represent tree structures using parentheses and commas.  
It encodes tree structures in a compact, text-based format where closely related species are grouped together in parentheses and branch points (nodes) indicate common ancestors. This format is widely used in bioinformatics tools like iTOL for visualizing evolutionary trees.

### **Example of a Newick Tree:**  
```
(A,B,(C,D));
```
This means:  
- **A & B** are closely related.  
- **C & D** are also closely related.  
- The **(C,D) group** is more distant from **A & B**.  

Or, in the following example:

```(Human, Chimp, (Horse, (Lizard, Spider)))```

This translates to:
- Humans & Chimps are closely related.
- Lizards & Spiders are more closely related to each other than to Horses.
- Horses are more distant from Humans & Chimps but still closer than Lizards and Spiders.
- The (Lizard, Spider) group is the most distantly related to the others.

Now, your task is to manually create a tree, using your **distance matrix** (you already created this with EMBOSS DistMat) to determine which species should be grouped together. Use the information provided by the distance matrix and do this for all 10-ish samples you have chosen. 

Now, try the same but using "Jukes-Cantor" if you used the "Kimura" method. Since the point of this is to visualize the possible difference between these two models, it's enough if you ran JC just for COX1 (or CytB). And compare the trees produced using Kimura and JC. You don't have to run it for both COX1 and CytB, but you obviously can if you want to.

### **Question 2:**  

- Based on your distance matrix, can you write a **Newick format tree** that represents the relationships between species?
- In your answer, make sure you note which model generated which distance matrix and the suggested Newick format tree.

---

## **Constructing a Tree in iTOL**  

Now that you have your **Newick tree**, you will visualize it in **iTOL**.  
iTOL (Interactive Tree of Life) is an online tool for visualizing, editing, and annotating phylogenetic trees. It allows users to upload trees in Newick format, customize their appearance, and analyze evolutionary relationships. iTOL supports features like color-coding, branch labeling, and metadata integration, making it useful for interpreting phylogenetic data.

### **Steps:**  

1. Go to **[iTOL](https://itol.embl.de)** and create a **New Tree**.  (Click on `Upload a new tree`)
2. Click on Upload, go to Upload new tree section and paste your **Newick tree** in the tree text box and click on Upload.    
3. Save and export the tree as an image or pdf.  

### **Question 3:**  
- Based on this tree can you write down the sister relationships between different groups or species 
- Can you use this tree to answer your question (for eg: which ape is closely related to humans)?

OBS!
**During this lab, we effectively used the Neighbor-Joining (NJ) method, since we are constructing a tree based on pairwise genetic distances from the distance matrix. NJ is a fast and simple way to build trees by progressively joining the closest sequences. 
However, next time, we will use IQ-TREE, which applies Maximum Likelihood (ML), a more advanced statistical method that estimates the most probable evolutionary tree based on mutation models. ML trees are generally more accurate but require more computational power.**

---

## **Report Submission**  

**Submit a pdf file with answers to the questions:**  
**Q1:** All questions asked above 
**Q2:** Your manually written **Newick tree**.  
**Q3:** A screenshot of your tree in **iTOL** or the saved tree image in pdf or SVG format.  
