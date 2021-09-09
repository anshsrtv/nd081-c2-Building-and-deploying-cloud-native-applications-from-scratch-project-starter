import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://neighbourlydb:LaBMi1XqNUTjhU9heYMXtoXYGT0rg07Lsv4VLvOyS1DTFmd5xoCFUYxmjc3hopRwNQDhKaaSStp71nm1th7o1w==@neighbourlydb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighbourlydb@"
        client = pymongo.MongoClient(url)
        database = client['neighbourlymongodb']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

