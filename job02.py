class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde, decouvert=False):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print("Numéro de compte :", self.__num_compte)
        print("Nom :", self.__nom)
        print("Prénom :", self.__prenom)
        print("Solde :", self.__solde, "€")
        print("Autorisation de découvert:", "Oui" if self.__decouvert else "Non")

    def afficherSolde(self):
        print("Solde actuel :", self.__solde, "€")
    
    def versement(self, montant):
        self.__solde += montant
        print("Versement de ", montant, "€ effectué.")
        self.afficherSolde()

    def retrait(self, montant):
        if montant <= self.__solde:
            self.__solde -= montant
            print("Retrait de ", montant, "€ effectué.")
            self.afficherSolde()
        else:
            print("Solde insuffisant. Opération annulée.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            montant_agios = abs(self.__solde) * taux_agios
            self.__solde -= montant_agios
            print("Agios de", montant_agios, "€ appliqués.")
            self.afficherSolde()
    
    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement de", montant, "€ effectué vers le compte", compte_destinataire.__num_compte, ".")
        else:
            print("Solde insuffisant. Opération de virement annulée.")

compte1 = CompteBancaire("123456789", "Burton", "Tim", 1000, decouvert=True)

compte2 = CompteBancaire("987654321", "Spielberg", "Steven", -200, decouvert=True)

compte1.afficher()
print()
compte2.afficher()

montant_virement = 300
compte1.virement(compte2, montant_virement)

compte1.afficher()
print()
compte2.afficher()