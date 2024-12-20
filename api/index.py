from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('portfolio.html')  # Certifique-se de que o arquivo portfolio.html está na pasta templates

@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run(debug=True)
