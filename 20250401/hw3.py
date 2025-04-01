import os
from bs4 import BeautifulSoup
import html

# 指定包含所有 HTML 檔案的資料夾路徑
folder_path = "C:/Users/User/Documents/GitHub/cycu_oop_1132_10922162/"  # 替換為你的資料夾路徑

# 初始化結果列表
all_buses = []

# 遍歷資料夾中的所有 HTML 檔案
for file_name in os.listdir(folder_path):
    if file_name.endswith(".html"):  # 確保只處理 HTML 檔案
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(content, "html.parser")

        # 提取所有公車資訊
        buses = []
        for tr in soup.find_all("tr", class_=["ttego1", "ttego2"]):
            # 提取 <td> 元素
            tds = tr.find_all("td")
            if len(tds) < 4:  # 確保有足夠的 <td> 元素
                continue

            # 提取路線名稱、站牌名稱、去返程和預估到站時間
            route = tds[0].text.strip()  # 路線名稱
            stop_name = tds[1].text.strip()  # 站牌名稱
            direction = tds[2].text.strip()  # 去返程
            arrival_time = tds[3].text.strip()  # 預估到站時間

            buses.append({
                "路線": html.unescape(route),
                "站牌": html.unescape(stop_name),
                "方向": direction,
                "到站時間": arrival_time if arrival_time else "未發車"
            })

        # 將每個檔案的結果加入總結果
        all_buses.append({
            "檔案名稱": file_name,
            "公車資訊": buses
        })

# 顯示結果
for station in all_buses:
    print(f"檔案名稱: {station['檔案名稱']}")
    for bus in station["公車資訊"]:
        print(f"路線: {bus['路線']}, 站牌: {bus['站牌']}, 方向: {bus['方向']}, 到站時間: {bus['到站時間']}")
    print("-" * 50)