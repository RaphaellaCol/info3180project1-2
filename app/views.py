"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, session, flash, jsonify
import time
import os
from .forms import ContactForm
from app.models import User

app.secret_key = "Info3180"

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    
@app.route('/files/')
def files():
    """files view"""
    #if session['logged_in'] == True:
    return render_template("profile.html")
    #return redirect(url_for('login'))

@app.route('/add', methods=['POST'])
def add_entry():
    rootdir = os.getcwd() + '/app/static/uploads/'
    print rootdir
    """add a file"""
    title = request.form['title']
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(rootdir, filename))
    return render_template("profile.html",title=title)

@app.route('/profile/', methods=["GET","POST"])
def profile():
    """Render the website's profile page to add profile."""
    form = ContactForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        print "oh yeah"
        firstname= request.form['firstname']
        lastname= request.form['lastname']
        age= request.form['age']
        sex= request.form['sex']
        currenttime = timeinfo()
        newprof = User(firstname=firstname, lastname=lastname, age=age, sex=sex, currenttime = currenttime)
        db.session.add(newprof)
        db.session.commit()
        print "yeah"
        return redirect(url_for('profiles'))
    return render_template('profile.html', form=form)
    
def timeinfo():
    return time.strftime("%a %d / %m/ %Y")
    
@app.route('/profiles/', methods=["GET"])
def profiles():
    """Render the website's profile page to view profile list."""
    profiles = User.query.all()
    if request.method =='POST':
        print "POST"
    return render_template('profiles.html', profiles=profiles)
    
@app.route('/profile/<int:id>', methods=["GET", "POST"])
def prof(id):
    """Render the website's profile page to view profile."""
    profile = User.query.get(id)
    #if request.method == "GET":
        # retrieve the user information by 
        # use the name of the image and combine it with the path to the folder where images are stored
        # use the combined path to the image to return the image path along with the other user data
        # and display this in a template
    return render_template('userprofile.html', profile=profile)    
    
    
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
