C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREC = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88

name = input("Введите ноту и октаву, например С4: ")
note = name[0]
octave = int(name[1])

if note == 'С':
    result = C4_FREQ
elif note == 'D':
    result = D4_FREQ
elif note == 'E':
    result = E4_FREC
elif note == 'F':
    result = F4_FREQ
elif note == 'G':
    result = G4_FREQ
elif note == 'A':
    result = A4_FREQ
else:
    result = B4_FREQ

freq = result / 2 ** (4 - octave)

print(f"Чатота ноты {name} равна {freq}")
