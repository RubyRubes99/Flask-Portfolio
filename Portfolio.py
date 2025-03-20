from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__, static_folder='static')

# Sample project data (this can be moved to a JSON file later)
projects = [
    {
        "title": "Computer Vision Piano System",
        "description": "A computer vision-based piano that detects key presses using computer vision.",
        "video_url": "https://www.youtube.com/watch?v=HMfhrz4Kx3I",
        "image_url": "CVPiano.png",
        "github": "https://github.com/RubyRubes99/Computer-Vision-Based-Piano-System/blob/97e332680cf64f229362ca5e5fb9ebc742fd9c87/Computer%20Vision%20Based%20Piano%20System%20Report.pdf",
        "status": "Demo Available"
    },
    {
        "title": "Simple Real Time Hand Detector Tutorial",
        "description": "A real time hand detector made using computer vision techniques such as template matching and skin detection.",
        "image_url": "FD_FingerDetected.gif",
        "github": "https://github.com/RubyRubes99/Computer-Vision-Projects/tree/61d00f50d4239033643594d2dc96ffc74b412906/Simple-Real-Time-Hand-Detector",
        "status": "Demo Available"
    },
    {
        "title": "WiFi Lamp",
        "description": "An Android app that controls a lamp over WiFi.",
        "image_url": "WifiLampDisplay.jpg",
        "github": "https://github.com/RubyRubes99/WiFi-Lamp.git",
        "status": "Code Available, No Demo"
    },
    {
        "title": "Speech-to-Text Recognition App",
        "description": "An Android app that transcribes audio into text using offline ML.",
        "image_url": "WifiLampDisplay.jpg",
        "github": "https://github.com/your-repo",
        "status": "Currently not available"
    }
]

@app.route('/')
def home():
    # return render_template('index.html', projects=projects)
    for project in projects:
        project["image_url"] = url_for('static', filename=project["image_url"])
    return render_template('index.html', projects=projects)


@app.route('/projects')
def project_list():
    # return jsonify(projects)
    for project in projects:
        project["image_url"] = url_for('static', filename=project["image_url"])
    return render_template('index.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=True)
