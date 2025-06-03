import geopandas as gpd # type: ignore

# 讀取 GeoPackage 檔案
filepath = "taipei_city_bus_stop.gpkg"
gdf = gpd.read_file(filepath)

# 顯示資料
print(gdf.head())

# 儲存為其他格式（例如 Shapefile 或 CSV）
gdf.to_file("output.shp")  # 儲存為 Shapefile
gdf.to_csv("output.csv", index=False)  # 儲存為 CSV