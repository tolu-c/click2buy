from pymongo import MongoClient

def get_db_handle(db_name, host, port, username, password):

    client = MongoClient(
        host=host, port=int(port), username=username, password=password
    )
    db_handle = client["db_name"]

# mongodb+srv://toluMongo:<7kT5EpK@krNdJNtG>@cluster0.z0ree.mongodb.net/myFirstDatabase?retryWrites=true&w=majority