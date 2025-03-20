from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

# Sample project data (this can be moved to a JSON file later)
projects = [
    {
        "title": "Computer Vision Piano System",
        "description": "A computer vision-based piano that detects key presses using computer vision.",
        "video_url": "https://github.com/RubyRubes99/Computer-Vision-Based-Piano-System.git",
        "image_url": url_for('static', filename='CVPiano.png'),
        "github": "",
        "status": "Demo Available"
    },
    {
        "title": "Simple Real Time Hand Detector",
        "description": "A real time hand detector made using computer vision techniques such as template matching and skin detection.",
        "image_url": url_for('static', filename='FD_FingerDetected.gif'),
        "github": "",
        "status": "Demo Available"
    },
    {
        "title": "WiFi Lamp",
        "description": "An Android app that controls a lamp over WiFi.",
        "image_url": url_for('static', filename='WifiLampDisplay.jpg'),
        "github": "https://github.com/RubyRubes99/WiFi-Lamp.git",
        "status": "Code Available, No Demo"
    },
    {
        "title": "Speech-to-Text Recognition App",
        "description": "An Android app that transcribes audio into text using offline ML.",
        "image_url": url_for('static', filename='WifiLampDisplay.jpg'),
        "github": "https://github.com/your-repo",
        "status": "Currently not available"
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
