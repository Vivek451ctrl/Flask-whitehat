from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        'id': 1,
        'contact': u'9238501390',
        'name': u'Varun', 
        'done': False
    },
    {
        'id': 2,
        'contact': u'9837273103',
        'name': u'Vivek', 
        'done': False
    },
    {
        'id': 3,
        'contact': u'9567284092',
        'name': u'Ravi', 
        'done': False
    }
]
@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
    task = {
        'id': data[-1]['id'] + 1,
        'contact': request.json['contact'],
        'name': request.json.get('name', ""),
        'done': False
    }
    data.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)