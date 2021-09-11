import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://neighbourlyserver:y9i5GdhXxYq8KeITUXRBJa3uug3PaZeZqBJ0uIjYxyk4LPBD2I0mpLilv3CdhvukPwLIqWw6hNQefpc4w0Wbyg%3D%3D@neighbourlyserver.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighbourlyserver@"
            client = pymongo.MongoClient(url)
            database = client['neighbourlymongodb']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )