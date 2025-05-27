# 將資料存入變數
data = "20250527/GetEstimateTime"

# 分割資料
date, action = data.split("/")
print(f"日期: {date}")
print(f"動作: {action}")

# 將日期格式化為更易讀的格式
from datetime import datetime

formatted_date = datetime.strptime(date, "%Y%m%d").strftime("%Y-%m-%d")
print(f"格式化日期: {formatted_date}")

# 使用資料進行邏輯處理
if action == "GetEstimateTime":
    print("執行預估時間的相關邏輯...")