#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import enum

class FiliationType(str, enum):
    Father = "father"
    Mother = "mother"
    Wife = "wife"
    Husband = "husband"
    Daughter = "daughter"
    Son = "son"
    Sister = "sister"
    Brother = "brother"
    GrandSon = "grandson"
    GrandDaughter = "granddauther"
    GrandMother = "grandmother"
    GrandFather = "grandfather"
    

class FiliationGroupType(str, enum):
    Wifes = "wifes"
    Husbands = "husbands"
    Daughters = "daughters"
    Sons = "sons"
    Sisters = "sisters"
    Brothers = "brothers"


def main():
    print("= "*40)
    


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