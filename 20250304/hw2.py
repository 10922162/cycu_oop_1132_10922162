def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# 測試
print("gcd(11, 121) =", gcd(11, 121))  # 輸出 11
print("gcd(7, 49) =", gcd(7, 49))      # 輸出 7
