#|||||||||||||||||||||||||||||||||||||||||||||||
#||||||	   functions for tk_main (max)   	||||||
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import MaxPlus
maxEval = MaxPlus.Core.EvalMAXScript

import pymxs
rt = pymxs.runtime

from ctypes import windll, Structure, c_long, byref


#--getMousePosition--------------------------------------------------------------------

class POINT(Structure):
	_fields_ = [("x", c_long), ("y", c_long)]

def getMousePosition():
	pt = POINT()
	windll.user32.GetCursorPos(byref(pt))
	return { "x": pt.x, "y": pt.y}




#--getKeyState---------------------------------------------------------------------------

#The state will either be 0 or 1 when not pressed, and increase to something like 60000 when 
#pressed, so to get a True/False result, checking for > 1
#key = virtual-key code #https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
#microsoft docs: https://msdn.microsoft.com/en-us/library/windows/desktop/ff468859(v=vs.85).aspx
def getKeyState(key):
	if (key == "shift"): #VK_LSHIFT #left
		key = 0xA0
	if (key == "ctrl"): #VK_CONTR
		key = 0x11
	if (key == "alt"): #VK_MENU
		key = 0x12
	if (key == "del"): #VK_DELETE
		key = 0x2E
	if (key == "esc"): #VK_ESCAPE
		key = 0x1B
	if (key == "enter"): #VK_RETURN
		key = 0x0D
	value = windll.user32.GetKeyState(key)
	if (value > 1):
		return True #key down
	else:
		return False #key up




#--makeSelection-------------------------------------------------------------------------

# class Selection:

#builds a selection array, according to arguments.
#arg = selection type. "Current", "Geometry", "All"
#index = index of array element to return. 0 = all
#functionCall; if specified will call the specified fuction with selection as argument
def makeSelection (selectionType, arrayIndex, functionCall=None):

	if (selectionType == "Current"):
		maxEval("sel = $") #store FPValue
		sel = rt.sel	#get FPValue

	if (selectionType == "Geometry"):
		maxEval("sel = Geometry")
		sel = rt.sel

	if (selectionType == "All"):
		sel = maxEval("sel = $*")
		sel = rt.sel

	selectionArray = []
	
	if (sel < 1): # check if sel is empty
		print "-< Nothing selected >-"
		return "noSelection" #or rt.undefined

	if (len(sel) == 0): #check if selection is not an array
		selectionArray.append(sel)
		
	else: #else if array, build python array
		for obj in sel:
			selectionArray.append(obj)

	if (arrayIndex == 0):
		#~ print selectionArray
		if (functionCall != None):
			return functionCall(selectionArray);
		else:
			return selectionArray

	if (arrayIndex >= 1): #subtract one index position to match maxscript convention
		#~ print selectionArray[arrayIndex]
		if (functionCall != None):
			return functionCall(selectionArray[arrayIndex-1]); 
		else:
			return selectionArray[arrayIndex-1];



#--filterSelectionByBaseClass-------------------------------------------------------------

# returns the base class type as a string
def filterSelectionByBaseClass (baseObjClass):
	
	obj = baseObjClass

	#Editable Mesh
	if (obj == rt.Editable_Poly):
		return "Editable_Poly"
	
	if (obj == rt.Editable_Patch): #no pymxs.runtime attribute Editable_Patch
		return "Editable_Patch"
	
	if (obj == rt.Editable_mesh): #no pymxs.runtime attribute Editable_mesh
		return "Editable_Mesh"
		
	if (obj == rt.NURBSSurf): #no pymxs.runtime attribute NURBSSurf
		return "NURBSSurf"

	#Shapes
	if (obj == rt.Line or \
		obj == rt.Circle or \
		obj == rt.Arc or \
		obj == rt.NGon or \
		obj == rt.Text or \
		obj == rt.Egg or \
		obj == rt.Rectangle or \
		obj == rt.Ellipse or \
		obj == rt.Donut or \
		obj == rt.Star or \
		obj == rt.Helix or \
		obj == rt.Section):
		return "Shape"

	#Geometry
	if (obj == rt.Box or \
		obj == rt.Sphere or \
		obj == rt.Cylinder or \
		obj == rt.Torus or \
		obj == rt.Teapot or \
		obj == rt.TextPlus or \
		obj == rt.Cone or \
		obj == rt.GeoSphere or \
		obj == rt.Tube or \
		obj == rt.Pyramid or \
		obj == rt.Plane):
		return "Geometry"

#--classInfo-----------------------------------------------------------------------------

#returns various object class information as elements in an array
#calls filterSelectionByBaseClass()
def classInfo (obj, query=False):
	#functions used:
	#~ filterSelectionByBaseClass()

	if (obj == "noSelection"):
		return obj #rt.undefined

	baseObj = obj.baseObject
	baseObjClass = rt.classOf(baseObj) #get the base object class.  ie. Editable_Poly
	classTypeString = filterSelectionByBaseClass(baseObjClass) #func takes the base object class and returns the type as a string
	superClass = rt.superClassOf(obj)
	isValid = rt.isValidNode(obj)
	subObjectLevel = rt.getSelectionLevel(obj)
	
	# selectedVerts = rt.selectedVerts(obj)
	# selectedEdges = rt.selectedEdges(obj)
	# selectedFaces = rt.selectedFaces(obj)
	
	# numOfVerts = objMesh.GetNumVertices()
	# numOfFaces = objMesh.GetNumFaces()
	
	# faceBitArray = MaxPlus.BitArray(numFaces)
	# vertBitArray = MaxPlus.BitArray(numVerts)
	
	superClassString = "superClass: Unknown"
	if (superClass == rt.GeometryClass):
		superClassString = "GeometryClass"
	if (superClass == rt.shape):
		superClassString = "shape"
	if (superClass == rt.light):
		superClassString = "light"
	if (superClass == rt.camera):
		superClassString = "camera"
	if (superClass == rt.SpacewarpObject):
		superClassString = "SpacewarpObject"
	if (superClass == rt.helper):
		superClassString = "helper"
	if (superClass == rt.system):
		superClassString = "system"
	#rt.default: "default" #aka unknown type


	baseObjClassString = "objectClass: Unknown"
	if (baseObjClass == rt.Editable_Poly):
		baseObjClassString = "Editable_Poly"
	if (baseObjClass == rt.Editable_mesh):
		baseObjClassString = "Editable_Mesh"
	if (baseObjClass == rt.Editable_Patch):
		baseObjClassString = "Editble_Patch"
	if (baseObjClass == rt.NURBSSurf):
		baseObjClassString = "NURBSSurf"
	if (baseObjClass == rt.Box):
		baseObjClassString = "Box"
	if (baseObjClass == rt.Sphere):
		baseObjClassString = "Sphere"
	if (baseObjClass == rt.Cylinder):
		baseObjClassString = "Cylinder"
	if (baseObjClass == rt.Torus):
		baseObjClassString = "Torus"
	if (baseObjClass == rt.Teapot):
		baseObjClassString = "Teapot"
	if (baseObjClass == rt.TextPlus):
		baseObjClassString = "TextPlus"
	if (baseObjClass == rt.Cone):
		baseObjClassString = "Cone"
	if (baseObjClass == rt.GeoSphere):
		baseObjClassString = "GeoSphere"
	if (baseObjClass == rt.Tube):
		baseObjClassString = "Tube"
	if (baseObjClass == rt.Pyramid):
		baseObjClassString = "Pyramid"
	if (baseObjClass == rt.Plane):
		baseObjClassString = "Plane"
	if (baseObjClass == rt.Line):
		baseObjClassString = "Line"
	if (baseObjClass == rt.Circle):
		baseObjClassString = "Circle"
	if (baseObjClass == rt.Arc):
		baseObjClassString = "Arc"
	if (baseObjClass == rt.NGon):
		baseObjClassString = "NGon"
	if (baseObjClass == rt.Text):
		baseObjClassString = "Text"
	if (baseObjClass == rt.Egg):
		baseObjClassString = "Egg"
	if (baseObjClass == rt.Rectangle):
		baseObjClassString = "Rectangle"
	if (baseObjClass == rt.Ellipse):
		baseObjClassString = "Line"
	if (baseObjClass == rt.Donut):
		baseObjClassString = "Donut"
	if (baseObjClass == rt.Star):
		baseObjClassString = "Star"
	if (baseObjClass == rt.Helix):
		baseObjClassString = "Helix"
	if (baseObjClass == rt.Section):
		baseObjClassString = "Section"

	
	returnedClassInfoArray = []
	returnedClassInfoArray.append(obj)
	returnedClassInfoArray.append(baseObj)
	returnedClassInfoArray.append(superClass)
	returnedClassInfoArray.append(superClassString)
	returnedClassInfoArray.append(baseObjClass)
	returnedClassInfoArray.append(baseObjClassString)
	returnedClassInfoArray.append(classTypeString)
	returnedClassInfoArray.append(isValid)
	returnedClassInfoArray.append(subObjectLevel)
	# returnedClassInfoArray.append(selectedVerts)
	# returnedClassInfoArray.append(selectedEdges)
	# returnedClassInfoArray.append(selectedFaces)
	# returnedClassInfoArray.append(numberOfVerts)
	# returnedClassInfoArray.append(numberOfFaces)
	# returnedClassInfoArray.append(vertBitArray)
	# returnedClassInfoArray.append(faceBitArray)
	
	
	if (query == True):
		#python index / maxscript array index starting at 1
		print "0-1---object:----------------------", returnedClassInfoArray[0]
		print "1-2---baseObject:------------------", returnedClassInfoArray[1]
		print "2-3---superClass:------------------", returnedClassInfoArray[2]
		print "3-4---superClass:|string|----------", returnedClassInfoArray[3]
		print "4-5---baseObjectClass:-------------", returnedClassInfoArray[4]
		print "5-6---baseObjectClass:|string|-----", returnedClassInfoArray[5]
		print "6-7---baseObjectClass TYPE:|string|", returnedClassInfoArray[6] #eg. Editable,Shape,Geometry
		print "7-8---isValidNode:|bool|-----------", returnedClassInfoArray[7] #True, False, 1, 0
		print "8-9---subObjectLevel:|int|---------", returnedClassInfoArray[8] #[mesh] 0=object level,1=vertex level,2=edge level,3=face,4=polygon,5=element,[poly] 0=object level,1=vertex level,2=edge level,3=border,4=polygon,5=element
		# print "9-10--selectedVerts:|array|--------", returnedClassInfoArray[9] #selectedVerts
		# print "10-11-selectedEdges:|array|--------", returnedClassInfoArray[10] #selectedEdges
		# print "11-12-selectedFaces:|array|--------", returnedClassInfoArray[11] #selectedFaces
		# print "12-13-numberOfVerts:|int|----------", returnedClassInfoArray[12] #number of selected vertices
		# print "13-14-numberOfFaces:|int|----------". returnedClassInfoArray[13] #number of selected faces
		# print "14-15-vertBitArray:----------------", returnedClassInfoArray[14]
		# print "15-16-faceBitArray:----------------", returnedClassInfoArray[15]
		print "="*40

	return returnedClassInfoArray



#--setSnapState--------------------------------------------------------------------------

#set grid and snap settings on or off
#state = string: "true", "false"
def setSnapState (state):

	maxEval('''
	state = false
	if (state == "true") then
	(
		state = true
	)

	/*grid and snap settings*/

	/*body shapes*/
	snapmode.setOSnapItemActive 1 1 (state);
	snapmode.setOSnapItemActive 1 2 (state);
	snapmode.setOSnapItemActive 1 3 (state);
	snapmode.setOSnapItemActive 1 4 (state);
	snapmode.setOSnapItemActive 1 5 (state);
	/*nurbs*/	
	snapmode.setOSnapItemActive 2 1 (state);
	snapmode.setOSnapItemActive 2 2 (state);
	snapmode.setOSnapItemActive 2 3 (state);
	snapmode.setOSnapItemActive 2 4 (state);
	snapmode.setOSnapItemActive 2 5 (state);
	snapmode.setOSnapItemActive 2 6 (state);
	snapmode.setOSnapItemActive 2 7 (state);
	snapmode.setOSnapItemActive 2 8 (state);
	snapmode.setOSnapItemActive 2 9 (state);
	snapmode.setOSnapItemActive 2 10 (state);
	/*Point Cloud Shapes*/
	snapmode.setOSnapItemActive 3 1 (state);
	/*standard*/
	snapmode.setOSnapItemActive 4 1 (state);
	snapmode.setOSnapItemActive 4 2 (state);
	/*standard*/
	snapmode.setOSnapItemActive 5 1 (state);
	snapmode.setOSnapItemActive 5 2 (state);
	/*standard*/
	snapmode.setOSnapItemActive 6 1 (state);
	snapmode.setOSnapItemActive 6 2 (state);
	/*standard*/
	snapmode.setOSnapItemActive 7 1 (state);
	snapmode.setOSnapItemActive 7 2 (state);
	snapmode.setOSnapItemActive 7 3 (state);
	snapmode.setOSnapItemActive 7 4 (state);
	snapmode.setOSnapItemActive 7 5 (state);
	snapmode.setOSnapItemActive 7 6 (state);
	''')


#Detaches editable_mesh elements into new objects	
def detachElement (obj):

	elementArray = []

	print obj[0] #object
	print obj[6] #baseObject class TYPE |string|
	print obj[7] #isValidNode

	if (obj[4] == rt.Editable_Poly and obj[7]): #or obj[6] == "Shape" or obj[6] == "Geometry" 

		rename = obj[0].name	
		rename += "_ele"
		#~ maxEval("undo \"DetachToElement\" on")
		while ((rt.polyOp.getNumFaces(obj[0])) > 0):
			elementToDetach = rt.polyOp.getElementsUsingFace(obj[0],[1]) #(1)
			rt.polyOp.detachFaces(obj[0], elementToDetach, delete=True, asNode=True, name=rename)
		rt.delete(obj[0])
		elementArray = rt.execute("$"+rename+"*")

		rt.select(elementArray)

	else:
		print "-< Object must be an Editable_Poly >-"
	
	return elementArray



#--alignVertices-------------------------------------------------------------------------

#align vertices
# 'vertex.pos.x = vertPosX' ect doesnt work. had to use maxscript
# selection: as array
# mode:
# 0 - YZ
# 1 - XZ
# 2 - XY
# 3 -  X
# 4 -  Y
# 5 -  Z
#notes: (align all vertices at once) by putting each vert index and coordinates in a dict (or two arrays) then if when iterating through a vert falls within the tolerance specified in a textfield align that vert in coordinate. then repeat the process for the other coordinates x,y,z specified by checkboxes. using edges may be a better approach. or both with a subObjectLevel check
#create edge alignment tool and then use subObjectLevel check to call either that function or this one from the same buttons.
#to save ui space; have a single align button, x, y, z, and align 'all' checkboxes and a tolerance textfield.
def alignVertices (selection, mode):

	# maxEval('undo "alignVertices" on')

	componentArray = selection.selectedVerts
	
	if len(componentArray) == 0:
		print "No vertices selected"
	
	if len(componentArray) < 2:
		print "Selection must contain at least two vertices"
		return
	
	lastSelected = componentArray[-1]#3ds max re-orders array by vert index, so this doesnt work for aligning to last selected
	#~ print lastSelected.pos
	aX = lastSelected.pos[0]
	aY = lastSelected.pos[1]
	aZ = lastSelected.pos[2]
	
	for vertex in componentArray:
		#~ print vertex.pos
		vX = vertex.pos[0]
		vY = vertex.pos[1]
		vZ = vertex.pos[2]

		maxEval('global alignXYZ')
		
		if mode == 0: #align YZ
			maxEval('''
			fn alignXYZ mode vertex vX vY vZ aX aY aZ=
			(
				vertex.pos.x = vX
				vertex.pos.y = aY
				vertex.pos.z = aZ
			)
			''')
			
		if mode == 1: #align XZ
			maxEval('''
			fn alignXYZ mode vertex vX vY vZ aX aY aZ=
			(
				vertex.pos.x = aX
				vertex.pos.y = vY
				vertex.pos.z = aZ
			)
			''')
		
		if mode == 2: #align XY
			maxEval('''
			fn alignXYZ mode vertex vX vY vZ aX aY aZ=
			(
				vertex.pos.x = aX
				vertex.pos.y = aY
				vertex.pos.z = vZ
			)
			''')
		
		if mode == 3: #X
			maxEval('''
			fn alignXYZ mode vertex vX vY vZ aX aY aZ=
			(
				vertex.pos.x = aX
				vertex.pos.y = vY
				vertex.pos.z = vZ
			)
			''')
		
		if mode == 4: #Y
			maxEval('''
			fn alignXYZ mode vertex vX vY vZ aX aY aZ=
			(
				vertex.pos.x = vX
				vertex.pos.y = aY
				vertex.pos.z = vZ
			)
			''')
		
		if mode == 5: #Z
			maxEval('''
			fn alignXYZ mode vertex vX vY vZ aX aY aZ=
			(
				vertex.pos.x = vX
				vertex.pos.y = vY
				vertex.pos.z = aZ
			)
			''')
		
		print 100*"-"
		print "vertex.index:", vertex.index
		print "position:", vX, vY, vZ
		print "align:   ", aX, aY, aZ
		
		rt.alignXYZ(mode, vertex, vX, vY, vZ, aX, aY, aZ)
		
		print "result:  ", vertex.pos[0], vertex.pos[1], vertex.pos[2]



#--scaleObject--------------------------------------------------------------------------

#'s' argument is a textfield scale amount
#'x,y,z' arguments are checkbox boolean values. 
#basically working except for final 'obj.scale([s, s, s])' command in python. variable definitions included for debugging. to get working an option is to use the maxEval method in the alignVertices function.
def scaleObject (size, x, y ,z):
	# global tk_textField__000
	tk_textField_000 = 1.50
	tk_isChecked_002 = True
	tk_isChecked_003 = True
	tk_isChecked_004 = True

	s = tk_textField_000
	x = tk_isChecked_002
	y = tk_isChecked_003
	z = tk_isChecked_004
	#-------------------------
	s = size
	sel = makeSelection ("Current", 0)

	for obj in sel:
		if (tk_isChecked_002 and tk_isChecked_003 and tk_isChecked_004):
			obj.scale([s, s, s])
		if (not tk_isChecked_002 and tk_isChecked_003 and tk_isChecked_004):
			obj.scale([1, s, s])
		if (tk_isChecked_002 (not tk_isChecked_003) and tk_isChecked_004):
			obj.scale([s, 1, s])
		if (tk_isChecked_002 and tk_isChecked_003 (not tk_isChecked_004)):
			obj.scale([s, s, 1])
		if (not tk_isChecked_002 (not tk_isChecked_003) and tk_isChecked_004):
			obj.scale([1, 1, s])
		if (tk_isChecked_002 (not tk_isChecked_003) (not tk_isChecked_004)):
			obj.scale([s, 1, 1])
		if (tk_isChecked_002 and tk_isChecked_003 and tk_isChecked_004):
			obj.scale([1, s, 1])
		if (not tk_isChecked_002 (not tk_isChecked_003) (not tk_isChecked_004)):
			obj.scale([1, 1, 1])




#--ExtrudeObject------------------------------------------------------------------------

#extrudes one object at a time but can be called repeatedly for an array of selected objects
#takes classString as an argument which is an array containing the object and class information
#~ --	[0] --object
#~ --	[1] --baseObject
#~ -- [4] --baseObject class
#~ -- [6] --baseObject class type string. eg. Editable,Shape,Geometry
#notes: in another function; if selection (subobjectlevel) is == face or edge, store that face if necessary in an array and then extrude by a certain amount (if needed surface normal direction). then switch to move tool (calling a center pivot on component if needed) so that the extrude can be manipulated with widget instead of spinner.
def extrudeObject (objects):
	if (objects == rt.undefined or objects == "noSelection"):
		print "Nothing selected. Returned string: noSelection"
		return "noSelection"

	for obj in objects:
		
		classString = classInfo(obj)
		
		if (classString[6] == "Editable_Poly" or classString[4] == rt.Editable_mesh): #had to add Editable_mesh explicitly, here and in the error catch, because the keyword was unknown to pymxs.runtime. added it to the called function anyhow in case they fix it at some point
			maxEval('macros.run "Modifiers" "Face_Extrude"')
			print classString[4]
			
		if (classString[6] == "Shape"):
			#if 'convert to mesh object' checkbox true convert currently selected:
			if (tk_isChecked_000 == True):
				maxEval('''
				convertTo $ PolyMeshObject; --convert to poly
				macros.run "Modifiers" "Face_Extrude"; --extrude modifier
				''')
			else:
				maxEval('macros.run "Modifiers" "Extrude"')
			print classString[4]

		if (classString[6] == "Geometry"):
			#if 'convert to mesh object' checkbox true convert currently selected:
			if (tk_isChecked_000 == True):
				maxEval('''
				convertTo $ TriMeshGeometry; --convert to mesh object
				maxEval('macros.run "Modifiers" "Face_Extrude"; --extrude
				''')

		#else, if undefined..
		else:
			print "::unknown object type::"
			print classString[4]

		if (objects.count > 1):
			rt.deselect(classString[0])
		
	if (objects.count > 1): #reselect all initially selected nodes
		rt.clearSelection()
		for obj in objects:
			rt.selectMore(obj)


#--centerPivotOnSelection----------------------------------------------------------------

def centerPivotOnSelection ():

	#Get the face vertices, add their positions together, divide by the number of the vertices 
	#- that's your centerpoint.

	# the above method will get you the average position of the vertices that constitute the 
	#faces in question. For the center of the bounds of these vertices (if that's of interest 
	#to you), you'll need to get the min position and the max position of the vertex set and 
	#then calculate the median position:
	#p3_minPosition + P3_maxPosition / 2 -- The min and the max position values contain the 
	#minimum x, y and z values and the maximum x, y and z values of the vertex set 
	#respectively. That is to say, for example, that the min x value may come from a 
	#different vert than the min y value.

	#component bounding box method:
	#two bits of code written by anubis will need cleaning up, but might be helpful
# 	(	
# 	if selection.count == 1 and classOf (curO = selection[1]) == Editable_Poly do
# 	(
# 		if (selFacesBA = polyop.getFaceSelection curO).numberset != 0 do
# 		(
# 			faceVertsBA = polyop.getVertsUsingFace curO selFacesBA
# 			with redraw off 
# 			(
# 				tMesh = mesh mesh:curO.mesh
# 				tMesh.pos = curO.pos
# 				tMesh.objectOffsetPos = curO.objectOffsetPos
# 				if faceVertsBA.count > 0 do 
# 				(
# 					delete tMesh.verts[((tMesh.verts as BitArray) - (faceVertsBA))]
# 				)
# 				c = snapshot tMesh
# 				c.transform = matrix3 1
# 				d = dummy boxsize:(c.max - c.min)
# 				delete c
# 				d.transform = tMesh.transform
# 				d.pos = tMesh.center
# 				d.name = tMesh.name + "_box"
# 				delete tMesh
# 			)
# 		)
# 	)
# )


	pass



#third party script to return node information
def getElements(node):
	obj = node.GetObject()
	objTriMesh = obj.AsTriObject()
	objMesh = objTriMesh.GetMesh()

	numVerts = objMesh.GetNumVertices()
	numFaces = objMesh.GetNumFaces()

	allElements = []

	faces = MaxPlus.BitArray(numFaces)
	faces.SetAll()
	verts = [[] for i in range(numVerts)]

	for i in range(0, numFaces):
		face = objMesh.GetFace(i)
	for k in range(0,3):
		verts[face.GetVert(k)].append(i)

	for i in range(0, numFaces): 
		if faces[i]:

			element = []
			element.append(i)
			faceBits = MaxPlus.BitArray(numFaces)
			vertBits = MaxPlus.BitArray(numVerts)

			#for j in range(0, len(element)):
			j = 0
			while j < len(element):
				fi = element[j]
				j += 1

			if not faceBits[fi]:
				face = objMesh.GetFace(fi)

			for k in range(0,3):
				v = face.GetVert(k)

			if vertBits[v]:
				continue

	for singleFace in range(0, len(verts[v])):
		element.append(verts[v][singleFace])
		vertBits.Set(v, True)

		faceBits.Set(fi, True)
		faces.Clear(fi)

		allElements.append(MaxPlus.BitArray(faceBits))

	return allElements






# ||||||||||||||||||||||||||||||||||   Button Commands   ||||||||||||||||||||||||||||||||||||||

# -------------------------------------------------
# Push Buttons
# -------------------------------------------------
class ButtonCommand(object): 
	def __init__(self, HotBox):
		self.hotBox = HotBox                             
		#move to class when used. button id only needs to be unique to the particular class
		# # tk_isChecked__001 = bool(self.ui.chk001.isChecked())
		# # tk_isChecked__004 = bool(self.ui.chk004.isChecked())#Move constrain edge
		# # tk_isChecked__005 = bool(self.ui.chk005.isChecked())#Move constrain surface

	





class Main(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(Main, self).__init__(*args, **kwargs)







class MainOptions(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(MainOptions, self).__init__(*args, **kwargs)

		self.ui = self.hotBox.stackedLayout.widget(3)






class Viewport(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(Viewport, self).__init__(*args, **kwargs)

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






class ViewportOptions(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(ViewportOptions, self).__init__(*args, **kwargs)

		self.ui = self.hotBox.stackedLayout.widget(4)

	def b000(self): #
		self.hbHide()
		maxEval('')

	def b001(self): #
		self.hbHide()
		maxEval('')

	def b002(self): #
		self.hbHide()
		maxEval('')

	def b003(self): #
		self.hbHide()
		maxEval('')

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







class Normals(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(Normals, self).__init__(*args, **kwargs)

		self.ui = self.hotBox.stackedLayout.widget(5)

	def b000(self): #
		self.hbHide()
		maxEval('')

	def b001(self): #
		self.hbHide()

	def b002(self): #
		self.hbHide()

	def b003(self): #
		self.hbHide()

	def b004(self): #
		self.hbHide()


class Create(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(Create, self).__init__(*args, **kwargs)

		self.ui = self.hotBox.stackedLayout.widget(6)

	def b000(self): #box
		self.hbHide()
		maxEval('Box realWorldMapSize:on')

	def b001(self): #Cone
		self.hbHide()
		maxEval('Cone realWorldMapSize:on')

	def b002(self): #Sphere
		self.hbHide()
		maxEval('Sphere realWorldMapSize:on')

	def b003(self): #GeoSphere
		self.hbHide()
		maxEval('GeoSphere realWorldMapSize:on')

	def b004(self): #Cylinder
		self.hbHide()
		maxEval('Cylinder realWorldMapSize:on')

	def b005(self): #Tube
		self.hbHide()
		maxEval('Tube realWorldMapSize:on')

	def b006(self): #Torus
		self.hbHide()
		maxEval('Torus realWorldMapSize:on')

	def b007(self): #Pyramid
		self.hbHide()
		maxEval('Pyramid realWorldMapSize:on')

	def b008(self): #TextPlus
		self.hbHide()
		maxEval('TextPlus layouttype:0 Plane:0')

	def b009(self): #Plane
		self.hbHide()
		maxEval('Plane realWorldMapSize:on')

	def b010(self): #Shapes
		self.hbHide()
		try:
			self.shapes.hbShow()
		except:
			self.shapes = ToolBar(name="shapes", style=1, size=[100,220], offset=[-75,-50])
			self.shapes.hbShow()
		# shapes.hbShow()

	def b011(self): #Lights
		self.hbHide()

		try:
			self.lights.hbShow()
		except:
			self.lights = ToolBar(name="lights", style=1, size=[100,220], offset=[-75,-50])
			self.lights.hbShow()
		# lights.hbShow()

	def b012(self): #Cameras
		self.hbHide()

		try:
			self.cameras.hbShow()
		except:
			self.cameras = ToolBar(name="cameras", style=1, size=[100,220], offset=[-75,-50])
			self.cameras.hbShow()
		# cameras.hbShow()

	def b013(self): #Helpers
		self.hbHide()

		try:
			self.helpers.hbShow()
		except:
			self.helpers = ToolBar(name="helpers", style=1, size=[100,220], offset=[-75,-50])
			self.helpers.hbShow()
		# helpers.hbShow()

	def b014(self): #Space Warps
		self.hbHide()

		try:
			self.spacewarps.hbShow()
		except:
			self.spacewarps = ToolBar(name="spacewarps", style=1, size=[100,220], offset=[-75,-50])
			self.spacewarps.hbShow()
		# spacewarps.hbShow()

	def b015(self): #Systems
		self.hbHide()

		try:
			self.systems.hbShow()
		except:
			self.systems = ToolBar(name="systems", style=1, size=[100,220], offset=[-75,-50])
			self.systems.hbShow()
		# systems.hbShow()







class Edit(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(Edit, self).__init__(*args, **kwargs)

		self.ui = self.hotBox.stackedLayout.widget(7)

	def b000(self): #Mirror
		self.hbHide()
		maxEval('max mirror')

	def b001(self): #Array
		self.hbHide()
		maxEval('max array')

	def b002(self): #
		self.hbHide()
		maxEval('')

	def b003(self): #Convert N to quads
		self.hbHide()
		maxEval('macros.run \"Modifiers\" \"QuadifyMeshMod\"')

	def b004(self): #Measure
		self.hbHide()
		maxEval('macros.run \"Tools\" \"two_point_dist\"')

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






class Transform(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(Transform, self).__init__(*args, **kwargs)

		self.ui = self.hotBox.stackedLayout.widget(8)

	def b000(self): #Scale
		self.hbHide()
		maxEval('max tti')

	def b001(self): #Transform tools
		self.hbHide()
		maxEval('macros.run \"PolyTools\" \"TransformTools\"')

	def b002(self): #Freeze transformations
		self.hbHide()
		maxEval('macros.run \"Animation Tools\" \"FreezeTransform\"')

	def b003(self): #Center pivot on selection
		self.hbHide()
		maxEval('''
		if selection.count > 0 then
		(
			selection.pivot = selection.center
		)
		''')

	def b004(self): #alignX
		self.hbHide()
		sel = makeSelection ("Current", 1)
		alignVertices(sel, 3)

	def b005(self): ##alignY
		self.hbHide()
		sel = makeSelection ("Current", 1)
		alignVertices(sel, 4)

	def b006(self): ##alignZ
		self.hbHide()
		sel = makeSelection ("Current", 1)
		alignVertices(sel, 5)

	def b007(self): ##alignYZ
		self.hbHide()
		sel = makeSelection ("Current", 1)
		alignVertices(sel, 0)

	def b008(self): ##alignXZ
		self.hbHide()
		sel = makeSelection ("Current", 1)
		alignVertices(sel, 1)

	def b009(self): ##alignXY
		self.hbHide()
		sel = makeSelection ("Current", 1)
		alignVertices(sel, 2)







class Selection(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(Selection, self).__init__(*args, **kwargs)

		self.ui = self.hotBox.stackedLayout.widget(9)

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







class Polygons(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(Polygons, self).__init__(*args, **kwargs)

		self.ui = self.hotBox.stackedLayout.widget(10)

	def b000(self): #Merge
		self.hbHide()
		maxEval('macros.run \"Modifiers\" \"VertexWeld\"')

	def b001(self): #Fill holes
		self.hbHide()
		maxEval('macros.run \"Modifiers\" \"Cap_Holes\"')

	def b002(self): #Separate
		self.hbHide()
		sel = makeSelection ("Current", 1, classInfo)
		detachElement(sel)

	def b003(self): #Combine
		self.hbHide()
		sel = makeSelection ("Current", 0)
		maxEval('''
		j = 1;
		count = sel.count;

		undo off;

		while sel.count > 1 do
		(
			if classof sel != Editable_Poly then converttopoly sel
			(
				polyop.attach sel sel;
			  deleteItem sel (j+1);

			  j += 1;

			  if (j + 1) > sel.count then 
			  (
			      j = 1
			  )
			)
		)
		''')

	def b004(self): #Detach
		self.hbHide()
		maxEval('''
		if subObjectLevel == 4 then
			$.EditablePoly.detachToElement #Face keepOriginal:off --element
			--$.EditablePoly.detachToElement #Face keepOriginal:on --clone
		if subObjectLevel == 2 then
			$.EditablePoly.detachToElement #Edge keepOriginal:off --element
			--$.EditablePoly.detachToElement #Face keepOriginal:on --clone
		''')

	def b005(self): #Bridge
		self.hbHide()
		maxEval('$.EditablePoly.Bridge ()')

	def b006(self): #Extrude
		self.hbHide()
		sel = makeSelection("Current", 0)
    	
		if (sel != "noSelection"):
			for obj in sel:
				extrudeObject(obj)
				# classInfo = classInfo(obj)
				# componentArray = []

				# if classInfo[9] == 4
				#		subObject = ""
				#		componentArray.append(subObject)
				#		extrudeObject(obj)
				#	option #maxEval('maxOps.CollapseNode $ off; --collapse modifier stack')

	def b007(self): #Bevel
		self.hbHide()
		maxEval('modPanel.addModToSelection (Bevel ()) ui:on')

	def b008(self): #Chamfer
		self.hbHide()
		maxEval('macros.run \"Modifiers\" \"ChamferMod\"')

	def b009(self): #Collapse component
		self.hbHide()
		#--[mesh] 0=object level,1=vertex level,2=edge level,3=face,4=polygon,5=element,
		#--[poly] 0=object level,1=vertex level,2=edge level,3=border,4=polygon,5=element
		
		if (rt.subObjectLevel == 1): #--vertex level
			maxEval('''
			$.EditablePoly.collapse #Vertex
			''')
		if (rt.subObjectLevel == 2): #--edge level
			maxEval('''
			$.EditablePoly.collapse #Edge
			''')
		if (rt.subObjectLevel == 3): #--face level
			maxEval('''
			$.EditablePoly.collapse #Face
			''')

	def b010(self): #Add divisions
		self.hbHide()
		maxEval('macros.run \"Modifiers\" \"Tessellate\"')

	def b011(self): #Smooth
		self.hbHide()
		maxEval('macros.run \"Modifiers\" \"Smooth\"')

	def b012(self): #Multi-cut
		self.hbHide()
		maxEval('''
		Try
		(
			If SubObjectLevel == undefined then Max Modify Mode
			local A = Filters.GetModOrObj()
			if (Filters.Is_This_EditPolyMod A) then (A.ToggleCommandMode #Cut)
			else (A.toggleCommandMode #CutVertex)   -- (Really a general Cut mode.)
		)
		Catch (print "cut (poly) error")
		''')

	def b013(self): #Slice plane
		self.hbHide()
		maxEval('''
		local retValue = false
		if( Ribbon_Modeling.ValidSOMode() ) then
		(
			curmod = Modpanel.getcurrentObject()
			retValue = (curmod.getCommandMode() == #SlicePlane)
		)
		retValue
		''')

	def b014(self): #Quick Slice
		self.hbHide()
		maxEval('''
		if( Ribbon_Modeling.ValidSelection() ) then
		(
			curmod = Modpanel.getcurrentObject()
			(curmod.getCommandMode() == #QuickSlice)
		)
		else
		(
			false
		)
		''')

	def b015(self): #Delete edgeloop
		self.hbHide()
		maxEval('''
		$.EditablePoly.Remove ()
		''')

	def b016(self): #Inset
		self.hbHide()
		maxEval('''
		Try 
		(
			If SubObjectLevel == undefined then Max Modify Mode
			local A = modPanel.getCurrentObject()
			if keyboard.shiftpressed then A.popupDialog #Inset
			else A.toggleCommandMode #InsetFace
		)
		Catch()
		''')

	def b017(self): #Bridge options
		self.hbHide()
		maxEval('''
		if Ribbon_Modeling.ValidSOMode() and (subobjectlevel == 2 or subobjectlevel == 3) then
		(
			curmod = Modpanel.getcurrentObject()
			if subobjectlevel == 2 then
			(   
			    curmod.popupDialog #BridgeEdge
			)
			else 
			(
			    curmod.popupDialog #BridgeBorder
			)
		)
		''')

	def b018(self): #Extrude options
		self.hbHide()
		maxEval('''
		If SubObjectLevel == undefined then Max Modify Mode
		-- default to Face level:
		if subobjectLevel == 0 then subobjectLevel = 4
		local A = modPanel.getCurrentObject()
		if (Filters.Is_This_EditPolyMod A) then
		(
			local level = A.GetMeshSelLevel()
			if (level == #Vertex) then (A.PopupDialog #ExtrudeVertex)
			else if (level == #Edge) then (A.PopupDialog #ExtrudeEdge)
			else if (level == #Face) then (A.PopupDialog #ExtrudeFace)
		)
		else (A.popupDialog #Extrude)
		''')

	def b019(self): #Tessellate options
		self.hbHide()
		maxEval('''
		Try 
		(
			local A = modPanel.getCurrentObject()
			A.popupDialog #Tessellate
		)
		Catch ()
		''')

	def b020(self): #Inset options
		self.hbHide()
		maxEval('''
 		local A = modPanel.getCurrentObject()
		A.popupDialog #Inset
		''')







class Nurbs(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(Nurbs, self).__init__(*args, **kwargs)

		self.ui = self.hotBox.stackedLayout.widget(11)

	def b000(self): #
		self.hbHide()
		maxEval('')

	def b001(self): #
		self.hbHide()
		maxEval('')

	def b002(self): #
		self.hbHide()
		maxEval('')

	def b003(self): #
		self.hbHide()
		maxEval('')

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








class Texturing(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(Texturing, self).__init__(*args, **kwargs)

		self.ui = self.hotBox.stackedLayout.widget(12)

	def b000(self): #UVW map
		self.hbHide()
		maxEval('modPanel.addModToSelection (Uvwmap ()) ui:on')

	def b001(self): #Select by material ID
		self.hbHide()
		maxEval('''
		if subobjectlevel == undefined then
			max modify mode; \
		if subobjectlevel != 4 then 
			subobjectlevel = 4; \
		Try(ApplyOperation Edit_Patch PatchOps.SelectByMatID)Catch();
		''')

	def b002(self): #
		self.hbHide()
		maxEval('')

	def b003(self): #
		self.hbHide()
		maxEval('')

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







class Animation(ButtonCommand):
	def __init__(self, *args, **kwargs):
		super(Animation, self).__init__(*args, **kwargs)

		self.ui = self.hotBox.stackedLayout.widget(13)

	def b000(self): #
		self.hbHide()
		maxEval('')

	def b001(self): #
		self.hbHide()
		maxEval('')

	def b002(self): #
		self.hbHide()
		maxEval('')

	def b003(self): #
		self.hbHide()
		maxEval('')

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

# ---------------------------------------------