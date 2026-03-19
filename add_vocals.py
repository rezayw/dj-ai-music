#!/usr/bin/env python3
"""
Add Vocal Tracks - Male & Female
Generates and overlays vocals on the instrumental track
"""

import os
import numpy as np
import pyttsx3
import soundfile as sf
from pydub import AudioSegment
from pydub.effects import normalize
import librosa

# Configuration
INSTRUMENTAL_FILE = "/Users/rezayw4/Desktop/dj-ai-music/midnight_drift_mixed.wav"
OUTPUT_FILE = "/Users/rezayw4/Desktop/dj-ai-music/midnight_drift_with_vocals.wav"
TEMP_DIR = "/Users/rezayw4/Desktop/dj-ai-music/temp_vocals"

# Create temp directory for vocal files
os.makedirs(TEMP_DIR, exist_ok=True)

# Lyrics split between male and female voices
MALE_VOCALS = {
    "intro_build": "Whispers in the neon glow",
    "verse1_part1": "Fading into the undertow, City lights are burning slow",
    "verse1_part2": "Find the peace you need to know",
    "pre_chorus": "Let it go, let it flow",
    "verse2_part1": "Echoes dancing on the beat, Synths are pure, the vibes are sweet",
    "verse2_part2": "Moving with celestial grace, Shadow dancing in this space",
}

FEMALE_VOCALS = {
    "pre_chorus_response": "Close your eyes, feel the sound",
    "chorus_part1": "In the midnight drift, we rise",
    "chorus_part2": "Watch the darkness fade tonight",
    "chorus_part3": "Every moment, every breath",
    "chorus_part4": "Take me to the eternal rest",
    "chorus_outro": "Midnight drift, drift, drift...",
}

def generate_vocal_track(text, voice_type, output_path):
    """Generate vocal audio using text-to-speech"""
    print(f"  🎤 Generating {voice_type} vocals: '{text[:40]}...'")
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)  # Slower, more dramatic delivery
    engine.setProperty('volume', 0.9)
    
    # Set voice type
    voices = engine.getProperty('voices')
    if voice_type == "male":
        engine.setProperty('voice', voices[0].id if len(voices) > 0 else voices[0].id)
    else:  # female
        engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
    
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    
    # Load the generated audio
    audio, sr = librosa.load(output_path, sr=44100)
    return audio, sr

def create_vocal_tracks():
    """Generate all male and female vocal parts"""
    print("🎤 Generating Vocal Tracks...")
    print()
    
    all_male_audio = []
    all_female_audio = []
    sr = 44100
    
    # Generate male vocals
    print("👨 Male Voice Vocals:")
    for key, text in MALE_VOCALS.items():
        output_path = os.path.join(TEMP_DIR, f"male_{key}.wav")
        try:
            audio, _ = generate_vocal_track(text, "male", output_path)
            all_male_audio.append((audio, key))
        except Exception as e:
            print(f"    ⚠️ Error generating '{key}': {e}")
    
    print()
    print("👩 Female Voice Vocals:")
    for key, text in FEMALE_VOCALS.items():
        output_path = os.path.join(TEMP_DIR, f"female_{key}.wav")
        try:
            audio, _ = generate_vocal_track(text, "female", output_path)
            all_female_audio.append((audio, key))
        except Exception as e:
            print(f"    ⚠️ Error generating '{key}': {e}")
    
    return all_male_audio, all_female_audio, sr

def load_instrumental():
    """Load the instrumental track"""
    print("📂 Loading instrumental track...")
    audio, sr = librosa.load(INSTRUMENTAL_FILE, sr=44100)
    print(f"   ✓ Loaded: {INSTRUMENTAL_FILE}")
    print(f"   Duration: {len(audio) / sr:.2f} seconds")
    return audio, sr

def mix_vocals_with_instrumental(instrumental, male_vocals, female_vocals, sr):
    """Mix vocal tracks with instrumental"""
    print("\n🎛️ Mixing Vocals with Instrumental...")
    
    # Initialize output (stereo)
    num_samples = len(instrumental)
    output = np.zeros((num_samples, 2))
    
    # Add instrumental to both channels
    instrumental_stereo = np.column_stack((instrumental, instrumental)) * 0.9
    output = instrumental_stereo.copy()
    
    # Vocal timing configuration (in samples, for 3:32 track)
    sr_sec = sr  # samples per second
    
    # Male vocals placement
    male_timings = [
        (0 * sr_sec, male_vocals[0][0] if len(male_vocals) > 0 else np.array([])),       # Intro
        (30 * sr_sec, male_vocals[1][0] if len(male_vocals) > 1 else np.array([])),      # Verse 1 part 1
        (45 * sr_sec, male_vocals[2][0] if len(male_vocals) > 2 else np.array([])),      # Verse 1 part 2
        (60 * sr_sec, male_vocals[3][0] if len(male_vocals) > 3 else np.array([])),      # Pre-chorus
        (90 * sr_sec, male_vocals[4][0] if len(male_vocals) > 4 else np.array([])),      # Verse 2 part 1
        (150 * sr_sec, male_vocals[5][0] if len(male_vocals) > 5 else np.array([])),     # Verse 2 part 2
    ]
    
    # Female vocals placement
    female_timings = [
        (45 * sr_sec, female_vocals[0][0] if len(female_vocals) > 0 else np.array([])),  # Pre-chorus response
        (80 * sr_sec, female_vocals[1][0] if len(female_vocals) > 1 else np.array([])),  # Chorus part 1
        (95 * sr_sec, female_vocals[2][0] if len(female_vocals) > 2 else np.array([])),  # Chorus part 2
        (110 * sr_sec, female_vocals[3][0] if len(female_vocals) > 3 else np.array([])), # Chorus part 3
        (130 * sr_sec, female_vocals[4][0] if len(female_vocals) > 4 else np.array([])), # Chorus part 4
        (200 * sr_sec, female_vocals[5][0] if len(female_vocals) > 5 else np.array([])), # Chorus outro
    ]
    
    # Mix male vocals
    print("  Placing male vocals...")
    for position, audio_data in male_timings:
        if len(audio_data) > 0:
            pos = int(position)
            duration = len(audio_data)
            end_pos = min(pos + duration, num_samples)
            actual_duration = end_pos - pos
            
            if actual_duration > 0:
                vocal_stereo = np.column_stack((audio_data[:actual_duration], audio_data[:actual_duration])) * 0.7
                output[pos:end_pos] += vocal_stereo
    
    # Mix female vocals
    print("  Placing female vocals...")
    for position, audio_data in female_timings:
        if len(audio_data) > 0:
            pos = int(position)
            duration = len(audio_data)
            end_pos = min(pos + duration, num_samples)
            actual_duration = end_pos - pos
            
            if actual_duration > 0:
                vocal_stereo = np.column_stack((audio_data[:actual_duration], audio_data[:actual_duration])) * 0.7
                output[pos:end_pos] += vocal_stereo
    
    # Normalize to prevent clipping
    print("  Normalizing mix...")
    max_val = np.max(np.abs(output))
    if max_val > 0:
        output = output / (max_val * 1.05)
    
    return output

def save_final_track(mixed_audio, sr):
    """Save the final mixed track"""
    print(f"\n💾 Saving final track: {OUTPUT_FILE}")
    
    # Convert to 16-bit PCM
    mixed_int16 = np.int16(mixed_audio * 32767)
    
    sf.write(OUTPUT_FILE, mixed_int16, sr)
    
    file_size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
    duration_sec = len(mixed_audio) / sr
    
    print(f"✅ Final track complete!")
    print(f"   Duration: {duration_sec:.2f} seconds (3:32)")
    print(f"   File size: {file_size_mb:.2f} MB")
    print(f"   Format: 44.1kHz stereo WAV")
    print()

def cleanup_temp_files():
    """Clean up temporary vocal files"""
    print("🧹 Cleaning up temporary files...")
    import shutil
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    print("   ✓ Cleaned")

def main():
    print("=" * 60)
    print("🎶 VOCAL TRACK GENERATOR - Male & Female Voices")
    print("=" * 60)
    print()
    
    try:
        # Load instrumental
        instrumental, sr = load_instrumental()
        
        # Generate vocal tracks
        male_vocals, female_vocals, sr = create_vocal_tracks()
        
        # Mix everything
        mixed = mix_vocals_with_instrumental(instrumental, male_vocals, female_vocals, sr)
        
        # Save final track
        save_final_track(mixed, sr)
        
        # Cleanup
        cleanup_temp_files()
        
        print("🎧 NOW COMPLETE: 'Midnight Drift' with Male & Female Vocals")
        print()
        print("📋 Track contains:")
        print("   ✓ Instrumental loops (layered)")
        print("   ✓ Male voice vocals (verses & prechorusb)")
        print("   ✓ Female voice vocals (chorus & response)")
        print("   ✓ Full 3:32 duration")
        print()
        print("🎯 Next steps:")
        print("   1. Open in your DAW for final mixing")
        print("   2. Adjust vocal levels if needed")
        print("   3. Add effects (reverb, EQ, compression)")
        print("   4. Master and export at 320kbps MP3")
        print()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
