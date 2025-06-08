from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "I wasn’t able to attend class lately because I have a problem with my allowance, and I didn’t have the means to cover my transportation.!"

@app.route('/about')
def about():
    return "About page"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)