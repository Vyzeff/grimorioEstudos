import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")
"""
# Function to check for dangerous SQL inputs
def checkText(input):
    dangerChar = ["--", "-", "'", ";", "/"]
    isDanger = False
    for x in dangerChar:
        if x in input:
            isDanger = True
    if isDanger == True:
        return apology("Please do not use special characters.")
    else:
        return True

    return True
"""
transaction = False
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    #TODO
    userCash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    userWallet = db.execute("SELECT symbol, company, shares, price, total FROM wallet WHERE id = ? GROUP BY symbol", session["user_id"])

    totalCash = userCash
    for share in userWallet:
        totalCash += share["price"] * share["shares"]
    if transaction == True:
        return render_template("index.html", userCash=usd(userCash), userWallet=userWallet, total=usd(totalCash), transaction=True)
    else:
        return render_template("index.html", userCash=usd(userCash), userWallet=userWallet, total=usd(totalCash))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        # Ensures Symbol is a valid input
        buyRequest = lookup(request.form.get("symbol"))
        confirmation = request.form.get("shares").lower()
        if buyRequest == None or not confirmation:
            return apology("Invalid Symbol")

        if  int(request.form.get("shares"))% 1 != 0:
            return ("Invalid number")
        # Ensures Shares is a valid positive number
        sharesRequest =int(request.form.get("shares"))
        if sharesRequest <=0:
            return apology("Invalid shares value.")

        # Check if user has enough cash for transaction
        userCash = int(db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"])
        opCost = int(buyRequest["price"] * sharesRequest)
        remainingCash = userCash - opCost
        if userCash < opCost:
            return apology("Not enough money for transaction.")
        # Reduct money from user
        db.execute("UPDATE users SET cash = ? WHERE id = ?", remainingCash, session["user_id"])
        date = datetime.now()
        # Chenge wallet table with info
        # Check if user has bought with that company before
        if len(db.execute("SELECT symbol FROM wallet WHERE id = ? AND company = ?", session["user_id"], buyRequest["name"])) == 0:
            db.execute("INSERT INTO wallet (id, symbol, company, shares, price, total) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], buyRequest["symbol"], buyRequest["name"], sharesRequest, buyRequest["price"], (buyRequest["price"] * sharesRequest))
            db.execute("INSERT INTO purchases (id, type, symbol, shares, price, total, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)",session["user_id"], "BUY",  buyRequest["symbol"], sharesRequest, opCost, userCash, date)
        else:
            userHas = db.execute("SELECT shares, total FROM wallet WHERE symbol = ? AND id = ?", buyRequest["symbol"], session["user_id"])
            db.execute("UPDATE wallet SET shares = ?, total = ? WHERE id = ? AND symbol = ?", sharesRequest + int(userHas[0]["shares"]), ((int(buyRequest["price"]) * sharesRequest) + int(userHas[0]["total"])), session["user_id"], buyRequest["symbol"])
            db.execute("INSERT INTO purchases (id, type, symbol, shares, price, total, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)",session["user_id"], "BUY",  buyRequest["symbol"], sharesRequest, opCost, userCash, date)

        transaction = True
        return redirect("/")
    else:
        return render_template("buy.html")
@app.route("/history")
@login_required
def history():
    history = db.execute("SELECT type, symbol, shares, price, total, timestamp FROM purchases WHERE id = ? ORDER BY timestamp DESC", session["user_id"])
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username").lower())

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        transaction = False
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":

        # Ensure Symbol is a valid input
        if not request.form.get("symbol"):
            return apology("Please input a valid symbol.", 400)

        # Get the dict values
        quoteVar = lookup(request.form.get("symbol"))

        # Check if lookup symbol is possible
        if quoteVar == None:
            apology("Invalid Symbol.", 400)

        transaction = False
        confirmation = request.form.get("symbol").lower()
        if not confirmation:
            return apology("Invalid Symbol")
        else:
            return render_template("quoted.html", name=quoteVar["name"], symbol=quoteVar["symbol"], price=quoteVar["price"])
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    # If the form is used:
    if request.method == "POST":

        # Ensure username input
        if not request.form.get("username"):
                return apology("must provide username", 400)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 400)
        # Ensure confirmantion submition
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("please confirm your password", 400)
        # Lower the username for consistensy
        lowUser = request.form.get("username").lower()

        # Query if username in db, if there is already one like the input, return
        if len(db.execute("SELECT * FROM users WHERE username = ?", lowUser)) == 1:
            return apology("username already taken", 400)

        # Hash password with sha256 and salt 8
        passHash = generate_password_hash(request.form.get("password"), "sha256", 8)

        # Insert values into database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", lowUser, passHash)

        return redirect("/login")

    if request.method == "GET":
        return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        # Ensures Symbol is a valid input and user has any shares of that company
        sellRequest = lookup(request.form.get("sell"))
        if sellRequest == None:
            return apology("Invalid Symbol")
        if len(db.execute("SELECT symbol FROM wallet WHERE id = ?", session["user_id"])) == 0:
            return apology("Sorry, you do not have any shares on that company.")
        if  request.form.get("shares")% 1 != 0:
            return ("Invalid number")
        # Ensures Shares is a valid positive number
        sharesRequest =int(request.form.get("shares"))
        if sharesRequest <=0:
            return apology("Invalid shares value.")

        # Check if user has enough shares for transaction
        userShares = int(db.execute("SELECT shares FROM wallet WHERE id = ? AND symbol = ?", session["user_id"], sellRequest["symbol"])[0]["shares"])
        if userShares < sharesRequest:
            return apology("Not enough shares for transaction.")
        transValue = (sharesRequest * int(sellRequest["price"]))
        newCash = transValue + int(db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"])

        date = datetime.now()
        # Reduct shares from user or delete row if shares = 0 and update cash
        if userShares == sharesRequest:
            db.execute("DELETE FROM wallet WHERE id = ? AND symbol = ?", session["user_id"], sellRequest["symbol"])
            db.execute("UPDATE users SET cash = ? WHERE id = ?", newCash, session["user_id"])
            db.execute("INSERT INTO purchases (id, type, symbol, shares, price, total, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)",session["user_id"], "SELL",  sellRequest["symbol"], sharesRequest, transValue, newCash, date)
            transaction = True
            return redirect("/")

        newShares = userShares - sharesRequest
        newTotal = newShares * int(sellRequest["price"])

        db.execute("UPDATE wallet SET shares = ?, total = ? WHERE id = ? AND symbol = ?", newShares, newTotal, session["user_id"], sellRequest["symbol"])
        db.execute("UPDATE users SET cash = ? WHERE id = ?", newCash, session["user_id"])
        db.execute("INSERT INTO purchases (id, type, symbol, shares, price, total, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)",session["user_id"], "SELL",  sellRequest["symbol"], sharesRequest, transValue, newCash, date)


        transaction = True

        return redirect("/")

    else:
        return render_template("sell.html")

