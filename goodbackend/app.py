from flask import Flask, render_template,request
from datetime import datetime
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json

# from model import *
import json
import os
import psutil
import time
import gzip
import uuid

import csv
import shutil
from model import Model

from flask_cors import CORS,cross_origin

app = Flask(__name__)
FlaskJSON(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def debuild(incomingConfig):
    out={}

    for param in incomingConfig:
        if ',' in incomingConfig[param]:
            que=incomingConfig[param].split(',')
            if '-' in que[0]:
                que=[que[x].split('-') for x in range(len(que))]
        else:
            que=incomingConfig[param]  
        out[param]=que
        
    return out

@app.route('/api/datarequest/',methods=['GET','POST'])
@cross_origin()
def datarequest():

    argument=request.args.get('filename')
    print('argument',argument)
    filename='saveddata/'+argument+'/bigdata.json'
    with open(filename) as json_data:
        data = json.load(json_data)
    # with gzip.GzipFile(filename, 'r') as fin:
        # data = json.loads(fin.read().decode('utf-8'))
    # print(data)
    return json_response(response=data)

@app.route('/api/delete',methods=['GET','POST'])
@cross_origin()
def delete():
	toDelete=request.json['simName']
	shutil.rmtree('saveddata/'+toDelete)
	print(toDelete,'has been removed')
	return json_response(response={'foo':'bar'})


@app.route('/api/rename',methods=['GET','POST'])
@cross_origin()
def rename():
	toRename=request.json['simName']
	return json_response(response={'foo':'bar'})



@app.route('/api/newSimThread',methods=['GET','POST'])
@cross_origin()
def newSimThread():
    incomingConfig=debuild(request.json['incomingConfig'])
    model=Model(incomingConfig)
    model.run()
    return json_response(response={'foo':'bar'})


@app.route('/api/folderCache',methods=['GET','POST'])
@cross_origin()
def folderCache():

    def readstatus(simName):
        with open('saveddata/'+simName+'/cache.json') as json_data:
            data = json.load(json_data)
        return data

    def main():

        files=os.listdir('saveddata')

        newfiles=[]

        for x in range(len(files)):
            simName=files[x]
            data=readstatus(simName)

            timeStarted,pureName=simName.split('_')
            

            obj={
                'simName':simName,
                'pureName':pureName,
                'timeStarted':timeStarted,
                't':data['status'],
                'ready':data['ready'],
                'computeTime':data['computeTime']
            }

            newfiles.append(obj)

        sortedlist=sorted(newfiles, key=lambda k: k['timeStarted'], reverse=True)

        return sortedlist

    try:

        newfiles=main()

        return json_response(response={'simulations':newfiles})

    except json.decoder.JSONDecodeError:
        print('decoder error')
        newfiles=[]

# if __name__=="__main__":
	# app.run(host='127.0.0.1:5000')
