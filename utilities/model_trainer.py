import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

from utilities.data_loader import load_data
from utilities.model import extract_features

def train_model():
    data = load_data('datasets/ISCX-URL-2016.csv', 'datasets/Phish_Storm.csv')
    X = data['url'].apply(extract_features).tolist()  # Hàm trích xuất đặc trưng
    y = data['label'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = XGBClassifier()
    model.fit(X_train, y_train)
    return model
