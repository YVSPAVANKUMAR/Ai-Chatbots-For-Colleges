import os

from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key")

BOTS = [
    {
        "slug": "st-anns",
        "campus_label": "ST ANN'S COLLEGE",
        "name": "St. Ann's College of Engineering & Technology",
        "description": "A serene academic campus established in 2001, offering strong engineering programs with modern facilities near the Bay of Bengal.",
        "image": "images/dashboard/sacet.jpeg",
        "shareable_url": "https://cdn.botpress.cloud/webchat/v2.2/shareable.html?configUrl=https://files.bpcontent.cloud/2025/01/28/08/20250128082206-0MLEL39X.json",
        "status_text": "Open chat support",
    },
    {
        "slug": "bapatla-engineering-college",
        "campus_label": "BAPATLA ENGINEERING COLLEGE",
        "name": "Bapatla Engineering College",
        "description": "An accredited institution known for engineering excellence, strong ethics, and a broad portfolio of technical programs.",
        "image": "images/dashboard/bec.png",
        "shareable_url": "https://cdn.botpress.cloud/webchat/v2.2/shareable.html?configUrl=https://files.bpcontent.cloud/2025/02/01/06/20250201060603-QYVX20JF.json",
        "status_text": "Chat with the campus bot",
    },
    {
        "slug": "chirala-engineering-college",
        "campus_label": "CHIRALA ENGINEERING COLLEGE",
        "name": "Chirala Engineering College",
        "description": "A respected college approved by AICTE and affiliated with JNTU Kakinada, delivering high-quality technical education.",
        "image": "images/dashboard/cec.png",
        "shareable_url": "https://cdn.botpress.cloud/webchat/v2.2/shareable.html?configUrl=https://files.bpcontent.cloud/2025/01/28/08/20250128082240-IV6NFH3T.json",
        "status_text": "Start a chat",
    },
    {
        "slug": "vrs-yrn-college",
        "campus_label": "VRS & YRN COLLEGE",
        "name": "VRS & YRN College",
        "description": "A long-standing institution since 1951, focused on moral values, quality academics, and community impact.",
        "image": "images/dashboard/vrs.jpeg",
        "shareable_url": "https://cdn.botpress.cloud/webchat/v2.2/shareable.html?configUrl=https://files.bpcontent.cloud/2025/01/28/08/20250128082311-HRLKSL0T.json",
        "status_text": "Launch the bot",
    },
]

BOT_LOOKUP = {bot["slug"]: bot for bot in BOTS}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", bots=BOTS)


@app.route("/chatbot/<bot_slug>")
def chatbot(bot_slug):
    bot = BOT_LOOKUP.get(bot_slug)
    if not bot:
        abort(404)
    return render_template("chatbot.html", bot=bot)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 - Page Not Found</h1>", 404


if __name__ == "__main__":
    app.run(debug=True)
