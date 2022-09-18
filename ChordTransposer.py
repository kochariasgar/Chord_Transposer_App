from tkinter.colorchooser import Chooser


ChordList=['E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#']
ChordListM=['Em','Fm','F#m','Gm','G#m','Am','A#m','Bm','Cm','C#m','Dm','D#m','Em','Fm','F#m','Gm','G#','Am','A#m','Bm','Cm','C#m','Dm','D#m']
ChordList7=['E7','F7','F#7','G7','G#7','A7','A#7','B7','C7','C#7','D7','D#7','E7','F7','F#7','G7','G#7','A7','A#7','B7','C7','C#7','D7','D#7']

InputChords=[]
OutputChords=[]
number= input('How many chords do you want to transnpose? ')
print('Choose teh Chords one by one')
for i in range(int(number)):
    inpt = input('Chord'+str(i+1)+': ')
    InputChords.append(inpt)
print('Your Chords Are: '+str(InputChords))


Choose=input('Choose a chord to Transpose: ')
Choose2=input('Choose a chord to tranpose to: ')

#Finding the index of teh chord to transpose
if 'm' in str(Choose):

    ChordNumber1=ChordListM.index(str(Choose))
elif '7' in str(Choose):
    ChordNumber1=ChordList7.index(str(Choose))
else:
    ChordNumber1=ChordList.index(str(Choose))


if 'm' in str(Choose2):


    ChordNumber2=ChordListM.index(str(Choose2))
elif '7' in str(Choose2):
    ChordNumber2=ChordList7.index(str(Choose2))
else:
    ChordNumber2=ChordList.index(str(Choose2))
 
GapNumber=ChordNumber2-ChordNumber1
print(GapNumber)
for i in range(int(number)):
    #The Chord we are trying to transpose
    OurChord=(InputChords[i])
    print(str(i)+'Our Chord')
    #The Index of the Chord that we are trying to transpose
    if 'm' in str(InputChords[i]): 
        
        OurIndex=ChordListM.index(OurChord)
           # print('our index'+str(OurIndex))
        NewIndex=OurIndex+GapNumber
           # print('new index'+str(NewIndex))
        NewChord=str(ChordListM[NewIndex])
           # print('new chord'+str(NewChord))
    elif '7' in str(InputChords[i]):
        OurIndex=ChordList7.index(OurChord)
           # print('our index'+str(OurIndex))
        NewIndex=OurIndex+GapNumber
           # print('new index'+str(NewIndex))
        NewChord=str(ChordList7[NewIndex])
           # print('new chord'+str(NewChord))
    else:
        OurIndex=ChordList.index(OurChord)
           # print('our index'+str(OurIndex))
        NewIndex=OurIndex+GapNumber
           # print('new index'+str(NewIndex))
        NewChord=str(ChordList[NewIndex])
           # print('new chord'+str(NewChord))
    OutputChords.append(NewChord)
print('Transposed Chords: '+str(OutputChords))
#ADD M TO ALL THE LIST