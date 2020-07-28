# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:46:51 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

w=10
h=10
i=10

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
mc.setBlocks(x,y,z,x+w,y+h,z+1,57)
mc.setBlocks(x+1,y+1,z+1,
             x+w-1,y+h-1,z+1,1,0)












































