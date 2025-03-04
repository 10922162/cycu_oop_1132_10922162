import math

# 修正的絕對值函數
def absolute_value_fixed(x):
    if x < 0:
        return -x
    return x  # 確保所有情況都有回傳值

# 簡化的絕對值函數
def absolute_value_improved(x):
    return -x if x < 0 else x  # 單行表達式

# 修正的判斷函數
def is_divisible(x, y):
    return x % y == 0  # 直接回傳布林值

# 計算兩點之間的距離
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 測試函數
print("absolute_value_fixed(-5):", absolute_value_fixed(-5))  # 5
print("absolute_value_improved(3):", absolute_value_improved(3))  # 3
print("is_divisible(10, 5):", is_divisible(10, 5))  # True
print("is_divisible(7, 3):", is_divisible(7, 3))  # False
print("distance(1, 2, 4, 6):", distance(1, 2, 4, 6))  # 5.0
