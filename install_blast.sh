### Installing BLAST+ locally
#move to root
cd
#Downloading
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-$1+-x64-linux.tar.gz
#Unzip
tar -zxvf ncbi-blast-$1+-x64-linux.tar.gz
#Set Paths
export PATH=$HOME/tools/BLAST/ncbi-blast-$1+/bin:$PATH
echo export PATH=$HOME/tools/BLAST/ncbi-blast-$1+/bin:$PATH >> .bash_profile
echo export PATH=$HOME/tools/BLAST/ncbi-blast-$1+/bin:$PATH >> .bashrc


