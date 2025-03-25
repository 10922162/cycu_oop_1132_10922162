import json
import os
import random
import matplotlib.pyplot as plt

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

def manual_bus_stop_input():
    """手動輸入公車站牌資訊"""
    print("請手動輸入公車去程站牌資訊（輸入完畢請輸入 'end' 結束）：")
    stops = []
    while True:
        stop_name = input("站牌名稱: ").strip()
        if stop_name.lower() == 'end':
            break
        stop_address = input("站牌地址: ").strip()
        stops.append({
            'name': stop_name,
            'address': stop_address,
            'status': "未發車",  # 預設狀態
            'eta': None  # 預計到站時間（分鐘）
        })
    return stops

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

def search_stops(stops, keyword):
    """搜尋站牌"""
    results = []
    for i, stop in enumerate(stops, 1):
        if keyword.lower() in stop['name'].lower():
            results.append({
                'sequence': i,
                'name': stop['name'],
                'address': stop['address'],
                'status': stop['status'],
                'eta': stop['eta']
            })
    return results

def plot_stop_name_lengths(stops):
    """繪製站牌名稱長度分佈圖"""
    lengths = [len(stop['name']) for stop in stops]
    plt.figure(figsize=(10, 6))
    plt.hist(lengths, bins=range(1, max(lengths) + 2), color='skyblue', edgecolor='black')
    plt.title('站牌名稱長度分佈圖', fontsize=16)
    plt.xlabel('名稱長度', fontsize=14)
    plt.ylabel('站牌數量', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def display_real_time_info(stops):
    """顯示所有站牌的即時資訊"""
    print("\n=== 即時公車資訊 ===")
    for i, stop in enumerate(stops, 1):
        print(f"第 {i} 站: {stop['name']} - {stop['status']}")

def main():
    print("=== 公車站牌查詢系統 ===")
    file_path = 'bus_stops.json'

    # 載入已儲存的站牌資訊
    stops = load_stops(file_path)
    if stops:
        print(f"已載入 {len(stops)} 個站牌資訊")
    else:
        print("尚無站牌資訊，請手動輸入")

    # 手動輸入站牌資訊
    new_stops = manual_bus_stop_input()
    if new_stops:
        stops.extend(new_stops)
        save_stops(file_path, stops)
        print(f"已儲存 {len(new_stops)} 個新站牌資訊")

    if not stops:
        print("未輸入任何站牌資訊，程式結束")
        return

    print(f"\n目前共有 {len(stops)} 個站牌資訊")

    # 模擬即時狀態更新
    update_real_time_status(stops)

    # 互動式查詢
    while True:
        print("\n請輸入要查詢的站牌名稱 (或輸入 'exit' 離開，'all' 查看所有站牌即時資訊):")
        keyword = input().strip()

        if keyword.lower() == 'exit':
            break

        if keyword.lower() == 'all':
            display_real_time_info(stops)
            continue

        if not keyword:
            continue

        results = search_stops(stops, keyword)

        if not results:
            print(f"找不到包含 '{keyword}' 的站牌")
        else:
            print(f"找到 {len(results)} 個結果:")
            for result in results:
                print(f"第 {result['sequence']} 站: {result['name']} - {result['status']}")

if __name__ == "__main__":
    main()