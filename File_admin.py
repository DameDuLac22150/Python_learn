#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
Source d'inspiration:
https://stackoverflow.com/questions/19672352/how-to-run-python-script-with-elevated-privilege-on-windows
"""
 
import sys
import os
import ctypes
 
#############################################################################
def administrateur(argv=None):
    """permet d'obtenir les droits administrateur sous Windows
       nb: compatible avec un exécutable "exe" obtenu par PyInstaller
    """
    if sys.platform != "win32":
        return False # on n'est pas sous Windows
 
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True # on a actuellement les droits administrateur
 
    executable = sys.executable
 
    if argv is None:
        argv = sys.argv
    if getattr(sys, 'frozen', False):
        arguments = argv[1:] # programme traité par pyinstaller
    else:
        arguments = argv # programme normal .py
    ligne_args = ' '.join(arguments)
 
    # relance du programme avec les droits administrateur
    ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", executable, ligne_args, None, 1)
    if ret <= 32:
        return False # erreur
 
    # la demande des droits admin a été acceptée dans le programme relancé
    return None
 
#############################################################################
if __name__ == '__main__':
 
    # demande d'obtention des droits administrateur
    ok = administrateur()
 
    if ok is None:
        # les droits admin viennent d'être obtenus: il faut laisser le
        # programme qui vient d'être relancé avec ces droits et arrêter ici
        sys.exit(0)
 
    elif ok:
        print("J'ai les droits administrateur")
        # suite normale du programme qui s'exécute avec les droits administrateur
 
        # tentative de mener une action qui nécessite des droits administrateur
        # suppose ici que "c:" est le drive système et que "c:\test" n'existe pas
        try:
            os.mkdir(r"c:\test")    
        except Exception as msgerr:
            print(msgerr)
 
        x = input("Faites 'entrée' pour sortir")
 
    else:
        raise Exception ("Erreur: je n'ai pas pu obtenir les droits administrateur")