import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://neighbourlyserver:y9i5GdhXxYq8KeITUXRBJa3uug3PaZeZqBJ0uIjYxyk4LPBD2I0mpLilv3CdhvukPwLIqWw6hNQefpc4w0Wbyg%3D%3D@neighbourlyserver.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighbourlyserver@"
        client = pymongo.MongoClient(url)
        database = client['neighbourlymongodb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)