# Fretboard Drills

The basics page of the guitar practice app (see `../README.md`). It has finger exercises for scales and chords that also teach where every note is, plus licks that put the drills to work. Its companions are the [Pentatonic Box Map](../pentatonicBoxMap/) and [Tuner & Metronome](../practiceTools/). Every page links to the others in its top bar.

## Tabs

| Tab | Exercises |
|---|---|
| Daily plan | A 10/20/30-minute session of five timed blocks (warm-up, scale, chord changes, note quiz, lick) that moves you to each drill in turn; day streak, 14-day calendar, best clean tempos |
| Warm-ups | Spider 1-2-3-4 (six finger orders, string skipping, climbing); finger pairs |
| Scales | Two-octave major scale and minor pentatonic Box 1, played straight, in 3s, in 4s or in thirds, in any key |
| Chords | Chord changes with a next-chord outline, a "what moves" analysis and one-minute changes; 12-bar blues in A, E or G (with optional quick change); CAGED shapes |
| Fretboard memory | Natural notes on one string; find every note (string by string or in octave pairs); note quiz (name it or find it) |
| Licks | 11 licks from easiest to hardest: blues, legato, rock, double stops, major pentatonic and a Box 1 → Box 2 slide. Each can be played in any key, has a tab view with techniques (hammer-on, pull-off, slide, bends, release, vibrato), can be practised in halves, and links to the drills it builds on |

## Player

Tempo 40–200 BPM with a count-in, metronome click, plucked-note sound (bends, slides and vibrato are simulated), loop, notes per click, and **Call it first**, which hides each note name for half a beat so you say it before it appears. The **Speed trainer** adds 2 or 5 BPM per loop. **Log clean run** saves your best tempo for the current drill and version; the Daily plan lists them.

Keyboard: `Space` play/stop (or count a change while the one-minute timer runs), `←` `→` step, `A`–`G` answer in the note quiz.

## Editing

`index.html` here is generated. Edit `../_src/fretboard-drills.html` and run `python3 ../_src/build.py`.
