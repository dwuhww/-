def get_gene_string():
    gene_string = input("Enter a genome string(with A,C,T,G):")
    number = 0
    for i in gene_string:
        if i in "ATCG":
            number += 1

    if number == len(gene_string):
        return gene_string
    else:
        print("no gene is found")
        return 0

def check(gene_string):
    gene_list = []
    atg_split_list = gene_string.split("ATG")
    if len(atg_split_list) > 1:
        atg_split_list.pop(0)
    for i in atg_split_list:
        if ("TAG" in i):
            gene1 = i.split("TAG")[0]
            if len(gene1)%3==0:
                gene_list.append(gene1)
        elif("TAA" in i):
            gene2 = i.split("TAA")[0]
            if len(gene2) % 3 == 0:
                gene_list.append(gene2)
        elif("TGA" in i):
            gene3 = i.split("TGA")[0]
            if len(gene3) % 3 == 0:
                gene_list.append(gene3)
        else:
            print("no gene is found")

    if len(gene_list) == 0:
        print("no gene is found")
    else:
        for i in gene_list:
            print(i)


gene_string = get_gene_string()
if gene_string != 0:
    check(gene_string)









