from json import JSONEncoder
#from connexion.apps.flask_app import FlaskJSONEncoder
from bson.objectid import ObjectId

class MongoEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:            
            return JSONEncoder.default(self, obj)