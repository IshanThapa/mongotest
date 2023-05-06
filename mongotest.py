import pymongo
client = pymongo.MongoClient("mongodb+srv://THAPAISHAN:ishan9696248110@cluster0.4hoj7vi.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
<<<<<<< HEAD
=======
coll.insert_one(d )

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )db1 = client['mongotest']
coll = db1['test']
>>>>>>> 39dd41f (This is my second code push in git.)
coll.insert_one(d )