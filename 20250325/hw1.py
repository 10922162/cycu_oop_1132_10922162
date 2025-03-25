import pandas as pd

# 定義檔案路徑
file_path = r'C:\Users\User\Documents\GitHub\cycu_oop_1132_10922162\20250325\ExchangeRate@202503251852.csv'

# 讀取 CSV 檔案
df = pd.read_csv(file_path)

# 檢查資料
print("原始資料：")
print(df.head())  # 查看前 5 筆資料
print("欄位名稱：", df.columns)