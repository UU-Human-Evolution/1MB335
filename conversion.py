#This script uses a conversion table to switch between a short and a long header name
import sys
import argparse

def read_conversion_table(conversion_table_file):
    """Reads the conversion table and returns a dictionary for quick lookup."""
    conversion_dict = {}
    with open(conversion_table_file, 'r') as f:
        for line in f:
            long_name, short_name = line.strip().split('\t')
            conversion_dict[long_name] = short_name
            conversion_dict[short_name] = long_name  # Add reverse mapping
    return conversion_dict

def update_fasta_headers(input_fasta, output_fasta, conversion_dict, target_format):
    """Updates FASTA headers based on the target format (short or long)."""
    with open(input_fasta, 'r') as infile, open(output_fasta, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):
                header = line.strip()
                if target_format == 'short' and header in conversion_dict:
                    outfile.write(conversion_dict[header] + '\n')
                elif target_format == 'long' and header in conversion_dict:
                    outfile.write(conversion_dict[header] + '\n')
                else:
                    outfile.write(line)  # Keep unchanged if no match
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
