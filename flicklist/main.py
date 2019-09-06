from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    
    movie = get_random_movie()

    tomorrow_movie = get_random_movie()

    
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    
    content += "<h1>Tomorrow's movie</h1>"
    content += "<ul>"
    content += "<li>" + tomorrow_movie + "</li>"

    return content

def get_random_movie():
    
    movie_list = ["Batman Returns","Aquaman", "Taken 3", "Spiderman", "Shutter Island"]

    return random.choice(movie_list)


app.run()
