#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import subprocess

FNULL = open(os.devnull, 'w')

racine="C:/Users/Renaud/Documents/Dorian/Prepa"

def latex(seq,num,tpe,ilot):
    if ilot != 0:
		path="{0}/S{1}/{2}{3}/Ilot_{4}".format(racine,"%02d" % seq,tpe,"%02d" % num,"%02d" % ilot)
		fichier="{0}-{1}{2}-I{3}".format("%02d" % seq,tpe,"%02d" % num,"%02d" % ilot)
    else:
		path="{0}/S{1}/{2}{3}".format(racine,"%02d" % seq,tpe,"%02d" % num)
		fichier="{0}-{1}{2}".format("%02d" % seq,tpe,"%02d" % num)
    os.chdir(path)
    com1='pdflatex -synctex=1 -interaction=nonstopmode -jobname={0} \def\public{{}}\input{{{0}.tex}}'.format(fichier)
    com2='pdflatex -synctex=1 -interaction=nonstopmode -jobname={0}_prive \def\prive{{}}\input{{{0}.tex}}'.format(fichier) 
    if os.path.isfile('{0}/{1}.tex'.format(path,fichier)):
		subprocess.call(com1, stdout=open(os.devnull, 'wb'))
		subprocess.call(com1, stdout=open(os.devnull, 'wb'))
		subprocess.call(com2, stdout=open(os.devnull, 'wb'))
		subprocess.call(com2, stdout=open(os.devnull, 'wb'))
		print '{0} Ok!'.format(fichier)
    else: 
		print 'Pas de fichier {0}/{1}.tex'.format(path,fichier)
		print '{0} Ko :('.format(fichier)    
    
def latex_tp(seq,num):
    path="{0}/S{1}/TP{2}".format(racine,"%02d" % seq,"%02d" % num)
    ilots=os.listdir(path)
    
    if os.path.isdir("{0}/S{1}/TP{2}/Ilot_01".format(racine,"%02d" % seq,"%02d" % num)):
        for ilot in ilots:
            if ilot[0:5]=='Ilot_':
                c=int(ilot[5:7])
                latex(seq,num,'TP',c)
    else:
        latex(seq,num,'TP',0)
        
              
	
def compiler(seq,t):
    chemin = "{0}/S{1}/".format(racine,"%02d" % seq)
    dossiers=os.listdir(chemin) 

    if len(dossiers)!=0:
         for dossier in dossiers:
             if dossier[0]=='C' and (t==0 or t==1):
                 c=int(dossier[1:3])
                 latex(seq,c,'C',0)
             if dossier[0:2]=='TD' and (t==0 or t==2):
                 td=int(dossier[2:4])
                 latex(seq,td,'TD',0)
             if dossier[0:2]=='TP' and (t==0 or t==3):
                 tp=int(dossier[2:4])
                 latex_tp(seq,tp)
             if dossier[0:2]=='KH' and (t==0 or t==4):
                 kh=int(dossier[2:4])
                 latex(seq,kh,'KH',0)
				 

def latex_info(num,tpe,s):
    path="{0}/Informatique/{1}{2}{3}".format(racine,tpe,"%02d" % num,s)
    fichier="I-{0}{1}".format(tpe,"%02d" % num)
    os.chdir(path)
    com1='pdflatex -synctex=1 -interaction=nonstopmode -jobname={0} \def\public{{}}\input{{{0}.tex}}'.format(fichier)
    com2='pdflatex -synctex=1 -interaction=nonstopmode -jobname={0}_prive \def\prive{{}}\input{{{0}.tex}}'.format(fichier) 
    if os.path.isfile('{0}/{1}.tex'.format(path,fichier)):
		subprocess.call(com1, stdout=open(os.devnull, 'wb'))
		subprocess.call(com1, stdout=open(os.devnull, 'wb'))
		subprocess.call(com2, stdout=open(os.devnull, 'wb'))
		subprocess.call(com2, stdout=open(os.devnull, 'wb'))
		print '{0} Ok!'.format(fichier)
    else: 
		print 'Pas de fichier {1}.tex'.format(path,fichier)
		print '{0} Ko :('.format(fichier)
    
    
def compiler_info():
	chemin ='{0}/Informatique/'.format(racine)
	dossiers=os.listdir(chemin) 
	if len(dossiers)!=0:
         for dossier in dossiers:
             if dossier[0]=='C':
                 c=int(dossier[1:3])
                 latex_info(c,'C','')
             if dossier[0:2]=='TD':
                 td=int(dossier[2:4])
                 latex_info(td,'TD','')
             if dossier[0:2]=='TP' and dossier[-1]!='t' :
                 tp=int(dossier[2:4])
                 latex_info(tp,'TP','')
             if dossier[0:2]=='TP' and dossier[-1]=='t' :
                 tp=int(dossier[2:4])
                 latex_info(tp,'TP','_secret')

seq=input('Re-compiler sequence (2000=all, 1000=si, 306=info) ?')
type=input('Compiler quoi (1:cours, 2:td, 3:tp, 4:kh, 0:tout) ?')

nb=14 #Derniere sequence pouvant etre compilee

if seq==2000:
    for i in range(nb+1)[1:]:
        print i
        compiler(i,type)
    print "Info"
    compiler_info()
elif seq==1000:
    for i in range(nb+1)[1:]:
        print i
        compiler(i,type)
elif seq==306:
    compiler_info() 
elif seq in range(nb+1):
    compiler(seq,type)
else:
    print 'La sequence {0} ne peut pas être compilee automatiquement'.format("%02d" % seq)