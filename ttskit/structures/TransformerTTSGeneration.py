"""
TTSKit by mrfakename

Copyright (c) 2023 by mrfakename. All rights reserved.
This software may be used and redistributed under the terms of the NOSCL-C-2.0 software license. A copy of this license should be provided with this software.
"""

from ..implementations.TransformerTTS.data.audio import Audio
class TransformerTTSGeneration:
    _audio = None
    _out = None
    wav = None
    def __init__(self, audio, out):
        self._audio = audio
        self._out = out
        self.wav = self._audio.reconstruct_waveform(self._out['mel'].numpy().T)
    def save_wav(self, filename):
        self._audio.save_wav(self.wav, filename)