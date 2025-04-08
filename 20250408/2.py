import os
import subprocess
import sys

# 確保安裝 requests 模組
try:
    import requests
except ModuleNotFoundError:
    print("未找到 requests 模組，正在安裝...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests