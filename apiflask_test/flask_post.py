from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/posthere', methods=['POST'])
def post_here():
    print("CHECKPOINT 1")
    if request.method == 'POST':
        print("CHECKPOINT 2")
        data = request.json # get data from the request
        print("CHECKPOINT 3")
        # process the data (e.g., save it to a database)
        response = {"message": "Data received", "data": data}
        print("CHECKPOINT 4")
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
