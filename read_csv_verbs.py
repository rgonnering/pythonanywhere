# -*- coding: utf-8 -*-
# read_csv_verbs.py
# 
# utility to modify the database, data.py
#
# add present subjunctive
# for pythonanywhere.com flask app
# conjugame
# https://www.pythonanywhere.com/user/rgonnering
# http://rgonnering.pythonanywhere.com/

"""
conjaGame_database.notes
========================
4/1/2106

How to refresh the database:
----------------------------
A go to http://www.conjugation.org/
    get words in list form
Copy each word to the verbs.xlsx
Copy all of verbs.xlsx
Copy Special|Transpose to spanish_verbs.csv
    spanish_verbs should be cleaned up with just verb data
$ python verb_index.py
Copy each tense to 
    https://www.pythonanywhere.com/user/rgonnering/files/home/rgonnering/mysite/data.py?edit



Instructions to change verb list
--------------------------------
    Copy conjugated verbs to spreadsheet
        OR
        Download the Spradsheet from
            http://rgonnering.pythonanywhere.com/
    Transpose conjugated verbs
    Save conjugated verbs as spanish_verbs.csv
    From spanish_verbs.csv, Remove 
        rows: 1, 2, 5, and empty rows
        columns: A, B, and empty columns
    Start ipython
        In []: cd /home/roger/python/pythonanywhere/conjuGame
        In []: run read_csv_verbs.py
        In []: cat verb_data.txt

unicode
-------
    s.decode(encoding)
        convert <type 'str'> to <type 'unicode'>
    u.encode(encoding)
        convert <type 'unicode'> to <type 'str'>
    to save Unicode to disk you have to encode it
"""

import csv     

verbs_present = []
verbs_preterit = []
verbs_imperfect = []
verbs_future = []
verbs_imperative = []
verbs_present_subjunctive = []

# -------------------------------------- functions
def read():
    print "\nREAD"
    fd = open('spanish_verbs.csv','r')
    reader = csv.reader(fd)
    wordlines = list()
    for line in reader:
        print line
        words = list()        
        for verbs in line:
            words.append( verbs) 
        wordlines.append(words)
        print words
    fd.close()
    return wordlines

def write(verbs):
    fd = open('spanish_verbs.txt','w')  
    print
    print "---------------------------- write()"
    verb_line = str()
    for line in verbs:
        verb_line = verb_line + "["
        for word in line:
            verb_line = verb_line + "u\'" + word + "\',"
            #verb_line = verb_line + word + ","
        verb_line = verb_line[:-1] + "]"
        verb_line = verb_line + '\n'
        #verb_line = verb_line[:-1] + '\n'
        # You can not write a list to file handle - cast line as str
    print verb_line
    fd.write( ( verb_line ) )
    fd.close()
    return 

def read_data():
    fd = open('spanish_verbs.txt', 'r')
    reader = csv.reader(fd)
    print "\nREAD_DATA"
    for tense in range(6):
        """
        Column  Description
        0       Infinitive
        1       English (semi-colon separated)
        2-7     Present Indicative
        8-13    Imperfect
        14-19   Preterit
        20-25   Future
        26-31   Conditional
        32      Imperative (second person, singular)
        37-42   Present Subjunctive
        43-48   Imperfect Subjunctive
        49      Gerund
        50      Past Pariciple
        """
        if tense == 0:
            print "# -----------------------------------------"
            print "present_tense = ["
            for line in reader:
                print "\nLINE"
                print line
                print line[0], ",", line[1], 
                for i in range(2,8):
                    print ",", line[i], 
                print "],"
            print "]"
        if tense == 1:
            print "# -----------------------------------------"
            print "preterit_tense = ["
            fd.seek(0,0)
            for line in reader:
                print line[0], ",", line[1], 
                for i in range(14,20):
                    print ",", line[i], 
                print "],"
            print "]"                
        if tense == 2:
            print "# -----------------------------------------"
            print "imperfect_tense = ["
            fd.seek(0,0)
            for line in reader:
                print line[0], ",", line[1], 
                for i in range(8, 14):
                    print ",", line[i], 
                print "],"
            print "]"                
        if tense == 3:
            print "# -----------------------------------------"
            print "future_tense = ["
            fd.seek(0,0)
            for line in reader:
                print line[0], ",", line[1], 
                for i in range(20, 26):
                    print ",", line[i], 
                print "],"
            print "]"  
        if tense == 4:
            print "# -----------------------------------------"
            print "imperative_tense = ["
            fd.seek(0,0)
            for line in reader:
                print line[0], ",", line[1], 
                i=32
                print ",", line[i], 
                print "],"
            print "]" 
        if tense == 5:
            print "# -----------------------------------------"
            print "Present Subjunctive = ["
            fd.seek(0,0)
            for line in reader:
                print line[0], ",", line[1], 
                for i in range(37, 43):
                    print ",", line[i], 
                print "],"
            print "]"               
    fd.close()
    return
    
# ------------------------------------------ Main
myVerbs = read()
write(myVerbs)
read_data()

