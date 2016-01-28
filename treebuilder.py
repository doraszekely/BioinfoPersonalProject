#! /usr/bin/env python
  
#original script for building the tree is the product of Luna&Onno co.
#importing the modules from ete3 tree building program
from ete3 import Tree, TreeStyle
#also importing module os to use shell commands
import os 
#a bit unnecessary but more user friendly
ImportantDecision = raw_input( " Do you wanna make a tree that you can actually read? (yes or no) ")
#deciding if creating a nicer tree is what we want
if ImportantDecision == 'yes':
	#it greps the tree.txt that was previously made by the newick input in my shell funtion
	#creating a list of the strings that are in the txt file
	FileList = os.popen("ls ~/Desktop/bioinfo_project/everything/ | grep tree.txt").read().split()
	#creating a variable that contains .svg
	Ext_svg = '.svg'
	#for cycle for creating the tree
	#going through the elements in FileList
	for file in FileList:
		t = Tree(file)
		ts = TreeStyle()
		ts.show_branch_support = True
		ts.show_leaf_name = True
		#creating a circular type of tree
		ts.mode = "c"
		#this zooms in on a horizontal scale, 120 pixels per branch length 
		ts.scale =  120
		#zooms in the vertical scale, 30 pixels between adjacent branches
		ts.branch_vertical_margin = 30
		#creating an outfile with a .svg ending
		OutFile = file + Ext_svg
		#rendering the tree into an svg file with the previously set tree style
		t.render(OutFile,tree_style=ts)
#pretty much useless also		
else:
	print "Then off we go for a beer"



