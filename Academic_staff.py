from User_class import User
from Faculty_class_test import Faculty
from abc import ABC, abstractmethod


class Academic_staff ():
    def teaches(self):
        pass
    #def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title):
    #    super().__init__(type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title)



class Teaching_Assistant (Academic_staff):
    #def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title):
    #    super().__init__(type, name, pass_id, email, date_of_birth, gender, nationality, phone,  course, occupation, hours, salary, title)


    def teaches(self):
        print("Teaching assistants")


class Lecturer(Academic_staff):
    #def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title):
    #    super().__init__(type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title)
    def teaches(self):
        print("Lecturers")



class Senior_Lecturer (Academic_staff):
    #def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title):
    #    super().__init__(type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title)

    def teaches(self):
        print("Senior Lecturers")


class Assistant_Professor (Academic_staff):
    #def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title):
    #    super().__init__(type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title)

    def teaches(self):
        print("Assistant Professor")


class Associate_Professor (Academic_staff):
    #def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title):
    #    super().__init__(type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title)

    def teaches(self):
        print("Associate Professor")


class Full_Professor (Academic_staff):
   # def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title):
   #     super().__init__(type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title)

    def teaches(self):
        print("Full Professor")


class Academician (Academic_staff):
    #def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title):
    #    super().__init__(type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title)

    def teaches(self):
        print("Academician")

Full_Professor().teaches()