"""
TTSKit by mrfakename

Copyright (c) 2023 by mrfakename. All rights reserved.
This software may be used and redistributed under the terms of the NOSCL-C-2.0 software license. A copy of this license should be provided with this software.
"""

from ..implementations.TransformerTTS.data.audio import Audio
from ..implementations.TransformerTTS.model.factory import tts_ljspeech
from ..structures.TransformerTTSGeneration import TransformerTTSGeneration
class TransformerTTS:
    _model = None
    _audio = None
    def __init__(self):
        self._model = tts_ljspeech()
        self._audio = Audio.from_config(self._model.config)
    def speak(self, text) -> TransformerTTSGeneration:
        out = self._model.predict(text)
        return TransformerTTSGeneration(self._audio, out)