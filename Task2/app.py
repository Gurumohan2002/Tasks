import os
import psycopg2
from flask import Flask, render_template,request

app=Flask(__name__)

# API for WEB HomePage
@app.route("/")
def hello():
    try:
       return "<html><body><h1> Hello To Web Page </h1></body></html>"
    except Exception as e:
       print(f"An error occurred: {e}")
       return "<html><body> <h1> An unexpected error occurred. </h1></body></html>"

#API for inserting the data in postgresql table with database connections using POST method
@app.route("/psqlcreate",methods=["POST"])
def create():
    if request.method=="POST":
        try:
            conn=psycopg2.connect(
                database="guru",
                user="postgres",
                password="Guru@2607",
                host="localhost", port="5433")
            cur = conn.cursor()

            cur.execute('DROP TABLE IF EXISTS booksnew;')
            cur.execute('CREATE TABLE booksnew (id serial PRIMARY KEY,'
                                        'title varchar (150) NOT NULL,'
                                        'author varchar (50) NOT NULL,'
                                        'pages_num integer NOT NULL,'
                                        'review text,'
                                        'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                        )

            cur.execute('INSERT INTO booksnew (title, author, pages_num, review,date_added)'
                    'VALUES (%s, %s, %s, %s,%s)',
                    ('A Tale of Two Cities',
                    'Charles Dickens',
                    489,
                    'A great classic!',"21-10-2023")
                    )

            cur.execute('INSERT INTO booksnew (title, author, pages_num, review,date_added)'
                    'VALUES (%s, %s, %s, %s, %s)',
                    ('Anna Karenina',
                    'Leo Tolstoy',
                    864,
                    'Another great classic!',"25-10-2023")
                    )

            conn.commit()
            cur.close()
            conn.close()
            
            return "Database created successfully"
        
        except psycopg2.Error as e:
            print(f"PostgreSQL error: {e}")
            return "An error occurred while performing database operations."

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "An unexpected error occurred."
    else:
        print(f"An unexpected error occurred:")
        return "An unexpected error occurred."
        
# API for getting the data from the database and Displaying the data from the Table using GET method      
@app.route("/psqlshow",methods=["GET"])
def show():
    if request.method=="GET":
        try:
            conn=psycopg2.connect(
                database="guru",
                user="postgres",
                password="Guru@2607",
                host="localhost", port="5433")
            
            cur=conn.cursor()
            cur.execute('''select * from booksnew''')
            values=cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            return render_template('index.html',data=values)
    
        except psycopg2.Error as e:
            print(f"PostgreSQL error: {e}")
            return "An error occurred while performing database operations."

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "An unexpected error occurred."
        
    else:
        print(f"An unexpected error occurred:")
        return "An unexpected error occurred."

#Main function
if __name__ == "__main__":
    app.run(debug=True)