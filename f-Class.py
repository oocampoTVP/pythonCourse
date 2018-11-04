class Comedian():

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. __str__"

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is {self.age}. __repr__'

new_comedian=Comedian('Edgar','ocampo','31')
print(new_comedian)
print('----')
