#currently in TuneTaskAnalysis directory

import os
from SungMelodyAssessment.SMM import SMM
from SungMelodyAssessment.MFE import MFE

for i in list(os.walk('./TuneTask/Repetition'))[0][1]: #for each participant
    os.system('mkdir -p '+i)
    os.system('mkdir -p '+i+'/Repetition')
    os.system('mkdir -p '+i+'/Repetition/matricies')
    os.system('mkdir -p '+i+'/Repetition/mp3')
    os.system('mkdir -p '+i+'/Perception')
    #now do repetition analysis
    os.system('echo tune_num,note_interval_error,rhythm_error,note_difference > ./'+i+'/Repetition/'+i+'.csv')
    for j in range(55,115): #for each wav file in each participant
        tunenumber = str(j)
        filename_name = i+'_'+tunenumber
        filename = './TuneTask/Repetition/'+i+'/'+filename_name+'.wav'
        os.system('ffmpeg -i '+filename+' -vn -ar 44100 -ac 2 -b:a 192k ./'+i+'/Repetition/mp3/'+filename_name+'.mp3') #convert to mp3 and save in repetition/mp3 folder
        SMM('./'+i+'/Repetition/mp3/'+filename_name+'.mp3') #saves file in tunetaskanalyses directory
        os.system('mv '+filename_name+'.txt ./'+i+'/Repetition/matricies/'+filename_name+'.txt') #move to correct directory
        results = MFE('./TuneTaskApps/thetunes/matricies/tune'+tunenumber+'.txt', './'+i+'/Repetition/matricies/'+filename_name+'.txt')
        os.system('echo '+tunenumber+','+','.join(str(i) for i in results)+' >> ./'+i+'/Repetition/'+i+'.csv')
    #now copy the perception analysis csv file (1 per participant, created by TuneTaskApp(Perception))
    os.system('cp ./TuneTask/Perception/'+i+'/'+i+'_points.csv ./'+i+'/Perception/'+i+'.csv')
