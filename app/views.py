"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from pydoc import describe
from app import app,db
from flask import render_template, render_template_string, request, redirect, send_from_directory, url_for, flash
from app.forms import PropertyForm
from app.models import propertyProfile
from werkzeug.utils import secure_filename
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
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['POST','GET'])
def property():
    """Render the website's property form page."""
    myForm = PropertyForm()
    if request.method == 'POST' and myForm.validate_on_submit():
        title = request.form['title']
        description = request.form['description']
        bedrooms = request.form['bedrooms']
        bathroom = request.form['bathroom']
        price = request.form['price']
        type = request.form['type']
        location = request.form['location']
        photo= request.files['photo']
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                
        property = propertyProfile(title, bedrooms, bathroom, location, price, type, description, filename)
        db.session.add(property)
        db.session.commit()
        flash('property created successfully', 'success')
        return redirect(url_for('properties'))
    return render_template('propertyForm.html', form=myForm)

@app.route('/properties')
def properties():
    """Render the website's properties page."""
    property_profiles = db.session.query(propertyProfile).all()
    print(property_profiles)
    return render_template('properties.html',property_profiles=property_profiles)

@app.route('/properties/<propertyid>')
def individualproperty(propertyid):
    """Query database for complete property info for id, then pass to a template to render the info"""
    Iid = propertyProfile.query.filter_by(id=propertyid).first()
    return render_template('individualproperty.html', Iid = Iid)
        

@app.route("/uploads/<filename>") 
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)
    
def get_uploaded_images():
    uploadlist = []
    for subdir, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for file in files:
            f_name, f_ext = os.path.splitext(file)
            if f_ext in [".png",".jpg"]:
                uploadlist.append(file)
    return uploadlist


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
