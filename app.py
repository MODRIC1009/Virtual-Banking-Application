from flask import Flask, render_template, request # type: ignore
from bank import Bank

app = Flask(__name__)
bank = Bank()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    msg = None
    if request.method == "POST":
        acc = bank.create_account(
            request.form["name"],
            request.form["pin"],
            float(request.form["balance"])
        )
        msg = f"Account created. ID: {acc.account_id}"
    return render_template("create.html", msg=msg)


@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    msg = None
    if request.method == "POST":
        _, msg = bank.deposit(
            request.form["acc_id"],
            float(request.form["amount"])
        )
    return render_template("deposit.html", msg=msg)


@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    msg = None
    if request.method == "POST":
        _, msg = bank.withdraw(
            request.form["acc_id"],
            request.form["pin"],
            float(request.form["amount"])
        )
    return render_template("withdraw.html", msg=msg)


@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    msg = None
    if request.method == "POST":
        _, msg = bank.transfer(
            request.form["sender"],
            request.form["pin"],
            request.form["receiver"],
            float(request.form["amount"])
        )
    return render_template("transfer.html", msg=msg)


@app.route("/payee", methods=["GET", "POST"])
def payee():
    msg = None
    if request.method == "POST":
        _, msg = bank.add_payee(
            request.form["acc_id"],
            request.form["payee_id"]
        )
    return render_template("payee.html", msg=msg)


@app.route("/details", methods=["GET", "POST"])
def details():
    acc = None
    if request.method == "POST":
        acc = bank.get(request.form["acc_id"])
    return render_template("details.html", acc=acc)


@app.route("/transactions", methods=["GET", "POST"])
def transactions():
    acc = None
    if request.method == "POST":
        a = bank.get(request.form["acc_id"])
        if a and a.verify_pin(request.form["pin"]):
            acc = a
    return render_template("transactions.html", acc=acc)


@app.route("/close", methods=["GET", "POST"])
def close():
    msg = None
    if request.method == "POST":
        _, msg = bank.close(
            request.form["acc_id"],
            request.form["pin"]
        )
    return render_template("close.html", msg=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
