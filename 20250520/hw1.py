import pandas as pd
import os

# 設定檔案路徑
base_dir = os.path.dirname(__file__)  # 取得當前程式所在目錄
input_file = os.path.join(base_dir, 'midterm_scores.csv')
output_file = os.path.join(base_dir, 'failing_students.csv')

# 檢查檔案路徑
print(f"Reading file from: {input_file}")
if not os.path.exists(input_file):
    print(f"Error: File '{input_file}' not found.")
    exit()

# 檢查工作目錄
print(f"Current working directory: {os.getcwd()}")

# 檢查檔案是否為空
if os.path.getsize(input_file) == 0:
    print(f"Error: File '{input_file}' is empty.")
    exit()

# 直接載入 CSV 檔案
try:
    df = pd.read_csv(input_file, encoding='utf-8')
    print("File loaded successfully!")
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# 定義科目欄位
subjects = ['Chinese', 'English', 'Math', 'History', 'Geography', 'Physics', 'Chemistry']

# 計算每位學生不及格科目的數量
df['FailingSubjects'] = (df[subjects] < 60).sum(axis=1)

# 篩選出超過一半科目不及格的學生
failing_students = df[df['FailingSubjects'] > len(subjects) / 2]

# 將結果保存為 CSV 檔案
failing_students[['Name', 'StudentID', 'FailingSubjects']].to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"Failing students list saved to '{output_file}'")