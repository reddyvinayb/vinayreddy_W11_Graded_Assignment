from flask import Flask, request, jsonify
import joblib
import gzip

app = Flask(__name__)

try:
    with gzip.open('../Microservices/model/model_binary.dat.gz', 'rb') as f:
        model = joblib.load(f)
except Exception as e:
    print(f"Error loading Model: {e}")


@app.route('/')
def home():
    return "Congratulations it's a web app"

@app.route('/info')
def info():
    return jsonify({"info": "This is the info endpoint"})

@app.route('/health')
def health():
    return jsonify({"info": "This is the health endpoint"})

@app.route('/predict',methods=['POST'])
def predict():
    data = request.json
    features = [list(data.values())]
    prediction = model.predict(features)[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




