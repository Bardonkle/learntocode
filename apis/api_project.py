from flask import Flask,jsonify

app = Flask(__name__)

books_data = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/published/', methods=['GET'])
def books():
    return jsonify(books_data)


@app.route("/books/<int:book_id>", methods=["GET"])
def book_by_id(book_id):
    for book in books_data:
        if book_id == book["published"]:
            return jsonify(book)
    return jsonify({"status": "not found"}), 404


app.run()