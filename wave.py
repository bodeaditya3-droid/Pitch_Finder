import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

SAMPLE_RATE = 44100
BLOCK_SIZE = 200

audio_data = np.zeros(BLOCK_SIZE)

plt.ion()

fig, ax = plt.subplots()
line, = ax.plot(audio_data)

ax.set_ylim(-1, 1)
ax.set_xlim(0, BLOCK_SIZE)
ax.set_title("Real-Time Microphone Waveform")
ax.set_xlabel("Samples")
ax.set_ylabel("Amplitude")


def audio_callback(indata, frames, time, status):
    global audio_data

    if status:
        print(status)

    audio_data = indata[:, 0].copy()


with sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=2,
    blocksize=BLOCK_SIZE,
    callback=audio_callback
):

    while True:
        line.set_ydata(audio_data)

        fig.canvas.draw()
        fig.canvas.flush_events()

        plt.pause(0.01)