class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        self.gender = gender
        if "@" in email:
            self.email = email
        else:
            print("Please give a real email address")

    def name1(self):
        return self.name

    def email1(self):
        return self.email

    def gender1(self):
        return self.gender

    def isMale(self):
        if self.gender == "male":
            return True
        return False

    def isFemale(self):
        if self.gender == "female":
            return True
        return False

    def __str__(self):
        return "This panda's name is {}. They are {} and their email address is {}".format(self.name, self.gender, self.email)

    def __eq__(self, b):
        if self.name == b.name and self.email == b.email and self.gender == b.gender:
            return True
        return False

    def __hash__(self):
        sum = 0
        for c in self.name:
            sum += ord(c)
        return sum


class PandaSocialNetwork:

    pandas = []
    pandaFriends = {}
    friendAmount = {}

    def __init__(self):
        self.self = self

    @staticmethod
    def add_panda(panda):
        if panda in PandaSocialNetwork.pandas:
            print("{} IS ALREADY IN THE NETWORK".format(panda.name1()))
        else:
            PandaSocialNetwork.pandas.append(panda)
            PandaSocialNetwork.friendAmount[panda.name1] = 0
            PandaSocialNetwork.pandaFriends[panda.name1()] = []

    @staticmethod
    def has_panda(panda):
        if panda in PandaSocialNetwork.pandas:
            return True
        return False

    @staticmethod
    def make_friends(panda1, panda2):
        if panda1 and panda2 in PandaSocialNetwork.pandas:
            friends = [panda2]
            PandaSocialNetwork.pandaFriends[panda1.name1()] = PandaSocialNetwork.pandaFriends.get(panda1.name1()) + friends
            PandaSocialNetwork.friendAmount[panda1.name1] = PandaSocialNetwork.friendAmount.get(panda1.name1) + 1
            friends2 = [panda1]
            PandaSocialNetwork.pandaFriends[panda2.name1()] = PandaSocialNetwork.pandaFriends.get(panda2.name1()) + friends2
            PandaSocialNetwork.friendAmount[panda2.name1] = PandaSocialNetwork.friendAmount.get(panda2.name1) + 1
        elif PandaSocialNetwork.are_friends(panda1, panda2):
            print("{} and {} are already friends".format(panda1.name1(), panda2.name1()))
        else:
            PandaSocialNetwork.add_panda(panda1)
            PandaSocialNetwork.add_panda(panda2)
            friends = [panda2]
            PandaSocialNetwork.pandaFriends[panda1.name1()] = PandaSocialNetwork.pandaFriends.get(panda1.name1()) + friends
            friends2 = [panda1]
            PandaSocialNetwork.pandaFriends[panda2.name1()] = PandaSocialNetwork.pandaFriends.get(panda2.name1()) + friends2

    @staticmethod
    def are_friends(panda1, panda2):
        if panda2 in PandaSocialNetwork.pandaFriends.get(panda1.name1()) and panda1 in PandaSocialNetwork.pandaFriends.get(panda2.name1()):
            return True
        return False

    @staticmethod
    def friends_of(panda):
        if panda not in PandaSocialNetwork.pandas:
            return False
        returnedList = []
        for panda in PandaSocialNetwork.pandaFriends[panda.name1()]:
            returnedList.append(panda.name1())
        return returnedList