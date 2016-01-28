#! /bin/bash

#calling for my python script
allorfull.py

echo "If you want to see your tree type: SeeMyTree+space+all or full "
#rest is in a custom function
SeeMyTree(){
#first argument would be all
#it's not the best solution
#if it's stated otherwise it goes with the elif way
Type="all"
        if [ $1 = 'all' ]
                then
                        #clustalw2 I used for my OS X
                        #infile would be the previously made allsequece.fas and the sequences are aligned 
                        clustalw2 -infile=allsequences.fas -type=DNA -outfile=allsequences_test_tree.phy -output=PHYLIP
                        #phyml creates the tree with all the datafiles, makes the bootstrapping here the value is set to 10
                        phyml -i allsequences_test_tree.phy -d nt -n 1 -b 10 -m HKY85
                        #newick creats the actual tree according to the txt file made by phyml and puts it into an svg file
                       	nw_display -s -S -v 25 -b ’opacity:0’ -i ’font-size:8’ allsequences_test_tree.phy_phyml_tree.txt > allsequences_test_tree.phy_phyml_tree.svg
        elif [ $1 ]
                then
     					#same happens here just only with the full sequences               
                        clustalw2 -infile=justfullsequences.fas -type=DNA -outfile=justfullsequences_test_tree.phy -output=PHYLIP
                        phyml -i justfullsequences_test_tree.phy -d nt -n 1 -b 10 -m HKY85
                        nw_display -s -S -v 25 -b ’opacity:0’ -i ’font-size:8’ justfullsequences_test_tree.phy_phyml_tree.txt > justfullsequences_test_tree.phy_phyml_tree.svg
	fi
#finally I call my python script to make the tree in the ete3 program	
treebuilder.py
}


