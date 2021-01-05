import requests
from flask import Flask, request

app = Flask(__name__)

url = 'https://disease.sh/v3/covid-19/historical/'


def find_peak(cases):
    cases_values = list(cases.values())
    absuloute_values = []
    for i in range(len(cases_values) - 1):
        absuloute_values.append(cases_values[i + 1] - cases_values[i])
    cases_keys = list(cases.keys())
    del cases_keys[0]
    cases_with_absulotue = {cases_keys[i]: absuloute_values[i] for i in range(len(absuloute_values))}
    max_value = max(cases_with_absulotue.values())
    max_keys = [k for k, v in cases_with_absulotue.items() if v == max_value]
    return max_value, max_keys


@app.route('/newCasesPeak')
def new_cases_peak():
    country = request.args.get("country", default=None)
    lastdays = request.args.get("lastdays", default=30)
    try:
        country_url = url + country + '?lastdays=' + str(lastdays)
        response_json = requests.get(country_url).json()['timeline']['cases']
    except Exception:
        return '{}'
    max_value, max_keys = find_peak(response_json)
    return_value = dict(country=country, method='newCasesPeak', date=''.join(max_keys), value=max_value)
    return f'{return_value}'


@app.route('/recoveredPeak')
def recovered_peak():
    country = request.args.get("country", default=None)
    lastdays = request.args.get("lastdays", default=30)
    try:
        country_url = url + country + '?lastdays=' + str(lastdays)
        response_json = requests.get(country_url).json()['timeline']['recovered']
    except Exception:
        return '{}'
    max_value, max_keys = find_peak(response_json)
    return_value = dict(country=country, method='recoveredPeak', date=''.join(max_keys), value=max_value)
    return f'{return_value}'


@app.route('/deathsPeak')
def deaths_peak():
    country = request.args.get("country", default=None)
    lastdays = request.args.get("lastdays", default=30)
    try:
        country_url = url + country + '?lastdays=' + str(lastdays)
        response_json = requests.get(country_url).json()['timeline']['deaths']
    except Exception:
        return '{}'
    max_value, max_keys = find_peak(response_json)
    return_value = dict(country=country, method='deathsPeak', date=''.join(max_keys), value=max_value)
    return f'{return_value}'


@app.route('/status')
def status():
    country_url = url
    try:
        response_json = requests.get(country_url)
    except Exception:
        return '{}'
    return_value = dict(status='success' if response_json else 'failed')
    return f'{return_value}'


if __name__ == '__main__':
    app.run(port=5555)
