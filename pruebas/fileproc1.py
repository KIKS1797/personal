#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#CARGAR ARCHIVO Y QUITAR COMAS 

import string

name_archivo=input("ingresar archivo:   ")
datos=open(name_archivo,"r")

list_new = [item.replace('addi','0001') for item in datos]
list_new = [item.replace('add','0000') for item in list_new]
list_new = [item.replace('andi','0011') for item in list_new]
list_new = [item.replace('and','0010') for item in list_new]
list_new = [item.replace('beq','0100') for item in list_new]
list_new = [item.replace('bne','0101') for item in list_new]
list_new = [item.replace('jr','1010') for item in list_new]
list_new = [item.replace('jal','1110') for item in list_new]
list_new = [item.replace('j','0110') for item in list_new]
list_new = [item.replace('lb','1011') for item in list_new]
list_new = [item.replace('or','1100') for item in list_new]
list_new = [item.replace('sb','1101') for item in list_new]
list_new = [item.replace('sll','1110') for item in list_new]
list_new = [item.replace('srl','1111') for item in list_new]

#with open(name_archivo,"r") as f:
 #   text = f.read()
  #  list_new = [item.replace()]
   # words = text.split()
    #table = str.maketrans("", "", string.punctuation)
    #stripped = [W.translate(table) for W in words]
    #print (stripped)
    
#list_new = [item.replace('addi','0001') for item in stripped]
#list_new = [item.replace('add','0000') for item in stripped]
print(list_new)

