from flask import Flask, render_template
from exceptions import  UnderConstructionError, NotImplementedPageError

app = Flask(__name__)

# Обычные вьюшки

@app.route('/1/')
def page_1():

    # Здесь может находиться код, который, в числе прочего, будет рейзить ошибку.
    raise UnderConstructionError("Проводятся работы над этой страницей")


@app.route('/2/')
def page_2():

    # Здесь может находиться код, который, в числе прочего, будет рейзить ошибку.
    raise NotImplementedPageError("Страница еще не готова")

# Обработчики ошибок


@app.errorhandler(404)
def page_404(error):
    return f"Страница не найдена на нашем сервере: {error}", 404


@app.errorhandler(UnderConstructionError)
def page_under_construction(error):
    return f"Страница находится на доработке: {error}", 403


@app.errorhandler(NotImplementedPageError)
def page_under_construction(error):
    return f"Страница еще готова {error}", 403


app.run(debug=True)

