import eel
#from app import app

if __name__ == "__main__":
   eel.init("app")
   eel.start("templates/index.html", size=(1000, 600))
   #app.run(port=8000)