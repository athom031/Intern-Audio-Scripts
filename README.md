# Split Script

Method to take raw lab test wav files and split them into individual utterances.
##### Script for Knowles Intelligent Audio test team.

1. Use AudioSegment to convert wav file to array.
2. Iterate throught file to find instance of sound.
3. Travel till end of uttterance (silence iterval).
4. Splice audio segment and export new utterance wav file.

## Demo Images
1. Used for algo training, users repeated utterances for 9 keywords.
![Verification](https://github.com/athom031/SplitScript/blob/master/demo_img/Verification.jpg)

## Prerequisites

1. Use pip to install python files.
* https://pip.pypa.io/en/stable/installing/pydub 
2. Use pip to install pydub and use AudioSegment.
* https://pypi.org/project/pydub/
3.
### Getting Started

1. Update config.JSON with raw and Utterance directories.
2. Make sure Utterance directory is empty.
3. Run python script to split every raw file in raw directory:
```
    python json_splitscript.py
```

## Inspiration: 
Optimized Keving Chuang's split script implementation
