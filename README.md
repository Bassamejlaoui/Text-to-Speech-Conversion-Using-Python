# Text to Speech Conversion Using Python

This repository contains a simple Python script to generate speech from text using the `gTTS` (Google Text-to-Speech) library. 

![image](https://github.com/mejbass/Text-to-Speech-Conversion-Using-Python/assets/130122304/266dc33b-5363-4e9f-b0d6-77364b090639)
---
## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

Text-to-speech (TTS) technology converts written text into spoken words. This project demonstrates how to use the `gTTS` library to create an MP3 file from a given text string.

## Installation

Before you begin, ensure you have Python installed on your system. You can install the `gTTS` library using `pip`.

```bash
pip install gTTS
```

## Usage

Here is the Python script to generate speech from text:

```python
from gtts import gTTS

language = "en"
text = "Hello, guys how are you doing? I hope you all are doing well."

speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
speech.save("textToSpeech.mp3")
```

### Explanation

- `from gtts import gTTS`: Imports the `gTTS` class from the `gTTS` module.
- `language = "en"`: Sets the language to English.
- `text = "Hello, guys how are you doing? I hope you all are doing well."`: The text you want to convert to speech.
- `speech = gTTS(text=text, lang=language, slow=False, tld="com.au")`: Creates a `gTTS` object with the specified text, language, speed (slow=False for normal speed), and tld (Top Level Domain) to use the Australian English accent.
- `speech.save("textToSpeech.mp3")`: Saves the generated speech to an MP3 file named `textToSpeech.mp3`.

### Running the Script

Save the script to a file, for example `text_to_speech.py`, and run it using the Python interpreter:

```bash
python text_to_speech.py
```

This will generate an MP3 file named `textToSpeech.mp3` in the same directory.
