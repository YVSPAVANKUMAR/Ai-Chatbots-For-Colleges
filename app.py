from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "your_secret_key"

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["college_chatbot"]
bots_col = db["bots"]

# Sample Bot Document Format in MongoDB
# {
#   "name": "Library Bot",
#   "description": "Answers library-related questions",
#   "channel": "library-bot"   # Botpress shareable link path
# }

# ROUTES

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    bots = list(bots_col.find())
    return render_template("dashboard.html", bots=bots)

@app.route("/chatbot/<bot_id>")
def chatbot(bot_id):
    bot = bots_col.find_one({"_id": ObjectId(bot_id)})
    if not bot:
        return "Bot not found", 404
    return render_template("chatbot.html", bot=bot)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Placeholder login route (to be expanded)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # TODO: Authenticate user
        return redirect(url_for("dashboard"))
    return render_template("login.html")

# Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Page Not Found</h1>", 404

# MAIN
if __name__ == "__main__":
    app.run(debug=True)
