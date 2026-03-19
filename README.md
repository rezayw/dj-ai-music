# 🎵 Midnight Drift - DJ AI Music Project

A professional electronic music track created entirely through code automation and audio synthesis. This project demonstrates how to combine electronic sound packs, generate synthetic vocals, and apply professional mastering effects to create a complete, radio-ready song.

## 📋 Project Overview

**Track:** "Midnight Drift"  
**Duration:** 3:32 (212 seconds)  
**BPM:** 150 (unified)  
**Genre:** Cool, Calm Electronic  
**Production Style:** Bruno Mars warmth + Lady Gaga clarity  
**Sample Rate:** 44.1kHz / 16-bit Stereo  

## 🎧 What's Included

### Final Tracks (Ready to Use)
- **`midnight_drift_enhanced.wav`** - Professional WAV format (35.66 MB)
- **`midnight_drift_enhanced.mp3`** - Club/streaming ready, 320kbps (8.09 MB)

### Intermediate Files
- **`midnight_drift_mixed.wav`** - Instrumental only (35.66 MB)
- **`midnight_drift_with_vocals.wav`** - Instrumental + raw vocals (35.66 MB)

### Documentation
- **`COOL_CALM_SONG_GUIDE.md`** - Complete production guide with lyrics, arrangement details, and mixing tips

## 📁 Project Structure

```
dj-ai-music/
├── README.md                           # This file
├── COOL_CALM_SONG_GUIDE.md            # Detailed production guide & lyrics
├── Sound-packs/                        # Audio sample packs
│   ├── Loops/                          # 22 electronic loops (SHAPES pack)
│   ├── LICENSE.txt                     # Sound pack licensing
│   └── SoundPacks.com - Shapes Electronic Loops.jpg
├── build_track.py                      # Instrumental audio builder
├── add_vocals.py                       # Vocal generator (male & female)
├── enhance_track.py                    # Professional mastering effects
└── .venv/                              # Python virtual environment

```

## 🎵 Track Features

### Instrumentation
- **7 Layered Electronic Loops** from SHAPES pack (148-155 BPM)
  - Loops 11, 12, 13, 14, 15, 18, 19
- **Time-stretched to unified 150 BPM** for perfect synchronization
- **Dynamic arrangement** with progressive build from intro to chorus

### Vocals
- **Male Voice** - Verses and pre-chorus sections
- **Female Voice** - Chorus and response lines
- **Duet arrangement** - Natural call-and-response pattern

### Professional Enhancement
✓ Bass warmth (Bruno Mars smoothness)  
✓ Vocal presence boost (Lady Gaga clarity)  
✓ Reverb shimmer (spaciousness)  
✓ Soft compression (cohesion)  
✓ Stereo width enhancement  
✓ Professional mastering loudness  

## 📝 Lyrics

### Verse 1
```
Whispers in the neon glow
Fading into the undertow
City lights are burning slow
Find the peace you need to know
```

### Pre-Chorus
```
Let it go, let it flow
Close your eyes, feel the sound
```

### Chorus
```
In the midnight drift, we rise
Watch the darkness fade tonight
Every moment, every breath
Take me to the eternal rest
Midnight drift, drift, drift...
```

### Verse 2
```
Echoes dancing on the beat
Synths are pure, the vibes are sweet
Moving with celestial grace
Shadow dancing in this space
```

## 🛠️ Technical Details

### Audio Specifications
- **Format:** WAV (lossless) & MP3 (320kbps for streaming)
- **Sample Rate:** 44.1kHz
- **Bit Depth:** 16-bit
- **Channels:** Stereo
- **Duration:** 212 seconds (3:32)

### Production Pipeline

1. **Instrumental Building** (`build_track.py`)
   - Loads 7 electronic loops
   - Time-stretches each to 150 BPM
   - Layers them according to production timeline
   - Applies section-based volume control
   - Normalizes to prevent clipping

2. **Vocal Generation** (`add_vocals.py`)
   - Generates male voice track (pyttsx3 TTS)
   - Generates female voice track (pyttsx3 TTS)
   - Times vocals to specific sections (0-212 seconds)
   - Mixes vocals with instrumental (70% vocal level)
   - Final normalization for balanced mix

3. **Professional Enhancement** (`enhance_track.py`)
   - Bass warmth boost (Gaussian filter @ low frequencies)
   - Vocal presence enhancement (high-frequency boost)
   - Reverb shimmer (1.8s decay convolution)
   - Soft compression (transparent dynamic control)
   - Stereo width enhancement (mid-side processing)
   - Loudness mastering (-14dB target)

## 🎛️ Arrangement Timeline

| Section | Time | Loops | Volume |
|---------|------|-------|--------|
| Intro | 0:00-0:30 | 13 | 40% |
| Verse 1 | 0:30-1:15 | 13, 19 | 50% |
| Pre-Chorus | 1:15-1:50 | 13, 19, 15, 18 | 75% |
| Chorus | 1:50-2:35 | 13, 19, 18, 12 | 85% |
| Verse 2 | 2:35-3:05 | 13, 19, 18, 14 | 70% |
| Final/Outro | 3:05-3:32 | 13, 19, 18, 12 | 85% → 0% fade |

## 🚀 How to Use

### Option 1: Use the Final Track Directly
Simply open `midnight_drift_enhanced.mp3` in:
- DJ software (Serato, Rekordbox, Virtual DJ)
- Digital Audio Workstation (Ableton, FL Studio, Logic Pro)
- Music players (Spotify, Apple Music, etc.)

### Option 2: Edit/Remix in a DAW
1. Open `midnight_drift_enhanced.wav` in your DAW
2. Adjust levels, EQ, effects as needed
3. Re-export in your desired format

### Option 3: Rebuild from Scratch
```bash
# Create fresh instrumental
python build_track.py

# Add vocals
python add_vocals.py

# Apply professional enhancement
python enhance_track.py
```

## 📦 Dependencies

### Python Packages
```
librosa==0.10.0
pydub==0.25.1
soundfile==0.12.1
numpy==1.24.3
scipy==1.11.0
pyttsx3==2.90
```

### System Requirements
- Python 3.14+
- macOS (tested on macOS)
- FFmpeg (for MP3 conversion)

### Installation
```bash
# Install FFmpeg (macOS)
brew install ffmpeg

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install librosa pydub soundfile numpy scipy pyttsx3
```

## 🎨 Sound Pack Details

**Pack Name:** SHAPES Electronic Loops  
**Source:** SoundPacks.com  
**Format:** WAV files  
**BPM Range:** 148-170 BPM  
**Total Loops:** 22 professional electronic loops  

### Loops Used
- Loop 11: 155 BPM
- Loop 12: 150 BPM
- Loop 13: 148 BPM
- Loop 14: 148 BPM
- Loop 15: 148 BPM
- Loop 18: 155 BPM
- Loop 19: 155 BPM

## 📊 Audio Quality Comparison

| Format | File Size | Bitrate | Quality | Use Case |
|--------|-----------|---------|---------|----------|
| WAV | 35.66 MB | Lossless | Studio/Master | Professional editing |
| MP3 | 8.09 MB | 320kbps | High | Streaming/DJing |
| MP3 | ~4 MB | 192kbps | Good | Web/Mobile |
| MP3 | ~2.5 MB | 128kbps | Fair | Low bandwidth |

## 🎙️ Vocal Production Notes

### TTS Settings
- **Engine:** pyttsx3 (Python Text-to-Speech)
- **Rate:** 130 WPM (slow, dramatic delivery)
- **Volume:** 90%
- **Male Voice:** System default male voice
- **Female Voice:** System default female voice

### Vocal Timing
- Male vocals layer throughout verses (0-30s, 30-75s, 60-105s, 155-195s)
- Female vocals dominate chorus (45-80s, 80-130s, 200s+)
- Natural call-and-response rhythm
- 20% reverb tail on all vocals for spatial depth

## 🎯 Production Best Practices Applied

✓ **Time-Stretching:** All loops normalized to 150 BPM for seamless layering  
✓ **Phase Alignment:** Loops aligned at beat boundaries  
✓ **Gain Staging:** Progressive volume build (40% → 85%)  
✓ **Mixing:** Proper headroom maintained (-14dB target loudness)  
✓ **EQ:** Warmth (bass) + clarity (presence) for radio-ready sound  
✓ **Compression:** Transparent dynamic control for cohesion  
✓ **Mastering:** Professional loudness normalization  

## 💡 Tips for DJs

1. **Use in DJ Sets:** Import `midnight_drift_enhanced.mp3` into Serato/Rekordbox
2. **Blend with Other Tracks:** 150 BPM matches most electronic/house tracks
3. **Filter Automation:** Use low-pass filters for smooth drops
4. **Layering:** Beatmix with other 150 BPM tracks for seamless transitions
5. **Remix Potential:** Use `midnight_drift_mixed.wav` as a remix base

## 🔧 Customization

To create variations:

1. **Change Vocals:** Re-run `add_vocals.py` with different lyrics
2. **Adjust Mix:** Edit volume levels in `build_track.py`
3. **Add Effects:** Modify enhancement chain in `enhance_track.py`
4. **Different BPM:** Change `TARGET_BPM` in `build_track.py`

## 📜 Licensing

- **Sound Packs:** See `Sound-packs/LICENSE.txt` for SHAPES pack licensing
- **Code:** This Python code is provided as-is for educational/personal use
- **Generated Track:** Free to use for non-commercial purposes

## 👤 Credits

**Production:** AI-assisted music production pipeline  
**Sound Pack:** SHAPES Electronic Loops from SoundPacks.com  
**Vocals:** Synthetic voices (pyttsx3)  
**Enhancement:** Professional audio mastering techniques  

## 📞 Support

### Common Issues

**Issue:** Audio files not found
- **Solution:** Ensure all Python scripts are run from project root directory

**Issue:** MP3 conversion fails
- **Solution:** Install FFmpeg: `brew install ffmpeg`

**Issue:** Vocal quality sounds robotic
- **Solution:** This is expected with TTS. For professional vocals, record human singers separately

## 🎉 Next Steps

1. ✅ Listen to `midnight_drift_enhanced.mp3`
2. ✅ Use in your DJ sets at 150 BPM
3. ✅ Customize the track further in your DAW
4. ✅ Remix with your own audio elements
5. ✅ Share and distribute!

---

**Created:** March 2026  
**Version:** 1.0  
**Status:** Production Ready ✓
