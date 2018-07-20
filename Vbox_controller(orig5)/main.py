from flask import Flask, request, render_template, url_for, redirect
from running_vms import get_running_vms
from start_vms import poweron_vm
from stop_vms import poweroff_vm


current_Station = ''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/station/<string:id>')
def station(id):
    global current_Station
    global current_Station
    current_Station = str(id)
    return render_template('index1.html')
    
@app.route('/startvmid', methods=['POST','GET'])
def startvmid():
    if request.method == "POST":
        #print("start current = "+current_Station)
        poweron_vm(current_Station)
        #return render_template('index1.html')
        return redirect('http://10.10.3.155/labs')

@app.route('/stopvmid', methods=['POST','GET'])
def stopvmid():
    if request.method == "POST":
        try:
            #print("stop current = "+current_Station)
            poweroff_vm(current_Station)
            return render_template('index1.html')
        except:
            return render_template('index.html')

@app.route('/listvm', methods=['POST','GET'])
def listvm():
    if request.method == "POST":
        stations = get_running_vms()
        #print("list current = "+current_Station)
        #return render_template('index1.html')
        return render_template('index1.html', stations = stations)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
