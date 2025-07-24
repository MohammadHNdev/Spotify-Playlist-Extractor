# 📚 API Reference

## SpotifyExtractor Class

### Constructor

```python
SpotifyExtractor(client_id=None, client_secret=None)
```

**Parameters:**
- `client_id` (str, optional): Spotify Client ID
- `client_secret` (str, optional): Spotify Client Secret

اگه نده، از environment variables میگیره.

### Methods

#### extract_tracks()

```python
extract_tracks(playlist_url, include_details=False)
```

**Parameters:**
- `playlist_url` (str): لینک پلی‌لیست اسپاتیفای
- `include_details` (bool): جزئیات بیشتر آهنگ‌ها

**Returns:**
- `list`: لیست آهنگ‌ها

**Example:**
```python
tracks = extractor.extract_tracks("https://open.spotify.com/playlist/...")
```

#### get_playlist_info()

```python
get_playlist_info(playlist_url)
```

**Returns:**
```python
{
    'name': 'نام پلی‌لیست',
    'owner': 'سازنده',
    'description': 'توضیحات',
    'total_tracks': 50,
    'url': 'لینک'
}
```

#### save_to_txt()

```python
save_to_txt(tracks, filename)
```

**Parameters:**
- `tracks` (list): لیست آهنگ‌ها
- `filename` (str): نام فایل

#### save_to_csv()

```python
save_to_csv(tracks, filename)
```

CSV با ستون‌های: نام، خواننده، آلبوم، سال، URL

#### save_to_json()

```python
save_to_json(tracks, filename)
```

JSON با اطلاعات کامل.

#### get_stats()

```python
get_stats(tracks)
```

**Returns:**
```python
{
    'total_tracks': 50,
    'unique_artists': 25,
    'unique_albums': 30,
    'top_artist': 'محبوب‌ترین خواننده',
    'oldest_track': 1980,
    'newest_track': 2024
}
```

#### extract_and_save()

```python
extract_and_save(playlist_url, format='txt', filename=None)
```

یکجا استخراج و ذخیره.

**Parameters:**
- `format` (str): `'txt'`, `'csv'`, یا `'json'`
- `filename` (str, optional): اگه نده، خودش میسازه

## CLI Reference

### Basic Usage

```bash
spotify-extract [OPTIONS] PLAYLIST_URL
```

### Options

| Option | شرح |
|--------|-----|
| `-f, --format` | فرمت خروجی: txt, csv, json |
| `-o, --output` | نام فایل خروجی |
| `--stats` | نمایش آمار |
| `--info-only` | فقط اطلاعات پلی‌لیست |
| `-v, --verbose` | خروجی کامل |
| `--help` | راهنما |

### Examples

```bash
# ساده
spotify-extract https://open.spotify.com/playlist/...

# با آمار
spotify-extract --stats playlist_url

# JSON format
spotify-extract -f json -o my_music.json playlist_url

# فقط اطلاعات
spotify-extract --info-only playlist_url
```

## Error Handling

### Common Exceptions

- `ValueError`: Client ID/Secret نیست
- `ConnectionError`: مشکل اینترنت
- `HTTPError`: خطای API
- `FileNotFoundError`: مسیر فایل اشتباه

### Example:

```python
try:
    tracks = extractor.extract_tracks(url)
except ValueError as e:
    print(f"خطای تنظیمات: {e}")
except ConnectionError:
    print("مشکل اینترنت!")
```

## Rate Limiting

API اسپاتیفای محدودیت داره:
- **100 requests per minute**
- کتابخانه خودش مدیریت می‌کنه
- برای پلی‌لیست‌های بزرگ صبر کن

## Advanced Usage

### Batch Processing

```python
urls = [
    "playlist1_url",
    "playlist2_url",
]

all_tracks = []
for url in urls:
    tracks = extractor.extract_tracks(url)
    all_tracks.extend(tracks)

# حذف تکراری‌ها
unique_tracks = {track['url']: track for track in all_tracks}.values()
```

### Custom Processing

```python
tracks = extractor.extract_tracks(url, include_details=True)

# فیلتر کردن
rock_tracks = [t for t in tracks if 'rock' in t.get('genres', [])]

# مرتب‌سازی
sorted_tracks = sorted(tracks, key=lambda x: x['popularity'], reverse=True)
```