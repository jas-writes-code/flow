import pygame
import pyaudio
import random
import time
import math
import os
import json

pygame.mixer.init()
pygame.mixer.music.load("our music.mp3")
pygame.mixer.music.play

clock = pygame.time.Clock()


def detect_beat():
    raw_audio = pygame.mixer.music.get_raw()
    audio_array = np.frombuffer(raw_audi, dtype.int16)
    fft_data = np.fft.fft(audio_array)
    freq_bins = np.fft.fftfreq(len(fft_data))
    bass_index = np.where((freq_bins >= 20) & (freq_bins <= 200))[0]
    bass_amplitude = np.sum(np.abs(fft_data[bass_index]))
    scaled_amplitude = int(bass_amplitude / (len(bass_index) * 10000) * 255)
    return min(max(scaled_amplitude, 0), 255)


running = true
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

screeb.fill(0,0,0)

beat_value = detect_beat()

font = pygame.font.SysFont(None, 36)
text = font.render("Beat Value: " + str(beat_value), True, (255, 255, 255))
screen.blit(text, (10, 10))

pygame.display.flip()
clock.tick(30)





    





