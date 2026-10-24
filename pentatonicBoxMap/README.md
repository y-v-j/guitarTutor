# Pentatonic Box Map

An interactive guitar fretboard (standard tuning, frets 0–22) for learning the five pentatonic box shapes in any key.

Part of the guitar practice app (see `../README.md`) with [Fretboard Drills](../fretboardDrills/) (the basics page) and [Tuner & Metronome](../practiceTools/). Every page links to the others in its top bar, and it all works offline.

- Scales: minor pentatonic, major pentatonic, blues (minor pentatonic + ♭5)
- Pick a key, step through Box 1–5 (or show all), label dots with note names or scale degrees
- Memory hooks that update with the selected box: index/pinky rule, stretch pattern, BEADG wide pair, leapfrog frets, blue-note positions
- Play a box up and down, or click any dot to hear it (synthesized pluck)

## Use

Open `index.html` in a browser. It's a single file with no build step.
Fonts come from Google Fonts; offline it falls back to system fonts. Your last key, scale and box are remembered in the browser.

Keyboard: `←` `→` step through the boxes.

Box numbers follow the minor-pentatonic shapes: Box 1 always has the minor root under the index finger on the low E string.

## Status

Demo (2026-10-25). Ideas for the full version:

- Fingering numbers inside each box
- Tempo control for playback
- Quiz mode (name the box, find the root)
- Connecting boxes along a single string

## Editing

`index.html` here is generated. Edit `../_src/pentatonic-box-map.html` and run `python3 ../_src/build.py`.
