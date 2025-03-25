import json
import os
import random
import time

def load_stops(file_path):
    """從 JSON 檔案讀取站牌資訊"""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_stops(file_path, stops):
    """將站牌資訊儲存到 JSON 檔案"""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(stops, file, ensure_ascii=False, indent=4)

def generate_default_stops():
    """自動生成預設的站牌資訊"""
    return [
        {"name": "蘆洲總站", "address": "蘆洲區中正路", "status": "未發車", "eta": None},
        {"name": "王爺廟口", "address": "蘆洲區中山一路", "status": "未發車", "eta": None},
        {"name": "空中大學", "address": "蘆洲區中正路", "status": "未發車", "eta": None},
        {"name": "幸福市場", "address": "蘆洲區幸福路", "status": "未發車", "eta": None},
        {"name": "捷運徐匯中學站", "address": "蘆洲區徐匯路", "status": "未發車", "eta": None},
    ]

def update_real_time_status(stops):
    """模擬更新即時狀態"""
    for i, stop in enumerate(stops):
        if i == 0:
            stop['status'] = "未發車"
            stop['eta'] = None
        elif random.random() < 0.3:
            stop['status'] = "將到站"
            stop['eta'] = 1
        else:
            eta = random.randint(2, 10)
            stop['status'] = f"{eta} 分後到達"
            stop['eta'] = eta

def display_real_time_info(stops):
    """顯示所有站牌的即時資訊"""
    print("\n=== 即時公車資訊 ===")
    for i, stop in enumerate(stops, 1):
        print(f"第 {i} 站: {stop['name']} - {stop['status']}")

def auto_refresh(stops, refresh_interval=5):
    """自動刷新即時資訊"""
    while True:
        update_real_time_status(stops)  # 更新即時狀態
        display_real_time_info(stops)  # 顯示即時資訊
        print(f"\n（每 {refresh_interval} 秒自動刷新，按 Ctrl+C 結束）")
        time.sleep(refresh_interval)  # 等待指定的刷新間隔

def main():
    print("=== 公車站牌查詢系統 ===")
    file_path = 'bus_stops.json'

    # 載入已儲存的站牌資訊，或生成預設站牌資訊
    stops = load_stops(file_path)
    if not stops:
        print("尚無站牌資訊，正在生成預設站牌...")
        stops = generate_default_stops()
        save_stops(file_path, stops)
        print(f"已生成 {len(stops)} 個預設站牌資訊")

    print(f"\n目前共有 {len(stops)} 個站牌資訊")

    # 自動刷新即時資訊
    try:
        auto_refresh(stops, refresh_interval=5)  # 每 5 秒刷新一次
    except KeyboardInterrupt:
        print("\n已停止自動刷新，程式結束")

if __name__ == "__main__":
    main()