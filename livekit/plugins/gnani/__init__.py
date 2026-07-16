"""Gnani Vachana plugin for LiveKit Agents

Support for speech-to-text and text-to-speech with [Gnani's Vachana platform](https://gnani.ai/).

Vachana provides high-accuracy STT and low-latency TTS for Indian languages,
including multilingual transcription scenarios.

For API access, get a key at https://app.gnani.ai/voice
"""

from gnani.tts import (
    DEFAULT_MODEL,
    SUPPORTED_TTS_LANGUAGES,
    TIMBRE_V20_VOICES,
    TIMBRE_V25_VOICES,
)

from .stt import STT, SpeechStream
from .tts import TTS, SynthesizeStream
from .version import __version__

__all__ = [
    "DEFAULT_MODEL",
    "STT",
    "SUPPORTED_TTS_LANGUAGES",
    "TIMBRE_V20_VOICES",
    "TIMBRE_V25_VOICES",
    "TTS",
    "SpeechStream",
    "SynthesizeStream",
    "__version__",
]


from livekit.agents import Plugin

from .log import logger


class GnaniPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(__name__, __version__, __package__, logger)


Plugin.register_plugin(GnaniPlugin())

_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
