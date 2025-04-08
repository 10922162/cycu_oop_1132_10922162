import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

def plot_lognormal_cdf(mu, sigma, output_file="lognormal_cdf.jpg"):
    """
    繪製對數常態累積分布函數圖並儲存為 JPG 檔案。

    :param mu: 對數常態分布的 μ
    :param sigma: 對數常態分布的 σ
    :param output_file: 輸出的 JPG 檔案名稱
    """
    x = np.linspace(0.01, 10, 1000)
    cdf = lognorm.cdf(x, s=sigma, scale=np.exp(mu))
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, cdf, label=f"μ={mu}, σ={sigma}")
    plt.title("Lognormal Cumulative Distribution Function")
    plt.xlabel("x")
    plt.ylabel("CDF")
    plt.legend()
    plt.grid()
    plt.savefig(output_file)
    plt.close()

# Example usage
plot_lognormal_cdf(1.5, 0.4)