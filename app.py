from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def question_page():
    """Home page to Madlibs game with questions listed"""

    # check how many inputs are in the story list
    # loop through the list
    # render the amount of inputs needed
    prompt_block = ""
    for prompt in silly_story.prompts:
        prompt_block += render_template("madlib_prompt.html", prompt = prompt)
    return prompt_block

