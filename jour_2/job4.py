class Student:
    def __init__(self, nom, prenom, numero):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numero
        self.__credits = 0
        self.__level = self.__student_eval()
    
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
    
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def student_info(self):
        print(f"Nom: {self.__nom} \nPrénom: {self.__prenom} \nID: {self.__numero} \nNiveau: {self.__level}")

student = Student("Doe", "John", 145)
student.add_credits(20)
student.add_credits(20)
student.add_credits(30)
student.student_info()