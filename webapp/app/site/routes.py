import json
import requests

from flask import render_template, request, flash, redirect, url_for
import os

from app.site.forms import MessageForm
from . import site


@site.route("/", methods=['GET', 'POST'])
def home():
    form = MessageForm()
    msg_type = ''

    if form.validate_on_submit():
        msg = form.text_area.data
        api_url = os.getenv('API_URL')
        msg_json = json.dumps({'text': msg})

        try:
            resp = requests.post(api_url, msg_json)
            if resp.status_code == 200:
                msg_type = json.loads(resp.content).get('value')[0]
            else:
                flash('{} Error'.format(resp.status_code), 'error')
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
            flash('API url should contain http(s)://.', 'error')
        except requests.exceptions.ConnectionError:
            flash('Could not establish connection with the API.', 'error')
        redirect(url_for('site.home', form=form, msg_type=msg_type))

    return render_template('index.html', form=form, msg_type=msg_type)


@site.route("/info")
def info():
    return render_template('info.html')


@site.route("/post", methods=["POST"])
def send_request():
    a=1

    r = request.form
    api_url = os.getenv('API_URL')
    req_data = list(request.form.keys())[0]

    try:
        resp = requests.post(api_url, req_data)
        if resp.status_code == 200:
            return resp.content
        else:
            print(resp.status_code)

    except Exception:
        return 'Cannot reach the api.'

    else:
        return 'error'