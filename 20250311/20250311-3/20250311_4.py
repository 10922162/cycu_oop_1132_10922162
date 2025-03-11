# 反轉字串的函式
def reverse_word(word):
    return ''.join(reversed(word))

# 判斷是否為回文的函式
def is_palindrome(word):
    return word == reverse_word(word)

# 測試用的單字清單
word_list = ['noon', 'rotator', 'civic', 'racecar', 'level', 'madam', 'redivider', 'detartrated', 'banana']

# 找出所有長度至少 7 個字母的回文字串
for word in word_list:
    if len(word) >= 7 and is_palindrome(word):
        print(word)