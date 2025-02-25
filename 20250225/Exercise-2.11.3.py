import math  # 引入數學模組

# Part 1: 計算半徑為 5 cm 的球體積
radius = 5  # 半徑 (cm)
volume = (4/3) * math.pi * (radius ** 3)  # 球體積公式: (4/3) * π * r³
print("Volume of sphere:", volume, "cubic cm")  # 輸出球體積 (cm³)

# Part 2: 驗證 sin²(x) + cos²(x) 是否接近 1
x = 42  # 測試角度 (以弧度為單位)
x_rad = math.radians(x)  # 轉換為弧度
sin_x = math.sin(x_rad)  # 計算 sin(x)
cos_x = math.cos(x_rad)  # 計算 cos(x)
sum_squares = sin_x**2 + cos_x**2  # 計算 sin²(x) + cos²(x)
print("sin²(42°) + cos²(42°) =", sum_squares)  # 顯示結果 (應接近 1)

# Part 3: 計算 e² 的三種方法
e_squared_1 = math.e ** 2  # 直接用 e**2
e_squared_2 = math.pow(math.e, 2)  # 用 math.pow 計算 e^2
e_squared_3 = math.exp(2)  # 用 math.exp(2) 計算 e^2

# 輸出計算結果
print("e^2 using **:", e_squared_1)
print("e^2 using math.pow:", e_squared_2)
print("e^2 using math.exp:", e_squared_3)

# 比較哪個方法最精確
difference1 = abs(e_squared_1 - e_squared_3)
difference2 = abs(e_squared_2 - e_squared_3)
print("Difference between e**2 and exp(2):", difference1)
print("Difference between pow(e,2) and exp(2):", difference2)
