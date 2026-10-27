from flask import Flask, render_template, request

app = Flask(__name__)

# Sample rates for this educational demo only.
CARDS = {
    "Food": {"name": "Foodie Rewards Card", "cashback": 5},
    "Shopping": {"name": "Smart Shopper Card", "cashback": 4},
    "Travel": {"name": "Travel Saver Card", "cashback": 6},
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    if request.method == "POST":
        category = request.form.get("category", "Food")
        try:
            amount = float(request.form.get("amount", "0"))
        except ValueError:
            amount = 0
        if category not in CARDS or amount <= 0:
            return render_template("recommend.html", error="Choose a category and enter an amount greater than zero.")
        card = CARDS[category]
        reward = amount * card["cashback"] / 100
        return render_template("result.html", category=category, amount=amount, card=card, reward=reward)
    return render_template("recommend.html", error=None)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
