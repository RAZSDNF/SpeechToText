import speech_recognition as sr

#print(sr.Microphone.list_microphone_names())
import pyaudio
#pa = pyaudio.PyAudio()
#chosen_device_index = -1
#for x in range(0,pa.get_device_count()):
#    info = pa.get_device_info_by_index(x)
#    print (pa.get_device_info_by_index(x))
#    if info["name"] == "pulse":
#        chosen_device_index = info["index"]
#        print ("Chosen index: ", chosen_device_index)

#p = pyaudio.PyAudio()
#stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input_device_index=chosen_device_index, input=True, output=False)
#stream.start_stream()
#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# enter the name of usb microphone that you found
# using lsusb
# the following name is only used as an example
mic_name = sr.Microphone.list_microphone_names()[8]
# Sample rate is how often values are recorded
sample_rate = 24000
# Chunk is like a buffer. It stores 2048 samples (bytes of data)
# here.
# it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
# Initialize the recognizer
r = sr.Recognizer()

# generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()

# the following loop aims to set the device ID of the mic that
# we specifically want to use to avoid ambiguity.
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i


    # use the microphone as source for input. Here, we also specify
# which device ID to specifically look for incase the microphone
# is not working, an error will pop up saying "device_id undefined"
with sr.Microphone(device_index=device_id, sample_rate=sample_rate,
                   chunk_size=chunk_size) as source:
    # wait for a second to let the recognizer adjust the
    # energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source)
    print ("Say Something")
    # listens for the user's input
    audio = r.listen(source,timeout=15)

    try:
        text = r.recognize_google(audio)
        print("you said: " + text)

        # error occurs when google could not understand what was said

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service;{0}".format(e))