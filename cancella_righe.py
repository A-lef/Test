def IsDirectory(Name):
	for Letter in Name:
		if Letter=='.':
			return False
	return True

def TextChanger (PercentageLines, PercentageLetters, FileName):
	#remove lines
	File=open(FileName,'r')#trasformo il file in lista di sue righe
	FileList=File.readlines()
	File.close()
	File=open(FileName, 'w')#riscrivo solo alcune righe del file
	for line in FileList:
		if random.randint(0,100)>=PercentageLines:#ricopio le righe solo il (100-"percentuale")% delle volte, ovvero, ne ho tolte il "percentuale"%
			File.write(line)
	
	#Change letters
	File=open(FileName, 'r')#trsformo il file in stringa per poterlo lavorare
	FileAsStr=File.read()
	File.close()
	File=open(FileName,'w')#riscrivo il file precedentemente salvato come stringa, eccetto alcune volte (caratteri random)
	Length=len(FileAsStr)
	for i in range(Length):
		if (random.randint(0,100)<PercentageLetters) and (FileAsStr[i]!='\n'):#evento che capita con probabilità del PercentageLetters%
			File.write(chr(random.randint(33,127)))
		else:
			File.write(FileAsStr[i])
	File.close()

def Visits(StartingAddress, ExtList, PercLines,PercLett):
	FileList=[]
	for DirPath, SubDir, FileNames in os.walk(StartingAddress):
		for File in FileNames:
			FileList.append(os.path.join(DirPath, File))
	for Element in FileList:
		if IsDirectory(Element)==False:
			TextChanger(PercLines, PercLett, Element)

import os
import random
import sys


NumberOfParameters=len(sys.argv)
if NumberOfParameters!=2 and NumberOfParameters!=4:
	print("non e' stato inserito il numero corretto di parametri (che sono, in ordine: indirizzo, percentuale caratteri, percentuale linee)")
	exit()

MyDir=sys.argv[1]
os.chdir(MyDir) #lavoro nella cartella con i file da modificare

if NumberOfParameters>2:
	perc_chars = int(sys.argv[2])
	perc_lines = int(sys.argv[3])
else:
	perc_chars = 5
	perc_lines = 5

#CONTROLLI MANUALI
#MyDir='C:\MyDir'
#perc_chars = 6
#perc_lines = 4
ExtensionList=['.txt', '.c']
Visits(MyDir, ExtensionList, perc_chars, perc_lines)

