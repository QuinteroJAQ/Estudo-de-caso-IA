from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Cargar el modelo desde el archivo .pkl
with open('melhor_modelo.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)