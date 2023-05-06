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
