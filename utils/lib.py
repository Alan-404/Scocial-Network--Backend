import random
from django.db.models.base import ModelBase
from datetime import datetime, timezone

def make_id(length: int) -> str:
    str = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    id = ""
    for _ in range(length):
        id += random.choice(str)
    return id

def from_dict(Model: ModelBase, dictionary: dict) -> object:
    obj = Model()
    for param in dictionary.keys():
        if param in obj.__dict__.keys():
            obj.__dict__[param] = dictionary[param]
    return obj

def get_data(obj: object, dictionary: dict) -> object:
    for param in dictionary.keys():
        if param in obj.__dict__.keys():
            obj.__dict__[param] = dictionary[param]
    return obj

def model_to_dict(object: ModelBase) -> dict:
    data = dict()
    for item in object.__dict__.keys():
        if item != "_state":
            if isinstance(object.__dict__[item], datetime):
                data[item]= object.__dict__[item].astimezone(timezone.utc).strftime('%d-%m-%Y %H:%M:%S')
            else:
                data[item] = object.__dict__[item]
    return data

def map(from_obj: object, to_obj: object) -> object:
    for item in to_obj.__dict__.keys():
        if item in from_obj.__dict__.keys():
            to_obj.__dict__[item] = from_obj.__dict__[item]

    return to_obj