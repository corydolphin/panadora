from flask import Flask, render_template, request, jsonify

#from boilerflask.models import User
#from boilerflask.forms import (LoginForm)
from pandorapi import app #, loginManager, crypt, db, cache
from pandora.pandora import Pandora, PandoraError

@app.route('/', methods=['GET'] )
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        p = Pandora()
        p.connect(request.form.get('username'),request.form.get('password'))
        return jsonify(p.json())
    except PandoraError as pe:
        return jsonify(errror="Invalid Credentials"), 401
    except:
        return jsonify(error="unknown error"), 500


@app.route('/stations')
def stations():
    p = getPandora()
    return jsonify(stations=[s.json() for s in p.get_stations()])

@app.route('/station/<station_id>/songs')
def getSongs(station_id):
    p = getPandora()
    return jsonify(songs= [s.json() for s in p.get_songs(station_id)])

def getPandora():
    attr_list = ['partnerId','partnerAuthToken','time_offset','userId','userAuthToken']
    _d = {attr : request.args.get(attr) for attr in attr_list}
    _d['time_offset'] = float(_d['time_offset'])
    return Pandora.hydrate(_d)



@app.errorhandler(404)
def page_not_found(error):
    return 'Cory should really handle this page_not_found'


@app.errorhandler(403)
def forbidden(error):
    return 'Cory should really handle this forbidden'


@app.errorhandler(500)
def internal_server_error(error):
    return 'Cory should really handle this internal server error'

