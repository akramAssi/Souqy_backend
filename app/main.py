from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/api',methods=['GET'])
def hello():
    d={}
    d["Query"]=str(request.args["Query"])
    return jsonify(d)
    
