# 🚀 راهنمای نصب

## ⚡ نصب سریع

```bash
pip install spotify-playlist-extractor
```

## 📋 پیش‌نیازها

- **Python 3.8+** (پیشنهاد: 3.10+)
- **Spotify Developer Account** (رایگان)

## 🔧 نصب از سورس

### GitHub:
```bash
git clone https://github.com/MohammadHNdev/Spotify-Playlist-Extractor.git
cd Spotify-Playlist-Extractor
pip install -e .
```

### PyPI Development:
```bash
pip install --pre spotify-playlist-extractor
```

## 🔑 تنظیم Spotify API

### 1. ساخت اپلیکیشن:
1. برو به [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. **"Create App"** کلیک کن
3. مشخصات:
   - **App name**: `My Playlist Extractor`
   - **App description**: `Personal playlist extraction tool`
   - **Redirect URI**: `http://localhost:8080` (اختیاری)
   - **APIs used**: Web API ✅

### 2. گرفتن Credentials:
- **Client ID**: کپی کن
- **Client Secret**: "Show client secret" کلیک کن و کپی کن

### 3. تنظیم Environment Variables:

#### Windows:
```cmd
set SPOTIFY_CLIENT_ID=your_client_id_here
set SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

#### macOS/Linux:
```bash
export SPOTIFY_CLIENT_ID="your_client_id_here"
export SPOTIFY_CLIENT_SECRET="your_client_secret_here"

# برای ماندگار شدن، به .bashrc یا .zshrc اضافه کن:
echo 'export SPOTIFY_CLIENT_ID="your_client_id_here"' >> ~/.bashrc
echo 'export SPOTIFY_CLIENT_SECRET="your_client_secret_here"' >> ~/.bashrc
```

#### .env فایل:
```bash
# ایجاد .env فایل در پروژه‌ت:
echo "SPOTIFY_CLIENT_ID=your_client_id_here" > .env
echo "SPOTIFY_CLIENT_SECRET=your_client_secret_here" >> .env
```

## ✅ تست نصب

```bash
# Test کتابخانه:
python -c "from spotify_extractor import SpotifyExtractor; print('✅ Library OK')"

# Test CLI:
spotify-extract --help

# Test کامل:
python -c "
from spotify_extractor import SpotifyExtractor
extractor = SpotifyExtractor()
print('✅ Ready to extract!')
"
```

## 🐛 مشکلات رایج

### خطای Import:
```
ModuleNotFoundError: No module named 'spotify_extractor'
```
**حل**: `pip install spotify-playlist-extractor`

### خطای Credentials:
```
ValueError: Client ID و Secret نداری!
```
**حل**: Environment variables رو تنظیم کن

### خطای Network:
```
ConnectionError: نشد وصل بشم به اسپاتیفای
```
**حل**: اینترنت و firewall چک کن

## 🔄 آپدیت

```bash
# آپدیت به آخرین نسخه:
pip install --upgrade spotify-playlist-extractor

# چک کردن نسخه:
pip show spotify-playlist-extractor
```

## 💻 نصب Web Interface

```bash
# نصب dependencies اضافی:
pip install spotify-playlist-extractor[web]

# اجرا:
cd web_app
streamlit run app.py
```

## 🏗️ نصب برای توسعه

```bash
git clone https://github.com/MohammadHNdev/Spotify-Playlist-Extractor.git
cd Spotify-Playlist-Extractor

# Virtual environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# نصب editable:
pip install -e .[dev]

# اجرای تست‌ها:
pytest
```

## 📞 کمک بیشتر

مشکل داری؟
- 📖 [FAQ](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/wiki/FAQ)
- 🐛 [Issues](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/issues)
- 💬 [Discussions](https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/discussions)