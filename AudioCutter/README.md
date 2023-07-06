# Audio Cutter

<p>

Give a user an easy to use GUI that allows cutting out unwanted ranges of audio files.

</p>

##### Python Desktop Widget to Take out sections of Music

1. Search Repository for User Suggested song.
2. Convert time index of start and stop to ms.
3. Export the desired music segment to new directory.


## Demo

Fixing the Humma Song to take out the entire unnecessary pop rap verse.
![DEMO](https://github.com/athom031/InternAudioScripts/blob/master/AudioCutter/Demo.png)

## Prerequisites

1. Use pip to install python files.
* https://pip.pypa.io/en/stable/installing/pydub
2. Use pip to install pydub and use AudioSegment.
* https://pypi.org/project/pydub/
3. Make sure you install ffmpeg or libav for dealing with mp3.
* https://ffmpeg.org/download.html
* https://libav.org/

## Getting Started

1. Update global variables with desired directories.
2. Run splitscript and enter the song name along with the time stamps.
```
    python entryWidget.py
```
3. Click the button to run app or exit the window to close the program

## Warnings
To avoid following runtime warning:
```
RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work
warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning)
```
run script with -W ignore
```
python -W ignore entryWidget.py
```

## Inspiration

After growing up with Indian music that are up to 10 minutes long, leveraged knowledge gained in internship to build an applciation to encapsulate audio cutting.
