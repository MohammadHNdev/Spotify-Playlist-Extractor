# ❓ Frequently Asked Questions

## 🚀 نصب و راه‌اندازی

### Q: چطور Spotify API credentials بگیرم؟
**A:** 
1. برو به [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. "Create App" کلیک کن
3. Client ID و Secret رو کپی کن
4. Environment variable تنظیم کن:
```bash
export SPOTIFY_CLIENT_ID="your_id"
export SPOTIFY_CLIENT_SECRET="your_secret"
```

### Q: Error میگه "No module named spotify_extractor"
**A:** نصب نکردی:
```bash
pip install spotify-playlist-extractor
```

### Q: چطور از سورس نصب کنم؟
**A:**
```bash
git clone https://github.com/MohammadHNdev/Spotify-Playlist-Extractor.git
cd Spotify-Playlist-Extractor
pip install -e .
```

## 🎵 استفاده

### Q: چه نوع پلی‌لیست‌هایی پشتیبانی میشه؟
**A:**
- ✅ Public playlists
- ✅ Private playlists (با authentication)
- ✅ Spotify's official playlists
- ❌ پلی‌لیست‌های محلی

### Q: چه اطلاعاتی استخراج میشه؟
**A:**
```python
{
    'name': 'نام آهنگ',
    'artist': 'خواننده',
    'album': 'آلبوم',  
    'release_date': '2024',
    'url': 'لینک اسپاتیفای',
    'duration': '3:45',
    'popularity': 85  # اختیاری
}
```

### Q: محدودیت چیه؟
**A:**
- هر دقیقه 100 request
- پلی‌لیست‌های 10000+ آهنگ کندتر
- کتابخانه خودش pace می‌کنه

## 🛠️ مشکلات رایج

### Q: "Client credentials not found"
**A:** Environment variables تنظیم نکردی:
```bash
# Check کن:
echo $SPOTIFY_CLIENT_ID
echo $SPOTIFY_CLIENT_SECRET

# تنظیم کن:
export SPOTIFY_CLIENT_ID="your_id"
export SPOTIFY_CLIENT_SECRET="your_secret"
```

### Q: "Connection timeout"
**A:**
- اینترنتت چک کن
- Firewall اسپاتیفای رو block نکرده باشه
- کمی صبر کن و دوباره امتحان کن

### Q: "Playlist not found" 
**A:**
- لینک رو درست چک کن
- پلی‌لیست private نباشه
- مطمئن شو که پلی‌لیست حذف نشده

### Q: فایل خروجی خالیه
**A:**
- مجوز نوشتن فایل داری؟
- مسیر فایل درسته؟
- پلی‌لیست آهنگ داره؟

## 💻 CLI

### Q: کامند پیدا نمیشه
**A:**
```bash
# مطمئن شو نصب شده:
pip show spotify-playlist-extractor

# PATH چک کن:
which spotify-extract

# مستقیم اجرا کن:
python -m spotify_extractor.cli --help
```

### Q: چطور فرمت خروجی عوض کنم؟
**A:**
```bash
# TXT (default)
spotify-extract playlist_url

# CSV 
spotify-extract -f csv playlist_url

# JSON
spotify-extract -f json playlist_url
```

## 🔧 پیشرفته

### Q: چطور چندین پلی‌لیست رو یکجا پردازش کنم؟
**A:**
```python
from spotify_extractor import SpotifyExtractor

extractor = SpotifyExtractor()
urls = ["url1", "url2", "url3"]

all_tracks = []
for url in urls:
    tracks = extractor.extract_tracks(url)
    all_tracks.extend(tracks)

# حذف تکراری‌ها
unique = {t['url']: t for t in all_tracks}.values() 
```

### Q: چطور پلی‌لیست خودم رو پردازش کنم؟
**A:** باید OAuth setup کنی که پیچیده‌تره. فعلاً فقط public playlists.

### Q: آیا Web interface داره؟
**A:** آره! 
```bash
pip install spotify-playlist-extractor[web]
cd web_app
streamlit run app.py
```

### Q: چطور performance بهتر کنم؟
**A:**
- از `include_details=False` استفاده کن
- پلی‌لیست‌های کوچکتر پردازش کن
- Cache results خودت پیاده کن

## 🤝 مشارکت

### Q: چطور کمک کنم؟
**A:**
1. Issues بخش برو
2. Bug report یا feature request کن
3. Pull request بده
4. Documentation بهتر کن

### Q: کجا سوال بپرسم؟
**A:**
- 🐛 Bug: GitHub Issues
- 💡 Feature: GitHub Issues  
- ❓ سوال: GitHub Discussions
- 📧 خصوصی: hosein.norozi434@gmail.com

## 📱 سوالات دیگه

### Q: روی موبایل کار می‌کنه؟
**A:** اگه Python داشته باشی، آره!

### Q: آیا رایگانه؟
**A:** کاملاً رایگان و MIT license

### Q: کی آپدیت میشه؟
**A:** [CHANGELOG.md](CHANGELOG.md) چک کن

### Q: برای commercial استفاده مجازه؟
**A:** آره، MIT license

---

**سوال دیگه‌ای داری؟** [Issue باز کن](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/issues) یا [Discussion شروع کن](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/discussions)! 😊