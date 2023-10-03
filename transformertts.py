from ttskit.implementations.TransformerTTS.data.audio import Audio
from ttskit.implementations.TransformerTTS.model.factory import tts_ljspeech

model = tts_ljspeech()
audio = Audio.from_config(model.config)
out = model.predict('Please, say something.')

# Convert spectrogram to wav (with griffin lim)
wav = audio.reconstruct_waveform(out['mel'].numpy().T)
audio.save_wav(wav, 'test.wav')