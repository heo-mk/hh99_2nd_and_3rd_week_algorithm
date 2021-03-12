class Person():
    def __init__(self, param_name):
        print("ssegdh", self)
        self.name = param_name
    
    def talk(self):
        print("안녕하세요 저는", self.name, "입니다.")
        
person_1 = Person("db_1")
print(person_1.name)
person_1.talk()

print()

person_2 = Person("db_2")
print(person_2.name)
person_2.talk()