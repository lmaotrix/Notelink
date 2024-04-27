from app import app

@app.route("/")
def index():
    return "welcome to NoteLink!"