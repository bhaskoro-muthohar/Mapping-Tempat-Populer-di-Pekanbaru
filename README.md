# Mapping-Tempat-Populer-di-Pekanbaru
[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kT34FJMQgJ3fC6rA7ve9oemYvAvYuKKi)

![](https://i.imgur.com/mizNR51.png)

Saya membuat peta interaktif (menggunakan pandas, python dan library folium) untuk mengoleksi data dari [Google Places API](https://developers.google.com/places/web-service/intro). Kemudian, lebih dari 400 tempat berhasil dikumpulkan dalam radius 30km dan dikelompokan kedalam 20 kategori. Raw data dari tempat tersebut terdapat dalam `places1.csv` dataset (`place_name`, `place_name`, `place_id`, `lat`, `lng` dan `type`).

Untuk mendapatkan dataset `places1.csv` menggunakan skript `read_places.py`. Sebelum menggunakan skript tersebut dibutuhkan [API key] (https://cloud.google.com/docs/authentication/api-keys). Setelah itu kita akan menempatkan tempat yang di `places1.csv` dengan "moments" menggunakan `get_places_popular_moments.py` dan akan mmenghasilkan dataset baru `places_with_moments.csv`.

Setelah mendapatkan tempat dengan "moments" dibutuhkan tahap cleaning data karena tidak semua tempat punya nilai "moments". Untuk membersihkan data digunakan skript `clear_places.py`. Skript akan menghasilkan dataset terakhir yang kita butuhkan `places_cleaned.csv`. Ok! Setelah itu dataset akan diproses langsung menggunakan Notebook `creating_map_time.ipynb`.
