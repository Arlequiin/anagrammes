rows=[]
with open("dico.txt") as f:
    for row in f:
        rows.append(row.strip())
def indice_mot(word):
  return ''.join(sorted(word))
def is_anagram(mot1,mot2):
    return indice_mot(mot1)==indice_mot(mot2)
def dictionnaire_indices_mots(liste):
  d={}
  for element in liste:
    l=[]
    for element2 in liste:
      if is_anagram(element,element2):
        l.append(element2)
    element=indice_mot(element)
    d[element]=l
  return d
print(dictionnaire_indices_mots(rows))

