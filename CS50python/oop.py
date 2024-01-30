class Dog:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def voice(self,sound):
        return "{} makes sound {}".format(self.name,sound)


    def test(self,sound):
        return "{}".format(sound)

tommy=Dog("tommy",3)
cris=Dog("chris",5)

print("{} is {}".format(tommy.name,tommy.age))
print(cris.voice("bow bow"))
print(tommy.test("maow"))
