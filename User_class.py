class User:

    def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone):
        self.set_type(type)
        self.set_name(name)
        self.set_pass_id(pass_id)
        self.set_email(email)
        self.set_date_of_birth(date_of_birth)
        self.set_gender(gender)
        self.set_nationality(nationality)
        self.set_phone(phone)

    # SETTERS
    def set_type(self, type):
        #if isinstance(type, str):
        #    self.type = type
        type = type.strip()
        f = open("User_type.txt")
        lines = f.readlines()
        f.close()
        for line in lines:
            list_types = line.split(" ")
        if type in list_types:
            self.__type = type
        else:
            raise ValueError("Invalid type entered")





    def set_name(self, name): # at least 2 words
        if isinstance(name, str):
            word = name.split(" ")
            if 2<= len(word) <= 4:
                self.__name = name
    def set_pass_id(self, pass_id):
        #if isinstance(pass_id, str):
        #    self.pass_id = pass_id
        pass_id = pass_id.strip().upper()
        if len(pass_id) == 9 and pass_id[0].upper().isalpha() and pass_id[1].upper().isalpha() and pass_id[2:8].isdigit():
            self.__pass_id = pass_id
        else:
            raise ValueError("Invalid pass_id")

    def set_email(self, email):
        email = email.strip()
        if isinstance(email, str) and "@" in email and "." in email:
            self.__email = email.lower()
        else:
            raise ValueError("Email must contain @ and .")
    def set_date_of_birth(self, date_of_birth):
        # if isinstance(date_of_birth, str):
        date_of_birth = date_of_birth.strip()
        if len(date_of_birth) == 10 and date_of_birth[0:4].isdigit() and date_of_birth[5:7].isdigit() and date_of_birth[8:10].isdigit() and date_of_birth[4] == "/" and date_of_birth[7] == "/":
            year = int(date_of_birth[0:4])
            month = int(date_of_birth[5:7])
            day = int(date_of_birth[8:10])

            if 1900 <= year <= 2024 and 1 <= month <= 12 and 1 <= day <= 31:
                if self.is_valid_date(year, month, day) == True:
                    self.__date_of_birth = date_of_birth
                else:
                    print("Invalid data entered")
            else:
                raise ValueError("Your input is out of range")
        else:
            raise ValueError("Input your date of birth with the following style: YYYY/MM/DD")


    def set_gender(self, gender):
        #if isinstance(gender, str):
        gender = gender.strip().lower()
        if gender == 'male' or gender == 'female':
             self.__gender = gender
        else:
            raise ValueError("Invalid gender")
    def set_nationality(self, nationality):
        #if isinstance(nationality, str):
        nationality = nationality.strip()
        f = open("User_nationality.txt")
        lines = f.readlines()
        f.close()
        for line in lines:
            list_nationality = line.split(", ")
        if nationality in list_nationality:
            self.__nationality = nationality
        else:
            raise ValueError("Invalid nationality type entered")



    def set_phone(self, phone):
        # if isinstance(phone, str):
        phone = phone.strip()
        if len(phone) == 12 and phone.isdigit() and phone.startswith("998"):
            self.__phone = phone
        else:
            raise ValueError("Invalid phone number")



    # GETTERS
    def get_type(self):
        return self.__type
    def get_name(self):
        return self.__name
    def get_pass_id(self):
        return self.__pass_id
    def get_email(self):
        return self.__email
    def get_date_of_birth(self):
        return self.__date_of_birth
    def get_gender(self):
        return self.__gender
    def get_nationality(self):
        return self.__nationality
    def get_phone(self):
        return self.__phone

    def is_valid_date(self, year, month, day):
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day_count_for_month[2] = 29
            return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])
        else:
            return False

if __name__ == "__main__":

    user = User('Students', "Alice", 'AA1234567', 'alice@gmail.com', '2023/02/10', 'female', 'French', '998901234567')
    print(user.is_valid_date(1800, 2, 29))

