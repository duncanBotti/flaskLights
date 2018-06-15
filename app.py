#!flask/bin/python
from flask import Flask, jsonify, render_template
from gpiozero import LED
from time import sleep

lightOneOn = LED(18)
lightOneOff = LED(23)
lightTwoOn = LED(24)
lightTwoOff = LED(25)
lightThreeOn = LED(20)
lightThreeOff = LED(21)

lightOnSuccess = [ {'light status': 'on'} ]
lightOffSuccess = [ {'light status': 'off'} ]



app = Flask(__name__)

@app.route('/lightApp/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    print("tasks")
    if task_id == 1:
        lightOneOn.on()
        sleep(1)
        lightOneOn.off()
        return jsonify({'light' : lightOnSuccess})
    elif task_id == 2:
        lightOneOff.on()
        sleep(1)
        lightOneOff.off()
        return jsonify({'light' : lightOffSuccess})
    elif task_id == 3:
        lightTwoOn.on()
        sleep(1)
        lightTwoOn.off()
        return jsonify({'light' : lightOnSuccess})
    elif task_id == 4:
        lightTwoOff.on()
        sleep(1)
        lightTwoOff.off()
        return jsonify({'light' : lightOffSuccess})
    elif task_id == 5:
        lightThreeOn.on()
        sleep(1)
        lightThreeOn.off()
        return jsonify({'light' : lightOnSuccess})
    elif task_id == 6:
        lightThreeOff.on()
        sleep(1)
        lightThreeOff.off()
        return jsonify({'light' : lightOffSuccess})
    return jsonify({'light' : lightOffSuccess})


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
