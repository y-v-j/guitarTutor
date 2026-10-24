# Tuner & Metronome

Part of the guitar practice app (see `../README.md`). Works offline.

## Tuner

- Standard tuning, E2 A2 D3 G3 B3 E4. Each string button plays a reference tone; **Hold the tone** keeps it sounding until you tap the string again.
- **Start listening** uses the microphone. A YIN pitch detector picks the nearest string and shows a needle from 50 cents flat to 50 cents sharp; within ±5 cents counts as in tune. The browser asks for permission the first time.
- Reference pitch is adjustable from A4 = 432 to 446 Hz.

## Metronome

30–250 BPM with tempo markings, ±1/±5 buttons, tap tempo, 1–7 beats per bar, subdivisions (8ths, triplets, 16ths, shuffle), accent on beat 1, three sounds (click, wood, beep), volume, and a speed trainer (+2 BPM every 4 bars or +5 every 8 bars).

Keyboard: `Space` start/stop, `T` tap, `↑` `↓` ±1 BPM.

## Editing

`index.html` here is generated. Edit `../_src/practice-tools.html` and run `python3 ../_src/build.py`.
