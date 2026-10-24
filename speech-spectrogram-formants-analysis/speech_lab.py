import sounddevice as sd
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import parselmouth
from scipy.signal import find_peaks
import os

# Global settings
SAMPLE_RATE = 16000
AUDIO_DIR = "audio"
PLOTS_DIR = "plots"

# Ensure folders exist
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)

# ==========================================

# TASKS
# ==========================================

def task1_record():
    print("\n--- TASK 1: Record 'start' 3 times ---")
    duration = 2.0 # seconds
    
    for i in range(1, 4):
        input(f"Press Enter to record 'start' ({i}/3)...")
        
        recording = sd.rec(
            int(duration * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32"
        )
        print("Recording...")
        sd.wait()
        
        filename = os.path.join(AUDIO_DIR, f"start_{i}.wav")
        sf.write(filename, recording, SAMPLE_RATE)
        print(f"Saved {filename}")

def task1_plot_and_analyze():
    for i in range(1, 4):
        filename = os.path.join("audio", f"start_{i}.wav")
        audio, sr = sf.read(filename) # Loadeing Audio and Sampling rate
        time = np.arange(len(audio)) / sr

        plt.figure(figsize=(10, 3))
        plt.plot(time, audio)
        plt.title(f"Waveform of start_{i}.wav")
        plt.savefig(os.path.join("plots", f"task1_waveform_{i}.png"))
        plt.close() # Important to close so your computer doesn't crash on a loop

        peak = np.max(np.abs(audio))
        rms = np.sqrt(np.mean(audio ** 2))

        print(f"Recording: start_{i}.wav")
        print(f"  RMS: {rms:.4f}")
        print(f"  Peak amplitude: {peak:.4f}")
        print("-" * 30)



def task2_fft():
    pass

def task3_spectrograms():
    pass

def task4_vowels():
    pass

def task5_endpoint():
    pass

if __name__ == "__main__":
    # We will uncomment these as we go
    task1_plot_and_analyze()