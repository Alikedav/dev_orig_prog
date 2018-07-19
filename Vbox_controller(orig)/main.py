from flask import Flask, request, render_template
from running_vms import get_running_vms
from start_vms import poweron_vm
from stop_vms import poweroff_vm

current_Station = ''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/station/<string:id>')
def station(id):
    current_Station = str(id)
    return render_template('index1.html')
    
@app.route('/startvmid', methods=['POST','GET'])
def startvmid():
    if request.method == "POST":
        #text = request.form['str_vm']
        poweron_vm(current_Station)
        return render_template('index1.html')

@app.route('/stopvmid', methods=['POST','GET'])
def stopvmid():
    if request.method == "POST":
        #text = request.form['stp_vm']
        poweroff_vm(current_Station)
        return render_template('index1.html')

@app.route('/listvm', methods=['POST','GET'])
def listvm():
    if request.method == "POST":
        #text = request.form['li_vm']
        #processed_text = text.upper()
        get_running_vms()
        return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug = True)
