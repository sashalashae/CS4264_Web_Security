#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �������:���$�P9��C枿B�m,���-h�O.e��-�x.ߘI�h��H��}'�g�Z&�J��K�,X���w�v=߭ߺW�9�J�j��l|�p���3��j�m�-y�
"""

from hashlib import sha256
x = sha256(blob).hexdigest()

y = '8de93c7497141f69099acc65c2bf1f3825baeb0b3fede8064b4bf346238166be'
z = '9630d13cb2a9647e1ff54c30166f95b385673d838897d2c7f359a55a983765b6'

if str(x)==y:
    print "I come in peace"
elif str(x) == z:
    print "Prepare to be destroyed!"

