# 📝 Changelog

تمام تغییرات مهم پروژه اینجا ثبت میشه.

## [1.0.0] - 2025-01-24

### 🎉 اولین نسخه رسمی!

#### ✨ اضافه شده:
- **Core Library**: کلاس `SpotifyExtractor` برای استخراج پلی‌لیست‌ها
- **CLI Tool**: ابزار خط فرمان `spotify-extract`
- **Multiple Formats**: خروجی TXT, CSV, JSON
- **Batch Processing**: پردازش چندین پلی‌لیست
- **Statistics**: آمارگیری کامل از پلی‌لیست‌ها
- **Error Handling**: مدیریت خطای قوی
- **Documentation**: راهنمای کامل و examples
- **PyPI Package**: قابل نصب با `pip install`

#### 🛠️ فنی:
- پشتیبانی Python 3.7+
- Spotify Web API integration
- Concurrent processing برای سرعت بالا
- Type hints و docstrings
- MIT License

#### 📦 ساختار:
- `spotify_extractor/` - کتابخانه اصلی
- `examples/` - نمونه‌های کاربرد
- `web_app/` - رابط وب (Streamlit)
- `tests/` - تست‌های خودکار

#### 🎯 قابلیت‌ها:
- استخراج playlist metadata
- گرفتن اطلاعات کامل آهنگ‌ها
- حذف duplicates
- آمار خواننده‌ها و آلبوم‌ها
- Export به فرمت‌های مختلف
- Pagination handling
- Rate limiting

---

## [Unreleased]

### 🔮 در حال توسعه:
- Cache system برای عملکرد بهتر
- GUI application
- Playlist comparison tools
- Integration با سرویس‌های دیگه

---

**نسخه‌بندی بر اساس [Semantic Versioning](https://semver.org/) انجام میشه.**

**فرمت بر اساس [Keep a Changelog](https://keepachangelog.com/) نوشته شده.**