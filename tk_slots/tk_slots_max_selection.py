import MaxPlus; maxEval = MaxPlus.Core.EvalMAXScript
from pymxs import runtime as rt

import os.path

from tk_slots import Slot
import tk_max_shared_functions as func





#                    dP                     dP   oo                   
#                    88                     88                        
#  .d8888b. .d8888b. 88 .d8888b. .d8888b. d8888P dP .d8888b. 88d888b. 
#  Y8ooooo. 88ooood8 88 88ooood8 88'  `""   88   88 88'  `88 88'  `88 
#        88 88.  ... 88 88.  ... 88.  ...   88   88 88.  .88 88    88 
#  `88888P' `88888P' dP `88888P' `88888P'   dP   dP `88888P' dP    dP 
#                                                           
class Selection(Slot):
	def __init__(self, *args, **kwargs):
		super(Selection, self).__init__(*args, **kwargs)

		#init widgets
		func.initWidgets(self)
		

		#set checked button states
		#chk004 ignore backfacing (camera based selection)
		state = pm.selectPref(query=True, useDepth=True)
		self.ui.chk004.setChecked(state)

		#on click event
		self.ui.chk003.clicked.connect(self.b001) #un-paint

		#symmetry: set initial checked state
		state = pm.symmetricModelling(query=True, symmetry=True) #application symmetry state
		axis = pm.symmetricModelling(query=True, axis=True)
		if axis == "x":
			self.ui.chk000.setChecked(state)
		if axis == "y":
			self.ui.chk001.setChecked(state)
		if axis == "z":
			self.ui.chk002.setChecked(state)

	def setSymmetry(self, axis, symmetry):
		if self.ui.chk005.isChecked():
			space = "object"
		if self.ui.chk006.isChecked():
			space = "topo"
		else:
			space = "world"

		tolerance = float(self.ui.s005.value())
		pm.symmetricModelling(edit=True, symmetry=symmetry, axis=axis, about=space, tolerance=tolerance)

	def t000(self): #select the selection set itself (not members of)
		name = str(self.ui.t000.text())+"Set"
		pm.select (name, noExpand=1) #noExpand=select set itself

	def t001(self): #Select by name
		searchStr = str(self.ui.t001.text()) #asterisk denotes startswith*, *endswith, *contains* 
		if searchStr:
			selection = pm.select (pm.ls (searchStr))

	def chk000(self): #Symmetry X
		func.setButtons(self.ui, unchecked='chk001,chk002')
		state = self.ui.chk000.isChecked() #symmetry button state
		self.setSymmetry("x", symmetry=state)

	def chk001(self): #Symmetry Y
		func.setButtons(self.ui, unchecked='chk000,chk002')
		state = self.ui.chk001.isChecked() #symmetry button state
		self.setSymmetry("y", symmetry=state)

	def chk002(self): #Symmetry Z
		func.setButtons(self.ui, unchecked='chk000,chk001')
		state = self.ui.chk002.isChecked() #symmetry button state
		self.setSymmetry("z", symmetry=state)

	def chk004(self): #Ignore backfacing (camera based selection)
		if self.ui.chk004.isChecked():
			pm.selectPref(useDepth=True)
			func.viewPortMessage("Camera-based selection <hl>On</hl>.")
		else:
			pm.selectPref(useDepth=False)
			func.viewPortMessage("Camera-based selection <hl>Off</hl>.")

	def chk005(self): #Symmetry: object
		self.ui.chk006.setChecked(False) #uncheck symmetry:topological
	
	def chk006(self): #Symmetry: topo
		self.ui.chk005.setChecked(False) #uncheck symmetry:object space
		if any ([self.ui.chk000.isChecked(), self.ui.chk001.isChecked(), self.ui.chk002.isChecked()]): #(symmetry)
			pm.symmetricModelling(edit=True, symmetry=False)
			func.setButtons(self.ui, unchecked='chk000,chk001,chk002')
			print "# Warning: First select a seam edge and then check the symmetry button to enable topographic symmetry #"

	def cmb000(self): #List selection sets
		index = self.ui.cmb000.currentIndex() #get current index before refreshing list
		sets = func.comboBox (self.ui.cmb000, [str(set_) for set_ in pm.ls (et="objectSet", flatten=1)], "Sets")

		if index!=0:
			pm.select (sets[index])
			self.ui.cmb000.setCurrentIndex(0)

	def cmb001(self): #currently selected objects
		index = self.ui.cmb001.currentIndex() #get current index before refreshing list
		items = func.comboBox (self.ui.cmb001, [str(s) for s in pm.ls (selection=1, flatten=1)], "Currently Selected")

		if index!=0:
			pm.select (items[index])
			self.ui.cmb001.setCurrentIndex(0)

	def b000(self): #Create selection set
		name = str(self.ui.t000.text())+"Set"
		if pm.objExists (name):
			pm.sets (name, clear=1)
			pm.sets (name, add=1) #if set exists; clear set and add current selection 
		else: #create set
			pm.sets (name=name, text="gCharacterSet")
			self.ui.t000.clear()
			
	def b001(self): #Paint select
		if pm.contextInfo ("paintSelect", exists=True):
			pm.deleteUI ("paintSelect")

		radius = float(self.ui.s001.value()) #Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
		lowerradius = 2.5 #Sets the lower size of the brush (only apply on tablet).
		selectop = "select"
		if self.ui.chk003.isChecked():
			selectop = "unselect"

		pm.artSelectCtx ("paintSelect", selectop=selectop, radius=radius, lowerradius=lowerradius)#, beforeStrokeCmd=beforeStrokeCmd())
		pm.setToolTo ("paintSelect")

	def b002(self): #
		pass

	def b003(self): #
		pass

	def b004(self): #
		pass

	def b005(self): #
		pass

	def b006(self): #Select similar
		tolerance = str(self.ui.s000.value()) #string value because mel.eval is sending a command string
		mel.eval("doSelectSimilar 1 {\""+ tolerance +"\"}")

	def b007(self): #Select polygon face island
		rangeX = float(self.ui.s002.value())
		rangeY = float(self.ui.s003.value())
		rangeZ = float(self.ui.s004.value())
		mel.eval("tk_selectPolyFaceIsland("+str(rangeX)+","+str(rangeY)+","+str(rangeZ)+")")

	def b008(self): #Select N-th edge
		mel.eval("selectEveryNEdge;")

	def b009(self): #Select contigious edge loop
		maxEval('SelectContiguousEdges;')

	def b10(self): #Select contigious edge loop options
		maxEval('SelectContiguousEdgesOptions;')

	def b011(self): #Shortest edge path
		func.shortestEdgePath()
		# maxEval('SelectShortestEdgePathTool;')

	def b012(self): #Selection constraints
		maxEval('PolygonSelectionConstraints;')

	def b013(self): #Lasso select
		mel.eval("LassoTool;")

	def b014(self): #Grow selection
		maxEval('GrowPolygonSelectionRegion;')

	def b015(self): #Shrink selection
		maxEval('ShrinkPolygonSelectionRegion;')

	def b016(self): #Convert selection to vertices
		maxEval('PolySelectConvert 3;')

	def b017(self): #Convert selection to edges
		maxEval('PolySelectConvert 2;')

	def b018(self): #Convert selection to faces
		maxEval('PolySelectConvert 1;')

	def b019(self): #Convert selection to edge ring
		maxEval('SelectEdgeRingSp;')

	def b020(self): #select edge ring
		print "# Warning: add correct arguments for this tool #" 
		func.shortestEdgePath()




	def b000(self): #Selection sets
		self.hbHide()
		maxEval('macros.run \"Edit\" \"namedSelSets\"')

	def b001(self): #select contigious edge loop
		self.hbHide()
		maxEval('''
		curmod = Modpanel.getcurrentObject()
		if ( Ribbon_Modeling.IsEditablePoly() ) then
		(
			curmod.SelectEdgeRing();
		)
		else
		(
			curmod.ButtonOp #SelectEdgeRing;
		)
		''')

	def b002(self): #Shrink selection
		self.hbHide()
		#expand functionalitly as outlined below
		maxEval('''
		classString = makeSelection "Current" 1 classInfo

		if (classString[6] != Editable_Poly) then
		(
			--Shrink Selection
			curmod = Modpanel.getcurrentObject()
			if ( Ribbon_Modeling.IsEditablePoly() ) then
				curmod.ShrinkSelection()
		)
		else
		(
			--Shink Selection (Poly)
			Try (
				local A = Filters.GetModOrObj()
				A.buttonOp #ShrinkSelection
				)
			Catch (curmod.ButtonOp #ShrinkSelection)
		)
		''')

	def b003(self): #Grow selection
		self.hbHide()
		# expand functionalitly to grow according to selection type
		#grow line #PolytoolsSelect.Pattern7 1
		#grow loop #PolytoolsSelect.GrowLoop()
		#grow ring #PolytoolsSelect.GrowRing()
		maxEval('''
		curmod = Modpanel.getcurrentObject()
		if ( Ribbon_Modeling.IsEditablePoly() ) then
			curmod.GrowSelection()
		else
			curmod.ButtonOp #GrowSelection
		''')

	def b004(self): #
		self.hbHide()
		maxEval('')

	def b005(self): #
		self.hbHide()
		maxEval('')

	def b006(self): #
		self.hbHide()
		maxEval('')

	def b007(self): #
		self.hbHide()
		maxEval('')

	def b008(self): #
		self.hbHide()
		maxEval("")

	def b009(self): #
		self.hbHide()
		maxEval('')

#print module name
print os.path.splitext(os.path.basename(__file__))[0]
# -----------------------------------------------
# Notes
# -----------------------------------------------