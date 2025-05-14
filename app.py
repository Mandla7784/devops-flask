#Wow I am Officlally  a Devops in trainihg 
"""
    Here im just learnig Developement Operation basics
    as I am developing an interest on this filed as well 
    as Security application enhineer



"""


from flask import Flask

app = Flask(__name__)


@app.route("/")

def home():

    
    return "Yo Mandla! Devops in full effect "

if __name__ == "__main__":
    app.run(debug=True , host="0.0.0.0",port=5000)