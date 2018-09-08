import os.path

from PySide2.QtUiTools import QUiLoader

import MaxPlus
maxEval = MaxPlus.Core.EvalMAXScript

# import max_customTools_func
# makeSelection = max_customTools_func.makeSelection #sel = makeSelection ("Current", 1)
# classInfo = max_customTools_func.classInfo
# setSnapState = max_customTools_func.setSnapState
# alignVertices = max_customTools_func.alignVertices
# extrudeObject = max_customTools_func.extrudeObject
# getMousePosition = max_customTools_func.getMousePosition
# getKeyState = max_customTools_func.getKeyState



# ------------------------------------------------
# Get the main Max window as a QtGui.QMainWindow instance.
# ------------------------------------------------

mainWindow = MaxPlus.GetQMaxMainWindow()


# ------------------------------------------------
MaxPlus.FileManager.Reset(True)



# Generate-ui-file-paths--------------------------

def getQtui(name):
	path = "%CLOUD%/____Graphics/3ds Max/Scripts/Qt/tk_max_ui/tk_"+name+".ui"
	# print path
	uiFile = os.path.expandvars(path)
	qtui = QUiLoader().load(uiFile) # Load Qt ui file and set as child to dockWidget
	return qtui





#------------------------------------------------------------------------------