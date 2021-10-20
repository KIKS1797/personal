#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later



def readFile(fileName):
    fileObj = open(fileName, "r")
    words = fileObj.read().splitlines()
    fileObj.close()
    return words


#...
#main
filename = input("ingresar nombre del archivo:   ")
file = readFile(filename)

