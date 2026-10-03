from playsound import playsound
import threading

def play_music():
    threading.Thread(target=playsound, args=("8bit.mp3",), daemon=True).start()


play_music()