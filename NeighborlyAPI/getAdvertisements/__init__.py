import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://neighbourlyserver:gQAc6yevpaKB6T1KWKYdiPMXtLLZNBbRtncMxL1osx80XNzli0Isk9cnY2iiV2biKiiTdo7toJULAsx4HnmxTw%3D%3D@neighbourlyserver.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighbourlyserver@"
        client = pymongo.MongoClient(url)
        database = client['neighbourlydb']
        collection = database['advertisements']

    
        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

