def extract_features(url):
    # Trích xuất đặc trưng từ URL
    features = [len(url), url.count('.'), url.count('/')]
    return features
