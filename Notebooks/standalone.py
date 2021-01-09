#import sys
#import os.path

def write2file(gene_list, out_file1):
    """
    Takes a gene list and writes the output to file
    """
    with open("/home/eanbit12/Python4Bioinformatics2020/Notebooks/out_file1", 'w') as outfile1:
        outfile1.write('\n'.join(gene_list))

def remove_empty(gene_list):
    """
    Given a gene list, removes items
    that start with dash (empty)
    """
    tag = True
    while tag:
        try:
            gene_list.remove('-')
        except ValueError:
            tag = False
    return gene_list

def clean_genes(input_file, out_file1):
    """
    Given a chromosome annotation file, extract the
    genes and write them to another file
    """
    gene_list = []
    tag = False
    with open("/home/eanbit12/Python4Bioinformatics2020/Notebooks/humchrx.txt", 'r') as humchrx:
        for line in humchrx:
            if line.startswith('Gene'):
                tag=True
            if line == '\n':
                tag = False
            if tag:
                gene_list.append(line.split()[0])
    #clean the gene list
    gene_list.pop(2)
    gene_list[0] = gene_list[0]+"_"+gene_list[1]
    gene_list.pop(1)
   
    gene_list = remove_empty(gene_list)
   
    ## Writing to file
    write2file(gene_list, out_file1)
clean_genes('/home/eanbit12/Python4Bioinformatics2020/Notebooks/humchrx.txt', '/home/eanbit12/Python4Bioinformatics2020/Notebooks/testing.txt1')

print('bye')