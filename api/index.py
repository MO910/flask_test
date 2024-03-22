from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "hello, this is our first flask website"


# @app.route('/books/<book_name>')
# def home(book_name):
#     return f'the book is {book_name}'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
