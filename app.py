from flask import Flask, render_template, request
from utilities.model import extract_features
from utilities.model_trainer import train_model
from utilities.data_loader import load_data

app = Flask(__name__)

# Huấn luyện mô hình khi khởi động
model = train_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = str(request.form['url'])  # Đảm bảo url là chuỗi
    features = extract_features(url)  # Giả sử bạn có một hàm để trích xuất đặc trưng
    prediction = model.predict([features])  # Sử dụng features thay vì url
    result = 'Phishing' if prediction[0] == 1 else 'Legitimate'
    return render_template('result.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)
