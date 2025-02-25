def print_right(text):
    total_width = 40  # 設定目標對齊的位置 (第 40 列)
    spaces_needed = total_width - len(text)  # 計算需要補的空格數量
    print(" " * spaces_needed + text)  # 用空格填充後輸出

# 測試函數
print_right("Monty")
print_right("Python's")
print_right("Flying Circus")
