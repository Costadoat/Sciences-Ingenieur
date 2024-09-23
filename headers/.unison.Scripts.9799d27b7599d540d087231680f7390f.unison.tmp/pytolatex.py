# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:11:46 2016

@author: Renaud
"""

import os
import os.path

ilots=os.listdir('Code')
mon_fichier = open("fichier.tex", "w")
mon_fichier.write('\documentclass[a4paper,12pt,titlepage,twoside]{article} \n \usepackage[T1]{fontenc} \n ')
mon_fichier.write('\usepackage[french]{babel} \n \usepackage[gen]{eurosym} \n \usepackage{verbatim}')
mon_fichier.write('\setlength{\hoffset}{-18pt} \setlength{\oddsidemargin}{0pt} \n \setlength{\evensidemargin}{0pt} ')
mon_fichier.write('\setlength{\marginparwidth}{00pt} \n \setlength{\\textwidth}{481pt}')
mon_fichier.write('\setlength{\\voffset}{-18pt} \n \setlength{\marginparsep}{7pt} \n \setlength{\\topmargin}{-30pt}')
mon_fichier.write('\setlength{\headheight}{5pt} \n \setlength{\headsep}{20pt} \n \setlength{\\footskip}{30pt}')
mon_fichier.write('\setlength{\\textheight}{700pt} \n \\begin{document} \n \n')

if len(ilots)!=0:
    for ilot in ilots:
        if ilot[-2:]=='py':
            mon_fichier.write('\\begin{center} \n \\textbf{%s} \n \end{center} \n \\verbatiminput{Code/%s} \n \n \cleardoublepage \n \n' % (ilot[:-3],ilot))

mon_fichier.write('\n \end{document} \n \n')
mon_fichier.close()