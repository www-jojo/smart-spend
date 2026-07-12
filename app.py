from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

expenses_list = []

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/expenses")
def expenses():
    return render_template("expenses.html", expenses=expenses_list)


@app.route("/expenses/add", methods=["POST", "GET"])
def add_expense():
    if request.method == "POST":
        title = request.form["title"]
        category = request.form["category"]
        amount = request.form["amount"]
        date = request.form["date"]
        notes = request.form["notes"]

        new_expense = {
            "title": title,
            "category": category,
            "amount": amount,
            "date": date,
            "notes": notes
        }

        expenses_list.append(new_expense)

        return redirect(url_for("expenses"))
    
    return render_template("add_expense.html")
         


@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


if __name__ == "__main__":
    app.run(debug=True)
