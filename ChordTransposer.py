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
if len(Choose)==2 or len(Choose)==3:
    if Choose[1]=='m'or Choose[2]=='m':

        ChordNumber1=ChordListM.index(str(Choose))
    elif Choose[1]=='7'or Choose[2]=='7':
        ChordNumber1=ChordList7.index(str(Choose))
    else:
        ChordNumber1=ChordList.index(str(Choose))
else:
    ChordNumber1=ChordList.index(str(Choose))

if len(Choose2)==2 or len(Choose2)==3:
    if Choose2[1]=='m'or Choose2[2]=='m':

        ChordNumber2=ChordListM.index(str(Choose2))
    elif Choose2[1]=='7'or Choose2[2]=='7':
        ChordNumber2=ChordList7.index(str(Choose2))
    else:
        ChordNumber2=ChordList.index(str(Choose2))
else:
    ChordNumber2=ChordList.index(str(Choose2))    
GapNumber=ChordNumber2-ChordNumber1
print(GapNumber)
for i in range(int(number)):
    #The Chord we are trying to transpose
    OurChord=(InputChords[i])
    print(str(i)+'Our Chord')
    #The Index of the Chord that we are trying to transpose
    if len(InputChords[i])==2 or len(InputChords[i])==3:
        if InputChords[i][1]=='m'or InputChords[i][2]=='m':
            OurIndex=ChordListM.index(OurChord)
           # print('our index'+str(OurIndex))
            NewIndex=OurIndex+GapNumber
           # print('new index'+str(NewIndex))
            NewChord=str(ChordListM[NewIndex])
           # print('new chord'+str(NewChord))
        elif InputChords[i][1]=='7'or InputChords[i][2]=='7':
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