## **Lab 4: Distance Matrix & Manual Tree Construction in iTOL**  

During the last sessions, you collected and aligned mitochondrial sequences, COX1 and CytB, from databases that you will be using for the remaining sessions. Today, you will generate a **distance matrix** from your multiple sequence alignment and manually construct a phylogenetic tree using iTOL. You will also learn about **Newick format**, which is used to represent tree structures.  

## **Goals**  
+ Learn how to compute a **distance matrix** from a multiple sequence alignment.  
+ Interpret **genetic relationships** based on sequence similarity.  
+ Become familiar with the **Newick format** for phylogenetic trees.  
+ Construct a **phylogenetic tree manually** in iTOL.  

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
A **distance matrix** is a table that shows the genetic distances between sequences. A smaller distance means the sequences are more closely related.  

We will use the **EMBOSS DistMat** tool:  

### **Steps:**  
1️⃣ Upload your **aligned FASTA file** from the previous lab.  
2️⃣ Select a distance calculation method: **Kimura** or **Percent Identity**.  

### **Question 1:**  
- Which species have the **smallest** distance (most similar)?  
- Which species are the **most distant** from each other?  
- Do you see anything unusual with the distance matrix? 

---

## **Understanding the Newick Format**  

The **Newick format** is a simple way to represent tree structures using parentheses and commas.  

### **Example of a Newick Tree:**  
```
(A,B,(C,D));
```
This means:  
- **A & B** are closely related.  
- **C & D** are also closely related.  
- The **(C,D) group** is more distant from **A & B**.  

To manually create a tree, you will use your **distance matrix** to determine which species should be grouped together.  

### **Question 2:**  
- Based on your distance matrix, can you write a **Newick format tree** that represents the relationships between species?  

---

## **Constructing a Tree in iTOL**  

Now that you have your **Newick tree**, you will visualize it in **iTOL**.  

### **Steps:**  
1.)  Go to **[iTOL](https://itol.embl.de)** and create a **New Tree**.  
2.) Click on Upload, go to Upload new tree section and paste your **Newick tree** in the tree text box and click on Upload.    
3.) Save and export the tree as an image or pdf.  

### **Question 3:**  
- Based on this tree can you write down the sister relationships between different groups or species 
- Can you use this tree to answer your question (for eg: which ape is closely related to humans)? 
 
---

## **Report Submission**  

**Submit a pdf file with answers to the questions:**  
**Q1:** All questions asked above 
**Q2:** Your manually written **Newick tree**.  
**Q3:** A screenshot of your tree in **iTOL** or the saved tree image in pdf or SVG format.  
