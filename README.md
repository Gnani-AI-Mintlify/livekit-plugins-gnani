# livekit-plugins-gnani

[![PyPI](https://img.shields.io/pypi/v/livekit-plugins-gnani)](https://pypi.org/project/livekit-plugins-gnani/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

[LiveKit Agents](https://github.com/livekit/agents) plugin for **[Gnani](https://gnani.ai/)** — high-accuracy Speech-to-Text (Prisma) and low-latency Text-to-Speech (Timbre) for Indian languages.

>[Gnani.ai](https://gnani.ai) is a production-ready speech AI featuring **Prisma** (STT) and **Timbre** (TTS) models, supporting 10+ Indian languages with 6 voices, real-time streaming, and multilingual transcription.

## Installation

```bash
pip install livekit-plugins-gnani
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add livekit-plugins-gnani
```

This will also install the [`gnani`](https://pypi.org/project/gnani/) core SDK as a dependency.

## Prerequisites

You need a Gnani API key. [Gnani APIs](https://app.gnani.ai/voice) have this.

### Authentication

All APIs require a single API key — no `organization_id` or `user_id` needed.

Set your credentials as environment variables:

```bash
export GNANI_API_KEY="your-api-key"
```

**Or pass the key in the constructor:**

```python
stt = STT(api_key="your-api-key", language="hi-IN")
tts = TTS(api_key="your-api-key")
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
tts = TTS(voice="Pranav")

# SSE — streaming via Server-Sent Events (lower latency)
tts = TTS(voice="Pranav", synthesize_method="sse")

# WebSocket — real-time streaming via stream() (lowest latency)
tts = TTS(voice="Pranav", synthesize_method="websocket")
```

All three modes work with the standard LiveKit voice agent pipeline.
The `synthesize_method` controls which transport `synthesize()` uses
(REST, SSE, or WebSocket). The `stream()` method always uses WebSocket
regardless of this setting.

## Features

### STT (Prisma)

- **REST recognition** — REST API (`POST /stt/v3`) for file-based transcription
- **Real-time streaming** — WebSocket API (`wss://api.vachana.ai/stt/v3/stream`) for live audio transcription with VAD
- **10+ Indian languages** — see [supported language codes](https://docs.gnani.ai/api/STT/stt-websocket#supported-languages)
- **Sample rates** — 8 kHz and 16 kHz
- **ITN support** — set `format="transcribe"` to enable Inverse Text Normalization; use `itn_native_numerals=True` for native-script digits. Both parameters are forwarded over WebSocket via `x-format` and `itn_native_numerals` connection headers.

#### Streaming PCM Specification

All streaming audio must be sent as **raw PCM binary frames** — no container format (WAV, MP3) mid-stream.

| Property          | 16 kHz                                    | 8 kHz                                     |
|-------------------|-------------------------------------------|-------------------------------------------|
| Encoding          | PCM signed 16-bit little-endian           | PCM signed 16-bit little-endian           |
| Sample Rate       | 16,000 Hz                                 | 8,000 Hz                                  |
| Channels          | 1 (mono)                                  | 1 (mono)                                  |
| Samples per chunk | 512                                       | 512                                       |
| **Bytes per frame** | **1,024 bytes** (512 samples × 2 bytes) | **1,024 bytes** (512 samples × 2 bytes)   |
| Frame duration    | 32 ms                                     | 64 ms                                     |

Frames must be sent at **real-time cadence**. See **[STT Realtime — PCM Specification](https://docs.gnani.ai/api/STT/stt-websocket#pcm-specification)** for full details.

### TTS (Timbre)

- **REST synthesis** — single-request batch audio generation (`synthesize_method="rest"`)
- **SSE streaming** — lower-latency chunked synthesis via Server-Sent Events (`synthesize_method="sse"`)
- **WebSocket synthesis** — lowest-latency synthesis via `synthesize_method="websocket"` or the `stream()` method
- **4 voices** — Pranav, Kaveri, Shubhra, Deepak (see [Available Voices](https://docs.gnani.ai/api/TTS/tts-sse#available-voices))
- **Model** — Timbre (`vachana-voice-v3`) with voice cloning support
- **Configurable output** — sample rate (8000–44100), encoding (linear_pcm, oggopus), container (raw, mp3, wav, mulaw, ogg)

## Supported Languages

### STT Languages (Prisma)

Prisma uses BCP-47 locale codes (e.g. `hi-IN`). For the full list of supported languages, see:

- **[STT REST — Supported Languages](https://docs.gnani.ai/api/STT/speech-to-text#supported-languages)**
- **[STT Realtime — Supported Languages](https://docs.gnani.ai/api/STT/stt-websocket#supported-languages)**

---

### TTS Languages (Timbre)


For the full list of supported languages, see **[TTS — Supported Languages](https://docs.gnani.ai/api/TTS/tts-inference#supported-languages)**.

## Available Voices

See the [official voice list](https://docs.gnani.ai/api/TTS/tts-sse#available-voices) for the latest supported voices.

| Voice   | ID        | Gender | Description              |
|---------|-----------|--------|--------------------------|
| Pranav  | `Pranav`  | Male   | Bold, Trustworthy        |
| Kaveri  | `Kaveri`  | Female | Confident, Bright        |
| Shubhra | `Shubhra` | Female | Gentle, Expressive       |
| Deepak  | `Deepak`  | Male   | Grounded, Conversational |

## Architecture

```
gnani (>=0.6.0)           <- Core SDK (REST, WebSocket, SSE clients; single api_key auth)
    |
livekit-plugins-gnani     <- This package (LiveKit Agents adapter)
```

This plugin is a thin adapter that wraps the `gnani` SDK into LiveKit's `stt.STT` and `tts.TTS` base classes. It uses the **Prisma** model for speech-to-text and the **Timbre** model for text-to-speech. Voice lists, language constants, and model definitions are shared with the core SDK. Authentication uses a single `api_key` passed via the `X-API-Key-ID` header.

## Documentation

- [Gnani API Docs](https://docs.gnani.ai/)
- [LiveKit Agents Docs](https://docs.livekit.io/agents/)
- [gnani SDK](https://pypi.org/project/gnani/)

## License

Apache 2.0 — see [LICENSE](LICENSE).
