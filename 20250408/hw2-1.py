from datetime import datetime

def calculate_time_info(input_time):
    """
    計算輸入時間的星期幾與經過的太陽日。

    :param input_time: 時間字串，格式為 "YYYY-MM-DD HH:MM"
    :return: 該天的星期幾與經過的太陽日
    """
    try:
        # 解析輸入時間
        input_datetime = datetime.strptime(input_time, "%Y-%m-%d %H:%M")
        
        # 計算星期幾
        weekday = input_datetime.strftime("%A")
        
        # 計算 Julian Date
        def to_julian_date(dt):
            # Julian Day 的計算公式
            a = (14 - dt.month) // 12
            y = dt.year + 4800 - a
            m = dt.month + 12 * a - 3
            julian_day = dt.day + ((153 * m + 2) // 5) + 365 * y + (y // 4) - (y // 100) + (y // 400) - 32045
            julian_day += (dt.hour - 12) / 24 + dt.minute / 1440 + dt.second / 86400
            return julian_day

        julian_days_input = to_julian_date(input_datetime)
        julian_days_now = to_julian_date(datetime.now())
        elapsed_days = julian_days_now - julian_days_input
        
        return weekday, elapsed_days
    except ValueError:
        # 當輸入格式錯誤時，回傳預設值
        return "Invalid date format", None

# 手動輸入時間
input_time = input("請輸入時間 (格式為 YYYY-MM-DD HH:MM): ")
weekday, elapsed_days = calculate_time_info(input_time)

if elapsed_days is not None:
    print(f"輸入時間的星期: {weekday}")
    print(f"從輸入時間到現在經過的太陽日: {elapsed_days:.6f}")
else:
    print(f"錯誤: {weekday}")