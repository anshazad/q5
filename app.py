import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    n=int(jsonObj["enter the value of n"])
    response = ""
    f=1
    for i in range (n,0,-1):
        for j in range(1,i+1):
             f*=j
        response+="{}!={}<br>" .format()i,f
        f=1   
    
        
    	    
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
