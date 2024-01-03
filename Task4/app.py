from flask  import Flask,request

app=Flask(__name__)

#API which gets input in its URL and returns the sum as output in Web Page using GET method
@app.route('/tp/<int:a>/<int:b>',methods=['GET'])
def sum(a,b):
    try:   
        if request.method == 'GET':
            return f'{a+b}'
        else:
            return 'Error'
    except Exception as e:
        return f"A error occured : {e}"

#API for getting data from the user in JSON format and printing sum as a output using GET and POST method
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
    
#Main function
if __name__ == '__main__':
    app.run(debug=True)