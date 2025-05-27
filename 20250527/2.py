<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>公車動態地圖</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
</head>
<body>
    <h1>公車動態地圖</h1>
    <div id="map" style="height: 500px;"></div>

    <script>
        // 初始化地圖
        const map = L.map('map').setView([25.0330, 121.5654], 13); // 台北市中心

        // 加入地圖圖層
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 18,
        }).addTo(map);

        // 公車標記
        const busMarkers = {};

        // 更新公車位置
        async function updateBusLocations() {
            try {
                const response = await fetch("https://data.taipei/api/v1/dataset/2749b84d-a09c-4c03-a7ff-710e7ebf209c?scope=resourceAquire");
                const data = await response.json();

                // 確保資料存在
                if (data && data.result && data.result.results) {
                    const buses = data.result.results;

                    buses.forEach(bus => {
                        const busId = bus.BusID; // 公車 ID
                        const lat = parseFloat(bus.BusPosition.PositionLat); // 緯度
                        const lng = parseFloat(bus.BusPosition.PositionLon); // 經度

                        // 如果該公車已存在於地圖上，更新位置
                        if (busMarkers[busId]) {
                            busMarkers[busId].setLatLng([lat, lng]);
                        } else {
                            // 如果該公車不存在，新增標記
                            const marker = L.marker([lat, lng]).addTo(map);
                            marker.bindPopup(`公車 ID: ${busId}`);
                            busMarkers[busId] = marker;
                        }
                    });
                }
            } catch (error) {
                console.error("無法獲取公車位置資料：", error);
            }
        }

        // 每 10 秒更新一次公車位置
        setInterval(updateBusLocations, 10000);

        // 初始化時更新一次
        updateBusLocations();
    </script>
</body>
</html>