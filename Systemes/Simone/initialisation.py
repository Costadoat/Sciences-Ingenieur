# coding: utf8

import numpy as np
import time
import itertools
import sys
from pypot.dynamixel import Dxl320IO, get_available_ports

def init_param(ids_in):
    ## Connexion
    # Scan des ports series
    ports = get_available_ports()
    
    # Affichage des ports trouvés
    if not len(ports):
        print('Aucun port detecté!')
        sys.exit(1)
    
    print('ports trouvés!', ports)
    
    # Choix du port
#num_port = int(input('taper le numero du port dans la liste? (0,1,...)'))
    num_port=0
    ## Scan des servomoteurs
    io = Dxl320IO(ports[num_port])
    ids = io.scan([4,6])
    ids = io.scan(ids_in)
    print('motors found', ids)
#    time.sleep(2)
    return io,ids
    
def init_pilotage(io,ids):
    ## Mise en position initiale
    # Reglage gain pid
    all_gain = dict(zip(ids, itertools.repeat([8, 0.5, 0])))
    io.set_pid_gain(all_gain)
#    vitmin=dict(zip(ids,itertools.repeat(100)))
#    io.set_moving_speed(vitmin)
    # Envoi de la position
    pos = dict(zip(ids, itertools.repeat(0)))
    io.set_goal_position(pos)
    time.sleep(2)
#    vitmax=dict(zip(ids,itertools.repeat(0)))
#    io.set_moving_speed(vitmax)
#    time.sleep(0.5)
    return io,ids
    
def init_pilotage_pied(io,ids,ids2,ids3):
    ## Mise en position initiale
    # Reglage gain pid
    all_gain = dict(zip(ids, itertools.repeat([8, 0, 0])))
    io.set_pid_gain(all_gain)
    all_gain = dict(zip(ids2, itertools.repeat([8, 0, 0])))
    io.set_pid_gain(all_gain)
    all_gain = dict(zip(ids3, itertools.repeat([8, 0, 0])))
    io.set_pid_gain(all_gain)
    vitmin=dict(zip(ids,itertools.repeat(50)))
    io.set_moving_speed(vitmin)
    vitmin2=dict(zip(ids2,itertools.repeat(50)))
    io.set_moving_speed(vitmin2)
    vitmin3=dict(zip(ids3,itertools.repeat(50)))
    io.set_moving_speed(vitmin3)
    # Envoi de la position
    pos = dict(zip(ids, itertools.repeat(0)))
    io.set_goal_position(pos)
    time.sleep(1)
    pos2 = dict(zip(ids2, itertools.repeat(0)))
    io.set_goal_position(pos2)
    time.sleep(1) 
    pos3 = dict(zip(ids3, itertools.repeat(0)))
    io.set_goal_position(pos3)
    time.sleep(1)     
    vitmax=dict(zip(ids,itertools.repeat(400)))
    io.set_moving_speed(vitmax)
    time.sleep(0.5)
    vitmax2=dict(zip(ids2,itertools.repeat(400)))
    io.set_moving_speed(vitmax2)
    time.sleep(0.5)
    vitmax3=dict(zip(ids3,itertools.repeat(400)))
    io.set_moving_speed(vitmax3)
    time.sleep(0.5)
    return io,ids,ids2,ids3
    ## Fermeture du port
    #io.close()
    

