import requests

# 下載台北市所有路線的站點資料
url = "https://ptx.transportdata.tw/MOTC/v2/Bus/StopOfRoute/City/Taipei?$format=JSON"
routes = requests.get(url).json()

start_name = input("請輸入起點站名：")
end_name = input("請輸入終點站名：")

candidates = []
for route in routes:
    stops = [stop['StopName']['Zh_tw'] for stop in route['Stops']]
    if start_name in stops and end_name in stops:
        # 確認起點在終點前面（同方向）
        if stops.index(start_name) < stops.index(end_name):
            candidates.append({
                "路線名稱": route['RouteName']['Zh_tw'],
                "方向": route['Direction'],
                "起點序": stops.index(start_name),
                "終點序": stops.index(end_name)
            })

if candidates:
    print("可直達路線：")
    for c in candidates:
        print(f"{c['路線名稱']}（方向 {c['方向']}）")
else:
    print("查無直達路線")