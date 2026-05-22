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

Set your credentials as environment variables:

```bash
export GNANI_API_KEY="your-api-key"

# For REST STT only (optional):
export GNANI_ORGANIZATION_ID="your-org-id"
export GNANI_USER_ID="your-user-id"
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

tts = TTS(voice="Karan")

# Use with a LiveKit voice agent pipeline
```

## Features

### STT

- **Batch recognition** — REST API (`POST /stt/v3`) for file-based transcription
- **Real-time streaming** — WebSocket API for live audio transcription with VAD
- **23 Indian languages** — Assamese, Bengali, Bodo, Dogri, English (India), Gujarati, Hindi, Kannada, Kashmiri, Konkani, Maithili, Malayalam, Manipuri, Marathi, Nepali, Odia, Punjabi, Sanskrit, Santhali, Sindhi, Tamil, Telugu, Urdu
- **Code-switching** — Hinglish (en-hi-IN-latn) and Hindi-English mixed (en-hi-in-cm) for streaming
- **Sample rates** — 8 kHz and 16 kHz

### TTS

- **Chunked synthesis** — REST API for single-request audio generation
- **Real-time streaming** — WebSocket API for low-latency streaming synthesis
- **6 voices** — Karan, Simran, Nara, Riya, Viraj, Raju
- **Model** — `vachana-voice-v3` with voice cloning support
- **Configurable output** — sample rate (8000–44100), encoding (linear_pcm, oggopus), container (raw, mp3, wav, mulaw, ogg)

## Supported Languages

### STT Languages (Speech-to-Text) — 10 languages

STT uses BCP-47 locale codes (e.g. `hi-IN`):

| Language        | Code      |
|-----------------|-----------|
| English (India) | `en-IN`   |
| Hindi           | `hi-IN`   |
| Gujarati        | `gu-IN`   |
| Tamil           | `ta-IN`   |
| Kannada         | `kn-IN`   |
| Telugu          | `te-IN`   |
| Marathi         | `mr-IN`   |
| Bengali         | `bn-IN`   |
| Malayalam       | `ml-IN`   |
| Punjabi         | `pa-IN`   |

Plus streaming-only experimental: `en-hi-IN-latn` (Hinglish), `en-hi-in-cm` (code-mixed).

---

### TTS Languages (Text-to-Speech) — 10 languages

TTS uses ISO 639 language codes (e.g. `hi`, `bn`). Pass these via the `language` parameter.

| Language   | Code  |
|------------|-------|
| Assamese   | `as`  |
| Bengali    | `bn`  |
| English    | `en`  |
| Hindi      | `hi`  |
| Kannada    | `kn`  |
| Malayalam  | `ml`  |
| Marathi    | `mr`  |
| Odia       | `or`  |
| Tamil      | `ta`  |
| Telugu     | `te`  |

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
gnani-vachana (>=0.3.0)   ← Core SDK (REST, WebSocket, SSE clients, voice/language constants)
    ↑
livekit-plugins-gnani     ← This package (LiveKit Agents adapter)
```

This plugin is a thin adapter that wraps the `gnani-vachana` SDK into LiveKit's `stt.STT` and `tts.TTS` base classes. Voice lists, language constants, and model definitions are shared with the core SDK.

## Documentation

- [Vachana API Docs](https://docs.inya.ai/vachana/introduction/introduction)
- [LiveKit Agents Docs](https://docs.livekit.io/agents/)
- [gnani-vachana SDK](https://pypi.org/project/gnani-vachana/)

## License

Apache 2.0 — see [LICENSE](LICENSE).
