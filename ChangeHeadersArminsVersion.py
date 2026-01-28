# rename.headers.py
import sys
import argparse

def read_conversion_table(conversion_table_file):
    """Reads the conversion table and returns a dictionary for long -> short lookup."""
    conversion_dict = {}
    with open(conversion_table_file, 'r') as f:
        for line in f:
            long_name, short_name = line.strip().split('\t')
            conversion_dict[long_name] = short_name
    return conversion_dict

def update_fasta_headers(input_fasta, output_fasta, conversion_dict, target_format):
    """Updates FASTA headers based on the target format (short or long)."""
    with open(input_fasta, 'r') as infile, open(output_fasta, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):
                header = line.strip()
                if target_format == 'short' and header in conversion_dict:
                    # Replace long header with short header
                    outfile.write(conversion_dict[header] + '\n')
                else:
                    # For 'long' or unmatched headers, keep original
                    outfile.write(line)
            else:
                outfile.write(line)

def main():
    parser = argparse.ArgumentParser(description="Convert FASTA headers between short and long formats.")
    parser.add_argument('fasta_file', help="Input FASTA file")
    parser.add_argument('conversion_table', help="Conversion table file")
    parser.add_argument('output_file', help="Output FASTA file")
    parser.add_argument('format', choices=['short', 'long'], help="Target header format: 'short' or 'long'")
    
    args = parser.parse_args()

    # Read the conversion table into a dictionary
    conversion_dict = read_conversion_table(args.conversion_table)

    # Update the FASTA headers
    update_fasta_headers(args.fasta_file, args.output_file, conversion_dict, args.format)

if __name__ == '__main__':
    main()


########note the format of the file with headers should look like this (without the hasthtags)
#>PQ130352.1 Tubastraea sp. COX1 (COX1) gene, complete cds; mitochondrial	>Tubastraea
#>PQ554647.1 Salvinia molesta Cox1 (cox1) gene, complete cds; mitochondrial	>Salvinia_molesta
#>PQ554610.1 Marsilea mutica Cox1 (cox1) gene, complete cds; mitochondrial	>Marsilea_mutica
