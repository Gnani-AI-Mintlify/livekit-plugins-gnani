# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.2] - 2026-05-22

### Removed

- **`vachana-voice-v2` support** — all legacy v2 voices (`sia`, `raju`, `kanika`, `nikita`, `ravan`, `simran`, `karan`, `neha`) removed.
- **Language-specific v3 voices** — removed 320 language-specific voices.
- `LEGACY_V2_VOICES` and `V3_VOICES` sets removed.

### Changed

- `SUPPORTED_VOICES` now contains only 6 voices: `Karan`, `Simran`, `Nara`, `Riya`, `Viraj`, `Raju`.
- `GnaniTTSVoices` type narrowed to the 6 supported voices.
- TTS languages reduced to 10: Assamese, Bengali, English, Hindi, Kannada, Malayalam, Marathi, Odia, Tamil, Telugu.
- Minimum `gnani-vachana` dependency bumped to `>=0.3.1`.

## [0.3.0] - 2026-05-21

### Added

- **23 STT languages** — expanded from 10 to 23 languages including Assamese, Bodo, Dogri, Kashmiri, Konkani, Maithili, Manipuri, Nepali, Odia, Sanskrit, Santhali, Sindhi, and Urdu.

### Changed

- **Default TTS model** set to `vachana-voice-v3`.
- **Default TTS voice** changed from `"sia"` to `"Karan"`.
- **Default TTS language** changed from `"IND-IN"` to `"hi"` (ISO 639-1 code).
- Minimum `gnani-vachana` dependency bumped to `>=0.3.0`.

## [0.2.0] - 2026-05-13

### Changed

- Default TTS sample rate changed from 22050 to 16000 Hz for better compatibility with voice agent pipelines.
- Added sample rate validation in TTS constructor — raises `ValueError` if sample rate is not one of 8000, 16000, 22050, or 44100.
- Removed verbose debug logging from chunked TTS response handler.

## [0.1.0] - 2026-05-12

### Added

- **Speech-to-Text (STT)** — batch recognition via REST (`POST /stt/v3`) and real-time streaming via WebSocket (`wss://api.vachana.ai/stt/v3/stream`).
- **Text-to-Speech (TTS)** — chunked synthesis via REST (`POST /api/v1/tts/inference`) and real-time streaming via WebSocket (`wss://api.vachana.ai/api/v1/tts`).
- Support for 10 Indian languages: Bengali, English (India), Gujarati, Hindi, Kannada, Malayalam, Marathi, Punjabi, Tamil, Telugu.
- 8 voice options for TTS: sia, raju, kanika, nikita, ravan, simran, karan, neha.
- Configurable audio output: sample rate, encoding (linear_pcm, oggopus), container (raw, mp3, wav, mulaw, ogg).
- LiveKit Agents `Plugin.register_plugin()` integration for automatic discovery.
- Built on top of the [`gnani-vachana`](https://pypi.org/project/gnani-vachana/) core SDK.

[0.3.2]: https://github.com/Gnani-AI-Mintlify/livekit-plugins-gnani/releases/tag/v0.3.2
[0.3.0]: https://github.com/Gnani-AI-Mintlify/livekit-plugins-gnani/releases/tag/v0.3.0
[0.2.0]: https://github.com/Gnani-AI-Mintlify/livekit-plugins-gnani/releases/tag/v0.2.0
[0.1.0]: https://github.com/Gnani-AI-Mintlify/livekit-plugins-gnani/releases/tag/v0.1.0
