import MaxPlus; maxEval = MaxPlus.Core.EvalMAXScript
from pymxs import runtime as rt

import os.path

from tk_slots import Slot
import tk_max_shared_functions as func







# .d8888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b. .d8888b. 
# 88'  `"" 88'  `88 88'`88'`88 88ooood8 88'  `88 88'  `88 Y8ooooo. 
# 88.  ... 88.  .88 88  88  88 88.  ... 88       88.  .88       88 
# `88888P' `88888P8 dP  dP  dP `88888P' dP       `88888P8 `88888P'                                                               
#
class Cameras(Slot):
	def __init__(self, *args, **kwargs):
		super(Cameras, self).__init__(*args, **kwargs)

		#init widgets
		func.initWidgets(self)


	def chk000(self): #pin open a separate instance of the ui in a new window
		if self.ui.chk000.isChecked():
			print 'chk000'
			self.hotBox.pin(self.ui)
		else:
			self.hotBox.pin.hide()

	def b000(self): #
			pass

	def b001(self): #Custom camera
		maxEval('cameraView -edit -camera persp -setCamera $homeName;')

	def b002(self): #Set custom camera
		maxEval('string $homeName = `cameraView -camera persp`;')

	def b003(self): #Camera from view
		maxEval('')

	def b004(self): #Group cameras
		maxEval('''
		if (`objExists cameras`)
		{
		  print "Group 'cameras' already exists";
		}
		else
		{
		  group -world -name cameras side front top persp;
		  hide cameras;
		  // Now add non-default cameras to group
		  if (`objExists back`)
		  {
		  	parent back cameras;
		  }
		  if (`objExists bottom`)
		  {
		  	parent bottom cameras;
		  }
		  if (`objExists left`)
		  {
		  	parent left cameras;
		  }
		  if (`objExists alignToPoly`)
		  {
		  	parent alignToPoly cameras;
		  }
		}
		''')

	def b005(self): #Camera sequencer
		maxEval('SequenceEditor;')

	def b006(self): #Camera set editor
		maxEval('cameraSetEditor;')

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