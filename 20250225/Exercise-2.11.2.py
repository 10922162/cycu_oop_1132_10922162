# 測試 x = y = 1 (合法)
x = y = 1  
print("x:", x, "y:", y)  # 輸出: x: 1 y: 1

# 測試分號 (;)，雖然可以使用，但 Python 中不建議
a = 5;
print("a:", a)  # 輸出: a: 5

# 測試數字結尾的句點 (.)
b = 10.
print("b:", b)  # 10. 會被視為 10.0，輸出: b: 10.0

# 測試錯誤的模組名稱 (這行會報錯，所以不執行)
# import maath  # 這會導致 ModuleNotFoundError: No module named 'maath'

# **無法執行的語法 (SyntaxError)，不應寫入程式**
# 17 = n  # ❌ 無法賦值給數字，SyntaxError
# print(c.)  # ❌ 變數後面不能加 .，SyntaxError

