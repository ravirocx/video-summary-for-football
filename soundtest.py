from scipy.io import wavfile
import numpy
import matplotlib.pyplot as plt
import math
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

sampFreq, snd = wavfile.read('theaudio.wav')
print(snd.dtype)
snd=snd/(2.**15)
print(snd.shape)

shape=int(snd.shape[0])

print(shape/sampFreq)
print(sampFreq)
timeArray = numpy.arange(0, shape, 1)
timeArray = timeArray / sampFreq

s2 = snd[:,0] 
s2=numpy.square(s2)
s2=numpy.square(s2)
s2=numpy.square(s2)
#s2=numpy.square(s2)

#s2=numpy.sqrt(s2)
#s2=numpy.sqrt(s2)

plt.plot(timeArray, s2, color='k')
plt.ylabel('Amplitude')
plt.xlabel('Time (ms)')
plt.show()

print(s2)
mean=numpy.mean(s2)
array_of_time=numpy.array(0)
print(timeArray)
t=0
for x in s2:
	if x>0.0000015:
		print("mil gaya",t/sampFreq)
		temp_time=int(t/sampFreq)
		array_of_time= numpy.append(array_of_time,temp_time)
		#print(int(t/sampFreq))
	t=t+1
print(array_of_time)
print(numpy.unique(array_of_time))

unique_array_of_time=numpy.unique(array_of_time)
maxi=unique_array_of_time[-1]
final_array=numpy.zeros(maxi+1)
p=maxi
r=maxi
for x in range(10,len(unique_array_of_time)):
	if unique_array_of_time[x]-unique_array_of_time[x-10]<=15:
		print(unique_array_of_time[x-10],unique_array_of_time[x])
		final_array[unique_array_of_time[x-10]]=final_array[unique_array_of_time[x-10]]+1
		final_array[unique_array_of_time[x]]=final_array[unique_array_of_time[x]]-1
for x in range(1,maxi+1):
	final_array[x]=final_array[x]+final_array[x-1]

print(final_array)
final_ans=numpy.array(0)

for x in range(0,maxi+1):
	if final_array[x]>0:
		p=min(x,p)
	elif final_array[x]==0 and p!=maxi:
		r=min(x,r)
		final_ans=numpy.append(final_ans,p)
		final_ans=numpy.append(final_ans,r)
		p=maxi
		r=maxi
ffmpeg_extract_subclip("video.mkv", 10, 50, targetname="test.mp4")
print(final_ans)
for x in range(1,len(final_ans)):
	ffmpeg_extract_subclip("video.mkv", final_ans[x]+15, final_ans[x+1]+10, targetname="test.mp4")
	x=x+2
	

"""n = len(s1) 
p = numpy.fft.fft(s1) # take the fourier transform 
nUniquePts = int(math.ceil((n+1)/2.0))
p = p[0:nUniquePts]
p = abs(p)
p = p / float(n) # scale by the number of points so that
                 # the magnitude does not depend on the length 
                 # of the signal or on its sampling frequency  
p = p**2  # square it to get the power 

# multiply by two (see technical document for details)
# odd nfft excludes Nyquist point
if n % 2 > 0: # we've got odd number of points fft
    p[1:len(p)] = p[1:len(p)] * 2
else:
    p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft

freqArray = numpy.arange(0, nUniquePts, 1.0) * (sampFreq / n);
plt.plot(freqArray/1000, 10*numpy.log10(p), color='k')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Power (dB)')
plt.show()

rms_val = sqrt(mean(s1**2))
print(sqrt(sum(p)))
"""