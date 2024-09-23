#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import subprocess
import sys
import os
import os.path


 
conn = MySQLdb.connect (host = 'www.costadoat.fr',
                        user = 'site_web',
                        passwd = '46344634',
                        db = 'renaud')
#conn = MySQLdb.connect (host = 'localhost',
#                        user = 'root',
#                        passwd = '',
#                        db = 'renaud')
cursor = conn.cursor ()

racine="C:/Users/Renaud/Documents/Dorian/Prepa"

def gen_intro(n):
    cursor.execute ("SELECT * FROM cours_info WHERE Sequence={0}".format(n))
    rows = cursor.fetchall ()

    for row in rows:
            if row[7]==1:
                # cursor2 = conn.cursor ()
                # cursor2.execute ("SELECT * FROM competence_util WHERE Id_cours={0}".format(row[0]))
                # rows2 = cursor2.fetchall ()
                # competences =''
                # nb_comp = 0
                # for row2 in rows2:
                        # cursor3 = conn.cursor ()
                        # cursor3.execute ("SELECT * FROM competences WHERE Id={0}".format(row2[2]))
                        # rows3 = cursor3.fetchall ()
                        # comp =''
                        # for row3 in rows3:
                                # comp = row3[1] + ': ' + row3[2] 
                                # cursor3.close ()
                        # cursor2.close ()
                        # competences = competences + comp + ' \\\\ &  '
                        # nb_comp += 1
                # competences = competences[:-7]
                chemin = "{0}/Informatique/{1}{2}/intro.tex".format(racine,row[4],"%02d" % row[3])
                chemin_qr = "{0}/Informatique/{1}{2}/img".format(racine,row[4],"%02d" % row[3])
                if not os.path.isdir(chemin_qr):
                    os.mkdir(chemin_qr)
                if qrgen==1:
                    web="https://github.com/Costadoat/Informatique/blob/master/{0}{1}/I-{0}{1}.pdf?raw=true".format(row[4],"%02d" % row[3])
                    os.chdir("{0}\headers\Scripts".format(racine))
                    os.system("python ressources/generate.py ressources/LogoRen.svg {0} {1}/qrcode.svg".format(web,chemin_qr))
                    os.chdir(chemin_qr)
                    os.system("inkscape.exe -z -f {0}/qrcode.svg -w 400 -j -e {0}/qrcode.png".format(chemin_qr))
                fichier = open(chemin, "w")
                #info = "\\newcommand{{\\id}}{{{0}}}\r\\newcommand{{\\nom}}{{{1}}}\r\\newcommand{{\\sequence}}{{{2}}}\r\\newcommand{{\\num}}{{{3}}}\r\\newcommand{{\\type}}{{{4}}}\r\\newcommand{{\\descrip}}{{{5}}}\r\\newcommand{{\\competences}}{{{6}}}\r\\newcommand{{\\nbcomp}}{{{7}}}\r\\newcommand{{\\systemes}}{{{8}}}\r\\newcommand{{\\ilot}}{{{9}}}\r{10}".format(row[0],row[1],"%02d" % row[2],"%02d" % row[3],row[4],row[5],competences,nb_comp,systemes,row[7],img)
                info = "\\newcommand{{\\id}}{{{0}}}\r\\newcommand{{\\nom}}{{{1}}}\r\\newcommand{{\\sequence}}{{{2}}}\r\\newcommand{{\\num}}{{{3}}}\r\\newcommand{{\\type}}{{{4}}}\r\\newcommand{{\\descrip}}{{{5}}}\r".format(row[0],row[1],"%02d" % row[2],"%02d" % row[3],row[4],row[5])
                fichier.write(info)
                fichier.close()

n=input('Mise a jour de la sequence (all=2000) ')
qrgen=raw_input('Generer les QRCode ? (o/N) ')
if qrgen=='o':
    qrgen=1
else:
    qrgen=0
    #print "Du coup, je fais rien..."
    
if n==2000:
    for sequence in range(5):
        print sequence
        gen_intro(sequence)
else:
    gen_intro(n)

cursor.close () 
conn.close ()