import wave
import pydub 
import numpy as np
from scipy.io.wavfile import read


a = pydub.AudioSegment.from_mp3('nevero.mp3')
y = np.array(a.get_array_of_samples())


data = read('never-n.wav')
d = []
for i,j in zip(y,data[1]):
    d.append(j-i)


arr = np.array(d)
data = arr.astype(np.int16()).tobytes()

wf = wave.open('never-n.wav', 'r')
size = wf.getsampwidth()
print(size)
wf = wave.open('never.wav', 'wb')
wf.setnchannels(2)
wf.setsampwidth(2)
wf.setnframes(1)
wf.setframerate(44100)
wf.writeframes(data)
wf.close()

