import os

os.getcwd()
os.chdir("/Users/pramod/Desktop/Proteomics/16p_proteomics_1m_organoids")

def parse_census(filename):
    current_protein = None
    protein_data = list()
    sequence_data = list()

    with open(filename, "r") as infile:
        for line in infile.readlines():
            line = line.strip().split('\t')
            if line[0] == "H":
                if line[1] == "PLINE":
                    header_protein = '\t'.join(line)
                elif line[1] == "SLINE":
                    header_sequence = '\t'.join(["PROTEIN"] + line[1:])
                else:
                    continue
            if line[0] == "P":
                current_protein = line[1]
                protein_data.append('\t'.join(line))
            elif line[0] == "S":
                line = [current_protein] + line
                sequence_data.append('\t'.join(line))
        protein_data = [header_protein] + protein_data
        sequence_data = [header_sequence] + sequence_data
    
    return(tuple([protein_data, sequence_data]))

if __name__ == "__main__":

    filenames = [
        "census-out-15467-16p_1month_1_A-Pri.txt",
        "census-out-15538-16p_1month_1_B-Pri.txt",
        "census-out-16385-16p_1month_2_A-Jorge.txt",
        "census-out-16386-16p_1month_2_B-Jorge.txt"
    ]

    output_filenames = [
        "data/census-out-15467-16p_1month_1_A-Pri.txt",
        "data/census-out-15538-16p_1month_1_B-Pri.txt",
        "data/census-out-16385-16p_1month_2_A-Jorge.txt",
        "data/census-out-16386-16p_1month_2_B-Jorge.txt"
    ]

    for f, o in zip(filenames, output_filenames):
        with open(o, "w") as ofile:
            ofile.write('\n'.join(parse_census(f)[1]))
