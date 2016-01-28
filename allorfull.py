#! /usr/bin/env python

#importing module os to be able to call for shell commands
import os

print "This program if for making a phylogenetic tree" 
#creating a user input for the variable ChosenFile
ChosenFile = raw_input( "Would you like to create the tree with all the sequences or just full sequences? (enter: all or full) " )
#if statement for choosing weather all sequences or just full sequences are used
if ChosenFile == 'all': 
	#this is a variable to be able to list the sequences for double checking before alignment
	#os.popen imports shell commands into python, this is how I got the sequence headers
	AllSeq = os.popen('grep ">" allseq_test.fas').read()
	#creating an outfile again with the imported shell command, the outfile contains all the sequences
	#I used grep -A1 because it greps the line of the term I searched for plus n lines (in this case 1)
	OutFile = os.popen('grep -A1 ">" allseq_test.fas > allsequences.fas')
	print "These are the sequences: "
	#printing the AllSeq variable which contains all the sequence headers
	print AllSeq
	#creating a variable to count how many sequences are used  
   	SeqCount = os.popen('grep ">" allseq_test.fas | wc -l').read()
	print "Number of sequences: "
	#printing the variable SeqCount that would give back the number of sequences
	print SeqCount
#also could have used elif	
else:
	#if the user input is full it creates everything the same way as explained before
	if ChosenFile == 'full':
		AllSeq = os.popen('grep "full" allseq_test.fas').read()
		OutFile = os.popen('grep -A1 "full" allseq_test.fas > justfullsequences.fas')
        	print "These are the sequences: "
        	print AllSeq
		SeqCount = os.popen('grep "full" allseq_test.fas | wc -l').read()
        	print "Number of sequences: "
        	print SeqCount
		
