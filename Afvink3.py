from Bio import Entrez, Medline


def get_counts_idlist(term):
    Entrez.email = "JD.Versantvoort@student.han.nl"

    handle = Entrez.esearch(db="pubmed", term=term)
    record = Entrez.read(handle)
    handle.close()
    print(record["Count"])
    return record["Count"], record["IdList"]


def query_maker(compounds, genes, effect):
    for comp in compounds.split("\n"):
        # print(comp)
        for gen in genes.split("\n"):
            # print(gen)
            for eff in effect.split("\n"):
                print(
                    "start query: \"" + comp + "\" AND \"" + gen + "\" AND \""
                    + eff + "\"")
                counts, id_list = get_counts_idlist(
                    comp + " AND " + gen + " AND " + eff)
                most = 0
                id_list_most = []
                if int(counts) > most:
                    id_list_most = id_list
                get_tiab(id_list_most)


def get_tiab(id_list):
    for pub_id in id_list:
        search_handle = Entrez.efetch(db="pubmed", id=pub_id,
                                      rettype="medline",
                                      retmode="text")
        records = list(Medline.parse(search_handle))
        title = records[0].get("TI", "?")
        abstract = records[0].get("AB", "?")
        if title == "?" or abstract == "?":
            print("Title or abstract missing, quitting for now.")
            exit()
        else:
            print(pub_id)
            print(title)
            print(abstract)


def main():
    # test query
    counts, id_list = get_counts_idlist("\"hart\" AND \"hearing\" AND \"ear\"")
    print(counts)
    get_tiab(id_list)

    # opdracht query's
    compounds = open("compounds.txt").read()
    genes = open("genes.txt").read()
    effect = open("molecular_effects.txt").read()
    query_maker(compounds, genes, effect)


main()
