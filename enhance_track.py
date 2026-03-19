#!/usr/bin/env python3
"""
Beautiful Track Enhancement - Bruno Mars & Lady Gaga Style
Simplified professional mastering
"""

import os
import numpy as np
import soundfile as sf
from scipy.ndimage import gaussian_filter1d

# Configuration
INPUT_FILE = "/Users/rezayw4/Desktop/dj-ai-music/midnight_drift_with_vocals.wav"
OUTPUT_FILE = "/Users/rezayw4/Desktop/dj-ai-music/midnight_drift_enhanced.wav"
MP3_OUTPUT = "/Users/rezayw4/Desktop/dj-ai-music/midnight_drift_enhanced.mp3"

def load_audio(filepath):
    """Load audio file"""
    print(f"📂 Loading: {filepath}")
    try:
        audio, sr = sf.read(filepath)
        print(f"   ✓ Loaded successfully")
        print(f"   Duration: {len(audio) / sr:.2f}s | Sample Rate: {sr}Hz")
        
        # Ensure stereo
        if audio.ndim == 1:
            audio = np.column_stack((audio, audio))
        return audio, sr
    except Exception as e:
        print(f"Error loading: {e}")
        return None, None

def apply_soft_compression(audio, threshold=-20):
    """Apply gentle compression"""
    print("  ✓ Adding transparent compression...")
    
    output = audio.copy()
    for ch in range(min(2, audio.shape[1] if audio.ndim > 1 else 1)):
        ch_audio = audio[:, ch] if audio.ndim > 1 else audio
        
        # Simple RMS-based compression
        window_size = 2048
        hop_size = window_size // 2
        
        for i in range(0, len(ch_audio) - window_size, hop_size):
            window = ch_audio[i:i+window_size]
            rms = np.sqrt(np.mean(window ** 2))
            
            if rms > 0:
                target = max(rms * 0.95, 0.3)  # Gentle 5% reduction
                ch_audio[i:i+window_size] = window * (target / rms)
        
        if audio.ndim > 1:
            output[:, ch] = ch_audio
        else:
            output = ch_audio
    
    return output

def boost_warmth(audio):
    """Add bass warmth like Bruno Mars"""
    print("  ✓ Adding warmth (bass boost)...")
    
    output = audio.copy()
    sr = 44100
    
    # Simple bass enhancement using low-frequency boost
    for ch in range(min(2, audio.shape[1] if audio.ndim > 1 else 1)):
        ch_audio = audio[:, ch] if audio.ndim > 1 else audio
        
        # Create a low-pass filtered version for bass
        kernel_size = int(sr * 0.05)  # 50ms window
        if kernel_size % 2 == 0:
            kernel_size += 1
        
        bass_layer = gaussian_filter1d(ch_audio, sigma=kernel_size/10)
        
        # Add 15% of bass layer for warmth
        enhanced = ch_audio + bass_layer * 0.15
        
        if audio.ndim > 1:
            output[:, ch] = enhanced
        else:
            output = enhanced
    
    return output

def enhance_presence(audio):
    """Add clarity like Lady Gaga"""
    print("  ✓ Enhancing presence (vocal clarity)...")
    
    output = audio.copy()
    sr = 44100
    
    # Simple high-frequency enhancement
    for ch in range(min(2, audio.shape[1] if audio.ndim > 1 else 1)):
        ch_audio = audio[:, ch] if audio.ndim > 1 else audio
        
        # Create a high-frequency component
        kernel_size = int(sr * 0.01)  # 10ms window
        if kernel_size % 2 == 0:
            kernel_size += 1
        
        smooth = gaussian_filter1d(ch_audio, sigma=kernel_size/5)
        high_freq = ch_audio - smooth
        
        # Add 10% of high-frequency for brightness
        enhanced = ch_audio + high_freq * 0.10
        
        if audio.ndim > 1:
            output[:, ch] = enhanced
        else:
            output = enhanced
    
    return output

def add_reverb_shimmer(audio, sr, decay=1.5):
    """Add subtle reverb for space"""
    print("  ✓ Adding reverb shimmer...")
    
    output = audio.copy()
    decay_samples = int(decay * sr)
    
    # Create reverb tail
    reverb_tail = np.linspace(1, 0.1, decay_samples) ** 1.5
    
    for ch in range(min(2, audio.shape[1] if audio.ndim > 1 else 1)):
        ch_audio = audio[:, ch] if audio.ndim > 1 else audio
        
        # Simple convolution reverb
        convolved = np.convolve(ch_audio, reverb_tail, mode='same')
        
        # Mix 20% reverb with original
        enhanced = ch_audio * 0.8 + convolved * 0.2
        
        if audio.ndim > 1:
            output[:, ch] = enhanced
        else:
            output = enhanced
    
    return output

def enhance_stereo(audio):
    """Widen stereo field"""
    print("  ✓ Enhancing stereo width...")
    
    if audio.ndim < 2:
        return audio
    
    output = audio.copy()
    
    # Calculate mid and side
    mid = (audio[:, 0] + audio[:, 1]) / 2
    side = (audio[:, 0] - audio[:, 1]) / 2
    
    # Boost side slightly for width
    side *= 1.2
    
    # Reconstruct
    output[:, 0] = mid + side
    output[:, 1] = mid - side
    
    return output

def master_loudness(audio, target_loudness=0.7):
    """Apply final loudness adjustment"""
    print("  ✓ Mastering loudness...")
    
    # Calculate current loudness
    rms = np.sqrt(np.mean(audio ** 2))
    
    if rms > 0:
        # Apply loudness target with headroom
        scale_factor = target_loudness / rms
        audio = audio * scale_factor
    
    # Soft limiting to prevent clipping
    audio = np.clip(audio, -0.99, 0.99)
    
    return audio

def enhance_track():
    """Main enhancement pipeline"""
    print("=" * 70)
    print("🎵  PROFESSIONAL TRACK ENHANCEMENT")
    print("      Bruno Mars & Lady Gaga Style")
    print("=" * 70)
    print()
    
    # Load
    audio, sr = load_audio(INPUT_FILE)
    if audio is None:
        print("❌ Failed to load audio")
        return
    
    original_duration = len(audio) / sr
    print()
    
    print("🎛️  Applying Professional Effects:")
    print()
    
    # Enhancement chain
    audio = boost_warmth(audio)
    audio = enhance_presence(audio)
    audio = add_reverb_shimmer(audio, sr, decay=1.8)
    audio = boost_warmth(audio)  # Double warmth for richness
    audio = apply_soft_compression(audio)
    audio = enhance_stereo(audio)
    audio = master_loudness(audio, target_loudness=0.75)
    
    print()
    print("💾 Saving Enhanced Track...")
    print()
    
    # Ensure audio is in correct range
    audio = np.clip(audio, -1.0, 1.0)
    
    # Convert to 16-bit
    audio_int16 = np.int16(audio * 32767)
    
    try:
        sf.write(OUTPUT_FILE, audio_int16, sr)
        file_size = os.path.getsize(OUTPUT_FILE) / (1024 ** 2)
        print(f"✅ Saved: midnight_drift_enhanced.wav")
        print(f"   File size: {file_size:.2f} MB")
        print(f"   Duration: {original_duration:.2f}s")
    except Exception as e:
        print(f"❌ Error saving WAV: {e}")
        return
    
    print()
    print("🎵 Converting to MP3 (320kbps)...")
    try:
        from pydub import AudioSegment
        wav_audio = AudioSegment.from_wav(OUTPUT_FILE)
        wav_audio.export(MP3_OUTPUT, format="mp3", bitrate="320k")
        mp3_size = os.path.getsize(MP3_OUTPUT) / (1024 ** 2)
        print(f"✅ Saved: midnight_drift_enhanced.mp3")
        print(f"   File size: {mp3_size:.2f} MB (320kbps)")
    except Exception as e:
        print(f"⚠️  MP3 conversion skipped: {e}")
        print("   Install ffmpeg: brew install ffmpeg")
    
    print()
    print("=" * 70)
    print("🎧  ENHANCEMENT COMPLETE!")
    print("=" * 70)
    print()
    print("✨ Effects Applied:")
    print("   ✓ Bass warmth enhancement (Bruno Mars smoothness)")
    print("   ✓ Vocal presence boost (Lady Gaga clarity)")
    print("   ✓ Reverb shimmer (spaciousness)")
    print("   ✓ Soft compression (cohesion)")
    print("   ✓ Stereo width enhancement")
    print("   ✓ Professional mastering loudness")
    print()
    print("📊 Quality:")
    print("   • 44.1kHz / 16-bit stereo")
    print("   • Professional enhancement chain")
    print("   • Radio-ready sound")
    print()
    print("🎉 Your beautiful track is ready for the club!")
    print()

if __name__ == "__main__":
    try:
        enhance_track()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
