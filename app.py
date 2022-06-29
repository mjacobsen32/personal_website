from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', current="home")

@app.route('/resume')
def resume():
    return render_template('resume.html', current="resume")

@app.route('/research')
def research():
    return render_template('research.html', current="research")

@app.route('/projects')
def projects():
    return render_template('projects.html', current="projects")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    
    
    