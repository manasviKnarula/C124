from flask import Flask, jsonify,request

app = Flask(__name__)

tasks = [
    {
        "ID":1,
        "Title": u"buy groceries",
        "Description": u"milk,cheese,fruit,vegetables,pasta",
        "Done": False
    },
    {
        "ID":2,
        "Title": u"learn python",
        "Description": u"need to find a good python tutorial on the web",
        "Done": False
    }
]

@app.route("/")
def hello_world():
    return "Hello World"
    
@app.route("/add-data",methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data: "
        },400)

    task = {
        "ID":tasks[-1]["ID"]+1,
        "Title": request.json["Title"],
        "Description": request.json.get("Description",""),
        "Done": False
    }

    tasks.append(task)

    return jsonify({
        "status": "success!",
        "message": "Task added successfully!"
    })

@app.route("/get-data")
def get_data():
    return jsonify({
        "data": tasks
    })
if (__name__ == "__main__"):
    app.run(debug=True)
