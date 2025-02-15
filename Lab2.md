# **Lab 2 - Database Search & Phylogenetics**

## 0.0 **Introduction**  

Mitochondria are present in all eukaryotic cells, where they play a crucial role in energy production (ATP synthesis). Their genomes are relatively small (~16,000 bp in humans), making them easier to analyze compared to nuclear genomes. Additionally, they exist in multiple copies per cell, making them easier to sequence, even in challenging conditions such as environmental DNA or ancient DNA studies.  

Despite differences between species, mitochondrial genomes contain a core set of conserved **protein-coding genes, rRNAs, and tRNAs**, making them ideal for **comparative phylogenetic analysis**.  

![](Figures/Mitochondrion_structure.svg)


**Figure 1: Simplified structure of a mitochondrion.** 
*By Kelvinsong; modified by Sowlos - Own work based on: Mitochondrion mini.svg, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=27731882*

---

## 0.1 **Overview of Sessions 2 to 6 in the next few weeks to come**  

In this multi-session project, you will work in groups to answer an **evolutionary question** using bioinformatics methods.  

| **Lab**  | **Focus**  | **Tools Used**  |
|----------|-------------------------------|------------------------------------|
| **Lab 2**  | **Download genes & create datasets**  | NCBI GenBank, Python (data handling)  |
| **Lab 3**  | **Sequence alignment & visualization**  | MAFFT (alignment), AliView (visualization)  |
| **Lab 4**  | **Distance matrix and simple trees**  | ITOL, Newick format  |
| **Lab 5**  | **Blast, Phylogenetic tree construction & visualization**  | Online BLAST, IQ-TREE (model selection), FigTree (tree visualization)  |
| **Lab 6**  | **Finalizing results & presentation**  | Compare findings to known phylogenies, finalize project report  |

---

## 0.1.1 **Project Steps explained**  

### **Step 1: Define Your Research Question (Lab2)**  

Each group will investigate **one evolutionary relationship** (see questions below). Discuss:  
- **Which species to include** in your analysis.  
- **What makes a good outgroup** to root your phylogenetic tree.
- Write a few sentences on the selection of species and outgroup in your dataset. Which species did you choose and why? Explain how the species you picked will help resolve the phylogenetic relationship posed by your question  

---

### **Step 2: Gather Mitochondrial Gene Sequences (Lab2)**  

For each species:  
- **Search for mitochondrial COX1 and CytB genes** on [NCBI GenBank](https://www.ncbi.nlm.nih.gov/nucleotide/).  
- **Download sequences in FASTA format** (preferably full-length, high-quality sequences).  
- **Name your files clearly** (e.g., `Tiger_CytB.fasta`, `Tiger_COX1.fasta`).  
- If a species lacks a sequence, **find a closely related alternative** or ask the TAs for guidance. 
- Write a simple Python code for easily switching between long/short taxonomical names. 

*Tip:* If you are unsure whether a sequence belongs to the correct species/gene, you can check its annotation in GenBank or verify using **BLAST** in the next lab.  

---

### **Step 3: Build Phylogenies (Lab3, Lab4, Lab5)**  

- **Align your sequences** using **MAFFT**.  
- **Visualize your alignments** with **AliView**.  
- **Construct two separate phylogenetic trees** (one for COX1, one for CytB) using **IQ-TREE**.  
- **Compare your two trees**—do they tell the same evolutionary story?  

---

### **Step 4: Compare to Established Phylogenies (Lab6)**  

- **Use phylogenetic databases** (e.g., TimeTree, NCBI Taxonomy) to compare your results with existing knowledge.  
- **Are your trees consistent with known evolutionary relationships?** If not, why might that be?  

---

### **Step 5: Final Report & Presentation (Lab6)**  

Prepare a summary including:  
- **Your phylogenetic trees** (constructed using **IQ-TREE** and visualized with **FigTree**).  
- **A brief explanation of your findings**.  
- **How your results compare to known phylogenies**.  
- **Save your best-looking phylogenies and be ready to present them to the TAs!**  

---
### 0.1.2 **Final Notes**  

- Keep in mind that you're analyzing only mitochondrial genes, which represent just a small portion of the genome. Your results may not always align perfectly with broader evolutionary relationships.
If your findings seem unexpected, consider possible explanations such as incomplete lineage sorting, hybridization, or selection pressures.
- Stay organized! Clear file names and structured folders will make your work much easier.
- Since you will be producing numerous files, use **self-explanatory filenames** and maintain a **good folder structure**. This will make your work easier. It might be a good idea to write a short description about how the archive is organized and where the files are located (e.g., trees, scripts, alignments, etc.).
- Think critically about your choices—species selection, data quality, and analysis parameters will all influence your results. The lab assistants are here to guide you, but ultimately, your decisions shape your conclusions.

## 0.2 **What is an Outgroup?**

An outgroup is a species or group that is outside the main group of interest (the ingroup) but still related enough to be useful for comparison. It serves as a reference point to root the phylogenetic tree and determine the direction of evolutionary change. By comparing the ingroup to the outgroup, we can infer which traits or genetic differences are ancestral and which are derived.

However, choosing an appropriate outgroup is important:

- Avoid selecting an outgroup that is too distantly related, as this can lead to long branch attraction, a phenomenon where rapidly evolving sequences from distant species artificially cluster together, distorting true relationships.
- The ideal outgroup should be roughly equidistant to all members of the ingroup, meaning it shares a common ancestor with the ingroup but branched off before the ingroup species started diversifying.
- Using multiple outgroups is often beneficial, as it provides additional reference points and helps ensure a more reliable tree rooting.
- By carefully selecting an outgroup, we improve the accuracy of our phylogenetic tree and avoid misleading conclusions.

To better understand the concept of ingroup and outgroup, refer to the diagram below:

![](Figures/Outgroup.jpg)
_By Ngilbert202 - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=63950569_

In this example, the goal is to determine whether C is more closely related to B or D. The analysis shows that C is closer to D, as they share a more recent common ancestor. 


## 0.3 Group Tasks (Each Group gets one of these questions to answer):

**1. Canids and the Domestication of Dogs**

Among living canids (wolves, coyotes, jackals, etc.), which lineage is the closest relative of domestic dogs, and how do different wolf populations group relative to domestic dogs?
- Consider including domestic dogs and various wild canids.
- You might want to sample more than one wolf population to see how they cluster.
Outgroup suggestion: A more distantly related carnivore, that is cunning and farmers hate.

**2. Ape Relationships Within Hominidae**

Describe the relationship among humans, chimpanzees, bonobos, gorillas, orangutans, and gibbons. Which lineages split first, and which are most closely related? Do both genes tell the same story?
- Include multiple apes.
- You might want to sample different subspecies if available (e.g., for gorillas or orangutans).
Outgroup suggestion: An Old World or New World animal that climbs trees and loves bananas.

**3. Big vs. Small Cats in Felidae**

How do ‘big cats’ (lions, tigers, leopards, jaguars) compare to smaller felids (domestic cats, lynxes, pumas, ocelots, cheetahs)? Which lineages diverged earliest?
- Consider multiple species from both large and small cat lineages.
- Feel free to include extra small cat species (e.g., servals, caracals) if data are available.
Outgroup suggestion: A carnivoran that doesn't 'meow'.

**4. True Bears vs. Pandas**

Among the bear family (Ursidae), is the giant panda truly a bear, or does it form a separate lineage?
- Focus on diverse bear species from around the globe.
- Be sure to include the giant panda and at least two or three other bears.
Outgroup suggestion: Another carnivoran that is not a bear.

**5. Deer Family Dynamics Question**

In the deer family (Cervidae), how do moose, reindeer, white-tailed deer, red deer, fallow deer, and roe deer cluster? Do moose and reindeer group together, or do they pair with other deer first?
- Pick multiple deer species from different genera.
- Consider including a few lesser-known deer if available.
Outgroup suggestion: A different artiodactyl, perhaps something with a really long neck.

**6. Turtles and Tortoises**

How do sea turtles (green, loggerhead, hawksbill) cluster relative to freshwater turtles and giant tortoises, and which lineages seem most ancient?
- Include more than one sea turtle, and at least one freshwater turtle.
- You might include giant tortoises and a box turtle if possible.
Outgroup suggestion: Try something that is a close friend of Voldemort or something that does model work for Lacoste.

**7. Cetacean Radiation**

Describe the relationships among cetaceans. How do baleen whales (e.g., blue, humpback, fin) compare with toothed whales (sperm whale, orca, dolphins)? Which group appears most basal?
- Try more than one baleen whale species and multiple toothed whales.
- Look for any species with complete or partial sequences in databases.
Outgroup suggestion: Try a mud-loving artiodactyl.

**8. The Land Down Under**

How do Australian marsupials—including macropods (kangaroos, wallabies, quokkas), possums, and the Tasmanian devil — cluster relative to their closest marsupial relatives in mainland Asia (e.g., cuscuses and phalangers)? Do Australian marsupials form a single evolutionary group distinct from their Asian cousins, or do some species share closer relationships across the regions?
- Include different kangaroo and wallaby species.
- Include Tasmanian devils, wombats, koalas, and possums to see how they fit in the tree.
- Compare them with cuscuses and phalangers from Southeast Asia.
Outgroup suggestions: A South American marsupial (Opossum for example) or Perry the Platipus. 

**9. Penguins and Their Allies**

Within living penguins (emperor, king, gentoo, Adélie, chinstrap, rockhopper, little blue, etc.), which cluster closely, and which lineages diverged first?
- Try sampling multiple penguin species from different genera or habitats.
- Look for both subantarctic and Antarctic species if possible.
Outgroup suggestions: A non-penguin seabird.

**10. Arachnid Phylogeny**

Among spiders, scorpions, harvestmen (opiliones), and pseudoscorpions, which are closest relatives, and do scorpions cluster more closely with spiders or other arachnids?
- Include different spider species (orb weaver, tarantula, jumping spider).
- At least one scorpion, one harvestman, and a pseudoscorpion if you can find data.
Outgroup: A non-arachnid arthropod.

# 1.0 **Data Gathering and Dataset Preparation**

#### **Objective**
In this segment of the Lab2, you will:
1. **Select species** relevant to your phylogenetic question.
2. **Choose appropriate outgroups** for rooting your phylogenetic tree.
3. **Retrieve mitochondrial gene sequences (COX1 and CytB) from GenBank**.
4. **Organize your files properly** on the server.

---
## 1.1 **Set Up Your Workspace on the Server**

Since you will be working with multiple species and genes, it’s important to maintain a **structured directory setup**.

Open a terminal and connect to the server just like in Lab1:

```
ssh username@solander.ibg.uu.se
```
#### **Create a Project Directory**  

Once logged in, navigate to your profile directory and create a new folder for this project:

```
mkdir -p ~/Lab2_Phylogenetics
```
```
cd ~/Lab2_Phylogenetics
```

#### **Create Subdirectories for Each Gene**  

To keep your files organized, create separate folders for the two mitochondrial genes:

```mkdir COX1``` and ```mkdir CytB```

Your directory structure should now look like this:

```
~/Lab2_Phylogenetics/
│── COX1/  # All COX1 gene sequences go here
│── CytB/  # All CytB gene sequences go here
```

## 1.2 **Make a list and select the species you will work with**

- Discuss within your group which species you need to answer your chosen question.
- Choose an appropriate outgroup species that is distantly related to the groups you are comparing.
- If you need guidance, use the NCBI Taxonomy Browser.
- Make a list and aim for around 10 species, including at least one outgroup.
- The outgroup should be evolutionarily distant but not too far (avoid excessively long branch lengths in the phylogenetic tree).

## 1.3 **Retrieve Sequences from GenBank**

Your task is to **download the mitochondrial genes COX1 and CytB** for all species in your dataset. There are many ways you can get to the sequences of interest so it may be confusing at first. Below are **two methods** you can use to obtain the sequences.

### 1.3.A **Method 1: Direct Search for COX1 & CytB**  
This is the **quickest** way to retrieve mitochondrial genes if they are available as standalone entries.

#### **Access GenBank**  
- Go to **[NCBI GenBank](https://www.ncbi.nlm.nih.gov/nucleotide/)**.  
- In the **search bar**, type:  
```[Species Name] COX1```

**Example:**  
```Panthera leo COX1```

- Press **Enter**.

#### **Filter the Results**  
- If there are many results, use the **filters on the left sidebar**:  
- Under **Genetic compartments**, select `mitochondrion`.  
- This will narrow down the search to **mitochondrial COX1 sequences**.

#### **Download the COX1 Gene**  
- Click on the most **relevant** entry.  
- Click on the **FASTA** format option.  
- Save the file as:  
```Panthera_leo_COX1.fasta```


#### **Repeat for CytB**  
- In the **search bar**, type:  
```
[Species Name] CytB
```
**Example:**  
```
Panthera leo CytB
```
- Click on the most **relevant** entry.  
- Select **FASTA** format.  
- Save the file as:  
```Panthera_leo_CytB.fasta```

This method is the fastest and easiest for downloading mitochondrial genes if they are available as standalone sequences. They may not always be available though!

---

### 1.3.B **Method 2: Extract COX1 & CytB from Full Mitochondrial Genome**  
If standalone COX1 or CytB sequences are **not available**, use this method.

#### **Search for Full Mitochondrial Genome**  
- In the **NCBI GenBank** search bar, type:  
```
[Species Name] mitochondrion complete genome
```
**Example:**  
```
Panthera leo mitochondrion complete genome
```
- Press **Enter**.

#### **Select the Correct Entry**  
- Look for an entry labeled **“complete genome”** in the search results.  
- Click on the entry to open the **full genome record**.

#### **Scroll Down to the "FEATURES" Section**  
- Find the section labeled **"CDS" (Coding Sequences)**.  
- Look for **COX1 (Cytochrome c oxidase subunit I)** and **CytB (Cytochrome b)**.

#### **Extract COX1 & CytB**  
- Click on **COX1** to open its detailed page.  
- Click **FASTA format** to download.  
- Save the file as:  
```Panthera_leo_COX1.fasta```
- Repeat the same process for **CytB**.  
```Panthera_leo_CytB.fasta```

#### ** OBS! Make sure you aren't saving entire mitochondrial genomes! These will be a lot bigger than the lenght of a single gene. Always check the lenghts (in base pairs) of the genes you are saving. Mitochondrial genes will be in the range of hundreds to a thousand while entire genomes will be tens of thousands BP long!**

You can check using:
```
wc -l Panthera_leo_COX1.fasta
```

#### If a species lacks one or both sequences and you've tried both of these methods:
- Try a Close Relative: Select a closely related species with the missing gene(s).
- Ask for Assistance: If you struggle to find enough species with both sequences, consult a teaching assistant.

**By the end of this step, you should have two FASTA files per species, one for COX1 and one for CytB!**

#### 1.4 **Organize and Name Your Files**

To ensure clarity, follow a consistent naming convention for your files:

```SpeciesName_Cox1.fasta```
```SpeciesName_CytB.fasta```

Example:

```Pan_troglodytes_Cox1.fasta```
```Pan_troglodytes_CytB.fasta```

#### 1.5 **Transfer Files to your directory on the server**
#### **Upload Files Using SCP**  

On the server: Create the two directories `CytB` and `COX`.

Locally: Just like in Lab1, navigate to the directory where you downloaded your sequences on your ***local machine*** and use the same commands to transfer the files to your COX1 and CytB directories ***on the server***. Make sure you verify the file transfer and confirm the files have been uploaded.

Example:
```
ls thecorrectpathto/Lab2_Phylogenetics/COX1/
ls thecorrectpathto/Lab2_Phylogenetics/CytB/
```

***Question 1***

You have by now probably obtained both Cox1 and CytB sequences for every species in your dataset.
Write a few sentences on the selection of species and outgroup in your dataset. Which species did you choose and why? Explain how your selections will help resolve the phylogenetic relationship posed by your question. If you had difficulties finding some, write that as well.

**This may be a good place for a short break**

# 2.0 **Working with FASTA files**

Now that you have the sequences, let’s take a quick look inside a FASTA file.
FASTA is a simple text-based format used for storing biological sequences. Each entry follows this structure:

```
Header (contains species name & gene info) 
ACTGACTGACTGACTGACTGACTGACTG 
ACTGACTGACTGACTGACTGACTGACTG
````
#### 2.1 **Open a FASTA File**

Use `more` or `less` to view the contents of a FASTA file:

```
more Pan_troglodytes_Cox1.fasta
```

Example output:

```
NC_001643.1 Pan troglodytes cytochrome c oxidase subunit 1 (COX1) gene ATGGTAGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGA 
GAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGA 
GAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGA
```

#### **Close the Viewer**
To **exit** the `less` or `more` viewer, press:
```q```

#### **What You Just Saw**
- The **first line** (starting with `>`): Contains the sequence ID, species name, and gene information.
- The **following lines**: The nucleotide sequence (A, T, C, G).

Understanding the structure of FASTA files will be important when performing sequence alignment in the next lab.

## 2.2 **Data Gathering and Dataset Preparation**

#### **2.2.1 Merge FASTA Files for the Entire Dataset**

Now that you have downloaded individual COX1 and CytB sequences for each species, you will need to **combine them into two single FASTA files**:
- **One for COX1** (all species in one file)
- **One for CytB** (all species in one file)

#### **2.2.2 Merge Sequences into a Single FASTA File**
You can go step by step and copy each of the Fasta file's content into a file, or, much more elegantly, you use the `cat` command to merge all sequences.

```
cat *.fasta > merged_Cox1.fasta
```

Check your progress with 
```
less merged_Cox1.fasta
```
and make sure you haven't duplicated anything.

---

## 2.3 **Create a Name Conversion Table**

To facilitate working with the FASTA files, you will create **conversion tables** that map different versions of sequence headers. This will allow switching between:
1. **Short names** (e.g., `cytB_V_ursinus` for CytB or `cox1_V_ursinus` for COX1)
2. **Full headers** (the original header from GenBank)

### **2.3.1. Create Two Conversion Tables**
You will create two **tab-separated** files:
- **`conversion_table_Cox1.tsv`** → For COX1 dataset
- **`conversion_table_CytB.tsv`** → For CytB dataset

Each row in the table should follow this format:

```Short_Name<TAB>Full_Header```


#### **Example for CytB:**

```
cytB_V_Ursinus  NC_003322.1 Vombatus ursinus mitochondrion, complete genome 
cytB_H_sapiens  NC_003562.2 Homo sapiens mitochondrion, complete genome 
cytB_N_neander  NC_004571.2 Homo neanderthalensis mitochondrion, complete genome
```
For example, the first column should be the new (short) header, and the second is the original full lenght name.

** Important Notes:**

- **Use tabs (`\t`)** between columns, **not spaces**.
- **Be consistent** with naming conventions.
- If using Excel, make sure to save as **tab-separated values (.tsv)**, not a regular `.csv`.

To check your table after creation, use:
```
less conversion_table_CytB.tsv less conversion_table_Cox1.tsv
```

---
## 2.4 **Create a Python Script that can easily switch between FASTA Headers**

Now, you will write a **Python script** that:
1. **Takes a merged FASTA file as input** (`merged_Cox1.fasta` or `merged_CytB.fasta`).
2. **Uses your conversion table (`.tsv`)** to modify sequence headers.
3. **Allows switching between short and full headers** based on user input.
4. **Overwrites the original FASTA file** rather than creating a new one.

### **2.4.1 Example Script (`rename_headers.py`)**
Create a new Python script called `rename_headers.py` with the following functionality:

- The script will take **two arguments**:
  1. The **FASTA file** to modify.
  2. The **conversion table (`.tsv`)**.
  3. A **choice** to switch to either "short" or "full" headers.

---

### **2.4.2 Expected Usage:**

To rename headers to short format:
```
python rename_headers.py merged_Cox1.fasta conversion_table_Cox1.tsv short
```

To rename headers to full format:
```
python rename_headers.py merged_Cox1.fasta conversion_table_Cox1.tsv full
```
---

## **2.5 Final Checks**
Before submitting:
- **Run the script on both merged FASTA files.**  
- **Verify that headers change correctly by inspecting the output with `less` or `head`.**  
- **Ensure the final FASTA files contain the correct sequences and headers.**  
- **Confirm that your script does NOT create duplicate files but modifies the original.**  
- If you encounter issues with tab separation in your `.tsv` files, **check them with `cat -A conversion_table_Cox1.tsv`** to ensure tabs (`^I`) are correctly formatted.
- If something unexpected appears in your results, check for **hidden spaces or misformatted input files**.
- If your script does not work as expected, try running it on a **smaller test dataset** to debug before applying it to the full dataset.

### ** Question 2 **
Once your script works, submit:
- Your **Python script (`rename_headers.py`)**.
- The **two conversion tables** (`conversion_table_Cox1.tsv` and `conversion_table_CytB.tsv`).
- Your **merged FASTA files** (`merged_Cox1.fasta` and `merged_CytB.fasta`).

---

### **Lab2 Submission Instructions**

Submit the following files:  
- **Question 1**: A text document with your species selection explanation.  
- **Question 2**:  
  - **Python script** (`rename_headers.py`)  
  - **Two conversion tables** (`conversion_table_Cox1.tsv`, `conversion_table_CytB.tsv`)  
  - **Merged FASTA files** (`merged_Cox1.fasta`, `merged_CytB.fasta`)  
  - Indicate whether you used AI assistance and what prompts you used.  

### **Important Notes**
- **Submit code files in their original format** (`.py`, `.sh`).  
- **Non-code answers should be in text formats** (`.pdf`, `.txt`, `.docx`), NOT in `.pdf` for code.  
- **Clean up unnecessary files** on both the local computer and server.  
- **Double-check that your script works before submission.**  

Good luck!
