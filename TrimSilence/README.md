# Silence Trimmer and Audio Normalizer

Optimization of music editing.

1. Take directory of music files, and normalize audio.
2. Search the audio file for the actual music and cut out silence and trivial bits.
3. Export edited audio to new directory.

## Demo

![DEMO](https://github.com/athom031/InternAudioProjects/blob/master/TrimSilence/Demo.png)

## Prerequisites

1. Use pip to install python files.
* https://pip.pypa.io/en/stable/installing/pydub 
2. Use pip to install pydub and use AudioSegment.
* https://pypi.org/project/pydub/
3. Make sure you install ffmpeg or libav for dealing with mp3.
* https://ffmpeg.org/download.html
* https://libav.org/

## Getting Started

1. Update [config.JSON](https://github.com/athom031/InternAudioScripts/blob/master/TrimSilence/config.JSON) with desired directories. Default Audio levels can be changed as well. 
2. Run trimSilence script.
```
    python trimSilence.py
```

## Warnings 
For demo purposes the temporary, music, and edited directories are kept separate but in real life application this might use up a lot of space quick. 

The script will automatically clear up the temporary directory on its own.

Another additional way to save space is to make the destination directory the same as the music directory.

## Inspiration

As a software engineering intern for Knowles Intelligent Audio, I learned the importance of having audio normalized for lab testing. This project is a revamping of technology used to split test audio files. As an intern I used these scripts and wanted to make my own that would provide a more efficient execution of the logic.
