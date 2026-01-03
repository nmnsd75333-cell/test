class User:
    def __init__(self,name,mail,point,count):
        self.name = name
        self.mail = mail
        self.point = point
        self.count = count
    
    def add_point(self):
        if self.count >= 50:
            point = 100
        elif self.count >= 40:
            point = 50
        else:
            point = 30
        self.point +=point
        return self.point

user_1 = User("佐藤", "sato@mail", 370, 40)
print(user_1.add_point())

