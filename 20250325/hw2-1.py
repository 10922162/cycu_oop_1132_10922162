import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import font_manager

# 設定中文字型
font_path = r'C:\Windows\Fonts\msjh.ttc'  # 微軟正黑體
font_prop = font_manager.FontProperties(fname=font_path)
rcParams['font.sans-serif'] = font_prop.get_name()  # 設定全域字型
rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

# 定義檔案路徑
file_path = r'C:\Users\User\Documents\GitHub\cycu_oop_1132_10922162\20250325\11111.txt'

# 讀取 Tab 分隔的檔案，指定編碼
df = pd.read_csv(file_path, sep='\t', encoding='utf-16')  # 如果是 Big5，改為 encoding='big5'

# 去除欄位名稱的空白並移除重複的欄位
df.columns = df.columns.str.strip()  # 去除欄位名稱的空白
df = df.loc[:, ~df.columns.duplicated()]  # 移除重複的欄位

# 檢查並轉換資料日期
if '資料日期' in df.columns:
    df['資料日期'] = pd.to_datetime(df['資料日期'], format='%Y%m%d', errors='coerce')  # 將 '資料日期' 轉換為日期格式
    df = df.dropna(subset=['資料日期'])  # 移除無效日期的行
else:
    print("資料中缺少 '資料日期' 欄位，請檢查資料來源。")

# 將匯率相關欄位轉為數值
匯率欄位 = ['現金', '現金.1', '即期', '即期.1']
for col in 匯率欄位:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # 將無效值轉為 NaN

# 繪製現金匯率趨勢圖
if '現金' in df.columns and '現金.1' in df.columns:
    plt.figure(figsize=(12, 6))
    plt.plot(df['資料日期'], df['現金'], label='本行買入', color='red', marker='o')
    plt.plot(df['資料日期'], df['現金.1'], label='本行賣出', color='blue', marker='o')
    plt.xlabel('日期', fontproperties=font_prop)
    plt.ylabel('匯率', fontproperties=font_prop)
    plt.title('現金匯率趨勢圖', fontproperties=font_prop)
    plt.legend(prop=font_prop)
    plt.grid()
    plt.show()
else:
    print("資料中缺少 '現金' 或 '現金.1' 欄位，無法繪製現金匯率圖表。")

# 繪製即期匯率趨勢圖
if '即期' in df.columns and '即期.1' in df.columns:
    plt.figure(figsize=(12, 6))
    plt.plot(df['資料日期'], df['即期'], label='本行買入', color='red', marker='o')
    plt.plot(df['資料日期'], df['即期.1'], label='本行賣出', color='blue', marker='o')
    plt.xlabel('日期', fontproperties=font_prop)
    plt.ylabel('匯率', fontproperties=font_prop)
    plt.title('即期匯率趨勢圖', fontproperties=font_prop)
    plt.legend(prop=font_prop)
    plt.grid()
    plt.show()
else:
    print("資料中缺少 '即期' 或 '即期.1' 欄位，無法繪製即期匯率圖表。")