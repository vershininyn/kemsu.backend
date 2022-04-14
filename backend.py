from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask import request
from flask import jsonify

import csv
import uuid
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', str(os.urandom(50)))
csrf = CSRFProtect(app)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    title = request.json['title']
    weight = request.json['weight']
    color = request.json['color']

    json_status = {
        'status': True,
        'msg': '',
        'uuid': ''
    }

    json_status = validate(json_status, title, weight)

    if not json_status['status']:
        return jsonify(json_status)

    json_status['uuid'] = write_to_csv(title, weight, color)

    return jsonify(json_status)


def validate(json_status, title, weight):
    title_length = len(title)

    if (title_length < 3) or (title_length > 120):
        json_status['status'] = False
        json_status['msg'] = 'Длина названия должна быть от 3 до 120 символов'
        return json_status

    try:
        val = int(weight)

        if (val < 1) or (val > 500):
            json_status['status'] = False
            json_status['msg'] = 'Вес должен быть целым числом от 1 до 500 включительно'
            return json_status

    except ValueError:
        json_status['status'] = False
        json_status['msg'] = 'Вес должен быть целым числом'
        return json_status

    return json_status


def write_to_csv(title, weight, color):
    uuid_str = str(uuid.uuid4())

    with open('kemsu.backend.csv', 'a+', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow([uuid_str, str(title), str(weight), str(color)])
        csvfile.close()

    return uuid_str
