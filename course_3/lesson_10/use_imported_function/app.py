from flask import Flask, render_template
from views import main_views

app = Flask(__name__)

app.add_url_rule("/", view_func=main_views.page_index)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8800, debug=True)

