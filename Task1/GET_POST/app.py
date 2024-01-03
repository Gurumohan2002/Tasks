from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
   try:
      return "<html><body><h1> Hello To Web Page </h1></body></html>"
   except Exception as e:
      print(f"An error occurred: {e}")
      return "<html><body> <h1> An unexpected error occurred. </h1></body></html>"

@app.route('/sqrt', methods=['GET', 'POST'])
def squarenumber():
   if request.method == 'POST':
      try:
         data=request.get_json("data")
         a=data["a"]
         if a is None or a=="":
            return "<html><body> <h1> Invalid number </h1></body></html>"
         else:
            number= int(a)
            sqr = int(number) * int(number)
            return f'{sqr}'
      except KeyError as k:
         return f"<html><body> <h1> 'a' key not found in the request data </h1> <h1>{k}</h1></body></html>"
      except ValueError as v:
         return f"<html><body><h1> Invalid data type for 'a'.Please provide an integer.</h1><h1>{v} </h1></body></html>"
   else:
      return 'wertyuio'

@app.route('/g_p', methods=['GET', 'POST'])
def example():
   try:
      if request.method == 'GET':
          return 'This is a GET request.'
      elif request.method == 'POST':
          return 'This is a POST request.'
   except Exception as e:
      print(f"An error occured: {e}")
      return "<html><body><h1> An unexpected error occured. </h1></body></html>"
   
@app.route('/usersget', methods=['GET'])
def get_users():
   try:
      users = fetch_data(request)
      return users
   except Exception as e:
        print(f"An error occurred: {e}")
        return "<html><body> <h1> An unexpected error occurred. </h1></body></html>"

def fetch_data(request):
   try:
      data=request.data
      print("data", data)
      return data
   except Exception as e:
      print(f"An error ocuured : {e}")
      return f"<html><body> <h1> An unexpected error occurred.{None} </h1></body></html>"

@app.route('/userspost', methods=['POST'])
def post_users():
   if request.method=="POST":
      try:
         id = 1
         name = 'GURU'
         email = 'senthuri2002@gmail.com'
         details=[id,name,email]
         return details
      except Exception as e:
        print(f"An error occurred: {e}")
        return "An unexpected error occurred."
   else:
      return f"<html><body><h1> An error occured </h1> </body></html>"
   
@app.route('/usersput', methods=['PUT'])
def put_users():
   if request.method=="PUT":
      try:
         name = 'Guru'
         email = 'guru@gmail.com'
         user = [name,email]
         user["name"] = name
         user["email"] = email
         return user
      except Exception as e:
         print(f"An error occured: {e}")
         return "<html><body></h1> An unexpected error occured </h1></body></html>"

@app.route('/usersdelete', methods=['DELETE'])
def delete_user():
   try:
      user = 'Gurum'
      if user=="Gurum":
        print(user)
        user=""
        return 'User deleted successfully'
      else:
        return 'User not found', 404
   except Exception as e:
       print(f"An error occurred: {e}")
       return "An unexpected error occurred."
    
if(__name__ == "__main__"):
	app.run(debug=True)
