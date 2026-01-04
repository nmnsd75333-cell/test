from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    book = [
            {
            'title': 'はらぺこあおむし',
            'price': 1200,
            'arrival_day': '2020年1月6日'
            },
            {
            'title': 'ぐりとぐら',
            'price': 900,
            'arrival_day': '2020年1月8日'
            }
    ]

    return render_template(
        "index.html",
        bookinfo = book
        )

if __name__ == "__main__":
    app.run(debug=True, port=5001)
