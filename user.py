class User:
    def __init__(self, user_id, name, age, sex, height, weight):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.bmi = round(weight / ((height/100) ** 2), 1)

    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.name}, Age: {self.age}, Sex: {self.sex}, Height: {self.height}cm, Weight: {self.weight}kg, BMI: {self.bmi}"
