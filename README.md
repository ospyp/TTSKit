# TTSKit (Beta)

Easily run AI-based TTS (text-to-speech) models, quickly and efficiently. We support both TensorFlow and PyTorch (coming soon!) models.

## Install

**Important!** Do NOT install `ttskit`! This package is NOT affiliated with this project and is not managed by this project's authors!

```
pip install pyttskit
```

## Core Features

* No manual downloads required
* Supports CUDA/Nvidia GPUs, CPU, and Apple Silicon GPUs
* Easy to use
* Maintains inference structure of original models (basically if you were using a model this package supports previously, you can (probably) drop it in with little to no changes besides refactoring)
* Also offers uniform API structure
* Free + open-source

## Available Implementations

* [TransformerTTS](https://github.com/as-ideas/TransformerTTS)
* More coming soon! Have a suggestion? Please open a Discussion!

### Coming Soon

* [DiffGAN](https://github.com/keonlee9420/DiffGAN-TTS)
* [PortaSpeech](https://github.com/keonlee9420/PortaSpeech)

## License

Well... this is where things get complicated. This package uses multiple different models, and they have different licenses. We try to keep permissive licenses where you don't have to change your project's license if you use this package.

Please refer to the [LICENSE.md](LICENSE.md) file for more details.