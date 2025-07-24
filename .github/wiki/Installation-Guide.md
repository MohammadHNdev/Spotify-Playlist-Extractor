# 🚀 راهنمای نصب و راه‌اندازی

## ⚡ نصب سریع

### نصب از PyPI
```bash
pip install spotify-playlist-extractor
```

### تست نصب
```bash
# تست کتابخانه
python -c "from spotify_extractor import SpotifyExtractor; print('✅ Library OK')"

# تست CLI
spotify-extract --help
```

---

## 📋 پیش‌نیازها

- **Python 3.7+** (پیشنهاد: 3.9+)
- **Spotify Developer Account** (رایگان)
- **اتصال اینترنت** برای دسترسی به Spotify API

---

## 🔧 نصب از سورس

### از GitHub
```bash
git clone https://github.com/MohammadHNdev/Spotify-Playlist-Extractor.git
cd Spotify-Playlist-Extractor
pip install -e .
```

### نسخه Development
```bash
pip install --pre spotify-playlist-extractor
```

---

## 🔑 تنظیم Spotify API

### مرحله ۱: ساخت اپلیکیشن Spotify

1. به [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) بروید
2. روی **"Create App"** کلیک کنید
3. اطلاعات زیر را وارد کنید:
   - **App name**: `My Playlist Extractor`
   - **App description**: `Personal playlist extraction tool`
   - **Redirect URI**: `http://localhost:8080` (اختیاری)
   - **APIs used**: Web API ✅

### مرحله ۲: دریافت Credentials

1. **Client ID**: کپی کنید
2. **Client Secret**: روی "Show client secret" کلیک کنید و کپی کنید

### مرحله ۳: تنظیم Environment Variables

#### Windows (Command Prompt)
```cmd
set SPOTIFY_CLIENT_ID=your_client_id_here
set SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

#### Windows (PowerShell)
```powershell
$env:SPOTIFY_CLIENT_ID="your_client_id_here"
$env:SPOTIFY_CLIENT_SECRET="your_client_secret_here"
```

#### macOS/Linux (Bash/Zsh)
```bash
export SPOTIFY_CLIENT_ID="your_client_id_here"
export SPOTIFY_CLIENT_SECRET="your_client_secret_here"

# برای ماندگار شدن، به .bashrc یا .zshrc اضافه کنید:
echo 'export SPOTIFY_CLIENT_ID="your_client_id_here"' >> ~/.bashrc
echo 'export SPOTIFY_CLIENT_SECRET="your_client_secret_here"' >> ~/.bashrc
source ~/.bashrc
```

#### استفاده از فایل .env
```bash
# ایجاد فایل .env در پروژه
echo "SPOTIFY_CLIENT_ID=your_client_id_here" > .env
echo "SPOTIFY_CLIENT_SECRET=your_client_secret_here" >> .env
```

---

## ✅ تست نصب و تنظیمات

### تست کامل سیستم
```bash
# تست import کتابخانه
python -c "from spotify_extractor import SpotifyExtractor; print('✅ Library imported successfully')"

# تست CLI
spotify-extract --help

# تست اتصال به API
python -c "
from spotify_extractor import SpotifyExtractor
try:
    extractor = SpotifyExtractor()
    print('✅ Spotify API connection ready!')
except Exception as e:
    print(f'❌ Error: {e}')
"
```

---

## 💻 نصب Web Interface

### نصب Dependencies اضافی
```bash
pip install spotify-playlist-extractor[web]
```

### اجرای رابط وب
```bash
cd web_app
streamlit run app.py
```

اپلیکیشن در آدرس [http://localhost:8501](http://localhost:8501) باز می‌شود.

---

## 🏗️ نصب برای Development

### راه‌اندازی محیط توسعه
```bash
# کلون repository
git clone https://github.com/MohammadHNdev/Spotify-Playlist-Extractor.git
cd Spotify-Playlist-Extractor

# ایجاد virtual environment
python -m venv venv

# فعال‌سازی virtual environment
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\\Scripts\\activate

# نصب در حالت editable با dev dependencies
pip install -e .[dev]
```

### اجرای تست‌ها
```bash
pytest
```

---

## 🐛 حل مشکلات رایج

### خطای Import
```
ModuleNotFoundError: No module named 'spotify_extractor'
```
**حل**: 
```bash
pip install spotify-playlist-extractor
```

### خطای Credentials
```
ValueError: Client ID و Secret تنظیم نشده!
```
**حل**: Environment variables را درست تنظیم کنید:
```bash
# چک کردن تنظیمات فعلی
echo $SPOTIFY_CLIENT_ID
echo $SPOTIFY_CLIENT_SECRET

# تنظیم مجدد
export SPOTIFY_CLIENT_ID="your_actual_client_id"
export SPOTIFY_CLIENT_SECRET="your_actual_client_secret"
```

### خطای Network/Connection
```
ConnectionError: Failed to connect to Spotify API
```
**حل‌های ممکن**:
- اتصال اینترنت را چک کنید
- Firewall اسپاتیفای را مسدود نکرده باشد
- Client ID/Secret صحیح باشد
- کمی صبر کنید و دوباره امتحان کنید

### خطای Permission
```
PermissionError: [Errno 13] Permission denied
```
**حل**:
- از `sudo` استفاده نکنید
- Virtual environment استفاده کنید
- مجوزهای پوشه را چک کنید

### خطای CLI Command Not Found
```
command not found: spotify-extract
```
**حل**:
```bash
# مطمئن شوید که نصب شده
pip show spotify-playlist-extractor

# PATH چک کنید
which spotify-extract

# یا مستقیماً اجرا کنید
python -m spotify_extractor.cli --help
```

---

## 🔄 آپدیت

### آپدیت به آخرین نسخه
```bash
pip install --upgrade spotify-playlist-extractor
```

### چک کردن نسخه فعلی
```bash
pip show spotify-playlist-extractor
```

### مشاهده تغییرات
```bash
# مشاهده changelog
cat CHANGELOG.md
```

---

## 📞 دریافت کمک

اگر با مشکلی مواجه شدید:

1. 📖 [FAQ](FAQ.md) را مطالعه کنید
2. 🔍 [Issues موجود](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/issues) را جستجو کنید
3. 🆕 [Issue جدید](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/issues/new) ایجاد کنید
4. 💬 در [Discussions](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/discussions) سوال بپرسید

---

**موفق باشید! 🎵✨**