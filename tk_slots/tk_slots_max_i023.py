import MaxPlus; maxEval = MaxPlus.Core.EvalMAXScript
from pymxs import runtime as rt

import os.path

from tk_slots import Slot
import tk_max_shared_functions as func












class I023(Slot):
	def __init__(self, *args, **kwargs):
		super(I023, self).__init__(*args, **kwargs)

		#init widgets
		func.initWidgets(self)


	def b000(self): #
		pass

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