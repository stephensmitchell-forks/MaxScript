import sys
import os.path
# import imp
# try:
# 	from pysideuic import compileUi #PySide Uic workflow: https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2016/ENU/Maya/files/GUID-FAD0F6CC-15D0-4489-9372-028146B70F49-htm.html
# except:
# 	from pyside2uic import compileUi

# depricated. Use pyside2uic to convert qt .ui file to .py
# #convert .ui file to .py
# #Open/create .py file for writing (output)
# output_path = os.path.expandvars("%CLOUD%/____Graphics/3ds Max/Scripts/_Python/___Python_path/max_customTools_ui.py")
# python_file = open(output_path, 'w') #open in write mode
# #Read .ui file to convert (input)
# input_path = os.path.expandvars("%CLOUD%/____Graphics/3ds Max/Scripts/Qt/max_customTools_ui.ui")
# compileUi(input_path, python_file, False, 4, False)
# python_file.close()


#set path to tk_main
sysPath = os.path.expandvars("%CLOUD%/____Graphics/Maya/Scripts/_Python/_Python_startup")
sys.path.append(sysPath)


#set additional system paths
sysPath = os.path.expandvars("%CLOUD%/____Graphics/3ds Max/Scripts/_Python/___Python_path")
sys.path.append(sysPath)

sysPath = os.path.expandvars("%CLOUD%/____Graphics/3ds Max/Scripts/Qt")
sys.path.append(sysPath)



#implicit import
# max_customTools_main = imp.load_source("max_customTools_main", os.path.expandvars("%CLOUD%/____Graphics/3ds Max/Scripts/_Python/___Python_path/max_customTools_main.py"))
# uiFile = os.path.expandvars("%CLOUD%/____Graphics/3ds Max/Scripts/Qt/max_customTools_ui.ui")

# import max_customTools_main
# # max_customTools_main.showWindow(uiFile)
# execfile (os.path.expandvars("%CLOUD%/____Graphics/3ds Max/Scripts/_Python/___Python_path/max_customTools_main.py"))