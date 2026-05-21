# livekit-plugins-gnani

[![PyPI](https://img.shields.io/pypi/v/livekit-plugins-gnani)](https://pypi.org/project/livekit-plugins-gnani/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

[LiveKit Agents](https://github.com/livekit/agents) plugin for **[Gnani Vachana](https://gnani.ai/)** — high-accuracy Speech-to-Text and low-latency Text-to-Speech for Indian languages.

> **Vachana** is a production-ready speech AI platform by [Gnani.ai](https://gnani.ai) supporting 22+ Indian languages with 250+ voices, real-time streaming, multilingual transcription, and code-switching capabilities.

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
- **250+ voices** — language-specific voices across 22 Indian languages (e.g. Karan, Simran, Riya, Aarav, Priya, and many more)
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

### TTS Languages (Text-to-Speech) — 22 languages

TTS uses ISO 639 language codes (e.g. `hi`, `bn`). Pass these via the `language` parameter.

| Language   | Code  | Sample Voices               |
|------------|-------|-----------------------------|
| Assamese   | `as`  | Priya, Arjun                |
| Bengali    | `bn`  | Ananya, Abhik               |
| Bodo       | `brx` | Anamika, Anil               |
| Dogri      | `doi` | Asha, Ajay                  |
| Gujarati   | `gu`  | Avani, Akshay               |
| Hindi      | `hi`  | Aarav, Deepak               |
| Kannada    | `kn`  | Anitha, Aditya              |
| Kashmiri   | `ks`  | Aafreen, Altaf              |
| Konkani    | `kok` | Alka, Agnelo                |
| Maithili   | `mai` | Archana, Amaresh            |
| Malayalam  | `ml`  | Ambika, Abhilash            |
| Manipuri   | `mni` | Achouba, Dinamani           |
| Marathi    | `mr`  | Aparna, Amol                |
| Nepali     | `ne`  | Anita, Amar                 |
| Odia       | `or`  | Anuradha, Asutosh           |
| Punjabi    | `pa`  | Amandeep, Amarjit           |
| Sanskrit   | `sa`  | Akshara, Achyut             |
| Santhali   | `sat` | Arjun_S, Birsa              |
| Sindhi     | `sd`  | Ameena, Bhagwanti           |
| Tamil      | `ta`  | Abinaya, Anbarasan          |
| Telugu     | `te`  | Alekhya, Adithya            |
| Urdu       | `ur`  | Aiza, Asad                  |

## Available Voices (Sample)

The TTS API supports 250+ voices across all supported languages. Here are some primary voices:

| Voice   | ID        | Language    |
|---------|-----------|-------------|
| Karan   | `Karan`   | Primary     |
| Simran  | `Simran`  | Primary     |
| Nara    | `Nara`    | Primary     |
| Riya    | `Riya`    | Primary     |
| Viraj   | `Viraj`   | Primary     |
| Raju    | `Raju`    | Primary     |
| Aarav   | `Aarav`   | Hindi       |
| Priya   | `Priya`   | Assamese    |
| Ananya  | `Ananya`  | Bengali     |
| Avani   | `Avani`   | Gujarati    |
| Anitha  | `Anitha`  | Kannada     |
| Ambika  | `Ambika`  | Malayalam   |
| Aparna  | `Aparna`  | Marathi     |
| Abinaya | `Abinaya` | Tamil       |
| Alekhya | `Alekhya` | Telugu      |
| Aiza    | `Aiza`    | Urdu        |

Each language has 8–16 dedicated voices (male and female). Use `SUPPORTED_VOICES` from the package for the full list.

### Legacy v2 Voices

The following lowercase voices from `vachana-voice-v2` are still supported for backward compatibility:

| Voice   | ID        | Model           |
|---------|-----------|-----------------|
| Sia     | `sia`     | vachana-voice-v2 |
| Raju    | `raju`    | vachana-voice-v2 |
| Kanika  | `kanika`  | vachana-voice-v2 |
| Nikita  | `nikita`  | vachana-voice-v2 |
| Ravan   | `ravan`   | vachana-voice-v2 |
| Simran  | `simran`  | vachana-voice-v2 |
| Karan   | `karan`   | vachana-voice-v2 |
| Neha    | `neha`    | vachana-voice-v2 |

> **Note:** Casing matters! `"karan"` (lowercase) uses the old v2 model, while `"Karan"` (capitalized) uses the new v3 model.

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
