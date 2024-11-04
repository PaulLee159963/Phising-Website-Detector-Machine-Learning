import xgboost as xgb
import pickle
from sklearn.model_selection import train_test_split

def extract_features(url):
    # Ví dụ về cách trích xuất các tính năng từ URL
    return [len(url), url.count('.'), url.count('/')]

def train_model(data):
    X = data['url'].apply(extract_features).tolist()
    y = data['label']

    # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Huấn luyện mô hình
    model = xgb.XGBClassifier(use_label_encoder=False)
    model.fit(X_train, y_train)

    # Lưu mô hình
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

def load_model():
    # Tải mô hình đã huấn luyện
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model
