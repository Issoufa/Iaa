#!/usr/bin/python
# -*- coding: utf-8 -*-


class Individu:
    def __init__(self, birth_day, name, first_name):
        self.birth_day = birth_day
        self.name = name
        self.first_name = first_name
        self.sons = None
        self.daughters = None
        self.father = None
        self.mother = None


    def add_son(self, son):
        assert isinstance(son, Individu), print(f" son should be a Inididu type, not {type(son)}")
        if self.sons is None:
            # initiate sons list
            self.sons = []
        # add son in the list
        self.sons.append(son)


    def add_daughter(self, daughter):
        assert isinstance(daughter, Female), print(f" daughter should be a Female type, not {type(daughter)}")
        if self.daughters is None:
            # initiate sons list
            self.daughters = []
        # add son in the list
        self.daughters.append(daughter)


    def add_son(self, son):
        assert isinstance(son, Male), print(f" son should be a Male type, not {type(son)}")
        if self.sons is None:
            # initiate sons list
            self.sons = []
        # add son in the list
        self.sons.append(son)

    def add_mother(self, female):
        assert isinstance(female, Female), print(f" daughter should be a Female type, not {type(female)}")
        if self.mother is None:
           self.mother = female
           print(f"  self  = {self}")
        else:
            print(f" impossible to add new mother, {self.first_name} has already mother")
            print(f" motther: first name = {female.first_name},  name = {female.name}")



class Male(Individu):
    def __init__(self, birth_day, name, first_name):
        Individu.__init__(self, birth_day, name, first_name)
        self.genre = "male"


class Female(Individu):
    def __init__(self, birth_day, name, first_name):
        Individu.__init__(birth_day, name, first_name)
        self.genre = "female"


def main():
    print("= "*40)
    pere = Individu("2024/05/02", "Issouf", "Moussa")
    print(pere.name)
    fils = Individu("2024/05/02", "Issouf", "Illiya")
    pere.add_son(fils)
    pere.add_son("Hadj")

    print(f" les fils de {pere.name} sont {pere.sons}")

if __name__ == "__main__":
    print("Local test script...")
    files_directory = "/home/abdou/Documents/PROJECT/PostDoc/graph/learnGNN/tests/"

    main()