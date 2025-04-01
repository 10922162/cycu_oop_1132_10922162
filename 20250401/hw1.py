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
else:
    print(f"無法下載網頁，HTTP 狀態碼: {response.status_code}")