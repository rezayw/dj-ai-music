# 📦 Installation & Setup Guide

Complete instructions for setting up the DJ AI Music project on your system.

## System Requirements

### Minimum Requirements
- **OS:** macOS 10.13+, Windows 10+, or Linux (Ubuntu 18.04+)
- **Python:** 3.8 or higher (3.14.3 recommended)
- **RAM:** 2 GB (4 GB recommended for smooth processing)
- **Disk Space:** 200 MB total (100 MB for project + 80-100 MB for output)
- **Internet:** Only needed for initial package downloads

### Recommended Setup
- **OS:** macOS 12+ or Windows 11 or Ubuntu 22.04 LTS
- **Python:** 3.11+
- **RAM:** 8 GB
- **Disk Space:** 500 MB SSD
- **GPU:** Optional (NVIDIA for acceleration)

## Pre-Installation Steps

### macOS Setup

#### 1. Install Homebrew (if not already installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2. Install Python 3.14
```bash
brew install python@3.14
```

#### 3. Install FFmpeg (for MP3 encoding)
```bash
brew install ffmpeg
```

#### 4. Verify installations
```bash
python3 --version          # Should show 3.14.x
ffmpeg -version            # Should show version info
```

### Windows Setup

#### 1. Install Python from python.org
- Visit https://www.python.org/downloads/
- Download Python 3.14+
- **Important:** Check "Add Python to PATH" during installation

#### 2. Install FFmpeg
```powershell
# Using Chocolatey
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

#### 3. Verify installations
```powershell
python --version           # Should show 3.14.x
ffmpeg -version            # Should show version info
```

### Linux Setup (Ubuntu)

#### 1. Install Python and dependencies
```bash
sudo apt-get update
sudo apt-get install python3.11 python3-venv python3-pip ffmpeg
```

#### 2. Verify installations
```bash
python3 --version          # Should show 3.11+
ffmpeg -version            # Should show version info
```

## Project Installation

### Step 1: Clone or Extract Project

```bash
# If cloned from git
cd /path/to/dj-ai-music

# Or navigate to extracted folder
cd ~/Desktop/dj-ai-music
```

### Step 2: Create Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

You should see `(.venv)` in your terminal prompt.

### Step 3: Upgrade pip and setuptools

```bash
pip install --upgrade pip setuptools wheel
```

### Step 4: Install Dependencies

```bash
pip install librosa soundfile scipy numpy pydub pyttsx3
```

Or install from requirements (if available):
```bash
pip install -r requirements.txt
```

### Step 5: Verify Installation

```bash
python -c "import librosa, soundfile, scipy, numpy, pydub, pyttsx3; print('All packages installed!')"
```

Expected output:
```
All packages installed!
```

## Troubleshooting Installation

### Issue: "python3: command not found"

**macOS:**
```bash
# Use explicit python path
/usr/local/bin/python3.14 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```powershell
# Verify Python in PATH
where python

# Or use full path
C:\Python314\python.exe -m venv .venv
```

### Issue: "pip: command not found"

```bash
# macOS/Linux
python3 -m pip install --upgrade pip

# Windows
python -m pip install --upgrade pip
```

### Issue: "Permission denied" (macOS/Linux)

```bash
# Use --user flag
pip install --user librosa soundfile scipy numpy pydub pyttsx3

# Or use sudo (not recommended)
sudo pip install librosa soundfile scipy numpy pydub pyttsx3
```

### Issue: FFmpeg not found

**macOS:**
```bash
brew install ffmpeg
export PATH="/usr/local/opt/ffmpeg/bin:$PATH"
```

**Windows:**
- Download from https://ffmpeg.org/download.html
- Add to your PATH environment variable
- Or specify full path in code near pydub usage

**Linux:**
```bash
sudo apt-get install ffmpeg
```

### Issue: "No module named 'librosa'"

Ensure virtual environment is activated:
```bash
# Check if (.venv) appears in prompt
# If not:
source .venv/bin/activate     # macOS/Linux
.venv\Scripts\activate        # Windows
```

## Verifying Setup

### Quick Test (5 minutes)

```bash
# 1. Navigate to project
cd /Users/rezayw4/Desktop/dj-ai-music

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Run a quick test
python build_track.py
```

Expected output:
```
🎵 Building 'Midnight Drift' Track...
Target duration: 3:32 (212 seconds)
Target BPM: 150

📂 Loading loops...
  ✓ Loop 13...
  ✓ Loop 14...
  ...
✅ Track complete! File size: 35.66 MB
```

If successful, your environment is ready!

## Project File Organization

After installation, you should have:

```
dj-ai-music/
├── .venv/                    ← Virtual environment (created by you)
├── .git/                     ← Version control
├── .vscode/                  ← Editor settings
├── README.md                 ← Main documentation
├── QUICK_START.md           ← Quick reference
├── COOL_CALM_SONG_GUIDE.md  ← Production guide
├── TECHNICAL.md             ← Technical specs
├── CHANGELOG.md             ← Version history
├── INSTALLATION.md          ← This file
├── build_track.py           ← Instrumental builder
├── add_vocals.py            ← Vocal generator
├── enhance_track.py         ← Mastering effects
└── Sound-packs/             ← Audio loops
    ├── Loops/               ← 22 WAV files
    ├── LICENSE.txt          ← Audio licensing
    └── SoundPacks.com - Shapes Electronic Loops.jpg
```

## Operating Instructions

### Building Tracks (Standard Workflow)

```bash
# 1. Ensure you're in the project directory
cd /Users/rezayw4/Desktop/dj-ai-music

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Build instrumental (takes ~70 seconds)
python build_track.py

# 4. Generate vocals (takes ~80 seconds)
python add_vocals.py

# 5. Apply mastering (takes ~190 seconds)
python enhance_track.py

# Output: midnight_drift_enhanced.mp3 ready to use!
```

### Using Pre-Built Tracks

Your project includes pre-built tracks ready to use:
```bash
# Music files location:
/Users/rezayw4/Desktop/dj-ai-music/midnight_drift_enhanced.mp3
/Users/rezayw4/Desktop/dj-ai-music/midnight_drift_enhanced.wav
```

Just copy to your DJ software or media library!

## Virtual Environment Management

### Activate Environment
```bash
source .venv/bin/activate          # macOS/Linux
.venv\Scripts\activate             # Windows
```

### Deactivate Environment
```bash
deactivate
```

### Update Packages
```bash
pip list --outdated
pip install --upgrade librosa soundfile scipy
```

### Remove Virtual Environment
```bash
rm -rf .venv         # macOS/Linux
rmdir /s .venv       # Windows (PowerShell)
```

## Using Different Python Versions

### Check installed versions
```bash
python3.8 --version
python3.11 --version
python3.14 --version
```

### Create venv with specific version
```bash
# macOS/Linux
python3.11 -m venv .venv

# Windows
C:\Python311\python.exe -m venv .venv
```

## IDE Setup (Optional)

### VS Code

1. Install Python extension
2. Select interpreter: `.venv/bin/python`
3. Create `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true
}
```

### PyCharm

1. File → Settings → Project → Python Interpreter
2. Click ⚙️ → Add
3. Select "Existing Environment"
4. Navigate to `.venv/bin/python`

## Next Steps After Installation

1. **Run Quick Start:**
   ```bash
   python build_track.py
   ```

2. **Read Documentation:**
   - Start with `QUICK_START.md`
   - Then read `README.md` for overview
   - Check `TECHNICAL.md` for details

3. **Listen to Output:**
   - Find `midnight_drift_enhanced.mp3`
   - Play in your media player
   - Load into DJ software

4. **Customize:**
   - Edit lyrics in `add_vocals.py`
   - Change BPM in `build_track.py`
   - Adjust effects in `enhance_track.py`

## Performance Optimization

### For Faster Processing

1. **Reduce loop count:** Modify `ARRANGEMENT` in `build_track.py`
2. **Skip enhancement:** Comment out effects in `enhance_track.py`
3. **Use MP3 only:** Skip WAV generation, export directly to MP3

### For Better Quality

1. **Increase sample depth:** Use 24-bit float processing
2. **Add more loops:** Combine additional sound packs
3. **Record real vocals:** Replace TTS with professional recording

## System-Specific Notes

### macOS
- Uses native TTS voices (higher quality than Windows)
- FFmpeg installation via Homebrew is recommended
- M1/M2 Macs: All packages support ARM64 architecture

### Windows
- Requires FFmpeg installation in PATH
- TTS voices depend on system configuration
- PowerShell recommended over Command Prompt

### Linux
- All packages support Linux
- pyttsx3 uses system TTS (ESpeak often pre-installed)
- May need `sudo apt-get install libespeak-dev`

## What to Do If Something Goes Wrong

1. **Check Python version:**
   ```bash
   python --version  # Should be 3.8+
   ```

2. **Verify virtual environment:**
   ```bash
   which python       # macOS/Linux
   where python       # Windows
   ```
   Should point to `.venv`

3. **Reinstall packages:**
   ```bash
   pip uninstall librosa soundfile scipy numpy pydub pyttsx3
   pip install librosa soundfile scipy numpy pydub pyttsx3
   ```

4. **Check disk space:**
   ```bash
   df -h /Users/rezayw4/Desktop  # macOS/Linux
   dir C:\Users\...              # Windows
   ```

5. **Review error logs:**
   - Look for error messages in terminal output
   - Errors usually indicate missing dependencies or bad file paths

## Getting Help

### Documentation
- Read `README.md` for overview
- Check `TECHNICAL.md` for technical details
- See `QUICK_START.md` for usage examples

### Common Issues
See "Troubleshooting Installation" section above

### Verify Installation
Run `python build_track.py` (should complete without errors)

---

## Installation Checklist

- [ ] Python 3.8+ installed
- [ ] FFmpeg installed
- [ ] Virtual environment created (`.venv`)
- [ ] All pip packages installed
- [ ] FFmpeg in system PATH
- [ ] Project files accessible
- [ ] Test run successful (`python build_track.py`)
- [ ] Output files created

Once all items are checked, you're ready to use the project!

---

**Version:** 1.0  
**Last Updated:** March 2026  
**Status:** Complete ✓
