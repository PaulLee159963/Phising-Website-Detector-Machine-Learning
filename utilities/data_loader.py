import pandas as pd

def load_data(iscx_path, phish_storm_path):
    iscx_data = pd.read_csv(iscx_path)
    phish_storm_data = pd.read_csv(phish_storm_path)

    # Xử lý dữ liệu: gộp và chuẩn hóa
    combined_data = pd.concat([iscx_data, phish_storm_data], ignore_index=True)
    combined_data = combined_data[['url', 'label']]  # Chọn các cột cần thiết
    combined_data.dropna(inplace=True)  # Xóa giá trị null

    return combined_data
