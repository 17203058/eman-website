from flask import render_template

def hello(request):
    return render_template('eman.html')