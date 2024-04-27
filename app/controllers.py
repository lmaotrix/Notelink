from app import app

@app.route("/")
def index():
    return "welcome to NoteLink!"

@app.route("/posted", methods=["GET","POST"])
def posted():
    # TODO
    return render_template("posted.html")