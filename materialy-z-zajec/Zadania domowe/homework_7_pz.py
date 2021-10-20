"""
Użyj pętli for, aby napisać program, który będzie usuwał z jakiegoś przykładowego napisu
wszystkie znaki specjalne, np. .,:;?!
 """
inscription = "Dzisiaj jest piękny.... dzień! Nie trzeba wcześnie wstawać do: pracy, zrywać się z łóżka. " \
              "Może warto wyjść na rower? "
special_sign = [".", ",", ":", ";", "?", "!"]

# wymienia znaki specjalne na "brak znaku" -> ""
for i in inscription:
    if i in special_sign:
        inscription = inscription.replace(i, "")

print(inscription)

# filter() - wyświetla sam alfabet
for i in inscription[1]:
    new_inscription = filter(str.isalpha, inscription)
    new_inscription = "".join(new_inscription)
    print(new_inscription)
