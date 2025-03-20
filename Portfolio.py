from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample project data (this can be moved to a JSON file later)
projects = [
    {
        "title": "Computer Vision Piano System",
        "description": "A computer vision-based piano that detects key presses using computer vision.",
        "video_url": "https://github.com/RubyRubes99/Computer-Vision-Based-Piano-System.git",
        "github": "",
        "status": "Demo Available"
    },
    {
        "title": "WiFi Lamp",
        "description": "An Android app that controls a lamp over WiFi.",
        "github": "https://github.com/RubyRubes99/WiFi-Lamp.git",
        "status": "Code Available, No Demo"
    },
    {
        "title": "Speech-to-Text Recognition App",
        "description": "An Android app that transcribes audio into text using offline ML.",
        "github": "https://github.com/your-repo",
        "status": "Demo & Code Available"
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/projects')
def project_list():
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=True)
