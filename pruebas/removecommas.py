#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
#PRUEBA COMAS

import string

with open("codigo1.txt","r") as f:
    text = f.read()
    words = text.split()
    
    table = str.maketrans("", "", string.punctuation)
    stripped = [W.translate(table) for W in words]
    print (stripped)
