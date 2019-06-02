import os, argparse
import flask, json
from flask import request, jsonify
from datetime import datetime, tzinfo, timezone, date, timedelta
from dateutil import parser


json_file = "./data/big_dump/"

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/api/v1/help")
def hello():
        return "Help! I need somebody to Help!"

@app.route('/api/v1/data', methods=['GET'])
def api_filter():
    query_parameters = request.args

    location_id = query_parameters.get('id')
    start_date = query_parameters.get('start_date')
    start_date = parser.parse(start_date)
    start_date = int((start_date - datetime(1970, 1, 1)).total_seconds())
    end_date = query_parameters.get('end_date')
    end_date = parser.parse(end_date)
    end_date = int((end_date - datetime(1970, 1, 1)).total_seconds())
    
    results = {location_id:{'info':{}, 'readings':{}, 'error':{}}}
    #check if sensor data exists on server
    if (os.path.isfile(json_file + location_id + '.json')):
        #open json file
        with open(json_file + location_id + '.json', "r") as f:
            d = json.load(f)
            #get info
            results[location_id]['info'].update(
				d[location_id]['info']
				)

            #get all timestamps
            all_time = []
            for t in d[location_id]["readings"]:
                all_time.append(int(t))
            #order timestamps
            all_time.sort()
            for t in all_time:
                if (t > start_date) and (t < end_date):
                    results[location_id]['readings'][str(t)] = d[location_id]['readings'][str(t)]
    else:
        results[location_id]['error'] = {'human':"We don't have a sensor by that name round here"}
    #results = "blah"

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)