from utils import*
from flask import Flask, render_template

app = Flask(__name__)

candidates = load_candidates_from_json('data/candidates.json')

@app.route('/')
def index_page():
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:x>')
def candidate_page(x):
    candidate = candidates[x-1]
    print(candidate)
    return render_template('card.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def search_page(candidate_name):
    search_candidates = get_candidates_by_name(candidate_name, candidates)

    return render_template('search.html', candidates=search_candidates, count=len(search_candidates))

@app.route('/skill/<skill_name>')
def skill_page(skill_name):
    search_candidates = get_candidates_by_skill(skill_name, candidates)

    return render_template('skill.html', candidates=search_candidates, count=len(search_candidates))

if __name__ == '__main__':
    app.run()