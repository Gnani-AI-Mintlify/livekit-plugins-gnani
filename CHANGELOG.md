# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- **Bumped `gnani-vachana` dependency to `>=0.7.3,<1.0`** (from `>=0.7.1`), picking up the `uv`-based dev workflow and TTS type-casting fixes in the core SDK.
- **`websockets` lower bound relaxed to `>=12.0`** to align with the core SDK and support environments that pin `websockets < 13`.
- **WebSocket header compatibility** — STT and TTS WebSocket connections use `_ws_header_kwargs()` so `additional_headers` (websockets >= 13) and `extra_headers` (< 13) are selected automatically, matching `gnani-vachana` 0.7.2+.
- **STT streaming sample rates** — `STT` now accepts `44100` and `48000` Hz in addition to `8000` and `16000`, matching the documented `x-sample-rate` values.
- **STT REST language auto-detection** — `STT` now accepts any comma-separated combination of supported single language codes (e.g. `"en-IN,ta-IN"`) to enable server-side auto-detection.
- **STT streaming languages** — added experimental Hinglish codes `en-hi-IN-latn` and `en-hi-in-cm` to `STREAM_SUPPORTED_LANGUAGES`.
- **Local development uses [uv](https://docs.astral.sh/uv/)** — `scripts/setup.sh` creates `.venv` with `uv venv` and installs via `uv sync --extra dev`. `Makefile`, `release.sh`, and CI workflows use `uv run`. `uv.lock` is generated locally for reproducible installs.
- **Bumped `gnani` SDK dependency to `>=0.7.1,<1.0`** (from `>=0.6.0,<1.0`), picking up the `websockets` 12.x compatibility fix and the additional STT streaming sample rates (44100, 48000 Hz).
- **PyPI publish** — the publish workflow now also triggers on `v*.*.*` tag pushes (and `workflow_dispatch`), validates that the tag matches the `pyproject.toml` version, and runs `twine check` on the built distribution before uploading.

### Added

- **CI workflow** — GitHub Actions `CI` workflow (`.github/workflows/ci.yml`) runs ruff (lint + format check), mypy (advisory), and the test suite across Python 3.10–3.13 on every push and pull request.
- **Test suite is now committed** — `tests/`, `Makefile`, and `scripts/` are no longer gitignored, so the full unit + live integration suite can be run in CI and verified independently (`git clone` → `pip install -e ".[dev]"` → `pytest tests/`). The published wheel still ships only `livekit/`, so tests never reach `pip install` users.
- **`DEVELOPMENT.md`** — development & release runbook covering setup, testing, and the tag-based PyPI publish flow.
- **Versioning & release scripts** — `scripts/bump_version.py` (keeps `pyproject.toml` and `livekit/plugins/gnani/version.py` in sync) and `scripts/release.sh` (test → lint → bump → changelog → commit → tag → push).
- **`build`, `twine`** added to the `dev` optional dependencies; `make build` target builds the distribution and runs `twine check`. New `make bump-*` / `release-*` targets.

### Fixed

- **TTS `oggopus` live test** — updated the `oggopus` audio-config test to use `container="raw"` (the API rejects `oggopus` with `container="ogg"`).

## [0.5.1] - 2026-07-02

### Changed

- **TTS voices** — updated to 4 official voices: Pranav, Kaveri, Shubhra, Deepak. Removed legacy voices (Karan, Simran, Nara, Riya, Viraj, Raju). Default voice changed from `"Karan"` to `"Pranav"`. See [Available Voices](https://docs.gnani.ai/api/TTS/tts-sse#available-voices).

## [0.5.0] - 2026-06-23

### Removed

- **`language` parameter from TTS** — removed `language` from `GnaniTTSOptions`, `TTS.__init__()`, and `update_options()`. TTS no longer accepts a language parameter. The `language` field is no longer sent in WebSocket request bodies.

### Changed

- **STT documentation** — clarified that only REST and Streaming (WebSocket) modes are integrated; no batch STT. Added PCM specification details with link to [STT Realtime — PCM Specification](https://docs.gnani.ai/api/STT/stt-websocket#pcm-specification).

## [0.4.5] - 2026-06-15

### Changed 

- Url of the gnani documentation.


## [0.4.4] - 2026-05-31

### Removed

- **`organization_id` and `user_id` parameters** — removed from both `STT` and `TTS` classes. Authentication now requires only `api_key` (via constructor or `GNANI_API_KEY` env var). The `X-Organization-ID` and `X-API-User-ID` headers are no longer sent. Only `X-API-Key-ID` is used for authentication across all endpoints.

### Changed

- Minimum `gnani-vachana` dependency bumped to `>=0.4.3`.

## [0.4.3] - 2026-05-22

### Fixed

- **Double `end_segment()` in `SynthesizeStream`** — moved `end_segment()` out of the `finally` block to the normal completion path. The framework's `end_input()` already calls `__end_segment()` internally, so the `finally` was sending a duplicate `_EndSegment` message.

## [0.4.2] - 2026-05-22

### Fixed

- **SynthesizeStream mime_type** — `SynthesizeStream` now declares `mime_type="audio/pcm"` instead of `"audio/wav"`, matching the actual stripped-PCM data it emits. Prevents `AudioEmitter` from routing to the wrong decoder.
- **SSE parser** — restored missing `json.loads(buf)` / `JSONDecodeError` handling in `SSEChunkedStream`, which was silently broken (agents fork only).

## [0.4.1] - 2026-05-22

### Added

- **`WebSocketChunkedStream`** — `synthesize_method="websocket"` now correctly routes `synthesize()` through a WebSocket-backed `ChunkedStream`

## [0.4.0] - 2026-05-22

### Added

- **SSE streaming TTS** — new `SSEChunkedStream` class using `POST /api/v1/tts/sse` for lower-latency chunked synthesis with proper per-chunk WAV header stripping.
- **`synthesize_method` parameter** on `TTS` — choose `"rest"` (default), `"sse"`, or `"websocket"` to control which endpoint `synthesize()` uses.
- **WebSocket WAV fix** — `SynthesizeStream` now strips per-chunk WAV headers from WebSocket audio, producing correct PCM output for the LiveKit pipeline.

### Fixed

- **`_mark_started()` placement** — moved from before WebSocket connection to after the request body is sent, aligning with the convention used by all other LiveKit TTS plugins for accurate TTFB metrics.

### Removed

- **`vachana-voice-v2` support** — all legacy v2 voices removed.
- **Language-specific v3 voices** — removed 320 language-specific voices.

### Changed

- `SUPPORTED_VOICES` now contains only 6 voices: `Karan`, `Simran`, `Nara`, `Riya`, `Viraj`, `Raju`.
- `GnaniTTSVoices` type narrowed to the 6 supported voices.
- `streaming` capability set to `True` (was `False` in standalone package).
- TTS languages reduced to 10: Assamese, Bengali, English, Hindi, Kannada, Malayalam, Marathi, Odia, Tamil, Telugu.
- Minimum `gnani-vachana` dependency bumped to `>=0.4.0`.

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

[0.4.0]: https://github.com/Gnani-AI-Mintlify/livekit-plugins-gnani/releases/tag/v0.4.0
[0.3.0]: https://github.com/Gnani-AI-Mintlify/livekit-plugins-gnani/releases/tag/v0.3.0
[0.2.0]: https://github.com/Gnani-AI-Mintlify/livekit-plugins-gnani/releases/tag/v0.2.0
[0.1.0]: https://github.com/Gnani-AI-Mintlify/livekit-plugins-gnani/releases/tag/v0.1.0
