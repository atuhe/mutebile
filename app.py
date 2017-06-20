import os

# We are importing 'Flask' to create an application,
# 'render_template' to render the given template as the response

from flask import Flask, render_template

# Create a flask app and set a random secret key
app = Flask ( __name__ )


# / route and its view. This renders the index.html template
@app.route ( '/' )
def index():
    return render_template ( 'index.html' )


# Illustration of a single view handling multiple routes
@app.route ( '/about/mission&Vision/' )
def mission():
    return render_template ( 'about/page.html')

@app.route ( '/about/mandate/' )
def manadate():
    return render_template ( 'about/contact.html')

@app.route ( '/about/Executive-Director/')
def about():
    return render_template ( 'about/about.html')

@app.route ( '/about/Chairman-TMCE/' )
def chairman():
    return render_template ( 'about/chair.html')

@app.route ( '/about/background-of-TMCE/' )
def background():
    return render_template ( 'about/background.html')

@app.route ( '/about/activities/' )
def activity():
    return render_template ( 'about/activities.html')

@app.route ( '/staff-structure/' )
def staff():
    return render_template ( 'staff_structure.html')




if __name__ == '__main__':
    app.run (debug=True, port=int ( "4000" ))
