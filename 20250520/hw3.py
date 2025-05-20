import geopandas as gpd
import matplotlib.pyplot as plt

# 讀取地理數據檔案
shapefile_path = '0525HW3/COUNTY_MOI_1140318.shp'
gdf = gpd.read_file(shapefile_path)

# 篩選北北基桃 (台北市、新北市、基隆市、桃園市)
target_counties = ['台北市', '新北市', '基隆市', '桃園市']
filtered_gdf = gdf[gdf['COUNTYNAME'].isin(target_counties)]

# 指定每個縣市的顏色（台北市改為黃色）
county_colors = {
    '台北市': 'yellow',
    '新北市': 'lightgreen',
    '基隆市': 'gold',
    '桃園市': 'salmon'
}
filtered_gdf['color'] = filtered_gdf['COUNTYNAME'].map(county_colors)

# 繪製地圖
fig, ax = plt.subplots(figsize=(10, 8))  # 設定地圖大小
filtered_gdf.plot(ax=ax, edgecolor='black', color=filtered_gdf['color'])

# 加入縣市名稱標籤
for x, y, label in zip(filtered_gdf.geometry.centroid.x, 
                       filtered_gdf.geometry.centroid.y, 
                       filtered_gdf['COUNTYENG']):
    ax.text(x, y, label, fontsize=10, ha='center', color='darkblue')

# 設定標題與軸標籤
plt.title('北北基桃地圖', fontsize=16)
plt.xlabel('經度', fontsize=12)
plt.ylabel('緯度', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)  # 加入網格線
plt.show()