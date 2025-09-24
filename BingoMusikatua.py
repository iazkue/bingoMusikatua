# Iepaa, hau irakurtzebazu poztenaiz kodigo hau zabaldu izanataz, jakin hasiera batian @iazkue-k sortutakua dala, gestión de proyectos informaticos klasian asper-asper inda
# GOGORATU, BEHARREZKUA lenuo liburutegi hau ejekutatzia: 
    # sudo pip install keyboard
    # sudo pip installl pygame
    # sudo XDG_RUNTIME_DIR=/run/user/$(id -u)      PULSE_RUNTIME_PATH=/run/user/$(id -u)/pulse      python3 BingoMusikatua.py
# Bolumen minimoa, aldakaera edo bestelakuak aldatu nahi izanezkeo hementxe behian dakazu errex aldatzeko mouan







import pygame
import os
import threading
import time
import sys

pygame.init()
pygame.mixer.init()


#BOLUMENA ALDATZEKO, aldatu zenbakiak beldurrik gabe
#Ulertzeko: Bolumena 0.0-> Isilik, Bolumena 1.0-> Topea

VOLUME_STEP = 0.05  # Pultsazioko, bolumena zenbat aldatzean
VOLUME_MIN = 0.0 # Bolumen minimua
VOLUME_MAX = 1.0 # Bolumen maximua

current_volume = VOLUME_MAX
pygame.mixer.music.set_volume(current_volume)

def play_song(song_number):
    global current_volume
    filename = f"{song_number:02}.mp3"
    if not os.path.isfile(filename):
        print(f"Archivo '{filename}' EZ DA EXISTITZEN.")
        return
    pygame.mixer.music.stop()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(VOLUME_MAX)
    current_volume = VOLUME_MAX
    pygame.mixer.music.play()
    print(f"KANTA ERREPRODUZITZEN: {filename}")

def adjust_volume(direction):
    global current_volume
    if direction == "up":
        current_volume = min(VOLUME_MAX, current_volume + VOLUME_STEP)
    elif direction == "down":
        current_volume = max(VOLUME_MIN, current_volume - VOLUME_STEP)
    pygame.mixer.music.set_volume(current_volume)
    print(f"Vol: {int(current_volume*100)}%\n")

def listen_keys():
    import keyboard  
    while True:
        if keyboard.is_pressed('up'):
            adjust_volume("up")
            time.sleep(0.15)
        elif keyboard.is_pressed('down'):
            adjust_volume("down")
            time.sleep(0.15)
        time.sleep(0.05)

def main():
    # Lanzar el hilo para escuchar las teclas
    threading.Thread(target=listen_keys, daemon=True).start()
    print("Abestiaren bi zenbakiak idazi (adib: 03, 43)")
    while True:
        user_input = input("Zenbakia: ").strip()
        if len(user_input) == 2 and user_input.isdigit():
            play_song(int(user_input))
        else:
            print("Abestiaren bi zenbakiak idazi (adib: 03, 43)")

if __name__ == "__main__":
    main()
