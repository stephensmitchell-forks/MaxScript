import MaxPlus; maxEval = MaxPlus.Core.EvalMAXScript
from pymxs import runtime as rt

import os.path

from tk_slots import Slot
import tk_max_shared_functions as func




#          oo                   oo                   
#                                                 
# 88d888b. dP .d8888b. .d8888b. dP 88d888b. .d8888b. 
# 88'  `88 88 88'  `88 88'  `88 88 88'  `88 88'  `88 
# 88       88 88.  .88 88.  .88 88 88    88 88.  .88 
# dP       dP `8888P88 `8888P88 dP dP    dP `8888P88 
#                  .88      .88                  .88 
#              d8888P   d8888P               d8888P  
#
class Rigging(Slot):
	def __init__(self, *args, **kwargs):
		super(Rigging, self).__init__(*args, **kwargs)

		#init widgets
		func.initWidgets(self)


	def b000(self): #
		maxEval('')

	def b001(self): #
		maxEval('')

	def b002(self): #
		maxEval('')

	def b003(self): #
		maxEval('')

	def b004(self): #
		maxEval('')

	def b005(self): #
		maxEval('')

	def b006(self): #
		maxEval('')

	def b007(self): #
		maxEval('')

	def b008(self): #
		mel.eval("")

	def b009(self): #
		maxEval('')



#print module name
print os.path.splitext(os.path.basename(__file__))[0]
# -----------------------------------------------
# Notes
# -----------------------------------------------