# guitarTutor

An offline guitar practice app in a single HTML file. It has finger drills, scales, chords, licks, a fretboard note quiz, the five pentatonic boxes, a tuner and a metronome.

## Use

**Online:** https://y-v-j.github.io/guitarTutor/

**Offline:** download or clone the repository and open **`index.html`** in a modern browser (Firefox, Chrome, Edge or Safari). There is nothing to install and no build step, and it needs no internet connection. Everything, fonts included, is inside that one file, so it also works from a USB stick and in sandboxed browsers (Flatpak, Snap) that only get access to the file you open.

## What's inside

Three pages, switched with the bar at the top. A page stays loaded once opened, so a running metronome keeps going while you look at the drills.

| Page | What it's for |
|---|---|
| **Fretboard Drills** | The main page. Tabs: Daily plan, Warm-ups, Scales, Chords, Fretboard memory and Licks |
| **Pentatonic Box Map** | The five pentatonic box shapes in any key (minor, major and blues), with memory hooks for learning them |
| **Tuner & Metronome** | Standard-tuning tuner (reference tones plus a microphone needle) and a metronome |

### Fretboard Drills

- **Daily plan:** a 10, 20 or 30-minute session of five timed blocks (warm-up, scale, chord changes, note quiz, lick) that moves you through the drills. Shows your day streak, a 14-day calendar and your best clean tempos.
- **Warm-ups:** Spider 1-2-3-4 in six finger orders, with string skipping and position shifts; finger-pair trills.
- **Scales:** two-octave major scale and minor pentatonic Box 1, played straight, in groups of 3 or 4, or in thirds, in any key.
- **Chords:** chord changes with a next-chord outline, a "what moves" breakdown and a one-minute changes timer; the 12-bar blues in A, E or G; CAGED shapes.
- **Fretboard memory:** natural notes on one string, finding every instance of a note (string by string or in octave pairs), and a note quiz (name it or find it).
- **Licks:** 11 licks from easiest to hardest (blues, legato, rock, double stops, major pentatonic and a slide from Box 1 into Box 2). Each one can be played in any key and comes with tab notation and simulated bends, slides, hammer-ons, pull-offs and vibrato. You can practise a lick in halves, and each one links to the drills it builds on.

The player has a tempo from 40 to 200 BPM, a count-in, a metronome click, a plucked-string sound, looping, and **Call it first**, which hides each note name for half a beat so you say it before it appears. A **speed trainer** raises the tempo each loop, and **Log clean run** records your best tempo for each drill.

### Tuner & Metronome

- **Tuner:** reference tones for E A D G B E (hold a tone to tune by ear), a microphone pitch detector with a ±50-cent needle, and a reference pitch adjustable from A4 = 432 to 446 Hz.
- **Metronome:** 30–250 BPM with tempo markings and tap tempo, 1–7 beats per bar, subdivisions (8ths, triplets, 16ths, shuffle), an accented first beat, three sounds and a speed trainer.

### Keyboard

| Page | Keys |
|---|---|
| Drills | `Space` play/stop, `←` `→` step, `A`–`G` answer in the note quiz |
| Box Map | `←` `→` step through the boxes |
| Tuner & Metronome | `Space` start/stop the metronome, `T` tap tempo, `↑` `↓` change tempo |

## Privacy

Everything runs in your browser. Settings and practice history are kept in the browser's local storage, and nothing is sent anywhere. The microphone is only used after you press **Start listening**, and the audio never leaves the page.

## Project layout

```
index.html            the app (generated, opens on Fretboard Drills)
fretboardDrills/      the same app, plus notes on the drills
pentatonicBoxMap/     the same app opening on the Box Map
practiceTools/        the same app opening on the Tuner & Metronome
_src/                 page sources, fonts and the build script
```

## Building

The `index.html` files are generated. To change the app, edit the page sources in `_src/` and run:

```
python3 _src/build.py
```

The build needs only Python 3's standard library. It embeds the three pages and the fonts into each `index.html`, and stops with an error if an offline page contains any web address.

## License

The code is under the MIT license (see `LICENSE`). The bundled fonts are under the SIL Open Font License 1.1; see `_src/fonts/OFL-*.txt`:

- Big Shoulders Display, © The Big Shoulders Project Authors
- Figtree, © The Figtree Project Authors
- IBM Plex Mono, © IBM Corp., Reserved Font Name "Plex"
