# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-05-12

### Added

- **Speech-to-Text (STT)** — batch recognition via REST (`POST /stt/v3`) and real-time streaming via WebSocket (`wss://api.vachana.ai/stt/v3/stream`).
- **Text-to-Speech (TTS)** — chunked synthesis via REST (`POST /api/v1/tts/inference`) and real-time streaming via WebSocket (`wss://api.vachana.ai/api/v1/tts`).
- Support for 10 Indian languages: Bengali, English (India), Gujarati, Hindi, Kannada, Malayalam, Marathi, Punjabi, Tamil, Telugu.
- 8 voice options for TTS: sia, raju, kanika, nikita, ravan, simran, karan, neha.
- Configurable audio output: sample rate, encoding (linear_pcm, oggopus), container (raw, mp3, wav, mulaw, ogg).
- LiveKit Agents `Plugin.register_plugin()` integration for automatic discovery.
- Built on top of the [`gnani-vachana`](https://pypi.org/project/gnani-vachana/) core SDK.

[0.1.0]: https://github.com/Gnani-AI-Mintlify/livekit-plugins-gnani/releases/tag/v0.1.0
