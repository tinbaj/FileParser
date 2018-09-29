from flask import Flask, request
from flask_restful import Resource, Api
from Code import myApp as myApp

app = Flask(__name__)
api = Api(app)

class FileParser(Resource):
    def post(self, fileType):
        if fileType == 'TXT':
            request_data = request.get_json()
            request_data["funcName"] = fileType
            retval = myApp.myApp.main(myApp.myApp(), **request_data)
            print("retval: ",retval)
            return retval
        elif fileType == 'XML':
            request_data = request.get_json()
            request_data["funcName"] = fileType
            return request_data
        elif fileType == 'CSV':
            request_data = request.get_json()
            request_data["funcName"] = fileType
            return request_data
        else:
            return "Invalid File Type passed"
api.add_resource(FileParser,'/FileParser/<string:fileType>')

if __name__ == '__main__':
    app.run(port=5000,debug=True)