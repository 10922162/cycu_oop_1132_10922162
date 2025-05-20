import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# 設定檔案路徑
base_dir = os.path.dirname(__file__)
input_file = os.path.join(base_dir, 'midterm_scores.csv')
output_image = os.path.join(base_dir, 'grouped_score_distribution.png')

# 讀取資料
df = pd.read_csv(input_file, encoding='utf-8')
subjects = ['Chinese', 'English', 'Math', 'History', 'Geography', 'Physics', 'Chemistry']

# 定義分數區間
bins = np.arange(50, 101, 10)  # 50-59, 60-69, ..., 90-100
labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins)-1)]

# 計算每個科目在每個區間的數量
counts = []
for subject in subjects:
    hist, _ = np.histogram(df[subject], bins=bins)
    counts.append(hist)
counts = np.array(counts)  # shape: (科目數, 區間數)

# 畫群組長條圖
x = np.arange(len(labels))  # 區間的位置
bar_width = 0.12
plt.figure(figsize=(12, 7))

for i, subject in enumerate(subjects):
    plt.bar(x + i * bar_width, counts[i], width=bar_width, label=subject)

plt.xlabel('Score Range', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.title('Score Distribution by Subject and Range', fontsize=16)
plt.xticks(x + bar_width * (len(subjects)-1) / 2, labels, rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig(output_image, dpi=300)
plt.show()

print(f"Grouped bar chart saved to '{output_image}'")