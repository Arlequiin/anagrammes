rows=[]
out=[]
with open("dico.txt") as f:
    for row in f:
        rows.append(row.strip())
def dictionnaire_indices_mots(liste):
  d={}
  for element in liste:
    l=[]
    for element2 in liste:
      if sorted(element2)==sorted(element):
        l.append(element2)
    element=''.join(sorted(element))
    d[element]=l
  return d
print(dictionnaire_indices_mots(rows))
