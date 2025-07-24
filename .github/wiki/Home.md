# 🎵 SpotTrack - Spotify Playlist Extractor

**ابزاری قدرتمند و کاربرپسند برای استخراج، مدیریت و تولید لینک دانلود موزیک از پلی‌لیست‌های اسپاتیفای.**

---

## 📋 فهرست مطالب

- [🏠 صفحه اصلی](#home)
- [📖 درباره پروژه](#about-project)
- [⭐ ویژگی‌های کلیدی](#key-features)
- [⚙️ نحوه کارکرد](#how-it-works)
- [🔧 راه‌اندازی برای توسعه‌دهندگان](#developer-setup)
- [📚 راهنمای استفاده](#usage-guide)
- [🤝 مشارکت در پروژه](#contributing)
- [📞 تماس و پشتیبانی](#contact-support)

---

## 🏠 صفحه اصلی

### مقدمه
SpotTrack یک اپلیکیشن وب قدرتمند و کاربرپسند است که با استفاده از **Python** و **Streamlit** ساخته شده است. هدف این اپلیکیشن، ساده‌سازی فرآیند استخراج و مدیریت آهنگ‌ها از پلی‌لیست‌های اسپاتیفای است.

### لینک‌های مهم
- 🔗 [مخزن GitHub](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor)
- 📦 [نصب از PyPI](https://pypi.org/project/spotify-playlist-extractor/)
- 🌐 [رابط وب (Streamlit)](web_app/)
- 📚 [مستندات API](docs/API.md)

---

## 📖 درباره پروژه

SpotTrack یک اپلیکیشن وب قدرتمند و کاربرپسند است که با استفاده از **Streamlit** و **پایتون** ساخته شده است. هدف این اپلیکیشن، ساده‌سازی فرآیند استخراج و مدیریت آهنگ‌ها از پلی‌لیست‌های اسپاتیفای است.

این برنامه به کاربران امکان می‌دهد تا به راحتی لینک یک پلی‌لیست اسپاتیفای را وارد کرده، تمام آهنگ‌های موجود در آن را مشاهده، مرتب‌سازی، آهنگ‌های خاصی را انتخاب و **لینک‌های دانلود مستقیم را برای ربات تلگرام SpotTrack** تولید کنند.

این اپلیکیشن با هدف ارائه تجربه‌ای یکپارچه برای علاقه‌مندان به موسیقی طراحی شده است که مایلند آهنگ‌های اسپاتیفای مورد علاقه خود را به طور کارآمد سازماندهی و دانلود کنند.

---

## ⭐ ویژگی‌های کلیدی

### 🖥️ رابط کاربری بصری
یک رابط وب تمیز و با قابلیت ناوبری آسان که توسط Streamlit ارائه شده است.

### 🎵 استخراج پلی‌لیست
دریافت جزئیات جامع (نام، هنرمند، آلبوم، URL) برای تمام آهنگ‌های پلی‌لیست.

### 🔐 سیستم احراز هویت
سیستم احراز هویت ساده مبتنی بر نام کاربری برای کاربران تایید شده.

### 📋 مدیریت پیشرفته آهنگ‌ها
- مرتب‌سازی بر اساس نام، هنرمند، آلبوم
- صفحه‌بندی برای پلی‌لیست‌های بزرگ
- انتخاب آهنگ‌های تکی یا گروهی

### 📱 ادغام با ربات تلگرام
تولید لینک‌های مستقیم برای دانلود آهنگ‌های انتخاب شده از طریق ربات تلگرام SpotTrack.

### 📥 دانلود انبوه
امکان دانلود یک فایل متنی حاوی تمام URLهای آهنگ‌های انتخاب شده.

### 📊 آمارگیری
- نمایش آمار کلی پلی‌لیست
- اطلاعات هنرمندان
- مدت زمان کل آهنگ‌ها

---

## ⚙️ نحوه کارکرد

### مرحله ۱: ورود لینک پلی‌لیست
کاربر لینک پلی‌لیست اسپاتیفای را در اپلیکیشن وارد می‌کند.

### مرحله ۲: استخراج آهنگ‌ها  
اپلیکیشن با Spotify API ارتباط برقرار کرده و تمام جزئیات آهنگ‌ها را دریافت می‌کند.

### مرحله ۳: انتخاب و تولید لینک
کاربر آهنگ‌های مورد نظر را انتخاب کرده و لینک‌های دانلود برای ربات تلگرام تولید می‌شود.

---

## 🔧 راه‌اندازی برای توسعه‌دهندگان

### ۱. کلون کردن مخزن
```bash
git clone https://github.com/MohammadHNdev/Spotify-Playlist-Extractor.git
cd Spotify-Playlist-Extractor
```

### ۲. نصب کتابخانه
```bash
# نصب از PyPI
pip install spotify-playlist-extractor

# یا نصب از سورس
pip install -e .
```

### ۳. تنظیم متغیرهای محیطی
یک فایل `.env` در دایرکتوری اصلی پروژه ایجاد کرده و اعتبارنامه‌های Spotify API خود را وارد کنید:

```env
SPOTIFY_CLIENT_ID="your_spotify_client_id_here"
SPOTIFY_CLIENT_SECRET="your_spotify_client_secret_here"
```

> **نکته:** برای دریافت Client ID و Client Secret به [داشبورد توسعه‌دهندگان اسپاتیفای](https://developer.spotify.com/dashboard/) مراجعه کنید.

### ۴. اجرای اپلیکیشن وب
```bash
cd web_app
streamlit run app.py
```

اپلیکیشن در مرورگر وب پیش‌فرض شما باز می‌شود، معمولاً در آدرس [http://localhost:8501](http://localhost:8501).

### ۵. استفاده از CLI
```bash
# نمایش راهنما
spotify-extract --help

# استخراج پلی‌لیست
spotify-extract https://open.spotify.com/playlist/your-playlist-id

# با فرمت JSON
spotify-extract -f json https://open.spotify.com/playlist/your-playlist-id
```

---

## 📚 راهنمای استفاده

### استفاده از کتابخانه Python
```python
from spotify_extractor import SpotifyExtractor

# ایجاد extractor
extractor = SpotifyExtractor()

# استخراج آهنگ‌ها
tracks = extractor.extract_tracks("https://open.spotify.com/playlist/...")

# ذخیره در فایل
extractor.save_to_txt(tracks, "my_playlist.txt")
extractor.save_to_csv(tracks, "my_playlist.csv")
extractor.save_to_json(tracks, "my_playlist.json")

print(f"✅ {len(tracks)} آهنگ استخراج شد!")
```

### استفاده از CLI
```bash
# استخراج ساده
spotify-extract https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd

# با تنظیمات بیشتر
spotify-extract -f json -o my_music.json --stats [URL]

# فقط اطلاعات پلی‌لیست
spotify-extract --info-only [URL]
```

---

## 🤝 مشارکت در پروژه

### نحوه مشارکت
1. مخزن را Fork کنید
2. برانچ جدید ایجاد کنید: `git checkout -b feature-name`
3. تغییرات خود را Commit کنید: `git commit -m 'Add feature'`
4. به برانچ خود Push کنید: `git push origin feature-name`
5. Pull Request ایجاد کنید

### قوانین مشارکت
- کد خوانا و منطقی باشد
- کامنت‌های لازم اضافه شود
- مثال کاربرد ارائه شود
- Breaking changes اجتناب شود

### گزارش باگ یا درخواست قابلیت
- [Issues](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/issues) - گزارش مشکل یا درخواست قابلیت
- [Discussions](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/discussions) - بحث و گفتگو

---

## 📞 تماس و پشتیبانی

### توسعه‌دهنده
**محمدحسین نوروزی**
- 🐙 GitHub: [@MohammadHNdev](https://github.com/MohammadHNdev)
- 📧 Email: hosein.norozi434@gmail.com
- 💬 Telegram: [@ArvanCode](https://t.me/ArvanCode)

### روش‌های تماس
- 🐛 گزارش باگ: [GitHub Issues](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/issues)
- 💡 درخواست قابلیت: [GitHub Issues](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/issues)
- ❓ سوالات عمومی: [GitHub Discussions](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/discussions)
- 📧 تماس مستقیم: hosein.norozi434@gmail.com

---

## 📄 لایسنس

این پروژه تحت لایسنس MIT منتشر شده است. برای جزئیات بیشتر، فایل [LICENSE](LICENSE) را مطالعه کنید.

---

**ساخته شده با ❤️ برای جامعه فارسی‌زبان**