from flask import Flask  
app = Flask(__name__)

@app.route('/')          
def hello_world():
    return 'Hello World!'

@app.route('/dojo')          
def dojo():
    return 'Dojo!'

@app.route('/say/<word>')          
def word(word):
    return 'Hi '+ word + '!'


@app.route('/repeat/<num>/<word>')          
def numword(num,word):
    return (word + " ") *int(num)


if __name__=="__main__":   
    app.run(debug=True)