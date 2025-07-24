from setuptools import setup, find_packages

# خوندن README برای description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="spotify-playlist-extractor",
    version="1.0.0",
    author="Mohammad Hossein Norouzi",
    author_email="mohammadhn.dev@gmail.com",
    description="استخراج ساده و سریع پلی‌لیست‌های اسپاتیفای",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MohammadHNdev/Spotify-Playlist-Extractor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.8",
    install_requires=[
        "spotipy>=2.22.1",
        "requests>=2.28.0",
        "python-dotenv>=0.19.0",
    ],
    extras_require={
        "web": ["streamlit>=1.20.0", "pandas>=1.3.0"],
        "dev": ["pytest>=7.0.0", "black>=22.0.0", "flake8>=4.0.0"],
    },
    entry_points={
        "console_scripts": [
            "spotify-extract=spotify_extractor.cli:main",
        ],
    },
    keywords="spotify playlist music extractor download links",
    project_urls={
        "Bug Reports": "https://github.com/MohammadHNdev/Spotify-Playlist-Extractor/issues",
        "Source": "https://github.com/MohammadHNdev/Spotify-Playlist-Extractor",
        "Documentation": "https://github.com/MohammadHNdev/Spotify-Playlist-Extractor#readme",
    },
    include_package_data=True,
    zip_safe=False,
)