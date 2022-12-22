from flask import Flask, render_template

app = Flask(__name__)

nav = [
    {"title":"Спортивное Что? Где? Когда?","URL":"/chgk"},
    {"title":"Брейн-ринг","URL":"/brain"},
    {"title":"Своя игра","URL":"/sigame"},
    {"title":"О нас","URL":"/about"},
    {"title":"Глоссарий","URL":"/glossary"},
]

@app.context_processor
def global_context():
    return{
        "nav":nav
    }

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about")
def about_view():
    return render_template("about.html",name="О нас")

@app.route("/chgk")
def chgk_view():
    return render_template("chgk.html",name="Спортивное Что? Где? Когда?")


@app.route("/brain")
def brain_view():
    return render_template("brain.html",name="Брейн-ринг")

@app.route("/sigame")
def sigame_view():
    return render_template("sigame.html",name="Своя игра")

@app.route("/glossary")
def glossary_view():
    return render_template("glossary.html",name="Глоссарий")
