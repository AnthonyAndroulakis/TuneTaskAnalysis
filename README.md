# TuneTaskAnalysis
a simple script/method for automating the sung-melody-assessment code

## How to set up:
1) `git clone https://github.com/AnthonyAndroulakis/TuneTaskAnalysis.git`
2) `cd TuneTaskAnalysis` #go into TuneTaskAnalysis directory
3) install dependencies:
    i) git (https://git-scm.com/downloads)
    ii) ffmpeg (https://www.ffmpeg.org/download.html)
    iii) python3 (https://www.python.org/downloads/)
    iv) praat-parselmouth (pip3 install praat-parselmouth)
    v) numpy (pip3 install numpy)
    vi) scipy (pip3 install scipy)
    vii) more_itertools (pip3 install more_itertools)
4) `git clone https://github.com/AnthonyAndroulakis/SungMelodyAssessment.git`
5) `git clone https://github.com/AnthonyAndroulakis/TuneTaskApps.git`

## input
TuneTask folder contains a Perception folder and a Repetition folder .     
Within both the Perception and Repetition folders are folders for participants
For the Perception folder, there is a csv file within each participant folder (csv file created by https://github.com/AnthonyAndroulakis/TuneTaskApps/tree/master/MelodicPerceptionTask) (tunes 1-54)       
For the Repetition folder, there are .wav files of the participant humming each tune (.wav files created by https://github.com/AnthonyAndroulakis/TuneTaskApps/tree/master/MelodicRepetitionTask) (tunes 55-114)      

## How to run:
`python3 analyses.py`       

## output
analyses.py will create folders titled by participant number (# of folders = # of participants)     
within each folder will be a Perception folder and a Repetition folder         
within each of these folders, you will find a csv file. This csv file contains the analyzed data.
