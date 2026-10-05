# Binaural Loom

**Schumann-tuned binaural beat generator. Browser-based. No install. No accounts.**

[Open the live tool →](https://binaural-loom.vercel.app)

Built by Ontos Labs. Phase coherence as music.

---

## What it does

Generates binaural beats — two slightly-detuned sine tones, one in each ear, that the auditory cortex integrates into a perceived "third tone" pulsing at the difference frequency. Six brainwave-band presets including the **Schumann resonance at 7.83 Hz** because of course. Optional perfect-fifth drone for harmonic richness, optional pink noise bed for masking, live Lissajous + mandala visualizer that pulses on the beat.

Export any settings as a 16-bit / 44.1 kHz stereo WAV up to one hour long. Drops straight into FL Studio, Ableton, Logic, Reaper, Audition, or any audio editor.

## Three modes (v0.2)

- **Binaural** — one tone per ear, carrier ∓ Δ/2. The beat is not in the signal; your brainstem computes it from the interaural phase difference. Headphones required. Fusion fails above ~30 Hz, so the Gamma preset warns you.
- **Monaural** — both tones in both ears. The beat is a real amplitude envelope in the signal, demodulated by the cochlea. Works on speakers and phones, and collapses to mono without losing anything.
- **Isochronic** — a single tone at the carrier, amplitude-gated at Δ (sine gate, 100% depth). Also works on speakers. This is the classic stimulus for the auditory steady-state response; 40 Hz is honest here.

Exported filenames carry the mode: `monaural_200Hz_7p83Hz_60s.wav`.

## Presets

- **7.83 Hz Schumann** — Earth's electromagnetic cavity resonance
- 2.0 Hz Delta — sleep
- 6.0 Hz Theta — trance
- 10.0 Hz Alpha — calm
- 20.0 Hz Beta — focus
- 40.0 Hz Gamma — insight

## How to use

1. Pick a mode. Binaural needs headphones; Monaural and Isochronic work on anything
2. Pick a preset or dial your own carrier and beat frequencies
3. Hit Play, listen for the phantom pulsing tone
4. Optional: set duration, hit Export, drop the WAV anywhere you like

## Notes on the science (and the woo)

Binaural beats are an established acoustic phenomenon. Whether they "decalcify your pineal gland," "open your third eye," or "synchronize you with the cosmic substrate" is a matter of personal taste, and we encourage you to form your own opinions. The tool generates exactly what it says on the tin.

## Stack

Pure HTML + Web Audio API + Canvas 2D. Single file. No build step. No backend. No telemetry.

## License

MIT. Take it. Fork it. Remix it. Stick it in your meditation app. No permission required.

---

*Phase coherence as music. v0.2.*
