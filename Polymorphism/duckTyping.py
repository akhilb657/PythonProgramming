class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("Hy")

def callTalk(obj):
    obj.talk()

d = Duck()
h = Human()

callTalk(d)
callTalk(h)