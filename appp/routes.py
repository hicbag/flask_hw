from appp.forms import TopCities
from appp import myapp
from flask import render_template, flash, redirect
from appp import db
from sqlalchemy import asc
from appp.models import City



@myapp.route('/', methods=['GET', 'POST'])
def home():
    user = {"Username": "Thomas"}
    form = TopCities()
    
    cities = City.query.filter().order_by(City.rank.asc())

    db.create_all()
    
    if form.validate_on_submit():
        flash(f'Added data for city {form.city_name.data}')
        city_name = form.city_name.data
        city_rank = form.city_rank.data
        city_visited = form.is_visited.data
        entry = City(city_name, city_rank, city_visited)
        db.session.add(entry)
        db.session.commit()
        return redirect('/')
    return render_template('home.html', title='Top Cities', user=user, form=form, cities=cities)
