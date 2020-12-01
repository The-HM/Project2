from Project2_Flask import app, forms
from flask import request, render_template
import string

@app.route('/', methods=['GET', 'POST'])
def search():
    my_form = forms.MovieReviewSearch(request.form)
    if request.method == "POST":
        title = request.form["title"]
        title = title.replace(" ", "+")
        order = request.form["order"]
        critic = request.form["critics_picks"]
        search_results = forms.movie_search(title, order, critic)

        return render_template('results.html', result=search_results, title=title, order=order,
                               critic=critic, string=string, form=my_form)
    return render_template('search.html', form=my_form)
