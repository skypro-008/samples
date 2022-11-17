from flask import Flask, render_template, jsonify, request

# expenses_data = {
#     "milk": 150,
#     "sugar": 90,
#     "cookies": 200,
#     "corn-flakes": 140,
#     "nutella": 250,
# }

app = Flask(__name__)


def get_stats_from_expenses(expenses_data: dict) -> dict:
    exp_count = len(expenses_data)
    exp_values = expenses_data.values()
    exp_max = max(exp_values)
    exp_min = min(exp_values)
    exp_sum = sum(exp_values)
    exp_avg = exp_sum / exp_count

    return {"count": exp_count, "total": exp_sum, "max": exp_max, "min": exp_min, "avg": exp_avg}


@app.post('/api/1/grocery-stats')
def api_stats():
    expenses_data = request.get_json()
    stats = get_stats_from_expenses(expenses_data)
    return jsonify(stats), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
