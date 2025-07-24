# 🎵 Spotify Playlist Extractor

[![PyPI version](https://badge.fury.io/py/spotify-playlist-extractor.svg)](https://badge.fury.io/py/spotify-playlist-extractor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

**یه کتابخانه Python خیلی ساده برای استخراج پلی‌لیست‌های اسپاتیفای** 🚀

## 💡 چیکار می‌کنه؟

- پلی‌لیست اسپاتیفای رو میگیره
- اطلاعات همه آهنگ‌هاشو استخراج می‌کنه  
- به فرمت‌های مختلف ذخیره می‌کنه (TXT, CSV, JSON)
- CLI داره برای استفاده آسون
- آمارگیری از پلی‌لیست‌ها

## ⚡ نصب فوری

```bash
pip install spotify-playlist-extractor
```

## 🚀 استفاده خیلی آسون

### کتابخانه Python

```python
from spotify_extractor import SpotifyExtractor

# ساخت extractor
extractor = SpotifyExtractor()

# استخراج آهنگ‌ها
tracks = extractor.extract_tracks("https://open.spotify.com/playlist/...")

# ذخیره به فایل
extractor.save_to_txt(tracks, "my_playlist.txt")

print(f"✅ {len(tracks)} آهنگ استخراج شد!")
```

### خط فرمان (CLI)

```bash
# استخراج ساده
spotify-extract https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd

# با تنظیمات بیشتر
spotify-extract -f json -o my_music.json --stats [URL]

# فقط اطلاعات پلی‌لیست
spotify-extract --info-only [URL]
```

## 🛠️ تنظیمات

### API Credentials

از [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) یه App بساز و credentials بگیر:

```bash
# متغیرهای محیطی
export SPOTIFY_CLIENT_ID="your_client_id"
export SPOTIFY_CLIENT_SECRET="your_client_secret"
```

یا مستقیم تو کد:

```python
extractor = SpotifyExtractor("your_client_id", "your_client_secret")
```

## 📖 نمونه‌های کاربرد

### استخراج با جزئیات

```python
from spotify_extractor import SpotifyExtractor

extractor = SpotifyExtractor()

# اطلاعات پلی‌لیست
info = extractor.get_playlist_info(playlist_url)
print(f"نام: {info['name']}")
print(f"سازنده: {info['owner']}")
print(f"تعداد آهنگ: {info['total_tracks']}")

# استخراج کامل
tracks = extractor.extract_tracks(playlist_url, include_details=True)

# آمارگیری
stats = extractor.get_stats(tracks)
print(f"خواننده‌های مختلف: {stats['unique_artists']}")
print(f"محبوب‌ترین: {stats['top_artist']}")
```

### ذخیره در فرمت‌های مختلف

```python
# متن ساده
extractor.save_to_txt(tracks, "playlist.txt")

# CSV برای Excel
extractor.save_to_csv(tracks, "playlist.csv") 

# JSON برای برنامه‌نویسی
extractor.save_to_json(tracks, "playlist.json")

# یکجا استخراج و ذخیره
filename = extractor.extract_and_save(playlist_url, "json")
```

### پردازش دسته‌ای

```python
# چندین پلی‌لیست
urls = [
    "https://open.spotify.com/playlist/...",
    "https://open.spotify.com/playlist/...",
]

all_tracks = []
for url in urls:
    tracks = extractor.extract_tracks(url)
    all_tracks.extend(tracks)

# حذف تکراری‌ها
unique_tracks = {track['url']: track for track in all_tracks}.values()
```

## 🌐 Web App

اگه UI گرافیکی می‌خوای:

```bash
pip install spotify-playlist-extractor[web]
cd web_app
streamlit run app.py
```

## 📁 ساختار پروژه

```
spotify-playlist-extractor/
├── 📦 spotify_extractor/     # کتابخانه اصلی
│   ├── core.py              # کلاس اصلی
│   ├── helpers.py           # توابع کمکی
│   └── cli.py               # رابط خط فرمان
├── 🌐 web_app/              # رابط وب
├── 📚 examples/             # نمونه‌های کاربرد
│   ├── basic_usage.py       # استفاده ساده
│   └── batch_processing.py  # پردازش دسته‌ای
└── 📋 README.md
```

## 🎯 قابلیت‌ها

- ✅ استخراج سریع پلی‌لیست‌ها
- ✅ پشتیبانی از فرمت‌های مختلف
- ✅ CLI قدرتمند
- ✅ پردازش دسته‌ای
- ✅ آمارگیری کامل
- ✅ Web UI (اختیاری)
- ✅ حذف تکراری‌ها
- ✅ Python 3.7+ support

## 🔧 CLI Commands

```bash
# نمایش راهنما
spotify-extract --help

# استخراج با فرمت JSON
spotify-extract -f json playlist_url

# نمایش آمار
spotify-extract --stats playlist_url

# verbose mode
spotify-extract -v playlist_url

# فایل خروجی دلخواه
spotify-extract -o my_music.txt playlist_url
```

## 🤝 مشارکت

1. Fork کن
2. Branch جدید بساز: `git checkout -b feature-name`
3. تغییراتت رو commit کن: `git commit -m 'Add feature'`
4. Push کن: `git push origin feature-name`
5. Pull Request بده

## 📝 لایسنس

MIT License - برای جزئیات فایل [LICENSE](LICENSE) رو ببین.

## 🐛 Bug Report

مشکلی داری؟ [Issues](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/issues) بخش تو گزارش بده.

## 👤 سازنده

**محمدحسین نوروزی**
- GitHub: [@MohammadHNdev](https://github.com/MohammadHNdev)
- Email: hosein.norozi434@gmail.com


## ⭐ حمایت

اگه مفید بود، یه ستاره بده! 🌟

---

**ساخته شده با ❤️ برای جامعه فارسی‌زبان**