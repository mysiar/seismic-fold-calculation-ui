""" File Access"""
import json


def read_dict_from_file(filename: str):
    """read any JSON dictionary"""
    file = open(filename, "r")
    result = json.load(file)
    file.close()
    return result


def write_dict_to_file(filename: str, dictionary: dict):
    """writes any dictionary to JSON"""
    file = open(filename, "w")
    json.dump(dictionary, file)
    file.close()
