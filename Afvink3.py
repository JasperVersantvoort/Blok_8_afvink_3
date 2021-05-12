from Bio import Entrez


def get_counts(term):
    Entrez.email = "JD.Versantvoort@student.han.nl"

    handle = Entrez.esearch(db="pubmed", term=term)
    record = Entrez.read(handle)
    handle.close()
    print(record["Count"])
    print(record["IdList"])
    return record["IdList"]


def query_maker(compounds, genes, effect):

    for comp in compounds.split("\n"):
        # print(comp)
        for gen in genes.split("\n"):
            # print(gen)
            for eff in effect.split("\n"):
                print("start query: "+ comp + " AND " + gen + " AND " + eff)
                id_list = get_counts(comp + " AND " + gen + " AND " + eff)



def main():
    compounds = open("compounds_klein.txt").read()
    genes = open("genes_klein.txt").read()
    effect = open("molecular_effects_klein.txt").read()
    # query_maker(compounds, genes, effect)
    print(get_counts("hart AND hearing AND ear"))



main()
