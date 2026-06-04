# livekit-plugins-gnani

[![PyPI](https://img.shields.io/pypi/v/livekit-plugins-gnani)](https://pypi.org/project/livekit-plugins-gnani/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

[LiveKit Agents](https://github.com/livekit/agents) plugin for **[Gnani Vachana](https://gnani.ai/)** — high-accuracy Speech-to-Text and low-latency Text-to-Speech for Indian languages.

> **Vachana** is a production-ready speech AI platform by [Gnani.ai](https://gnani.ai) supporting 10+ Indian languages with 6 voices, real-time streaming, multilingual transcription, and code-switching capabilities.

## Installation

```bash
pip install livekit-plugins-gnani
```

This will also install the [`gnani-vachana`](https://pypi.org/project/gnani-vachana/) core SDK as a dependency.

## Prerequisites

You need a Gnani API key. Email **[speechstack@gnani.ai](mailto:speechstack@gnani.ai)** to get started — all new accounts receive free credits, no credit card required.

### Authentication

All APIs require a single API key — no `organization_id` or `user_id` needed.

**Option 1 — Environment variable (recommended):**

```bash
export GNANI_API_KEY="your-api-key"
```

**Option 2 — Constructor argument:**

```python
stt = STT(api_key="your-api-key", language="hi-IN")
tts = TTS(api_key="your-api-key", voice="Karan")
```

## Quick Start

### Speech-to-Text

```python
from livekit.plugins.gnani import STT

stt = STT(language="hi-IN")

# Use with a LiveKit voice agent pipeline
```

### Text-to-Speech

```python
from livekit.plugins.gnani import TTS

# REST (default) — single-request batch synthesis
tts = TTS(voice="Karan")

# SSE — streaming via Server-Sent Events (lower latency)
tts = TTS(voice="Karan", synthesize_method="sse")

# WebSocket — real-time streaming via stream() (lowest latency)
tts = TTS(voice="Karan", synthesize_method="websocket")
```

All three modes work with the standard LiveKit voice agent pipeline.
The `synthesize_method` controls which transport `synthesize()` uses
(REST, SSE, or WebSocket). The `stream()` method always uses WebSocket
regardless of this setting.

## Features

### STT

- **Batch recognition** — REST API (`POST /stt/v3`) for file-based transcription
- **Real-time streaming** — WebSocket API for live audio transcription with VAD
- **10+ Indian languages** — see [supported language codes](https://docs.inya.ai/vachana/STT/stt-websocket#supported-languages)
- **Code-switching** — supports multilingual and code-mixed audio
- **Sample rates** — 8 kHz and 16 kHz

### TTS

- **REST synthesis** — single-request batch audio generation (`synthesize_method="rest"`)
- **SSE streaming** — lower-latency chunked synthesis via Server-Sent Events (`synthesize_method="sse"`)
- **WebSocket synthesis** — lowest-latency synthesis via `synthesize_method="websocket"` or the `stream()` method
- **6 voices** — Karan, Simran, Nara, Riya, Viraj, Raju
- **Model** — `vachana-voice-v3` with voice cloning support
- **Configurable output** — sample rate (8000–44100), encoding (linear_pcm, oggopus), container (raw, mp3, wav, mulaw, ogg)

## Supported Languages

### STT Languages (Speech-to-Text)

STT uses BCP-47 locale codes (e.g. `hi-IN`). For the full list of supported languages, see:

- **[STT REST — Supported Languages](https://docs.inya.ai/vachana/STT/speech-to-text#supported-languages)**
- **[STT Realtime — Supported Languages](https://docs.inya.ai/vachana/STT/stt-websocket#supported-languages)**

---

### TTS Languages (Text-to-Speech)

TTS uses ISO 639 language codes (e.g. `hi`, `bn`). Pass these via the `language` parameter.

For the full list of supported languages, see **[TTS — Supported Languages](https://docs.inya.ai/vachana/TTS/tts-inference#supported-languages)**.

## Available Voices

| Voice   | ID        | Gender | Description              |
|---------|-----------|--------|--------------------------|
| Karan   | `Karan`   | Male   | Bold, Trustworthy        |
| Simran  | `Simran`  | Female | Confident, Bright        |
| Nara    | `Nara`    | Female | Gentle, Expressive       |
| Riya    | `Riya`    | Female | Cheerful, Energetic      |
| Viraj   | `Viraj`   | Male   | Commanding, Dynamic      |
| Raju    | `Raju`    | Male   | Grounded, Conversational |

## Architecture

```
gnani-vachana (>=0.4.3)   <- Core SDK (REST, WebSocket, SSE clients; single api_key auth)
    |
livekit-plugins-gnani     <- This package (LiveKit Agents adapter)
```

This plugin is a thin adapter that wraps the `gnani-vachana` SDK into LiveKit's `stt.STT` and `tts.TTS` base classes. Voice lists, language constants, and model definitions are shared with the core SDK. Authentication uses a single `api_key` passed via the `X-API-Key-ID` header.

## Documentation

- [Vachana API Docs](https://docs.inya.ai/vachana/introduction/introduction)
- [LiveKit Agents Docs](https://docs.livekit.io/agents/)
- [gnani-vachana SDK](https://pypi.org/project/gnani-vachana/)

## License

Apache 2.0 — see [LICENSE](LICENSE).
