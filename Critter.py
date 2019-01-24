#import time


class Critter(object):

    def __init__(self, name):
        self.name = name
        self.__hunger = 0
        self.__boredom = 0

    @property
    def mood(self):
        unhappiness = self.__boredom+self.__hunger
        if unhappiness < 5:
            mood = "happy"
        elif 6 <= unhappiness <= 10:
            mood = "okay"
        elif 11 <= unhappiness <= 15:
            mood = "frustrated"
        else:
            mood = "mad"

        return mood

    def __pass_time(self):
        self.__hunger += 1
        self.__boredom += 1

    def play(self):
        print("you have played with your critter and lowered it's boredom ")
        self.__boredom -= 2
        if self.__boredom < 0:
            self.__boredom = 0
        self.__pass_time()

    def talk(self):
        print(self.name, self.mood)
        self.__pass_time()

    def eat(self):
        print("you have played with your critter and lowered it's boredom ")
        self.__hunger -= 2
        if self.__hunger < 0:
            self.__hunger = 0
        self.__pass_time()


def main():
    name = input("what is your critters name")
    critter = Critter(name)
    choice = None
    while choice != "0":
        print("would you like to\ntalk to your critter 1\nfeed your critter 2\nplay with your critter 3\nor exit 0")
        choice = input()
        if choice == '0':
            print("good bye")
            break
        elif choice == '1':
            critter.talk()
        elif choice == '2':
            critter.eat()
        elif choice == '3':
            critter.play()
        else:
            print("not a good choice")


main()
