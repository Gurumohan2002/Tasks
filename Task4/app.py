from flask  import Flask,request

app=Flask(__name__)

@app.route('/tp/<int:a>/<int:b>',methods=['GET'])
def sum(a,b):
    try:   
        if request.method == 'GET':
            return f'{a+b}'
        else:
            return 'Error'
    except Exception as e:
        return f"A error occured : {e}"
    
@app.route('/ab',methods=["GET","POST"])
def sumab():
    data=request.get_json("data")
    a=data["a"]
    b=data["b"]
    if request.method==["POST"]:
        try:
            sum=a+b
            return {sum}
        
        except Exception as e:
            return f"AN error occured : {e}"   
    else:
        print("An error occured")
        return "An error occured"
    
if __name__ == '__main__':
    app.run(debug=True)