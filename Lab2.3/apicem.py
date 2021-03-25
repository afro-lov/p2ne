import requests, json
import pprint as pp

from flask import Flask, jsonify, render_template

app = Flask(__name__)




def new_ticket():
    url = 'https://sandboxapicem.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser","password": "Cisco123!"}
    header = {"content-type": "application/json"}

    response = requests.post(url, data=json.dumps(payload),headers=header, verify=False)

    return response.json()['response']['serviceTicket']

@app.route("/")
def index():
    return render_template("topology.html")

@app.route('/api/topology')
def topology():
    return jsonify(s)

if __name__ == '__main__':
    # https://sandboxapicem.cisco.com/api/v1/topology/physical-topology

    ticket = new_ticket()
    # controller = "devnetapi.cisco.com/sandbox/apic_em"
    controller = "sandboxapicem.cisco.com"
    # url = "https://" + controller + "/api/v1/topology/physical-topology"
    url = "https://" + controller + "/api/v1/topology/physical-topology"
    header = {"content-type": "application/json","X-Auth-Token": ticket}

    responce = requests.get(url, headers=header, verify=False)

    # print("Topology = ")

    s = responce.json()['response']
    print(s)
    app.run(debug=True)
