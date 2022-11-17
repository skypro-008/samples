from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

page_content = """

<head>
<link rel="stylesheet" href="/static/main.css" />
<script type="text/javascript" src="/static/main.js"> </script>
</head>

<h1>привет это мой сайтик </h1>

<img src="/static/img.png">

"""

@app.route('/')
def index():
    return page_content


@app.get('/uploads/<path:path>')
def send_from_uploads(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)


