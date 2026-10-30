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


def extract_middle_frame(audio, sr):
    frame_size = int(0.030 * sr)

    # Hint 1: Find the middle sample index.
    middle = len(audio) // 2

    # Hint 2: Start half a frame before the middle.
    start = middle - (frame_size // 2)

    # Hint 3: Slice the audio array.
    frame = audio[start : start + frame_size]

    return frame

def load_middle_frame():
    audio, sr = sf.read(os.path.join("audio", "start_1.wav"))

    frame = extract_middle_frame(audio, sr)

    return frame, sr

def compute_fft_magnitude(frame):
    fft_values = np.fft.rfft(frame) # gives us an array of complex numbers
    magnitude = np.abs(fft_values)
    return magnitude
# 15. Generate Frequency Bins
def compute_frequencies(frame, sr):
    frequencies = np.fft.rfftfreq(
        len(frame),
        d=1 /sr
    )
    return frequencies

def task2_fft():
    frame, sr = load_middle_frame()

    magnitude = compute_fft_magnitude(frame)
    frequencies = compute_frequencies(frame, sr)

    plt.figure(figsize=(10, 4))
    plt.plot(frequencies, magnitude)
    plt.xlim(0, 5000)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("Frequency Spectrum")
    plt.savefig(os.path.join(PLOTS_DIR, "task2_spectrum.png"))
    plt.close()

def magnitude_to_db(magnitude):
    magnitude_db = 20 * np.log10(magnitude + 1e-10)
    return magnitude_db


def detect_peaks(magnitude):
    peaks, properties = find_peaks(magnitude)
    return peaks

def plot_spectrum_db(frequencies, magnitude_db):
    plt.figure(figsize=(10, 4))

    # Your code here
    plt.plot(frequencies, magnitude_db)
    plt.xlim(0, 5000)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.title('Frequency Spectrum (dB)')

    plt.savefig(os.path.join(PLOTS_DIR, "task2_spectrum_db.png"))
    plt.close()


def task3_spectrograms():
    pass

def task4_vowels():
    pass

def task5_endpoint():
    pass

if __name__ == "__main__":
    # We will uncomment these as we go
    task2_fft()