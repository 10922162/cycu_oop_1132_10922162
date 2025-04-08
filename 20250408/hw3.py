import csv
from playwright.sync_api import sync_playwright

def fetch_bus_route_data_with_playwright(route_id, output_file="bus_route.csv"):
    """
    使用 Playwright 從臺北市公開網站取得公車路線資料並儲存為 CSV。

    :param route_id: 公車代碼
    :param output_file: 輸出的 CSV 檔案名稱
    """
    try:
        # 使用 Playwright 爬取資料
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # 建立 API URL
            url = f"https://ebus.gov.taipei/Route/StopsOfRoute?routeid={route_id}"
            page.goto(url)
            
            # 等待網頁載入完成
            content = page.content()
            browser.close()
        
        # 解析 JSON 資料
        import json
        data = json.loads(content)
        stops = data.get("stops", [])
        
        # 檢查是否有資料
        if not stops:
            print("無法取得公車站點資料，請檢查公車代碼是否正確。")
            return
        
        # 將資料寫入 CSV 檔案
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["arrival_info", "stop_number", "stop_name", "stop_id", "latitude", "longitude"])
            
            for stop in stops:
                writer.writerow([
                    stop.get("arrival_info", "N/A"),
                    stop.get("stop_number", "N/A"),
                    stop.get("stop_name", "N/A"),
                    stop.get("stop_id", "N/A"),
                    stop.get("latitude", "N/A"),
                    stop.get("longitude", "N/A")
                ])
        
        print(f"公車路線資料已成功儲存為 {output_file}")
    
    except Exception as e:
        print(f"資料處理失敗: {e}")

# 主程式
if __name__ == "__main__":
    # 手動輸入公車代碼
    route_id = input("請輸入公車代碼: ")
    output_file = input("請輸入輸出的 CSV 檔案名稱 (預設為 bus_route.csv): ") or "bus_route.csv"
    
    # 執行函數
    fetch_bus_route_data_with_playwright(route_id, output_file)
    