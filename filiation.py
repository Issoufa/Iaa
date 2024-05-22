#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import enum


class IndividuGenre(str, enum):
    Male = "male"
    Female = "female"

class Individu:
    """
    Individu class that is base of person declaration, it is not possible to initiate this class directly
    """

    def __init__(self, birth_day, name, first_name):
        assert (name, str), print(f" name should be str type, not {type(name)}")
        assert (first_name, str), print(f" first name should be str type, not {type(first_name)}")
        
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

    def add_mother(self, mother):
        assert isinstance(mother, Female), print(f" mother should be a Female type, not {type(mother)}")
        
        if self.mother is None:
           self.mother = mother
           print(f"  self  = {self}")

        else:
            print(f" impossible to add new mother, {self.first_name} has already mother")
            print(f" mother: first name = {mother.first_name},  name = {mother.name}")

    def add_father(self, father):
        assert isinstance(father, Male), print(f" father should be a Male type, not {type(father)}")
        
        if self.father is None:
           self.father = father
           print(f"  self  = {self}")
        else:
            print(f" impossible to add new father, {self.first_name} has already father")
            print(f" father: first name = {father.first_name},  name = {father.name}")


class Male(Individu):
    def __init__(self, birth_day, name, first_name, wife=None):
        Individu.__init__(self, birth_day, name, first_name)
        self.genre = IndividuGenre.Male
        self.wife = []
        if wife:
            self.wife.append(wife)

    def add_wife(self, wife):
        assert isinstance(wife, Female), print(f" Wife should be a Female type, not {type(wife)}")
        self.wife.append(wife)


class Female(Individu):
    def __init__(self, birth_day, name, first_name, husband=None):
        Individu.__init__(birth_day, name, first_name)
        self.genre = IndividuGenre.Female
        self.husband = []
        if husband:
            self.husband.append(husband)

    def add_husband(self, husband):
        assert isinstance(husband, Male), print(f" husband should be a Male type, not {type(husband)}")
        if self.husband is None:
            self.husband.append(husband)


def main():
    print("= "*40)
    pere = Individu("2024/05/02", "Issouf", "Moussa")
    print(pere.name)
    fils = Individu("2024/05/02", "Issouf", "Illiya")
    pere.add_son(fils)
    pere.add_son("Hadj")

    print(f" les fils de {pere.name} sont {pere.sons}")


if __name__ == "__main__":
    print("test script...")
    dict_type_keys_inherit = {}
    dict_type_keys_inherit[0] = {"father":0, "mother":0, "wifes":1, "husband":2, "daughter":0, "sons":0, "sisters":0, "brothers":0}
    dict_type_keys_inherit[1] = {"father":0, "mother":0, "wifes":1, "husband":2, "daughter":1, "sons":1, "sisters":1, "brothers":1}
    dict_type_keys_inherit[2] = {"father":0, "mother":0, "wifes":1, "husband":2, "daughter":1, "sons":1, "sisters":1, "brothers":1}
    dict_type_keys_inherit[3] = {"father":0, "mother":0, "wifes":1, "husband":2, "daughter":1, "sons":1, "sisters":1, "brothers":1}
    dict_type_keys_inherit[4] = {"father":0, "mother":0, "wifes":1, "husband":2, "daughter":1, "sons":1, "sisters":1, "brothers":1}
    dict_type_keys_inherit[5] = {"father":0, "mother":0, "wifes":1, "husband":2, "daughter":1, "sons":1, "sisters":1, "brothers":1}
    dict_type_keys_inherit[6] = {"father":0, "mother":0, "wifes":1, "husband":2, "daughter":1, "sons":1, "sisters":1, "brothers":1}
    dict_type_keys_inherit[7] = {"father":0, "mother":0, "wifes":1, "husband":2, "daughter":1, "sons":1, "sisters":1, "brothers":1}
    dict_type_keys_inherit[8] = {"father":0, "mother":0, "wifes":1, "husband":2, "daughter":1, "sons":1, "sisters":1, "brothers":1}
    
    main()