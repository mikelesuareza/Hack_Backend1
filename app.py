from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route("/h1", methods=["GET"])
def h1():
    return {"payload":"get"}


@app.route("/h2", methods=["POST"])
def h2():
    return {"payload":"post"}

@app.route("/h3", methods=['PUT'])
def h3():
    return {"payload":"PUT"}


@app.route("/h4", methods=['DELETE'])
def h4():
    return {"payload":"DELETE"}


@app.route("/h5", methods=["GET", "POST", "DELETE", "PUT"])
def h5():
    metodo= request.method
    result = {}
    
    if metodo=="GET":
        result = {"payload":"success","error": False}
    return result

@app.route("/h6", methods=["GET", "POST", "DELETE","PUT"])
def h6():
    metodo= request.method
    result= {}

    if metodo == "GET" or metodo == "POST" or metodo == "DELETE":
        result={"method":"type", "payload":"success", "error":False}

    else:
        result = {"method":metodo, "payload":None, "error":False}

    return result

@app.route ("/h7", methods=["GET"])
def h7():
    email= request.args.get("email")
    name= request.args.get("name")

    return {
            "payload":{"email":email, "name":name},
            "error":{"available":False,"err_msg":None},
            "status":200
          }

@app.route("/h8", methods=["POST"])
def fn_h8():

    data= request.get_json()
    return {
            "payload":{"email":data["email"], "name":data["alias"]},
            "error":{"available":False,"err_msg":None},
            "status":200
          }

@app.route("/h9", methods=['GET'])
def fn_h9():
    
    lista = ["foo","bar","baz","qux","fred"]
    alias = request.args.get("alias")
    result = {}
    if alias in lista: 
        result = {
            "payload":alias,
            "error":{"available":False,"err_msg":None},
            "status":200
             }
    else:
        result = {
                "payload":"not found",
                "error":{"available":False,"err_msg":None},
                "status":404
            }
                

    return result


@app.route("/h10", methods=['POST'])
def fn_h10():
    
    lista = ["foo","bar","baz","qux","fred"]

    data = request.get_json()
    result = {}
    if data["alias"] in lista: 
        result = {"payload":data["alias"]}

    else:
        result = {"payload":"not found"}
                

    return result





if __name__ == "__main__":
    app.run(debug=True)