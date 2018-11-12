import MaxPlus; maxEval = MaxPlus.Core.EvalMAXScript
from pymxs import runtime as rt

import os.path

from tk_slots import Slot
import tk_max_shared_functions as func



#          oo                                                  dP   
#                                                              88   
# dP   .dP dP .d8888b. dP  dP  dP 88d888b. .d8888b. 88d888b. d8888P 
# 88   d8' 88 88ooood8 88  88  88 88'  `88 88'  `88 88'  `88   88   
# 88 .88'  88 88.  ... 88.88b.88' 88.  .88 88.  .88 88         88   
# 8888P'   dP `88888P' 8888P Y8P  88Y888P' `88888P' dP         dP   
#                                 88                                
#                                 dP                                
#
class Viewport(Slot):
	def __init__(self, *args, **kwargs):
		super(Viewport, self).__init__(*args, **kwargs)

		#init widgets
		func.initWidgets(self)
	

	def v000(self): #viewport: back view
		maxEval('''
		if (`objExists back`)
		{
		  lookThru back;
		}
		else
		{
		  //create camera
		  string $cameraName[] = `camera`;
		  //cameraName[0] = camera node
		  //cameraName[1] = camera shape node

		  //rename camera node
		  rename($cameraName[0], "back");
		  lookThru back;

		  //initialize the camera view
		  viewSet -back;

		  //add to camera group
		  if (`objExists cameras`)
		  {
			parent back cameras;
		  }
		}
		''')

	def v001(self): #viewport: top view
		pm.lookThru ("topShape")

	def v002(self): #viewport: right view
		pm.lookThru ("sideShape")

	def v003(self): #viewport: left view
		maxEval('''
		if (`objExists left`)
		{
		  lookThru left;
		}
		else
		{
		  string $cameraName[] = `camera`;
		  //cameraName[0] = camera node
		  //cameraName[1] = camera shape node

		  rename($cameraName[0], "left");
		  lookThru left;

		  //initialize the camera view
		  viewSet -leftSide;

		  //add to camera group
		  if (`objExists cameras`)
		  {
			parent left cameras;
		  }
		}
		''')

	def v004(self): #viewport: perspective view
		pm.lookThru ("perspShape")

	def v005(self): #viewport: front view
		pm.lookThru ("frontShape")

	def v006(self): #viewport: bottom view
		maxEval('''
		if (`objExists bottom`)
		{
		  lookThru bottom;
		}
		else
		{
		  //create camera
		  string $cameraName[] = `camera`;
		  //cameraName[0] = camera node
		  //cameraName[1] = camera shape node

		  //rename camera node
		  rename($cameraName[0], "bottom");
		  lookThru bottom;

		  //initialize the camera view
		  viewSet -bottom;

		  //add to camera group
		  if (`objExists cameras`)
		  {
			parent bottom cameras;
		  }
		}
		''')

	def v007(self): #viewport: align view
		maxEval('''
		$cameraExists = `objExists alignToPoly`; //check exists if not create camera
		if ($cameraExists != 1)
		{ 
			string $camera[] = `camera`;
			string $cameraShape = $camera[1];

			rename $camera[0] ("alignToPoly");
			hide alignToPoly;
		}

		int $isPerspective = !`camera -query -orthographic alignToPoly`; //check if camera view is orthoraphicz
		if ($isPerspective) 
		{
			viewPlace -ortho alignToPoly;
		}

		lookThru alignToPoly;
		AlignCameraToPolygon;
		viewFit -fitFactor 5.0;

		//add to camera group
		if (`objExists cameras`)
		{
			parent alignToPoly cameras;
		}
		''')

	def v008(self): #component mode:vertex
		pm.selectMode (component=True)
		pm.selectType (subdivMeshPoint=1, polymeshVertex=True)
		func.viewPortMessage("<hl>vertex</hl> mask.")

	def v009(self): #component mode:edge
		pm.selectMode (component=True)
		pm.selectType (subdivMeshEdge=1, polymeshEdge=True)
		func.viewPortMessage("<hl>edge</hl> mask.")

	def v010(self): #component mode:facet
		pm.selectMode (component=True)
		pm.selectType (subdivMeshFace=1, polymeshFace=True)
		func.viewPortMessage("<hl>facet</hl> mask.")

	def v011(self): #object mode
		pm.selectMode (object=True)
		func.viewPortMessage("<hl>object</hl> mode.")

	def v012(self): #component mode:uv
		pm.selectMode (component=True)
		pm.selectType (subdivMeshUV=True, polymeshUV=True)
		func.viewPortMessage("<hl>UV</hl> mask.")

	def v013(self): #
		pass

	def v014(self): #
		pass

	def v015(self): #
		pass


	def v000(self): #viewport: back view
		self.hbHide()
		maxEval("max vpt back")

	def v001(self): #viewport: top view
		self.hbHide()
		maxEval("max vpt top")

	def v002(self): #viewport: right view
		self.hbHide()
		maxEval("max vpt right")

	def v003(self): #viewport: left view
		self.hbHide()
		maxEval("max vpt left")

	def v004(self): #viewport: perspective view
		self.hbHide()
		maxEval("max vpt persp user")

	def v005(self): #viewport: front view
		self.hbHide()
		maxEval("max vpt front")

	def v006(self): #viewport: bottom view
		self.hbHide()
		maxEval("max vpt bottom")

	def v007(self): #viewport: align view
		self.hbHide()
		maxEval('''
		max vpt iso user
		max align camera
		''')


#print module name
print os.path.splitext(os.path.basename(__file__))[0]
# -----------------------------------------------
# Notes
# -----------------------------------------------