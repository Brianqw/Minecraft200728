# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:02:52 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

import random

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

color=random.randrange(0,16)
mc.setBlocks(x+25,y-1,z+25,
            x-25,y-1,z-25,95,color)




































