from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def question_page():
    """Home page to Madlibs game with questions listed"""

    prompts = silly_story.prompts
    print("our prompts=", prompts)
    return render_template("questions.html", prompts=prompts)


@app.get("/results")
def generate_results():
    """Grab user inputs and produce story using Story instance."""

    text = silly_story.get_result_text(request.args)
    return render_template("results.html", text=text)

