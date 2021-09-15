import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        # try:
        url = "mongodb://neighbourlyserver:gQAc6yevpaKB6T1KWKYdiPMXtLLZNBbRtncMxL1osx80XNzli0Isk9cnY2iiV2biKiiTdo7toJULAsx4HnmxTw%3D%3D@neighbourlyserver.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighbourlyserver@"
        client = pymongo.MongoClient(url)
        database = client['neighbourlydb']
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
