import pandas as pd

# 讀取 Excel 檔案
df = pd.read_excel('C:\\Users\\User\\Desktop\\cycu_oop_1132_10922162\\20250311\\20250311-3\\311.xlsx')

# 假設欄位名稱為 'x' 和 'y'
df['sum'] = df['x'] + df['y']

# 印出相加結果
print(df['sum'])