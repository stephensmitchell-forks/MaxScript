import MaxPlus; maxEval = MaxPlus.Core.EvalMAXScript
from pymxs import runtime as rt

import os.path

from tk_slots import Slot
import tk_max_shared_functions as func




#                                                 dP          
#                                                 88          
#  88d888b. .d8888b. 88d888b. 88d8b.d8b. .d8888b. 88 .d8888b. 
#  88'  `88 88'  `88 88'  `88 88'`88'`88 88'  `88 88 Y8ooooo. 
#  88    88 88.  .88 88       88  88  88 88.  .88 88       88 
#  dP    dP `88888P' dP       dP  dP  dP `88888P8 dP `88888P' 
#                                                                                                                 
class Normals(Slot):
	def __init__(self, *args, **kwargs):
		super(Normals, self).__init__(*args, **kwargs)

		#init widgets
		func.initWidgets(self)


	def b000(self): #Display face normals
		size = float(self.ui.s001.value())
		# state = pm.polyOptions (query=True, displayNormal=True)
		state = func.cycle('displayNormals_1230')
		if state ==0: #off
			pm.polyOptions (displayNormal=0, sizeNormal=0)
			pm.polyOptions (displayTangent=False)
			func.viewPortMessage("Normals Display <hl>Off</hl>.")
		if state ==1: #facet
			pm.polyOptions (displayNormal=1, facet=True, sizeNormal=size)
			pm.polyOptions (displayTangent=False)
			func.viewPortMessage("<hl>Facet</hl> Normals Display <hl>On</hl>.")
		if state ==2: #Vertex
			pm.polyOptions (displayNormal=1, point=True, sizeNormal=size)
			pm.polyOptions (displayTangent=False)
			func.viewPortMessage("<hl>Vertex</hl> Normals Display <hl>On</hl>.")
		if state ==3: #tangent
			pm.polyOptions (displayTangent=True)
			pm.polyOptions (displayNormal=0)
			func.viewPortMessage("<hl>Tangent</hl> Display <hl>On</hl>.")
			
	def b001(self): #Soften edge normal
		pm.polySoftEdge (angle=180, constructionHistory=0)

	def b002(self): #Harden edge normal
		pm.polySoftEdge (angle=0, constructionHistory=0)

	def b003(self): #Soft edge display
		maxEval('int $g_cond[1]=`polyOptions -q -ae`; if ($g_cond[0]) polyOptions -se; else polyOptions -ae;')

	def b004(self): #Set normal angle
		normalAngle = str(self.ui.s000.value())
		pm.polySetToFaceNormal (setUserNormal=1) #reset to face
		pm.polySoftEdge (angle=normalAngle) #smooth if angle is lower than specified amount. default 30

	def b005(self): #Maya bonus tools: Adjust vertex normals
		maxEval('bgAdjustVertexNormalsWin;')

	def b006(self): #Set to face
		maxEval('polySetToFaceNormal;')

	def b007(self): #Average normals
		maxEval('polySetToFaceNormal;polyAverageNormal;')

	def b008(self): #harden creased edges
		mel.eval("PolySelectConvert 2")
		edges = pm.polyListComponentConversion (toEdge=1)
		edges = pm.ls (edges, flatten=1)

		pm.undoInfo (openChunk=1)
		func.mainProgressBar (len(edges))

		soften = self.ui.chk000.isChecked()

		for edge in edges:
			pm.progressBar ("tk_progressBar", edit=1, step=1)
			if pm.progressBar ("tk_progressBar", query=1, isCancelled=1):
				break
			crease = pm.polyCrease (edge, query=1, value=1)
			# print edge, crease[0]
			if crease[0]>0:
				pm.polySoftEdge (edge, angle=30)
			elif soften:
				pm.polySoftEdge (edge, angle=180)
		pm.progressBar ("tk_progressBar", edit=1, endProgress=1)
		pm.undoInfo (closeChunk=1)

	def b009(self): #Harden UV edges
		def createArrayFromSelection (): #(string sel[])	/* returns a string array of the selected transform nodes
			pm.select (hierarchy=1)
			nodes = pm.ls (selection=1, transforms=1)
			groupedNodes = pm.listRelatives (type="transform") #if the nodes are grouped then just get the children

			if groupedNodes[0] != "":	#check to see if the nodes are grouped
				size = len(groupedNodes)
				clear (nodes)
				appendStringArray(nodes, groupedNodes, size)
			return nodes

		uvBorder=edgeUVs=finalBorder=[]
		nodes = createArrayFromSelection()

		for node in nodes:
			pm.select (node, replace=1)
			pm.polyNormalPerVertex (unFreezeNormal=True)
			pm.polySoftEdge (node, angle=180, constructionHistory=1)
			maxEval('select -replace '+node+'.map["*"];')

			mel.eval("polySelectBorderShell 1;")

			uvBorder = pm.polyListComponentConversion (toEdge=1, internal=1)
			uvBorder = pm.ls (uvBorder, flatten=1)

			pm.clear(finalBorder)

			for curEdge in uvBorder:
				edgeUVs = pm.polyListComponentConversion (curEdge, toUv=1)
				edgeUVs = pm.ls (edgeUVs, flatten=1)

				if len(edgeUVs) >2:
					finalBorder[len(finalBorder)] = curEdge
				pm.polySoftEdge (finalBorder, angle=0, constructionHistory=1)

			pm.select (nodes, replace=1)

	def b010(self): #Reverse normals
		maxEval('ReversePolygonNormals;')

	def b011(self): #Lock/unlock vertex normals
		all_ = self.ui.chk001.isChecked()
		state = self.ui.chk002.isChecked()#pm.polyNormalPerVertex(vertex, query=1, freezeNormal=1)
		selection = pm.ls (selection=1, objectsOnly=1)
		maskObject = pm.selectMode (query=1, object=1)
		maskVertex = pm.selectType (query=1, vertex=1)

		if len(selection)>0:
			if (all_ and maskVertex) or maskObject:
				for obj in selection:
					count = pm.polyEvaluate(obj, vertex=1) #get number of vertices
					vertices = [vertices.append(str(obj) + ".vtx ["+str(num)+"]") for num in xrange(count)] #geometry.vtx[0]
					for vertex in vertices:
						if state:
							pm.polyNormalPerVertex(vertex, unFreezeNormal=1)
						else:
							pm.polyNormalPerVertex(vertex, freezeNormal=1)
					if state:
						func.viewPortMessage("Normals <hl>UnLocked</hl>.")
					else:
						func.viewPortMessage("Normals <hl>Locked</hl>.")
			elif maskVertex and not maskObject:
				if state:
					pm.polyNormalPerVertex(unFreezeNormal=1)
					func.viewPortMessage("Normals <hl>UnLocked</hl>.")
				else:
					pm.polyNormalPerVertex(freezeNormal=1)
					func.viewPortMessage("Normals <hl>Locked</hl>.")
			else:
				print "// Warning: Selection must be object or vertex. //"
		else:
			print "// Warning: No object selected. //"

	def b012(self): #
		pass
		



#print module name
print os.path.splitext(os.path.basename(__file__))[0]
# -----------------------------------------------
# Notes
# -----------------------------------------------
	#b008, b009, b012