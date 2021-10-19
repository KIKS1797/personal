#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

def main():
    """
    Comentario de la función
    """
name_archivo=input("ingresar archivo:   ")
datos=open(name_archivo,"r")
datos_leidos = datos.readlines()

valores = []
   
for i in range(len(datos_leidos)):
    valores.append(datos_leidos[i].rstrip().split()) 

print(valores)

if __name__ == "__main__":
    main()

