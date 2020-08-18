'''
Author: Alex Thomas
Last Updated: 8/18/2020 (added mac os implementation)
Script to split wav files into a folder of isolated utterances.

Improvement upon Kevin Chuang audiosplit.py program
'''

import json 
import sys  
import os                      #make directory and paths for new utterence folders
from pydub import AudioSegment #Open Source Python Library to process Audio as array


"""
Company Defaults

ADDED_SILENCE_MS      = 300 ms
SILENCE_BTWN_MS       = 750 ms
NOISE_INSTANCE_DBFS   = -30 dBFS
SILENCE_INSTANCE_DBFS = -54 dBFS
"""


#---------------------------- Open config.json and assign global variables ----------------------------#
with open('config.json') as config_file:
    data = json.load(config_file)

WAV_DIRECTORY         = data['wav_directory']
DESTINATION_DIRECTORY = data['destination_directory']
ADDED_SILENCE_MS      = data['added_silence_ms']
SILENCE_BTWN_MS       = data['silence_btwn_ms']
NOISE_INSTANCE_DBFS   = data['noise_instance_dBFS']
SILENCE_INSTANCE_DBFS = data['silence_instance_dBFS']
SYSTEM                = data['system_type']


if SYSTEM == "mac":
    dirChar = "/"
else:
    dirChar = "\\"
#------------------------------------------------------------------------------------------------------#


#-------------------------------------- Utterence Slice Indices ---------------------------------------#
def startOfUtterance(sound_file, start_point):
    for i in range(start_point, len(sound_file)):
        if(sound_file[i].dBFS > NOISE_INSTANCE_DBFS):
        #found starting instance of noise
            return(i - ADDED_SILENCE_MS)
            #return silence amount index before noise
    return -1
    #if no noise from start point to end of file then signify no utterance


def endOfUtterance(sound_file, ut_start):
    i = ut_start + ADDED_SILENCE_MS
    #we get the start of utterance from previous function and adjust 
    while(i < len(sound_file)):
    
        enter_loop = False
        if(sound_file[i].dBFS < SILENCE_INSTANCE_DBFS):
            #possible end of file
            enter_loop = True
        if (enter_loop):
            #test if index is the end of utterance
            noise = False
            j = 0
            while(j < SILENCE_BTWN_MS):
                if(sound_file[j + i].dBFS > NOISE_INSTANCE_DBFS):
                    #noise is detected
                    noise = True
                    
                    i += j
                    #i should then go to j+i value 
                    #OPTIMIZE CALCULATIONS
                    
                    j = SILENCE_BTWN_MS
                    #forces exit of loop

                else:
                    j += 1
                
            if (noise == False):
                return(i + ADDED_SILENCE_MS)
                #buffer of added_silence value following end of utterance
        i += 1
    return len(sound_file) - 1 
    #if sound occurs untill end, soundfiles end is the end of the utterence

#------------------------------------------------------------------------------------------------------#


def findAllUtterances(sound_file, file_name):
    ut_count = 1
    i = 0
    os.mkdir(DESTINATION_DIRECTORY + dirChar + file_name) #make a folder to put all splits for each wav file
    while (i < len(sound_file)):
        ut_start = startOfUtterance(sound_file, i)
        ut_end   = endOfUtterance(sound_file, ut_start)
        if(ut_start == -1): #no noise from start to end of file
            break
        new_audio = sound_file[ut_start:ut_end] #slice array
        new_audio.export(file_name + '_%s.wav' % ut_count, format="wav") #export sliced array as audio file

        os.rename(os.path.abspath(file_name + '_%s.wav' % ut_count), 
            DESTINATION_DIRECTORY + dirChar + file_name + dirChar + file_name + '_Utterance_%s.wav' % ut_count)
        #clean up path and naming convention

        i = ut_end 
        ut_count += 1


def main():
    #error if destination directory is not empty
    if (len(os.listdir(DESTINATION_DIRECTORY)) == 0): 
        for filename in os.listdir(WAV_DIRECTORY): 
            file_name = filename[:-4] #filename without '.wav'
            sound_file = AudioSegment.from_wav(WAV_DIRECTORY + dirChar + filename)
            
            findAllUtterances(sound_file, file_name)
            
    else:
        print("ERROR: Destination Directory entered is not empty and must be for a proper Split.")


if __name__ == '__main__':
    sys.exit(main())