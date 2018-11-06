from flask import Flask, render_template, request
import logging
from logging import Formatter, FileHandler
from forms import SearchForm
import os
from main import *

# App Config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'

# Controllers

#@app.route('/')
#def home():
#    return render_template('layouts/main.html')




@app.route('/', methods=['GET', 'POST'])
def search():

    form = SearchForm(request.form)
    if request.method == 'POST':
        RA = request.form['right_ascension']
        DEC = request.form['declination']
        mystar = star(RA, DEC)
    else:
        RA = ""
        DEC = ""
        mystar = ["", "", ""]

    print(mystar)
    return render_template('pages/search.html', form=form, RA=RA, DEC=DEC, dist=mystar[0], temp=mystar[1], radius=mystar[2])


# Error handlers.

#@app.errorhandler(500)
#def internal_error(error):
    #db_session.rollback()
#    return render_template('errors/500.html'), 500


#@app.errorhandler(404)
#def not_found_error(error):
#    return render_template('errors/404.html'), 404

#if not app.debug:
#    file_handler = FileHandler('error.log')
#    file_handler.setFormatter(
#        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
#    )
#    app.logger.setLevel(logging.INFO)
#    file_handler.setLevel(logging.INFO)
#    app.logger.addHandler(file_handler)
#    app.logger.info('errors')


# Launch

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
