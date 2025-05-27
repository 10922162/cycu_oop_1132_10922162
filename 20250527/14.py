import requests
import html
import pandas as pd
from bs4 import BeautifulSoup

# 網頁 URL
url = '''https://pda5284.gov.taipei/MQS/route.jsp?rid=10417'''

# 發送 GET 請求
response = requests.get(url)

# 確保請求成功
if response.status_code == 200:
    # 將內容寫入 bus1.html
    with open("bus1.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("網頁已成功下載並儲存為 bus1.html")

    # 重新讀取並解碼 HTML
    with open("bus1.html", "r", encoding="utf-8") as file:
        content = file.read()

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(content, "html.parser")

    # 初始化去程與回程的資料
    go_stops = []
    back_stops = []

    # 提取去程站名與連結
    for tr in soup.find_all("tr", class_=["ttego1", "ttego2"]):
        td = tr.find("td")
        if td and td.find("a"):
            stop_name = html.unescape(td.text.strip())
            stop_link = td.find("a")["href"]
            go_stops.append({"站名": stop_name, "連結": stop_link})

    # 提取回程站名與連結
    for tr in soup.find_all("tr", class_=["tteback1", "tteback2"]):
        td = tr.find("td")
        if td and td.find("a"):
            stop_name = html.unescape(td.text.strip())
            stop_link = td.find("a")["href"]
            back_stops.append({"站名": stop_name, "連結": stop_link})

    # 將資料轉換為 DataFrame
    go_df = pd.DataFrame(go_stops)
    back_df = pd.DataFrame(back_stops)

    # 輸出結果
    print("去程站名與連結:")
    print(go_df)
    print("\n回程站名與連結:")
    print(back_df)

    # 儲存為 CSV 檔案
    go_df.to_csv("去程站名與連結.csv", index=False, encoding="utf-8-sig")
    back_df.to_csv("回程站名與連結.csv", index=False, encoding="utf-8-sig")
    print("\n已將去程與回程資料分別儲存為 CSV 檔案。")

    # 整合 API 資料
    API_URL = "https://data.taipei/api/v1/dataset/2749b84d-a09c-4c03-a7ff-710e7ebf209c"
    RESOURCE_ID = "2749b84d-a09c-4c03-a7ff-710e7ebf209c"

    def fetch_bus_data(limit=100, offset=0):
        """從 API 獲取公車即時動態資料"""
        params = {
            "resource_id": RESOURCE_ID,
            "limit": limit,
            "offset": offset
        }
        response = requests.get(API_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if "result" in data and "records" in data["result"]:
                return data["result"]["records"]
            else:
                print("無法從 API 獲取有效資料。")
                return []
        else:
            print(f"API 請求失敗，HTTP 狀態碼: {response.status_code}")
            return []

    # 測試 API 請求
    bus_data = fetch_bus_data(limit=10)
    if bus_data:
        # 將資料轉換為 DataFrame
        df = pd.DataFrame(bus_data)
        print("公車即時動態資料：")
        print(df.head())

        # 儲存為 CSV 檔案
        df.to_csv("公車即時動態資料.csv", index=False, encoding="utf-8-sig")
        print("\n已將公車即時動態資料儲存為 CSV 檔案。")

    # 新增處理 "20250527/GetEstimateTime" 資料的邏輯
    data = "20250527/GetEstimateTime"
    date, action = data.split("/")
    print(f"\n處理資料: 日期={date}, 動作={action}")

    # 將日期格式化為更易讀的格式
    from datetime import datetime
    formatted_date = datetime.strptime(date, "%Y%m%d").strftime("%Y-%m-%d")
    print(f"格式化日期: {formatted_date}")

    # 根據動作執行對應邏輯
    if action == "GetEstimateTime":
        print("執行預估時間的相關邏輯...")
else:
    print(f"無法下載網頁，HTTP 狀態碼: {response.status_code}")