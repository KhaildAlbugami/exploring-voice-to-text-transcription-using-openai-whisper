import sounddevice as sd
import wavio
import whisper

#  Record Audio Function
def record_audio(filename, duration=20, fs=44100):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Recording complete.")
    wavio.write(filename, audio, fs, sampwidth=2)

# 1- Rec the audio and save it as "output.wav" using "record_audio() function"
record_audio('output.wav')

# 2- Load and Use Whisper Model for Transcription
model = whisper.load_model("base")  # can choose from (base/small/medium/large) based on the need.

result = model.transcribe("output.wav")

# Print the transcribed text
print('Transcribed Text:')
print(result["text"])
