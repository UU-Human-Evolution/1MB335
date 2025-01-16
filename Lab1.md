# Session 1 - basic command line tutorial

Before doing anything, make sure you open the terminal window and log in, using the credentials you received from uppmax into your Solander accounts.

```
ssh username@solander.ibg.uu.se
```
- You might be asked to type in yes/no - type `yes`.
- Then type in your password (*you won't be able to see what you're typing in in the password field but it is working*)

*P.S. Make sure you're typing in the correct letters (confusion can occur as lower case 'l'/upper case 'I', the letter 'O' and zero etc may look the same)*

Awesome. Once that's done we can start with the exercizes.

### What is UNIX?
Unix is an operating system that was originally developed at Bell Labs in the 1970s. It is based around a "modular design" where tools do very distinct and narrow tasks. To complete more complex tasks multiple modules are then combined through the use of "pipes" - more about those later. 
If you are interested in learning more about UNIX then you can have a look at the [wikipedia article](https://en.wikipedia.org/wiki/Unix) for UNIX, it's quite thorough and well written.  
### Why are Unix systems so popular in science?
While there is no straightforward answer to this question there are some things that are often brought up. UNIX (and Unix-like systems) in its design is quite simple and is nowadays very portable. This has lead to it being used to run anything from massive high-performance computer clusters to tiny single-board computers such as Arduino & raspberry pis. This ubiquity and popularity is probably one reason why it is still so popular. Since the year 2000 Mac computers are also running on Apple's own Unix system, another popular Unix-like system is the Android mobile operating system. 
While the original UNIX operating system is a commercial system there are many Unix-like operating systems such as Linux which are free and open-source (_these are generally based on the Linux kernel_).
The ecosystem of open source and free distribution suits the academic world very well. It is not science if you aren't sharing your findings and how you came to your conclusions - that generally includes your code. 

#### Using UNIX
Interaction with UNIX-style systems is typically done through a command-line interface (CLI) - a `terminal` of some sort. There is generally no GUI (graphical user interface), though there exist protocols to display graphics through the terminal such as `X11`.

To communicate with the system there needs something to interpret the user's command. In a UNIX-like system, this is called a `shell`, one of the most common ones - and the one found on `Uppmax` is called Bourn-Again shell or simply `bash`.
It's an interpreter and it's own (basic) programming language. 

Enough exposition, let's get going. Open up the terminal and proceed with the exercise. 

![Figure 1](Figures/Version_7_Unix_SIMH_PDP11_Emulation_DMR.png)

**Terminal display for version 7 of Unix**

*(By Huihermit - Own work, CC0, https://commons.wikimedia.org/w/index.php?curid=30560188)*

### Before starting

#### OBS! Do steps A/B **only if you are using your own computer** and not the local computers in the Labs. Any downstream issues you may encounter are solely your responsibility if you choose to do so. We strongly recommend using the computers in the labs but it is still a matter of choice.
#### For everyone using the local computers, jump directly to the 'Baby steps in Terminal' section below.

#### A. For Mac users (Only if you are using your own computer)
The macOS operating system is a Unix-system so modern Macs can natively interact with other Unix systems. macOS comes with an inbuilt terminal application called simply `Terminal`. 
It is functional and gets the job down, we, however, recommend that you instead install `iTerm2`, which comes with several quality of life improvements.
Download it from [https://iterm2.com/](https://iterm2.com/)

MacOS comes with a very bare-bones version of Unix which lacks many tools that most Unix installations come with. Thus we recommend that you install [Homebrew](https://brew.sh/) which is a package manager for Mac which makes it super easy to install missing programs and tools.

To install `Homebrew`; open the terminal and run:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
*Note that this will take around 5 min to complete and you will be prompted for your user password. The installation requires around 10GB of space*

Then you can install some useful tools:

```
 brew install wget
 brew install w3m
 brew install tree

```

#### B. For Windows users (Only if you are using your own computer)
If you are on a Windows machine then the easiest option for you is to download `MobaXterm`.

[https://mobaxterm.mobatek.net/](https://mobaxterm.mobatek.net/)

Another option is to use the Ubuntu app from the Windows app store or to set up a dedicated Linux partition. If you know how to do that then go for it, if not stick to MobaXterm.

Open a local terminal and run the following command to install `w3m` which we will use in today's lab:

```

apt-get install -y w3m-img
```

### Baby steps in Terminal

#### Moving around
When you connect to a system you usually end up in your home directory. To see the path to where you stand use the `pwd` command. Try it now:

```
pwd
```

it should return something like:

```
/home/user_name
```

As you move around in the systems directories this will of course change.

To make a directory (called folders on other systems) use the command `mkdir`, try the following out:

```
mkdir directory1
```

To figure out what happened use the `ls` command which lists the content of the current working directory:

```
ls
```

As you can see `mkdir` makes directories, all (or at least most) UNIX commands are named after their function. 

To go to your new directory use `cd` (change directory);

```
cd directory1
```

Now try to create another directory called `directory 2`

```
mkdir directory 2
```

Take a look at what you did using the `ls` command.

Looks like you created two directories, one called `2` and another called `directory`. Since the basic syntax for UNIX commands is:

```
command option1 option2 option3
```

Each extra option to the command is separated by a space, which means that spaces and other white characters, such as tabs, are not allowed in file or directory names!

To fix this issue use `rm` for, you guessed it - remove.
We can remove both at the same time:

```
rm directory 2
```

Ouch, `rm` by default only removes files, not directories. You need to tell `rm` that you want it to work recursively, using what's typically called a flag, in this case `-r`.

```
rm -r directory 2
```

Check that is worked using `ls`.


Ok, let's try and make a second directory again:

```
mkdir directory2
```

change into it using `cd` 

```
cd directory2
```

So now your current directory should be `home/your_usename/directory1/directory2`, to find out use `pwd`. If you want to go one directory up, in our case from directory2 to directory1 you can use `..` notation:

```
cd ..
```

Check that it took you to the right place. Here are two need things to know about `cd`

```
cd -
```

takes you back to the last place you were standing.
Just `cd` with no options takes you to your home directory.



### Playing around with files

```
w3m -dump https://en.wikipedia.org/wiki/Principal_component_analysis > PCA.txt
```

The above command reads the Wikipedia page for Principal Component Analysis and extracts the body text and saves it to the file `PCA.txt`. The `>` is used to redirect output to a file.


Now that we have some text to work here are some tools for inspecting files, try them out on `PCA.txt`.

```
cat - concatenates the file contents to standard out (the screen)
less - a nice and easy file viewer, press q to quit!
more - more than less
head - look at the head of a file, by default the first 10 lines.
tail - looks at the tail of a file, by default the 10 last lines.
```

It turns out that the PCA article is quite big, how big?
Counting is hard and slow for humans but easy for machines. Use the word count command `wc` on the file to figure out how many lines, words and characters it contains. 

**Question 1: What did you get? How many lines and words?**

Hmm, it's not that clear, is it? Have a look at the manual for `wc` to try and figure it out. 
All core UNIX commands have an inbuilt manual you can access it through the `man` command:

```
man wc 
```

Now that you figured that out, use the manual for `head` to figure out how to save the first 100 lines of `PCA.txt` and save them into `short_pca.txt`.

You can use `wc` to figure out if you did it correctly.

#### grep
`grep` is a useful tool that prints lines matching a provided pattern.
In our example we can use it to figure out how many lines contain the word `PCA`:

```
grep PCA short_pca.txt
``` 


### Pipes and multiple commands
One of the fundamental concepts behind UNIX from the beginning was an emphasis on small task-specific programs. These programs could then be chained together into pipelines to perform more complex tasks.

Imagine that you have a machine that cuts down trees, de-barks them, and cuts them into planks. If you have trees and want planks then this is fine, but what happens if you want to cut down the tree and keep the whole log? Your big fancy machine only makes planks.
In the UNIX world, your one machine would consist of smaller machines chained together. One that cuts down the tree, one that removed the bark, and one that cuts into planks. 
If you get a pile of logs from your neighbor then you can use one of your machines to make planks, etc.

This type of chaining together is called piping in UNIX and is done by the pipe character `|`. e.g.

```
command 1 | command 2 | command3 > output_file
```

By using `grep`, `pipe`, and `wc` we can now easily figure out how many lines of the Wikipedia article about Principle Component Analysis contains the word `PCA`:

```
grep PCA short_pca.txt | wc -l
```

Try it for the full article as well!

**Question 2:** **Write down how many times the term`"PCA"` appears in both the full `PCA.txt` and the `short_pca.txt` files.** 
Remember that there can be more than one hit per line so you need to account for that! Using grep alone might not lead to the correct answer (Hint! Try combining it with flags!)

--

### Hidden word exercise 
**Question 3:**
Now that you have some basic UNIX tools at your disposal go and do the [hidden word_exercise](hidden_word_exercise_instructions.md). (*Note*: You will need to download a file for this exercise. When working remotely, you can download it to your local computer first and then use `scp` (Description at the bottom of this page) to copy it to the remote computer.)
Submit the hidden word.

Do not continue with the next part until you are done with the hidden word exercise. 

**Question 4:** Write down the command you used to extract the name and nucleotide sequence!
This should be done in **one** command.

### sed and regex
Regular expressions(regex) are used to catch and match certain words or phrases. E.g
^
`^P[0-9]+` will match at the beginning of a line(`^`) the letter P literally, any  number (`[0-9]`) repeating (`+`)
it will thus catch the top line but not the second:

```
P674353
454646464 P 
```
These types of expression can be very useful and powerful 

`sed` is a powerful tool for editing streams of files. It is a common way of using rexes in Unix. It's often used to replace one thing with another:

if `My_file.txt ` contains:

`dog dog dog`

Then:

```
sed 's/dog/cat/' My_file.txt. # s is for substitute
cat dog dog
```
the first instance of `dog` is replaced with `cat`. We can also replace all instances using the `g` global flag:

```
sed 's/dog/cat/g' My_file.txt. # sg - substitute globally
cat cat cat
```

You can use `sed` on piped output from another program or straight on a single file. For a summary of some things that you can do with it have a look at [this link](https://github.com/tldr-pages/tldr/blob/master/pages/common/sed.md).

**Question 5 :**
You have been given a file that has been exported from excel in an odd format (something that is all too common in the life of a bioinformatician). Your task is to transform the file [orange.csv](example_data/orange.csv) into a normally formatted `.csv`-file. That is the decimal point should be a `.` and the delimiter (what separates one column from another) should be `,`. It also looks like someone has accidentally inserted some letters among the numbers, they also need to be removed.

Submit what `sed` command(s) you used to clean the file. (Make sure that it looks correct, i.e. **all** columns are separated with a comma)

_You will probably have to look up more information on how to do this. You can use `man sed` or `info sed` for more information, or google your way to it. As long as you know what your command does_

Note that if you want to upload the file to your Uppmax results you can use the `scp` command, you can find an example of how to use it at the bottom of the page.

### Basic bash scripting for future reference 
Bash is a programming language in itself so it is possible to set up quite advanced workflows with it. The most simple bash script is just a normal command you would type on the command line saved to a file. Or more realistically you might want to run a couple of things that take a few minutes or hours after each other.
This is something that you definitely will do in your future bioinformatics career.

An example of something like that:

```

echo “Wait for 5 seconds”
sleep 5
echo “Completed”

```

Add the above text to a file called `sleep.sh` and execute it with:

```
bash sleep.sh
```

You can see that the code is executed sequentially, it does not progress to the next line until the previous one has finished.

---


You can chain any type of program/script that you can run on the commandline like this, even those you have written yourself like the `perl` programs you ran in the hidden word excercise or the scripts you will write in Lab 2:

```
python my_python_script.py inputfile.txt

```

This is the end of the lab, please make sure that you did and wrote down the answers to all of the questions.
Also, make sure to delete any files that you no longer need - you can copy them somewhere else if you want to keep them.




Exercise: Downloading, Unzipping, and Transferring Files Using ssh and scp In this exercise, you will practice using ssh and scp to download a zipped file from GitHub, unzip it on your local machine, and then transfer the unzipped files to your profile on the Solander server. This workflow is common in bioinformatics for managing and transferring data.

Step 1: Download the Zipped File from GitHub Using scp

Note: Typically, scp is used for copying files between local and remote systems via SSH. To download files directly from GitHub, tools like git, wget, or curl are more commonly used. However, for the purpose of this exercise, we will simulate downloading a file using scp.

First, you'll use scp (Secure Copy) to download a zipped file from a GitHub repository to your local computer. Replace <github-username>, <repository>, and <file.zip> with the appropriate GitHub username, repository name, and file name.

scp <github-username>@github.com:<repository>/<file.zip> ~/Downloads/

Example:

scp johndoe@github.com:bioinformatics-tools/data.zip ~/Downloads/

This command copies data.zip from the GitHub repository bioinformatics-tools owned by johndoe to the Downloads directory on your local machine.

Step 2: Unzip the Downloaded File Using unzip

Once the file is downloaded, navigate to the Downloads directory and unzip the file using unzip. Note that gunzip is typically used for .gz files. If you're dealing with a .zip file, it's better to use unzip.

cd ~/Downloads/ unzip data.zip

If you're dealing with a .gz file:

gunzip data.gz

This command extracts the contents of data.zip into the current directory.

Step 3: Transfer the Unzipped Files to Your Solander Server Profile Using scp

After unzipping the files, you can transfer them to your profile on the Solander server. There are two methods to specify the destination directory on the server: using an absolute path or using . to represent the current directory.

Method 1: Using an Absolute Path Replace <your-username> with your actual username on the Solander server and <solander-server-address> with the server's address.

scp -r ~/Downloads/data <your-username>@<solander-server-address>:~/your-profile-directory/

Example:

scp -r ~/Downloads/data johndoe@solander.server.edu:~/bioinformatics_project/

The -r flag is used to copy directories recursively. ~/Downloads/data is the path to the unzipped data on your local machine. johndoe@solander.server.edu is your SSH username and the Solander server address. ~/bioinformatics_project/ is the destination directory on the Solander server where you want to store the data.

Method 2: Using . to Represent the Current Directory Alternatively, you can use . to indicate that the files should be copied to the current directory on the remote server. This method is especially useful when you are already within the desired destination directory on the server.

SSH into the Solander Server and Navigate to the Desired Directory

ssh johndoe@solander.server.edu

Once logged in, navigate to the directory where you want to place the files:

cd ~/bioinformatics_project/

Open a New Terminal Window or Tab on Your Local Machine Keep the SSH session open in the first terminal.

Use scp with . as the Destination

scp -r ~/Downloads/data johndoe@solander.server.edu:.

Here, . represents the current directory (~/bioinformatics_project/) on the Solander server where you navigated in the SSH session. This command copies the data directory directly into the current directory on the server without needing to specify the full path.

Advantages of Using .:

Simplicity: Reduces the need to type or remember long directory paths. Flexibility: Especially useful when you have already navigated to the desired directory via SSH.

Step 4: Verify the Transfer

To ensure that the files have been successfully transferred, you can SSH into the Solander server and list the contents of the destination directory.

ssh johndoe@solander.server.edu ls ~/bioinformatics_project/

You should see the transferred data directory listed.


