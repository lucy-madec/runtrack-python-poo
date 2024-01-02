class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    
    def se_presenter(self):
        return f"Je suis {self.prenom} {self.nom}"

personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupond")

presentation1 = personne1.se_presenter()
presentation2 = personne2.se_presenter()

print(presentation1)
print(presentation2)
