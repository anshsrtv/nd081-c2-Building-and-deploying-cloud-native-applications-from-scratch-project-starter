import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        # try:
        url = "mongodb://neighbourlyserver:y9i5GdhXxYq8KeITUXRBJa3uug3PaZeZqBJ0uIjYxyk4LPBD2I0mpLilv3CdhvukPwLIqWw6hNQefpc4w0Wbyg%3D%3D@neighbourlyserver.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighbourlyserver@"
        client = pymongo.MongoClient(url)
        database = client['neighbourlymongodb']
        collection = database['advertisements']
        
        query = {'_id': ObjectId(id)}
        result = collection.delete_one(query)
        print(result)
        return func.HttpResponse("")

        # except:
        #     print("could not connect to mongodb")
        #     return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
