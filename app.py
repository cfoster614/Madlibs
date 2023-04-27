from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story, story2, story3


app = Flask(__name__)
app.config['SECRET_KEY'] = "scamp"

debug = DebugToolbarExtension(app)

stories = {
    'Once upon a time...': story,
    'One day...': story2,
    'The ___ happily...': story3
}


@app.route('/')
def choose_story():

    return render_template('homepage.html', stories=stories.values())


@app.route('/questions')
def ask_questions():
    title= request.args['story_id']
    story = stories[title]
    prompt = story.prompts

    return render_template('questions.html', prompts=prompt, title=title, story=story)


@app.route('/story')
def show_story():
    title = request.args['story_id']
    story =  stories[title]
    text = story.generate(request.args)

    return render_template('story.html', text=text, title=title, story=story)
