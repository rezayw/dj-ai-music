#!/usr/bin/env python3
"""
Cool & Calm Electronic Track Builder
Combines SHAPES loops according to production guide
Duration: 3:32 (212 seconds)
"""

import os
import numpy as np
from pydub import AudioSegment
from pydub.effects import normalize
import librosa
import soundfile as sf
from pathlib import Path

# Configuration
LOOPS_DIR = "/Users/rezayw4/Desktop/dj-ai-music/Sound-packs/Loops"
OUTPUT_FILE = "/Users/rezayw4/Desktop/dj-ai-music/midnight_drift_mixed.wav"
TARGET_DURATION = 212000  # 3:32 in milliseconds
TARGET_BPM = 150  # Will time-stretch loops to this BPM

# Recommended loops (0-indexed loop numbers converted to filenames)
LOOPS_MAP = {
    11: "11 SHAPES 155 bpm.wav",
    12: "12 SHAPES 150 bpm.wav",
    13: "13 SHAPES 148 bpm.wav",
    14: "14 SHAPES 148 bpm.wav",
    15: "15 SHAPES 148 bpm.wav",
    18: "18 SHAPES 155 bpm.wav",
    19: "19 SHAPES 155 bpm.wav",
}

# Section arrangement (time in milliseconds, loops to layer, volume)
ARRANGEMENT = [
    # (start_ms, end_ms, [loop_numbers], volume_level)
    (0, 30000, [13], 0.4),           # Intro
    (30000, 75000, [13, 19], 0.5),   # Verse 1
    (75000, 105000, [13, 19, 15, 18], 0.75),  # Pre-Chorus
    (105000, 155000, [13, 19, 18, 12], 0.85), # Chorus
    (155000, 195000, [13, 19, 18, 14], 0.7),  # Verse 2
    (195000, 212000, [13, 19, 18, 12], 0.85), # Final Chorus + Fade
]

def load_and_resample_audio(filepath, target_sr=44100):
    """Load audio file and resample to target sample rate"""
    print(f"Loading: {filepath}")
    audio_data, sr = librosa.load(filepath, sr=target_sr)
    return audio_data, sr

def time_stretch(audio_data, original_bpm, target_bpm):
    """Time stretch audio to match target BPM"""
    stretch_factor = original_bpm / target_bpm
    stretched = librosa.effects.time_stretch(audio_data, rate=stretch_factor)
    return stretched

def create_track():
    """Build the complete track according to arrangement"""
    print("🎵 Building 'Midnight Drift' Track...")
    print(f"Target duration: 3:32 (212 seconds)")
    print(f"Target BPM: {TARGET_BPM}")
    print()
    
    # Initialize output audio (stereo, 44.1kHz)
    sr = 44100
    num_samples = int(sr * 212)
    output_audio = np.zeros((num_samples, 2))
    
    # Load all loops
    print("📂 Loading loops...")
    loops_data = {}
    loops_bpm = {
        11: 155, 12: 150, 13: 148, 14: 148, 15: 148,
        18: 155, 19: 155
    }
    
    for loop_num, filename in LOOPS_MAP.items():
        filepath = os.path.join(LOOPS_DIR, filename)
        if os.path.exists(filepath):
            audio_data, _ = load_and_resample_audio(filepath, target_sr=sr)
            
            # Time stretch to target BPM
            original_bpm = loops_bpm[loop_num]
            stretched = time_stretch(audio_data, original_bpm, TARGET_BPM)
            loops_data[loop_num] = stretched
            print(f"  ✓ Loop {loop_num:2d} ({original_bpm} BPM → {TARGET_BPM} BPM)")
        else:
            print(f"  ✗ Loop {loop_num:2d} NOT FOUND: {filename}")
    
    print()
    print("🎛️ Arranging sections...")
    
    # Build track section by section
    for section_idx, (start_ms, end_ms, loop_list, volume) in enumerate(ARRANGEMENT):
        start_sample = int(start_ms * sr / 1000)
        end_sample = int(end_ms * sr / 1000)
        duration_samples = end_sample - start_sample
        
        section_audio = np.zeros((duration_samples, 2))
        
        # Layer selected loops for this section
        for loop_num in loop_list:
            if loop_num in loops_data:
                loop_audio = loops_data[loop_num]
                
                # Tile the loop to fill the section
                loop_len = len(loop_audio)
                num_repeats = (duration_samples // loop_len) + 2
                tiled = np.tile(loop_audio, num_repeats)
                
                # Trim to exact section length
                section_loop = tiled[:duration_samples]
                
                # Stack to stereo if mono
                if section_loop.ndim == 1:
                    section_loop = np.column_stack((section_loop, section_loop))
                
                # Add to section (with volume adjustment)
                section_audio += section_loop * volume
        
        # Smooth volume transitions at section boundaries
        if section_idx > 0:
            fade_samples = int(0.5 * sr)  # 500ms fade
            fade_in = np.linspace(0, 1, fade_samples)
            section_audio[:fade_samples] *= fade_in.reshape(-1, 1)
        
        # Add final fade-out for outro
        if section_idx == len(ARRANGEMENT) - 1:
            fade_out = np.linspace(1, 0, int(5 * sr))  # 5 second fade
            fade_out_start = max(0, duration_samples - len(fade_out))
            section_audio[fade_out_start:] *= fade_out[-duration_samples+fade_out_start:].reshape(-1, 1)
        
        # Insert into output
        output_audio[start_sample:end_sample] = section_audio
        
        section_name = ["Intro", "Verse 1", "Pre-Chorus", "Chorus", "Verse 2", "Final/Outro"][section_idx]
        print(f"  ✓ {section_name:15} ({start_ms/1000:6.2f}s - {end_ms/1000:6.2f}s) | Loops: {loop_list} | Vol: {volume}")
    
    print()
    print("🔊 Normalizing audio...")
    
    # Normalize to prevent clipping
    max_val = np.max(np.abs(output_audio))
    if max_val > 0:
        output_audio = output_audio / (max_val * 1.05)  # Slight headroom
    
    # Convert to 16-bit PCM
    output_audio_int16 = np.int16(output_audio * 32767)
    
    print(f"💾 Saving to: {OUTPUT_FILE}")
    sf.write(OUTPUT_FILE, output_audio_int16, sr)
    
    file_size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
    print(f"✅ Track complete! File size: {file_size_mb:.2f} MB")
    print()
    print("🎧 Next steps:")
    print("1. Open the output file in your DAW")
    print("2. Add vocals using lyrics from COOL_CALM_SONG_GUIDE.md")
    print("3. Apply additional EQ, reverb, and compression")
    print("4. Master and export at 320kbps")
    print()

if __name__ == "__main__":
    try:
        create_track()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n⚠️ Make sure you have the required packages:")
        print("   pip install librosa pydub soundfile numpy")
