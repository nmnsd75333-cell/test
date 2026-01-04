# 演習1
names = [
    ("野村", "京平"),
    ("飯塚", "麻里奈"),
    ("佐藤", "太郎")
]

for myoji,namae in names:
    print(f"{myoji} {namae}さん")

# 演習2
scores = [72, 85, 90, 68, 75]

def average(scores):
    scores = sum(scores) / len(scores)
    return scores

print(average(scores))

# 演習3
students = {
    "野村": [72, 85, 90, 68, 75],
    "飯塚": [88, 91, 79, 84, 90],
    "佐藤": [60, 70, 65, 58, 62]
}
for name,scores in students.items():
    avg = sum(scores) / len(scores)
    print(f"{name}さんの平均点は {avg} 点です")

# 演習4
class User:
    def __init__(self,name,point):
        self.name = name
        self.point = point
    
    def add_point(self):
        self.point += 50

user = User("野村", 100)
user.add_point()
user.add_point()

print(user.point)

