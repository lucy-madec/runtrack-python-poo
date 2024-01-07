class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self._nom = nom
        self._prenom = prenom
        self._numero_etudiant = numero_etudiant
        self._credits = 0
        self._level = self._student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._student_eval()
        else:
            print("Erreur : Le nombre de crédits ajouté doit être supérieur à zéro.")

    def _student_eval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom = {self._nom}")
        print(f"Prénom = {self._prenom}")
        print(f"id = {self._numero_etudiant}")
        print(f"Niveau = {self._level}")

john_doe = Student("John", "Doe", 145)

john_doe.add_credits(10)
john_doe.add_credits(15)
john_doe.add_credits(5)

john_doe.student_info()
