
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def company_details():
    company_name= 'ABC Corporation' 
    location= 'India' 
    contact_no= '999-999-9999'    
    details = f'Company Name:{company_name}<br>Location:{location}<br>Contact Detail:{contact_no}'
    return details
print(company_details())

@app.route("/welcome")
def welcome():
    return "Welcome to ABC Corporation"

if __name__=="__main__":
    app.run(host="0.0.0.0")
