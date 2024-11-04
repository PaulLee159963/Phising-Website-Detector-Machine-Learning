import pandas as pd
from utilities.model import load_model, extract_features

def predict_urls(urls):
    model = load_model()  # Tải mô hình đã huấn luyện
    features = [extract_features(url) for url in urls]
    predictions = model.predict(features)
    return predictions

if __name__ == "__main__":
    # Ví dụ test với danh sách URL
    test_urls = ['http://example1.com', 'http://example2.com']  # Thay đổi với các URL của bạn
    results = predict_urls(test_urls)
    
    for url, result in zip(test_urls, results):
        label = "Phishing" if result == 1 else "Legitimate"
        print(f'URL: {url} - {label}')
