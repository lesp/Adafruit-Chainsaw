import audioio
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
# enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True
# make the input trigger
trigger = DigitalInOut(board.A1)
trigger.direction = Direction.INPUT
trigger.pull = Pull.DOWN
#Create a function to play audio files.
def play_file(filename):
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with audioio.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            audio.play(wave)
            while audio.playing:
                pass
    print("Finished")
#Main Loop, press a button...make noise!
while True:
    if trigger.value:
        play_file("sound.wav")