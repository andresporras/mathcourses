from pymongo import MongoClient
from bson.code import Code
from passlib.hash import sha256_crypt

client = MongoClient('localhost', 27017)

db = client['courses']

collection = db['courseData']

def getData():
    #query = str('db.courseData.find({})')
    #a =db.eval(query)
    a=collection.find({})
    return a

#db.courseData.insert({"cod" : "1", "name" : "basic algebra", "units" :[{"name":"equations", "cod":"1"}, {"name":"inequations", "cod":"2"}]})
#db.courseData.insert({"cod" : "2", "name" : "precalculus", "units" :[{"name":"series", "cod":"1"}, {"name":"limits", "cod":"2"}]})
