# 📚 مرجع API

## SpotifyExtractor Class

کلاس اصلی برای استخراج پلی‌لیست‌های اسپاتیفای.

### Constructor

```python
SpotifyExtractor(client_id=None, client_secret=None)
```

**پارامترها:**
- `client_id` (str, اختیاری): شناسه کلاینت اسپاتیفای
- `client_secret` (str, اختیاری): کلید مخفی کلاینت اسپاتیفای

اگر پارامترها داده نشوند، از متغیرهای محیطی استفاده می‌شود.

**مثال:**
```python
from spotify_extractor import SpotifyExtractor

# استفاده از environment variables
extractor = SpotifyExtractor()

# یا مستقیم دادن credentials
extractor = SpotifyExtractor("your_client_id", "your_client_secret")
```

---

## متدهای اصلی

### extract_tracks()

```python
extract_tracks(playlist_url, include_details=False)
```

استخراج آهنگ‌ها از یک پلی‌لیست اسپاتیفای.

**پارامترها:**
- `playlist_url` (str): لینک پلی‌لیست اسپاتیفای
- `include_details` (bool): شامل جزئیات بیشتر آهنگ‌ها

**برگشت:**
- `list`: فهرست دیکشنری‌های حاوی اطلاعات آهنگ‌ها

**مثال:**
```python
# استخراج ساده
tracks = extractor.extract_tracks("https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd")

# با جزئیات بیشتر
detailed_tracks = extractor.extract_tracks(
    "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd", 
    include_details=True
)

print(f"تعداد آهنگ‌ها: {len(tracks)}")
```

**ساختار خروجی:**
```python
[
    {
        'name': 'نام آهنگ',
        'artist': 'نام هنرمند',
        'album': 'نام آلبوم',
        'release_date': '2024-01-15',
        'url': 'https://open.spotify.com/track/...',
        'duration': '3:45',
        'popularity': 85  # فقط با include_details=True
    },
    # ...
]
```

---

### get_playlist_info()

```python
get_playlist_info(playlist_url)
```

دریافت اطلاعات کلی پلی‌لیست.

**پارامترها:**
- `playlist_url` (str): لینک پلی‌لیست اسپاتیفای

**برگشت:**
- `dict`: اطلاعات پلی‌لیست

**مثال:**
```python
info = extractor.get_playlist_info("https://open.spotify.com/playlist/...")

print(f"نام پلی‌لیست: {info['name']}")
print(f"سازنده: {info['owner']}")
print(f"تعداد آهنگ: {info['total_tracks']}")
print(f"توضیحات: {info['description']}")
```

**ساختار خروجی:**
```python
{
    'name': 'نام پلی‌لیست',
    'owner': 'نام سازنده',
    'description': 'توضیحات پلی‌لیست',
    'total_tracks': 50,
    'url': 'لینک پلی‌لیست',
    'image_url': 'لینک تصویر کاور',
    'public': True,
    'collaborative': False
}
```

---

## متدهای ذخیره‌سازی

### save_to_txt()

```python
save_to_txt(tracks, filename)
```

ذخیره آهنگ‌ها در فایل متنی.

**پارامترها:**
- `tracks` (list): فهرست آهنگ‌ها
- `filename` (str): نام فایل خروجی

**مثال:**
```python
tracks = extractor.extract_tracks(playlist_url)
extractor.save_to_txt(tracks, "my_playlist.txt")
```

**فرمت خروجی:**
```
1. آهنگ اول - هنرمند اول (آلبوم اول)
2. آهنگ دوم - هنرمند دوم (آلبوم دوم)
...
```

---

### save_to_csv()

```python
save_to_csv(tracks, filename)
```

ذخیره آهنگ‌ها در فایل CSV.

**پارامترها:**
- `tracks` (list): فهرست آهنگ‌ها  
- `filename` (str): نام فایل خروجی

**مثال:**
```python
tracks = extractor.extract_tracks(playlist_url)
extractor.save_to_csv(tracks, "my_playlist.csv")
```

**ستون‌های CSV:**
- نام آهنگ
- هنرمند
- آلبوم
- سال انتشار
- مدت زمان
- URL اسپاتیفای

---

### save_to_json()

```python
save_to_json(tracks, filename)
```

ذخیره آهنگ‌ها در فایل JSON.

**پارامترها:**
- `tracks` (list): فهرست آهنگ‌ها
- `filename` (str): نام فایل خروجی

**مثال:**
```python
tracks = extractor.extract_tracks(playlist_url)
extractor.save_to_json(tracks, "my_playlist.json")
```

---

## متدهای تحلیلی

### get_stats()

```python
get_stats(tracks)
```

محاسبه آمار پلی‌لیست.

**پارامترها:**
- `tracks` (list): فهرست آهنگ‌ها

**برگشت:**
- `dict`: آمارهای پلی‌لیست

**مثال:**
```python
tracks = extractor.extract_tracks(playlist_url)
stats = extractor.get_stats(tracks)

print(f"تعداد کل آهنگ‌ها: {stats['total_tracks']}")
print(f"تعداد هنرمندان مختلف: {stats['unique_artists']}")
print(f"محبوب‌ترین هنرمند: {stats['top_artist']}")
```

**ساختار خروجی:**
```python
{
    'total_tracks': 50,
    'unique_artists': 25,
    'unique_albums': 30,
    'top_artist': 'محبوب‌ترین هنرمند',
    'top_album': 'محبوب‌ترین آلبوم',
    'oldest_track': 1980,
    'newest_track': 2024,
    'total_duration': '2:30:45',
    'average_popularity': 75.5
}
```

---

### extract_and_save()

```python
extract_and_save(playlist_url, format='txt', filename=None)
```

استخراج و ذخیره یک‌جا.

**پارامترها:**
- `playlist_url` (str): لینک پلی‌لیست
- `format` (str): فرمت خروجی ('txt', 'csv', 'json')
- `filename` (str, اختیاری): نام فایل (اگر نداده شود، خودکار تولید می‌شود)

**برگشت:**
- `str`: نام فایل ایجاد شده

**مثال:**
```python
# با نام خودکار
filename = extractor.extract_and_save(playlist_url, 'json')
print(f"فایل ذخیره شد: {filename}")

# با نام دلخواه
extractor.extract_and_save(playlist_url, 'csv', 'my_music.csv')
```

---

## CLI Reference

### دستور پایه

```bash
spotify-extract [OPTIONS] PLAYLIST_URL
```

### گزینه‌ها

| گزینه | نوع | پیش‌فرض | توضیح |
|--------|-----|---------|-------|
| `-f, --format` | str | txt | فرمت خروجی (txt, csv, json) |
| `-o, --output` | str | auto | نام فایل خروجی |
| `--stats` | flag | False | نمایش آمار پلی‌لیست |
| `--info-only` | flag | False | فقط اطلاعات پلی‌لیست |
| `-v, --verbose` | flag | False | خروجی کامل |
| `--help` | flag | False | نمایش راهنما |

### مثال‌های CLI

```bash
# استخراج ساده
spotify-extract https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd

# با فرمت JSON
spotify-extract -f json https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd

# با نام فایل دلخواه
spotify-extract -f csv -o my_music.csv https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd

# نمایش آمار
spotify-extract --stats https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd

# فقط اطلاعات پلی‌لیست
spotify-extract --info-only https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd

# حالت verbose
spotify-extract -v -f json https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd
```

---

## Error Handling

### استثناهای رایج

```python
from spotify_extractor.exceptions import *

try:
    extractor = SpotifyExtractor()
    tracks = extractor.extract_tracks(url)
except SpotifyAuthError:
    print("خطا در احراز هویت - Client ID/Secret را چک کنید")
except PlaylistNotFoundError:
    print("پلی‌لیست پیدا نشد - لینک را چک کنید")
except RateLimitError:
    print("محدودیت نرخ - کمی صبر کنید")
except ConnectionError:
    print("مشکل اتصال اینترنت")
except Exception as e:
    print(f"خطای غیرمنتظره: {e}")
```

### مدیریت خطا در CLI

```bash
# خطاهای CLI به stderr ارسال می‌شوند
spotify-extract invalid-url 2> errors.log

# کدهای خروج:
# 0: موفق
# 1: خطای عمومی  
# 2: خطای پارامترها
# 3: خطای API
```

---

## Rate Limiting

API اسپاتیفای محدودیت دارد:
- **100 درخواست در دقیقه**
- کتابخانه خودکار مدیریت می‌کند
- برای پلی‌لیست‌های بزرگ صبر کنید

```python
# مثال مدیریت rate limiting
import time
from spotify_extractor import SpotifyExtractor

extractor = SpotifyExtractor()

playlists = [url1, url2, url3, ...]
all_tracks = []

for i, url in enumerate(playlists):
    try:
        tracks = extractor.extract_tracks(url)
        all_tracks.extend(tracks)
        print(f"✅ پلی‌لیست {i+1}/{len(playlists)} پردازش شد")
        
        # استراحت بین درخواست‌ها
        if i < len(playlists) - 1:
            time.sleep(1)
            
    except RateLimitError:
        print("⏳ منتظر بمانید...")
        time.sleep(60)  # صبر 1 دقیقه
        # تلاش مجدد
        tracks = extractor.extract_tracks(url)
        all_tracks.extend(tracks)
```

---

## استفاده پیشرفته

### پردازش دسته‌ای

```python
from concurrent.futures import ThreadPoolExecutor
import time

def process_playlist(url):
    extractor = SpotifyExtractor()
    return extractor.extract_tracks(url)

urls = ["url1", "url2", "url3"]

# پردازش موازی (محدود)
with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(process_playlist, urls))

all_tracks = []
for tracks in results:
    all_tracks.extend(tracks)

# حذف تکراری‌ها
unique_tracks = {track['url']: track for track in all_tracks}.values()
```

### فیلتر کردن آهنگ‌ها

```python
tracks = extractor.extract_tracks(url, include_details=True)

# فیلتر بر اساس سال
recent_tracks = [t for t in tracks if t.get('release_date', '').startswith('2024')]

# فیلتر بر اساس محبوبیت
popular_tracks = [t for t in tracks if t.get('popularity', 0) > 70]

# فیلتر بر اساس هنرمند
artist_tracks = [t for t in tracks if 'نام هنرمند' in t.get('artist', '')]
```

### ایجاد گزارش کامل

```python
def generate_report(playlist_url):
    extractor = SpotifyExtractor()
    
    # اطلاعات پلی‌لیست
    info = extractor.get_playlist_info(playlist_url)
    tracks = extractor.extract_tracks(playlist_url, include_details=True)
    stats = extractor.get_stats(tracks)
    
    report = f"""
# گزارش پلی‌لیست: {info['name']}

## اطلاعات کلی
- سازنده: {info['owner']}
- تعداد آهنگ: {info['total_tracks']}
- وضعیت: {'عمومی' if info['public'] else 'خصوصی'}

## آمار
- هنرمندان مختلف: {stats['unique_artists']}
- آلبوم‌های مختلف: {stats['unique_albums']}
- قدیمی‌ترین آهنگ: {stats['oldest_track']}
- جدیدترین آهنگ: {stats['newest_track']}
- محبوب‌ترین هنرمند: {stats['top_artist']}

## فهرست آهنگ‌ها
"""
    
    for i, track in enumerate(tracks, 1):
        report += f"{i}. {track['name']} - {track['artist']}\n"
    
    return report

# تولید گزارش
report = generate_report("https://open.spotify.com/playlist/...")
with open("playlist_report.md", "w", encoding="utf-8") as f:
    f.write(report)
```

---

**برای سوالات بیشتر، [Issues](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/issues) یا [Discussions](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/discussions) مراجعه کنید.**