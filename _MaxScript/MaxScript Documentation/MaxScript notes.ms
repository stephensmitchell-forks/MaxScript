-------------------------------------
---------------------- 3ds Max notes-
-------------------------------------


"GENERAL_SYNTAX:___________________________________________________________________________"







"COMMENTING:______________________________________________________________________________" 

-- single line 

/* 
multiple 
lines 
*/


"VARIABLES:_______________________________________________________________________________"

mystring = "This is my string."


"Scope"
-- define local
local variable

-- define global
global variable



"Conversion To


								int 					float 				string 				vector 				  matrix

int ($i)				perfect 			perfect 			perfect 	 <<$i, $i, $i>>		  none
________________________________________________________________________________________

float ($f)			without				perfect				perfect		 <<$f, $f, $f>>		  none
								fraction
________________________________________________________________________________________

string 					without 			perfect if 		perfect		  perfect if 				none
								fraction			starts with 						  starts with
								if starts			number,									  vector or floats	
								with number,	else 0									  with remaining
 								else 0																  elements 0
________________________________________________________________________________________

vector 					length of 		length of 		3 floats    perfect						perfect for
								vector 				vector 				separated											[1][3] matrix,
								without											by a space 										else none
								fraction
________________________________________________________________________________________

matrix					for [1][3] 		for [1][3]		none 				for [1][3] 				perfect
								matrix or 		matrix or 								matrix or 
								smaller, 			smaller,length 						smaller, perfect
								length of 		of matrix 								with remaining
								matrix without 													elements 0
								fraction"

  


   

 



 





"STRINGS:_________________________________________________________________________________"


\"	--	double quote

\		--	Line Continuation

;		--	Command Separation

\n 	--	new line (or: \r\n)

\r 	--	carriage return

\t 	--	TAB

\*	--	asterisk

\?	--	question mark

\\	--	single \

\%	--	percent

\x{d}	--hexadecimal


-- [string operators:]
"string" + "string"
-- Returns a new string that is the concatenation of two strings.
"string" == "string"
"string" != "string"
"string" > "string"
"string" < "string"
"string" >= "string"
"string" <= "string"
-- Standard lexical string comparisons (case sensitive).
-- To perform a case insensitive equality comparison, please use the stricmp() method that performs a lower-case comparison.
"string"[<index_number>]
-- Returns the indexed character as a single-character string, index starts at 1.
"string"[<index_number>]= <single_character_string>
-- Sets the indexed character to the given character.
"string"as<class>


-- [string methods]


--concatenation
ex.
s1 = "aa"
s2 = s1
append s1 "bb"
s1-- returns "aabb"
s2-- returns "aabb"and not "aa" 


<integer>findString"string" <search_string>
-- Returns the index of search_string in string or undefined if not found.





-- Convert string
--convert to class
ex.
"Foo" as name-- returns #foo

--convert to float
ex.
"123.4" as float-- returns 123.4 

--convert to stringstream
--Converting a string to a StringStream value allows you to read through a string using 
--the MAXScript's text file I/O operations.
ex.
"$box01" as stringstream-- returns the string as a stringstream 

--copy string
-- The new value contains a copy of the text contents of the copied 
--string and is independent of the copied string.
ex.
newstr = copy oldstr

--delete string
free <string>	--Frees the memory used by the string value without waiting for garbage collection.


--Compiles and evaluates the contents of the string as a MAXScript expression 
--and returns the result of the evaluation.
execute <string>


--search string for text
<integer>findString<string> <search_string> 
--Returns the index of search_string in string or undefined if not found.
ex.
findString "Thanks for all the fish!" "all" -- returns 12 


--tokenize
-- <array of strings>filterString "string" <token_string> [splitEmptyTokens:<boolean>]
--filterString splits the input string into substrings based on the characters given 
--in token_string , and returns each substring as a member of the array.
ex.
filterString "MAX Script, is-dead-funky" ", -"
-- WOULD RETURN
#("MAX","Script","is","dead","funky")




--If splitEmptyTokens is false or not specified, sequential tokens are handled as a 
--single token, and tokens at the beginning or end of the string are ignored. If 
--splitEmptyTokens is true , each token found will result in string element in the output, 
--with the string element in the cases ignored above being empty strings.
ex.
s = "One\t\tThree\tFour"
tokens = filterString s "\t"
--> #("One", "Three", "Four")
tokens = filterString s "\t" splitEmptyTokens:true
--> #("One", "", "Three", "Four")
s ="\t\t\tOne\t\t\tThree\tFour\t\t\t"
tokens = filterString s "\t"
--> #("One", "Three", "Four")
tokens = filterString s "\t" splitEmptyTokens:true
--> #("", "", "", "One", "", "", "Three", "Four", "", "", "")


--replace
--Returns a new string where the substring in string starting at index from_integer , 
--and of length length_integer , is replaced with the new_string.new_string can be any 
--length. 
ex.
s="1234567890"
s1=replace s 5 3 "inserted string"
-- RETURNS:
"1234inserted string890"


--filter substring
ex.
s ="Balerofon"
ss = substring s 5 3-- returns "rof"
ss = substring s 5 -1-- returns "rofon"
ss = substring s 5 100-- returns "rofon" 


--string contains
ex.
s="text1"
matchPattern s pattern:"text?"-- returns true
matchPattern s pattern:"T*"-- returns true
matchPattern s pattern:"T*"ignoreCase:false-- returns false
matchPattern s pattern:"s*"-- returns false 


--Case comparison
<integer>stricmp <string1> <string2>
-- In 3ds Max6 and higher, this method performs a lower case comparison of string1 
-- and string2. Returns an integer value < 0 if string1 is less than string 2, = 0 
--if string1 is identical to string 2, and > 1 if string1 is greater than string 2.


--Case conversion
toLower
ex.
toUpper "so long and thanks for all the scripts"
-- RESULT:
"SO LONG AND THANKS FOR ALL THE SCRIPTS"


--Substitute
--Returns a new string with all occurrences of <from_string> in <source_string> replaced 
--with <to_string>. Available in 3ds Max 2008 and higher. Previously available in the 
--Avguard Extensions .
ex.
s1 = "Truth, Justice And The American Way"
s2 = "The American Way"
s3 = "All That Stuff"
s4 = substituteString s1 s2 s3
-- RESULT:
"Truth, Justice And All That Stuff"





"OPERATORS:_______________________________________________________________________________"

+
-
*
/

-- There are assignment operators corresponding to the four math operations (+,-,*, and /) that apply the operation to the assignment’s destination with the result. Their syntax is:
<destination> += <expr> -- add <expr> to destination
<destination> -= <expr> -- subtract <expr> from destination
<destination> *= <expr> -- multiply destination by <expr>
<destination> /= <expr> -- divide destination by <expr>
ex. x = x + 1
-- Using this shorthand form of assignment can be written as
		x += 1

random		ex. random 1.0 100 -- return value type (Float or Integer) is the same as the type of the first argument 




"ITERATORS:_______________________________________________________________________________"





"COMPARATORS______________________________________________________________________________"

== -- equal
!= -- not equal 
> -- greater than
< -- less than
>= -- greater than or equal
<= -- less than or equal

-- where <compare_operand> can be one of:
<math_expr>
<operand>
<function_call>


not
and
or




"CONDITIONALS_&_LOOPS:____________________________________________________________________"


--	CONDITIONALS
--basic if
ex.
if a > b do 
(
	print d; 
	print e;
)
--basic if/else
ex.
if a > b then
( 
	print c
) 
else 
(
	print d
)

ex.
if ($pos.z < 0) then	--if object is below 0
	$.wirecolor=red
else
	$.wirecolor=green




ex.
a = (if d == 0 then 0 else a / d)






--	TOGGLE
--set to 'not current state'
--toggle for single object
ex.
if ($ != undefined) then
(
	toggle = not $.xray;
	$.xray = toggle;
)

--toggle for all geometry
ex.
toggle = not $.backfacecull;

for obj in Geometry do
(
	obj.backfacecull = toggle;
)




--	LOOPS

ex.
for i = 1 to snapmode.numOSnaps do
(
-- 	expression
)


--for a specified range
ex.
for i in 1 to 100 do 
(
	sphere
)

ex.
for i 1 to 10 do
(
	Box pos: [i*30, 0, 0]	--create 10 boxes at different x positions
)




--for 'obj in array' do
ex.
for obj in (selection as array)
where classOf obj == Cylinder do
(
	obj.scale.z = 2	--set scale value for cylinders in current selection
)






--	SWITCH/CASE
ex.
case (superClass) of --in case of variable superClass == shape, light, or camera, perform one of the following  
		(
			shape: superClassString = "shape"
			light: superClassString = "light"
			camera: superClassString = "camera"
		)







"PROCEDURES:______________________________________________________________________________"
-- functions

-- syntax:
mapped fn functionName argument:optDefaultValue = 
	(
	expression
	)

-- The parameters/arguments for a function are either positional or keyword.
-- 	Positional parameters are defined with a simple <name> and must be placed 
-- before any keyword parameters.
-- 	Keyword parameters have a ':' (colon) after the name and an optional default value. 
-- The caller of the function can optionally supply keyword arguments in any order. 
-- Those not supplied will be set to the default value given, or 
-- the special value unsupplied if a default value is not given.

--function call
functionToCall(arg1 arg2)

--keyword arguments
functionToCall keyword:arg1  keyword:arg2




"ARRAYS_&_DICTIONARYS____________________________________________________________________"

-- maxscript collection types
-- https://help.autodesk.com/view/3DSMAX/2018/ENU/?guid=__files_GUID_DAABD302_FB6A_40BB_882A_888631488FB7_htm


--Arrays/Lists
--create array
ex.
#()
ex.
a = #($Box01, $Box02, $Box03)


--Size of array
--Get/Set the number of elements in the array. 
<array>.count : Integer
ex.
a.showConstructors


--perform an operation on an array element
a[1].renderable = false


--Get element
--Indexes start at 1.
<array>[<integer>  ] --Returns element of array.
ex.
array[1]


--Set element of array to value, growing array as necessary.
<array>[<integer>] = <value> 
ex.
array[1] = "element"


--New array is constructed containing all the elements of the first and second operands
<array> + <collection>
ex.
a = #(1,2,3,4)
join a #(5,6,7,8)
(cameras as array) + lights
props = getPropNames Node
join props getPropNames (classOf $foo)
join props getPropNames $foo #dynamicOnly
sort props


--Create new array with only unique members of source array.
makeUniqueArray <array> 
ex.
makeUniqueArray # (1, 2, 3, 4, 3, 2, 1)
-- RESULT:
-- # (1, 2, 3, 4)


--Append value to array, growing it as necessary. 
append <array> <value>	--Returns the resulting array.


--Appends the value to the array if the value is not already in the array.
appendIfUnique <array> <value>  --boolean
ex.
(
local h = #(1,2,3,4)
appendIfUnique h 60 -- should work
appendIfUnique h 4 -- shouldn't work
if ((h.count != 5) or (h[5] != 60)) do
throw "Entry 5 in the array is incorrect"
format "%\n" h
)
-- RESULT:
-- #(1, 2, 3, 4, 60)
-- OK


--Convert collection to an array.
<collection> as array 



--Creates a copy of all the elements in the array.
-- If #noMap is specified, the copy made is what is called a shallow copy 
-- - only a copy of the upper-level value itself (that is, the array value) is created. 
-- Copies aren't made of values stored in the array, rather a reference to the same value 
-- is stored in both array values.
copy <array> [#noMap] -- mapped 
-- Returns a value of OK .


--Creates a copy of all elements in the array, including nested sub-arrays
deepCopy <array> --returns the new array


-- Delete element indexed by number from array, shrinking it in size by 1.
deleteItem <array> <number> --Returns the resulting array.



--Appends all the elements of the second argument to the array (first) argument.
join <array> <collection> 


--Inserts the value at the specified index in the array, growing the array if necessary.
insertItem <value> <array> <integer> --Returns OK.


--compare elements
-- performs a MAXScript '==' comparison between elements in the array and 
-- the target object and then returns the index of the first occurrence of 
-- the given value in the array or 0 (zero) if the value is not in the array.
-- Values such as Point3s and Strings match if they have the same contents.
findItem <array> <value> 


--Sorts the elements of the array into ascending order. All the elements must be comparable.
sort <array> 


--Sort and compare elements
-- Sorts the array using the specified function for element-by-element comparison. 
-- The comparison function must take 2 values as arguments, and return an integer number < 0 
-- if the first value is less than the second value, 0 if the values are equivalent, and 
-- an integer number > 0 if the first value is greater than the second value. The entire array is sorted 
-- unless a start or end value is specified.
qsort <array> <function> [start:<integer>] [end:<integer>] [user-defined key args passed to function] 
ex.
-- The following script generates 10 random positions, and then sorts 
-- the positions based on their distance from [0,0,0]:
-- positions =for i = 1 to 10 collect (random [0,0,0] [100,100,0])
fn compareFN v1 v2 =
(
local d = (length v1)-(length v2)
case of
(
(d < 0.): -1
(d > 0.): 1
default: 0
)
)
 
qsort positions compareFN
for p in positions do print p

ex.
-- All key arguments are passed to the comparison function. 
--This allows you to do things like an indexed sort:
fn compareFN v1 v2 valArray: =
(
local v1i = valArray[v1]
local v2i = valArray[v2]
local d = (length v1i) - (length v2i)
case of
(
(d < 0.): -1
(d > 0.): 1
default: 0
)
)
positions = for i = 1 to 10 collect (random [0,0,0] [100,100,0] )
indexArray = for i = 1 to positions.count collect i
qsort indexArray compareFN valArray:positions
 
for i = 1 to positions.count do print positions [indexArray[i] ]


--Binary search in a sorted list of arrays
bsearch <key> <array> <function> [start:<integer>] [end:<integer>] [user-defined key args passed to function] 


--Returns minimum value of items in the array or of the argument values. 
-- If the array size is zero or no arguments are specified, the value undefined is returned.
amin ( <array> | {value} ) 
ex.
myMin1 = amin #(5,1,4,2,8)
myMin2 = amin 5 1 4 2 8


--Returns maximum value of items in the array or of the argument values. 
-- If the array size is zero or no arguments are specified, the value undefined is returned.
-- the elements in an array are stored by reference rather than by value. 
-- When you operate directly on array elements, and the reference to the array is stored in 
-- more than one place, unexpected results may occur.
amax ( <array> | {value} ) 
ex.
RandomSets=#() -- create array
RandomSet=#() -- create array
for i = 1 to 3 do -- loop i
(for j=1 to 3 do -- for each i loop j
RandomSet[j] = random 1 100 -- set array element to random value
print RandomSet #nomap -- print array of random values
RandomSets[i] = RandomSet -- store random value array in array
)
print RandomSets -- print array of arrays of random values 
-- OUTPUT:
-- #() -- result of line 1
-- #() -- result of line 2
-- #(33, 47, 31) -- output from line 6, i =1
-- #(4, 52, 39) -- output from line 6, i =2
-- #(52, 36, 23) -- output from line 6, i =3
-- OK -- result of for loop, lines 3 to 8
-- #(52, 36, 23) -- 3 lines of output from line 7
-- #(52, 36, 23)
-- #(52, 36, 23)
-- OK -- result of line 9 


--Frees the memory used by the array value without waiting for garbage collection.
free <array>





-- Dictionarys
ex.
d = Dictionary #(#ss, 1) #(#tt, 2)
for i in d do print i
-- RESULTS
-- Dictionary #name ss:1 tt:2 
-- (DataPair key:#ss value:1)
-- (DataPair key:#tt value:2)


Dictionary() -- empty dictionary of type #name
Dictionary (#integer | #name | #string) -- empty dictionary of the specified type
Dictionary {#(key, value)}+ -- one or more two-value arrays
Dictionary {key:value}+ -- one or more explicit key:value pairs
Dictionary {(DataPair key value)} -- one or more DataPair objects


-- A count of items in the dictionary
<dictionary>.count : Integer, read-only

-- The type of the dictionary, which can be #name, #string, #integer.
<dictionary>.type read-only 

-- An array of the dictionary's keys. Note: changing this array does not affect the dictionary.
<dictionary>.keys : Array, read-only

-- Gets the value for key. If there is not an entry for the key, the value undefined is returned.
<dictionary>[key] 

-- Sets the value for key. An existing entry does not need to exist for the key.
<dictionary>[key] = <value>

-- Gets a value from the dictionary based on key. If there is no entry for the key, a value of undefined is returned.
GetDictValue <dictionary> <key >

-- Sets the value for an existing entry in dictionary based on key. If there is no entry for the key, nothing happens.
SetDictValue <dictionary> <key > <value>

-- Puts a value in dictionary based on key.
-- If putOnlyIfNew is true, the value is added only if there is no existing entry for the key.
PutDictValue <dictionary> <key > <value> putOnlyIfNew:<bool> -- defaults false

-- Removes the existing entry in the dictionary based on key
RemoveDictValue <dictionary> <key >

-- Returns whether there is an existing entry in the dictionary for the given key
HasDictValue <dictionary> <key >

-- Returns an array of key values in the dictionary.
GetDictKeys <dictionary>

-- Returns the key type of the dictionary - #name, #string, or #integer.
GetDictKeyType <dictionary>

-- Creates a shallow copy of the dictionary. 
copy <dictionary> [#nomap]

-- Frees the internal memory associated with the dictionary.
free <dictionary>




"VECTORS:_________________________________________________________________________________"







"MATRICES:________________________________________________________________________________"




"SELECTION:_______________________________________________________________________________"


--current selection
$

selection

getCurrentSelection)() --returns the current selection as an array


--select All
$*										


--set property on selected object
$.<property> = value	
	ex.
	$.renderable = false


SelectionManager.Nodes --provides an iterator for the selection list.
--You can now do the following:
def applyMaterialToNodes(m):
	for n in MaxPlus.SelectionManager.Nodes:
		n.Material = m


--select by name
--select object woth the name Box01
select <node> -- mapped
select $Box01		

--objects whose names start with 'Tile'
$Tile*					
--enclose in single quotes for searches containing whitespaces
$'Tile A'*			

--Add a node to the set of selected objects.
selectMore <node> -- mapped

--query if the specified point is selected. NURBS, poly and spline objects.
isPointSelected <node> <point_index> 

--Returns a floating point weighted point selection if the object supports soft selections.
--Most object types just return 1.0 if the point is selected and 0.0 if not.
pointSelection <node> <point_index>

--Deselect all.  Scene is redrawn unless redraw:false is specified.
clearSelection() clearNodeSelection [redraw:<boolean> ] 

--Deselects the given node(s).
deselect <node>-- mapped
ex.
deselect $box* --deselects all items whose names start with "box".

--Deselect a single node
deselectNode <node>

--number of selected objects
selection.count
--output to the script listener window
ex.
format "% objects selected." selection.count



--deselect
clearSelection()	--clears the current scene node selection

deselect <node>		--deselects the given nodes






"TRANSFORM:_______________________________________________________________________________"

--move
move $ [10,0,0]		--xyz

$.position = [10,10,0]	--absolute position

$.position.z = $.position.z + 10

--rotate
INode.Rotation
rotate $ [eulerangles 90 0 0]		--rotate relative

$rotation= (eulerangles 0 0 90) 

--scale
INode.Scaling
scale $ [2,2,1]		--scale 2x in xy.  z is 1:1 unchanged
$.scale = [1,1,2] --scale 2x in z

--query position
INode.Position
ex.
$.position

--gets or sets the position of the selected element in the mesh
--<vertexselection>.pos : Point3 
$foo.verts[i].pos = $bar.verts[j].pos + [10,0,0]


--Snap
--Get/Set snap mode state
snapMode.active --boolean
ex.
state = snapMode.active
snapMode.active = not state

--Get/Set the current snap type as a name. Possible names are #2D , #2_5D , #3D
snapMode.type
--
snapMode.toFrozen
--
snapMode.axisConstraint
--
snapMode.useAxisCenterAsStartSnapPoint
--
snapMode.strength
--
snapMode.snapRadius

--System Global which contains true if the Marker is currently snapped to something
snapMode.hit --undefined if Snaps are not active

--System Global which contains the node currently being snapped to
snapMode.node --undefined if not snapped to a node or if Snaps are not active

--System Global which contains the Snap System Flags as an integer
snapMode.flags --undefined if Snaps not active

--System Global which contains the last Snap Point as Point3 coordinate in local coordinates of the node snapped to.
snapMode.hitPoint --undefined if Snaps are not active.

--System Global which contains the last Snap Point as Point3 world coordinate.
snapMode.worldHitpoint --undefined if Snaps are not active.

--System Global which contains the last Snap Point as a Point3 screen coordinate.
snapMode.screenHitPoint --undefined if Snaps are not active.

--System Global which contains the last Snap Point as point3 world coordinate.
snapMode.refPoint --undefined if Snaps are not active.

--System Global which contains the first snap point as point3 world coordinate.
snapMode.topRefPoint --undefined if Snaps are not active.

--System Global which contains the number of OSnaps as an integer.
snapMode.numOSnaps --1"Body", 2"NURBS", 3"Standard", 4"Standard", 5"Standard", 6"Standard"

--Returns true if the indexed OSnap item in the indexed OSnap is active
snapMode.getOSnapItemActive <int osnap_index> <int osnap_item_index> 
ex.
-- snapMode.active  --set snapmode active
state = snapmode.getOSnapItemActive 4 1
snapmode.getOSnapItemActive 4 1 (not state)

--Returns the name of the indexed OSnap item in the indexed OSnap as string.
snapMode.getOSnapItemName <int osnap_index> <int osnap_item_index> 
ex.
snapMode.getOSnapItemName <int osnap_index> <int osnap_item_index>
-- Returns the name of the indexed OSnap item in the indexed OSnap as string.

-- Documentation
-- http://www.cgplusplus.com/online-reference/maxscript-reference/source/snapmode.htm

-- 1: name: "Body Snaps"
--  1: name: "Vertex"; tooltip: ""; state: false
--  2: name: "End Edge"; tooltip: ""; state: false
--  3: name: "Edge"; tooltip: ""; state: false
--  4: name: "Edge Midpoint"; tooltip: ""; state: false
--  5: name: "Face"; tooltip: ""; state: false
-- 2: name: "NURBS"
--  1: name: "CV"; tooltip: ""; state: false
--  2: name: "Point"; tooltip: ""; state: false
--  3: name: "Curve Center"; tooltip: ""; state: false
--  4: name: "Curve Normal"; tooltip: ""; state: false
--  5: name: "Curve Tangent"; tooltip: ""; state: false
--  6: name: "Curve Edge"; tooltip: ""; state: false
--  7: name: "Curve End"; tooltip: ""; state: false
--  8: name: "Surf Center"; tooltip: ""; state: false
--  9: name: "Surf Normal"; tooltip: ""; state: false
--  10: name: "Surf Edge"; tooltip: ""; state: false
-- 3: name: "Point Cloud Objects"
--  1: name: "Point Cloud Vertex"; tooltip: ""; state: true
-- 4: name: "Standard"
--  1: name: "Grid Points"; tooltip: ""; state: false
--  2: name: "Grid Lines"; tooltip: ""; state: false
-- 5: name: "Standard"
--  1: name: "Pivot"; tooltip: ""; state: false
--  2: name: "Bounding Box"; tooltip: ""; state: false
-- 6: name: "Standard"
--  1: name: "Perpendicular"; tooltip: ""; state: false
--  2: name: "Tangent"; tooltip: ""; state: true
-- 7: name: "Standard"
--  1: name: "Vertex"; tooltip: ""; state: false
--  2: name: "Endpoint"; tooltip: ""; state: false
--  3: name: "Edge/Segment"; tooltip: ""; state: false
--  4: name: "Midpoint"; tooltip: ""; state: false
--  5: name: "Face"; tooltip: ""; state: false
--  6: name: "Center Face"; tooltip: ""; state: false








"CREATE:__________________________________________________________________________________"


--[Primitives]

Box() pos: [-5,5,0] wireColor:red

-- test whether a given node is convertible into a given class
--[ Mesh, SplineShape, NURBSCurve, NURBSSurface, etc.]
canConvertTo <node> <class>
ex.
if canConvertTo $foo NURBSSurface then...

--general form of the existing specific conversion functions such as convertToMesh()
convertTo <node> <class> -- mapped
ex.
convertTo $circle01 SplineShape --If the conversion is not supported, returns undefined.

--Convert an object to an editable mesh
--it will remove all modifiers present
convertToMesh <node> -- mapped
convertToMesh()

--These functions work on those primitive geometry and shape classes that support 
--conversion to NURBS (such as boxes, spheres, circles, lines, etc.)
--Convert to a SplineShape object.
convertToSplineShape <node> -- mapped 
--Convert to a NURBSSurface
convertToNURBSSurface <node> -- mapped 
--Convert to a NURBSCurve
convertToNURBSCurve <node> -- mapped 




--[Modifiers]

addModifier $ (Bend())	--add bend modifier to selected
ex.
INode.AddModifier()

addModifier $ (Taper amound:1 primaryAxis:1)

--Tests whether a particular modifier or modifier class may be added the given <node> or 
--to all of the objects in the objectset or group.
validModifier [<node> | <objectset> | <group> ] <modifier |modifier_class> 

--Takes either a modifier value which is present on the <node> stack, or an index 
--specifying the index of the modifier to delete, counting from the top of the stack.
deleteModifier <node> <modifier_or_index> -- mapped

--Collapses the modifiers out of a stack
collapseStack <node> -- mapped 

--Prints a representation of the current modifier stack for the given node.
printStack <node>


--[Materials]
--assign material
$.material = StandardMaterial()
$.material.diffuse = color 255 0 0
$.material = VRayMtl()
$.material = VRayMtl diffuse:green reflection:grey reflection_glossiness:0.7

--assign to
$Tile*.material = medit.getCurMtl() --apply currently selected material in editor to all 
																		--objects whose name starts with 'Tile'
--remove material
$*.material = undefined






"OBJECTS_&_ATTRIBUTES:____________________________________________________________________"

--check for existence
IsValidNode <var> --is the object a node value. boolean.



--Object Name
--Get or set the scene object's name.
<node>.name String default: varies 
--If exact is false(default), the normal MAXScript node name comparisons are performed.
--If all is true, an array of nodes with the specified name is returned.
getNodeByName <string> exact:<bool> ignoreCase:<bool> all:<bool> --Returns first node with the specified name.
--[   Defaults:				 exact:false	ignoreCase:true 	all:false]
ex.
getnodebyname "AA" all:true
--($Teapot:aa @ [...], $Box:AA @ [...]) --returns all nodes named aa

--Access the base object in a scene node. This has relevance in nodes that have modifiers
--present that change the node type as it is processed up the stack. For example, a line 
--with an extrude modifier starts out as a Shape and turns into an Editable Mesh at the 
--top of the stack, its so-called world state. The baseObject property gives you access 
--to the base object in the modifier stack.
<node>.baseObject  A subclass of Node  default: varies
ex.
baseClass = classOf(obj.baseObject)


--store information about the geometry
INode.BaseObject.ParameterBlock


--query shape object
isShapeObject <node>	--boolean

--query if the node's object is deformable. 
--A deformable object is an object with points that can be modified.
--isDeformable might return true for some nodes, 
--this does not necessarily mean that they can be deformed.
--while all geometry primitives return false but can be deformed.
isDeformable <node>

--Returns the number of deformable points for the node's object.
numPoints <node>

--Returns the position of the indexed point for the node's object.
getPointPos <node> <index> 

--Returns a 2 element array containing the min and max points of 
--the node's bounding box in coordinate system matrix3 as point3 values.
nodeGetBoundingBox <node> <matrix3>

--Returns a 2 element array containing the min and max points of the node's local bounding box
nodeLocalBoundingBox <node> 






--Object properties
ex.
showProperties $
--explicitly
ex.
showProperties ( VRayLight() )

--Retrieves the node's user property with the given key as a string. 
--<key_string> is either a String or a Name value.
getUserProp <node> <key_string>

--Sets the node's user property with the given key to the given value.
setUserProp <node> <key_string> <value>

--This is effectively the contents of the User Defined Properties box in 
--the Object Properties dialog
getUserPropBuffer <node>

--Sets the user property buffer to the given string.
setUserPropBuffer <node> <string>



--Returns the rotation binding weight for the node.
getRotTaskWeight <node>

--Sets the rotation binding weight for the node.
setRotTaskWeight <node> <float> 

--Returns the position binding weight for the node.
getPosTaskWeight <node>

--Sets the position binding weight for the node.
setPosTaskWeight <node> <float> 

--query if the specified axis is turned on for position or rotation binding. 
--If an axis is turned off, the specified axis is no longer influenced by the 
--follow object or the IK Controller Position end effector . <pos_or_rot_integer> 
--sets whether the method returns the position state or the rotation state: 
--0 specifies position; 1 specifies rotation. 
--<axis_integer> sets the axis to check: 0 specifies X, 1 specifies Y, 2 specifies Z.
getTaskAxisState <node> <pos_or_rot_integer> <axis_integer> 

--Sets the axis state for position or rotation binding to the specified boolean value. 
--See getTaskAxisState() for a description of the parameters.
setTaskAxisState <node> <pos_or_rot_integer> <axis_integer> <boolean>

--Mirrors the specified IK constraints on the specified node's transform controller 
--about the specified axis . <axis_integer> specifies the axis of reflection: 
--0 for X, 1 for Y, 2 for Z . <pos_or_rot_integer> specifies which type of 
--constraints are being mirrored: 0 for position, 1 for rotation.
mirrorIKConstraints <node> <axis_integer> <pos_or_rot_integer>

--Call this method when one of the node level IK parameters has been changed.
nodeIKParamsChanged <node>

--query if the <ik_node> can be bound to the <node> as a follow object.
OKToBindToNode <ik_node> <node> --boolean





--query poly count
getPolygonCount <node>	--Returns a 2 element array [#of faces, #of vertices]

--query number of surfaces (loft objects)
numSurfaces <node>

--query if the node's showLinksOnly property is true .
isBoneOnly <node>





-- <node_constructor> [name: <string> ]
[ prefix: <string> ] 
[ material: <material> ] 
[ target: <node> ] 
[ pos: <point3> ] -- default [0,0,0] 
[ position: <point3> ] -- synonym for pos 
[ rotation: <quat> ] -- default 0 rotation 
[ scale: <point3> ] -- default 100% scale 
[ pivot: <point3> ] -- default normal node pivot location 
[ transform: <matrix3> ] -- default identity 
[ isSelected: <boolean> ] -- default false 
[ dir: <point3> ]-- set local z direction   

ex.
b = box name:"foo" position:[10,10,10] height:20

ex.
for i in 1 to 100 do sphere prefix:"baz"
--creates 100 spheres, giving each a unique name
--beginning with "baz", such as $baz01, $baz02, $baz03, etc.




--transform
move <node> <point3> -- mapped 
scale <node> <point3> -- mapped 
rotate <node> <angle> <axis_point3> -- mapped -- angle in degrees 
rotate <node> <quat> -- mapped 
rotate <node> <eulerangles> -- mapped 

--queries the transform axis of the indexed axis system of the node 
getTransformAxis (<node>|undefined) <index> --returns as a matrix3 value

--queries the transformation matrix of the givennode or rootnode
getNodeTM {<node> | <rootnode>} --returnsas a matrix3 value

--Returns the transform controller for the node
getTMController <node>

--Computes the distance between the pivot points of the two specified nodes.
distance <node> <node>

--Computes the closest intersection of the ray and the surface of the given node. 
--Returns another Ray which defines the position of intersection in 3D space and the 
--surface normal direction vector at that point. The intersection test respects the 
--face normals of the node, i.e. if a face's normal points away from the ray's source, 
--an intersection test is not performed on that face.
intersectRay <node> <ray> 

--Takes a ray and computes the closest intersection to the surface of the given node.
--It returns an array with the following three elements.
--1) A Ray defining the position of intersection in 3-space and the surface normal 
--	 direction vector at the point.
--2) The index of the face the ray intersects with
--3) The barycentric coordinates of the face that was hit.
intersectRayEx <node> <ray>

--Performs intersectRay on all nodes in the scene.
--Returns an array of results, one entry per node hit, where each entry is a 2 element 
--array containing the node and the intersectRay result for that node.
intersectRayScene <ray>

--query if the bounding boxes of the two specified nodes overlap.
intersects <node> <node>	--boolean




--clone
-- All the clone operations can take any of the standard node creation optional keyword 
-- arguments which are applied after the node has been copied.
copy <node> -- mapped 
reference<node> -- mapped 
instance<node> -- mapped 

--query instance
areNodesInstances <node> <node>
ex.
InstanceMgr.GetInstances $ &rptInstances
trueInstances = for n in rptInstances where\
(areNodesInstances $ n) collect n

--http://docs.autodesk.com/3DSMAX/15/ENU/MAXScript-Help/files/GUID-48C5E2F2-DE34-4EA3-A84C-4DBD463DBF90.htm#WS73099CC142F487553098682E12AC2FC2BC7-58BD
maxOps.cloneNodes 

--generates a new node that contains a copy of the world-state mesh of the source
snapshot <node> -- mapped

--Returns world state of node as a <mesh> value.
snapshotAsMesh <node>

--Lets you turn existing nodes into instances and references to other nodes. 
--You can use these, for example, to replace the geometry of one node with another
instanceReplace <dest_node> <src_node> -- mapped 
referenceReplace <dest_node> <src_node> -- mapped 
ex.
instanceReplace $foo* $baz
--makes all the foo* objects be instances of baz's geometry
--and modifier stack.




--Heirarchies
-- Makes <node2> a child of <node1> . Resets the current location of <node2> to 
-- the location of <node1> unless move:false is specified.
attachObjects <node1> <node2> [move:<boolean> ] 

--Group nodes. 
--You can optionally specify the group name or group name prefix. 
--Specifying select:true selects the group after it is made.
group <node_collection> [name:<string> ] [prefix:<string> ] [select:<boolean> ] --returns the group node.
ex.
group $box* name:"boxes"--makes a group of all box*'s named "boxes".
group selection--groups current selection. 

--Attaches a node collection to an existing group. 
--Nodes that are already members of a group cannot be attached to another group.
attachNodesToGroup <node_collection> <targetNode> 

--Detaches the specified nodes from the groups they belong to.
detachNodesFromGroup <node_collection>

--Ungroups one level of a group node.
ungroup <group_head_node> -- mapped 
ex.
ungroup $group01--ungroups group $group01 

--Ungroups all levels in a group node.
explodeGroup <group_head_node> -- mapped 





--Visibility
--Hides the specified node or node collection.
hide <node> -- mapped 
--If the optional doLayer keyword is set to true and the node is in a layer that is hidden,
--the entire layer is unhidden. When false (the default), just the node is unhidden.
unhide <node> [doLayer:<boolean>] -- mapped 
--Freezes the specified node or node collection.
freeze <node> -- mapped 
--If the optional doLayer keyword is set to true and the node is in a layer that is frozen, 
--the entire layer is unfrozen. When false (the default), just the node is unfrozen.
unfreeze <node> [doLayer:<boolean>] -- mapped


--Sets whether the node is renderable.
setRenderable <node> <boolean>


--query if node is displayed using vertex colors in shaded viewports, false otherwise.
getCVertMode <node> 

--Sets whether to display the effect of assigned vertex colors for the node in shaded viewports.
setCVertMode <node> <boolean>

--query if the vertex color display for the node is shaded in the viewports
getShadeCVerts <node> 

--Sets whether the vertex color display for the node is shaded in the viewports. 
--When true , the colors are unshaded and appear in their pure RGB values. 
--When false , the colors appear like any other assigned color in the viewports.
setShadeCVerts <node> <boolean>





--delete node
delete <node> -- mapped

-- When a node has been deleted,
<node> == undefined --returns false
<node> != undefined --returns true

--query if object still exists in the scene, as in variables or arrays.
isDeleted <MAXWrapper_object> --boolean




--filter geometry Objects
ex.
for obj in objects where classof obj == VRayLight do
(
	print obj;
)

-- alternative method
-- performs the loop through all objects in MAXScript, but instead of calling SuperClassOf 
-- o == GeometryClass it checks whether the class of the object is part of the list of valid 
-- eometryClass classes
ex.
for obj in objects where findItem geometryClass.classes (classof obj) > 0 collect obj



--[Object Sets]
--ObjectSets are collections of the current scene objects divided into the main 3ds max 
--object type categories/classes

objects 	--allobjects in the scene
geometry	--primitives, meshes, other geometry types
lights		--including VRay and third party
cameras		--
helpers		--
shapes		--lines, circles, rectangles, splines
systems		--eg. bones
spacewarps--forces, spacewarps, deflectors, etc
selection --current selection. interchangable with $


--convert objectSet to array
ex.
<objectSet> as array


--hide
ex.
hide shapes

--freeze
ex.
freeze geometry





"CLASSES:_________________________________________________________________________________"

--determine class
ex.
classOf <node> 


--Query class and parent class
obj = selection
print("ClassOf:"+(ClassOf obj) as string)
print("SuperClassOf:"+(SuperClassOf obj) as string)

--alternative method
for obj in selection do 
(
	case (superClassOf obj ) of 
	(
		(GeometryClass)	: (format "object : % | superclass : %\n" (obj.name) "this is GeometryClass")
		(light) : (format "object : % | superclass : %\n" (obj.name) "this is light")
		(camera)	: (format "object : % | superclass : %\n" (obj.name) "this is camera")
		(helper)	: (format "object : % | superclass : %\n" (obj.name) "this is helper")
		(SpacewarpObject)	: (format "object : % | superclass : %\n" (obj.name) "this is SpacewarpObject")
	)

)




struct
ex.
struct person (name, height, age, sex)

bill = person name: "Bill" height:72 age:34 sex:#male
joe = person name: "Joseph" sex:#male

bill.age  --returns 34
joe.age  --returns undefined
joe.age = bill.age-4 --assigns Bill's age less 4 to Joe's age.


ex. --expressions and procedures separated by commas
struct structName
(
	---,
	
	fn functionOne=
	(
	---
		(
		---
		)
	---
	),
	
	fn functionTwo=
	(
		if something then
		(
		---
		)
		else
		(
		---
		)
	)
	
)

Struct=structName()
Struct.functionTwo()




"HIERARCHIES:______________________________________________________________________________"

-- INode.Parent
ex.
$Tile.parent = $Wall						--link tile to wall object

-- INode.Children
ex.
$.children[1].name = "Tile_01"	--set name of first child object





"ANIMATION:________________________________________________________________________________"


animate on (at time 50f (move$ [0,0,5]))	--with AutoKey on, move object at frame 50

animate on (at time 100f ($.radius = 10))	--with AutoKey on, set radius at frame 100









--Out-of-Range Functions
--Gets the Out-of-Range type (ORT) for the controller for the time before the first key.
getBeforeORT <controller>
-- Returns one of the following name values:
-- #constant #cycle #loop #pingPong #linear #relativeRepeat

-- Gets the Out-of-Range (ORT) type for the controller for the time after the last key.
getAfterORT <controller>
--Returns one of the name values as for getBeforeORT() shown above.

-- Sets the Out-of-Range (ORT) type for the controller for the time before the first key.
-- The <ORT_type_name> must be one of the following name values:
-- #constant #cycle #loop #pingPong #linear #relativeRepeat
setBeforeORT <controller> <ORT_type_name>

-- Sets the Out-of-Range (ORT) type for the controller for the time after the last key. 
-- The <ORT_type_name> must be one of the symbolic values shown in setBeforeORT() above. 
-- No testing done on the validity of <ORT_type_name> is performed.
setAfterORT <controller> <ORT_type_name>

-- Enables or disables the Out-of-Range processing for the controller. 
-- If set to disabled with false , the controller effectively employs a constant ORT.
enableORTs <controller> <boolean>





"Render:__________________________________________________________________________________"

max quick render 	--equivalent to pushing the 'render' button

--additional function to kick off renders independant of the current render dialog settings
render camera:$Camera01 frame:100 outputfile:"%currentuser%\\desktop\\.filename.exr"

--set render type
rendTimeType = 1	--( 1= single frame
-- 										2= active frame
-- 										3= user range
-- 										4= frame string )

--set render start frame
rendStart = 100

--set render end frame
rendEnd = 250

--set render size
renderWidth = 1920
renderHight	= 1080

--render to disk
rendSaveFile = true

rendOutputFilename = "%currentuser%\\desktop\\.filename.exr"


--[VRay Specific]

--set current renderer to VRay
renderers.current = VRay()

--set adaptive sampling min rate
renderers.current.adaptiveSubdivision_minRate = 1

--turn on VRays GI calculation
renderers.current.gi_on = true







"ENVIRONMENT:_____________________________________________________________________________"

backgroundColor = color 0 0 0	--set environment background color

useEnvironmentMap = false	--turn environment map off

environmentMap = Checker()	--apply environment map. in this case checker


--[In-View Messages]



--[Ui]

-- get main window instance
window = QtGui.QWidget(MaxPlus.GetQMaxWindow())
_GCProtector.widgets.append(window)




-- basic rollout floater framework
(
	global rofTool	--start a new local variable scope here and declare a global variable for 
									--the rollout floater
	Rollout roTool "Tool"	--start a new rollout definition
	(
		spinner spSpinner "Value:"	--add a spinner and a button control to the rollout
		button btnButton "button text"

		on btnButton pressed do --event handler for the button
		(
			format "value: %\n" spSpinner.value --output current spinner value
		)
	)

	try	--mechanism to prevent opening more than one floater window.
	(
		closeRolloutFloater rofTool
	)
	catch()

	rofTool = newRolloutFloater "Tool Floater" 300 100

	addRollout roTool rofTool	--add rollout to the floater
)




-- Undo
--syntax
--["undo_item_label" | label:<string_operand> | variable_name ] <bool_expr> <expr>

--syntax description
--"undo_item_label" must be a string literal,
--<string_operand> evaluates to a string at runtime,
--variable_name is a global or local variable containing a string value.

ex.
rollout test "test"
(
local undoString = "Button Press"
local buttonPress = 0
button b "press me"
on b pressed dowith undo label:(undoString + (buttonPress +=1) as string) on box()
)

ex.
createdialog test
undo "add background" on
(
...
)

ex.
my_context_name = "An Undo Context"
undo my_context_name on
(
...
)




"TIME_____________________________________________________________________________________"

-- sleep
--interrupt sleep with ESC key; halts execution. SPACE bar to halt sleep & continue executing
--argument is a floating point number of seconds.
ex.
sleep 20 --pause a script in seconds




-- dotNetObject:System.Windows.Forms.Timer
-- alternative to the MAXScript rollout Timer control.
-- The main advantage of the DotNet version is the ability to call MAXScript functions at given intervals without the need for a rollout.
ex.
function PerformDelayedTasks sender evt=
	(
	sender.enabled = false -- important: don't repeat this timer event
	dotnet.RemoveEventHandler sender "Elapsed" PerformDelayedTasks -- for sanity and cleanup      

	-- put all delayed commands here          
	)

delayTimer= dotnetobject "Windows.Forms.Timer"
delayTimer.Interval=5000

dotnet.AddEventHandler delayTimer "Tick" PerformDelayedTasks

delayTimer.enabled = true


-- another dotNet example
ex.
theTimer = dotNetObject "System.Windows.Forms.Timer" --create a Timer
fn printTime = 
	(
	print localTime --define a MAXScript function to be called by the Timer.
	) 
dotnet.addEventHandler theTimer "tick" printTime --add ON TICK event hander to call the function
theTimer.interval = 1000 --set the tick interval to 1 second (1000 milliseconds)
theTimer.start() --start the Timer
--theTimer.stop() --use this method to stop the Timer.







"RANDOMIZE:_______________________________________________________________________________"

random

ex.
$.pos.x = random 0 10		--integer or float. randomize between first and second value.

ex.
$material.diffuseColor = color 0 0 (random 0 360) --randomize rgb 'b' value




"PYTHON:__________________________________________________________________________________"


--print list of available python methods to output window
showinterface python


Init(): --Loads Python if it is not loaded already.

-- [run python]
--run python code
ex.
python.Execute "print 'hello'"

--run python file from maxscript
ex.
python.ExecuteFile "tk_setup.py"
--full path
ex.
python.ExecuteFile @"C:\Program Files\Autodesk\3ds Max 2015\scripts\Python\demoBentCylinder.py"



--python modules in maxscript:
--import a module
--assign value to a variable when importing
ex.
max_customTools_func = python.Import "max_customTools_func"

--Documentation: https://knowledge.autodesk.com/search-result/caas/CloudHelp/cloudhelp/2017/ENU/Max-Python-API/developer/executing-python-from-maxscript-html.html
-- Python libraries can be imported and used in MAXScript, using Python.Import(). 
--In this example, we import the Python built-in methods and constants, 
--and use the pow() function:
builtIn = Python.Import "__builtin__"
-- <module '__builtin__' (built-in)>
builtIn.pow 2 3
-- 8

ex.
QtCore = python.Import "PySide2.QtCore"


--Reloads a Python module
--for example, a keyword gets re-defined 
Reload()
ex.
python.reload theModule
-- <module '__builtin__' (built-in)>


--Errors
--Returns, as a string, the error message associated with the last error encountered 
--while running the Init(), Execute(), or ExecuteFile() methods.
GetLastError(): 






-- MaxPlus
-- set a variable for a maxscript command in maxplus
MaxPlus.Core.EvalMAXScript("variable = $")

--retrieve the value from a FP wrapped variable
pymxs.runtime.variable


--transformation
ex.
MaxPlus.Point3(ScaleAmount, ScaleAmount, ScaleAmount)

ex.
box = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Box)
box.ParameterBlock.Length.Value = 10.0
box.ParameterBlock.Height.Value = 10.0
box.ParameterBlock.Width.Value = 10.0



--materials
ex.
--create a new default material as follows:
m = MaxPlus.Factory.CreateDefaultStdMat()
--set attributes
m.Diffuse = MaxPlus.Color(0, 0, 1)
m.Specular = MaxPlus.Color(1, 1, 1)
--assign it to the node of the object
node.Material = m




--Core:
--variable
GetRootNode () 
ex.
for node in MaxPlus.Core.GetRootNode().Children:

IsGlobalVariableNameSettable (args)

IsVariableNameValid (args)

--script
EditMAXScriptFile (args)

EvalMAXScript (args) 

ExecuteMAXScript (args) 

Print (args) 

Write (args) 

WriteLine (args) 

--time
ResetCurrentTimeContext () 

GetCurrentTime () 

GetCurrentTimeContext () 

SetCurrentTime (args) 

SetCurrentTimeContext (args) 

UseCurrentTimeContext () 

--interface
GetCOREInterface (args) 

GetCOREInterfaceAt (args) 

GetFPInterface (args) 

GetFPInterfaceDesc (args) 

GetInterface (args) 

GetWindowHandle () 


-- FPValvue --Function Publishing (Interface)
--Assign FPValue
--execute a MAXScript expression using Core.EvalMAXScript() and obtain a return value via FPValue 
--using either:
ex.
commandString1 = 
"import MaxPlus
MaxPlus.Core.EvalMAXScript(\"print #aaa\")
"
--RETURNS FPValue which is held in the commandString1 variable
--python.execute commandString1

--or:
ex.
fpValue = MaxPlus.FPValue()
evaluation_success = MaxPlus.Core.EvalMAXScript(<string>, fpValue)


--Get FPValue
--An FPValue wraps various types of values, for example, int, float, object, mesh, and so forth.

--obtain the value stored in the FPValue
ex.
<FPValue>.Get()
--or
ex.
MaxPlus.FPValue.Get(<FPValue>)


--Get Type
ex.
<FPValue>.GetType()
--or
ex.
MaxPlus.FPValue.GetType(<FPValue>)

--Get Type string
--return a string corresponding to the supplied type value
MaxPlus.FPTypeGetName(<FPValue>.GetType())


--help
--print to listener output a list of FPValue type names and their corresponding constants:
ex.
import MaxPlus
help(MaxPlus.FPTypeConstants)
--OUTPUT:

   AngAxis = 48						AngAxisTab = 2096			Angle = 5						AngleTab = 2053				BOOL = 4					BOOLTab = 2052			BezierShape = 71
   
   BezierShapeTab = 2119	BitArray = 51					BitArrayTab = 2099  Bitmap = 16						BitmapTab = 2064	Bool = 66						BoolTab = 2114
  
 	 Box3 = 70							Box3Tab = 2118				ClassDesc = 52			ClassDescTab = 2100		Color = 62				ColorChannel = 11		ColorChannelTab = 2059
   
   ColorTab = 2110				Control = 55					ControlTab = 2103		DWORD = 65						DWORDTab = 2113		Double = 69					DoubleTab = 2117
   
   Enum = 45							EnumTab = 2093				FPInterface = 59		FPInterfaceTab = 2107	FPValue = 63			FPValueTab = 2111		FRgb = 23
   
   FRgbTab = 2071					FileName = 9					FileNameTab = 2057	Float = 0							FloatTab = 2048		HWND = 60						HWNDTab = 2108
   
   Hsv = 10								HsvTab = 2058					IObject = 58				IObjectTab = 2106			Index = 19				IndexTab = 2067			Int = 1
   
   Int64 = 68							Int64Tab = 2116				IntPtr = 67					IntPtrTab = 2115			IntTab = 2049			Interval = 47				IntervalTab = 2095
   
   MSFloat = 254					Matrix3 = 20					Matrix3Tab = 2068		Mesh = 53							MeshTab = 2101		Mtl = 14						MtlTab = 2062
   
   Name = 61							NameTab = 2109				Node = 17						NodeTab = 2065				Object = 54				ObjectTab = 2102		PBlock2 = 21
   
   PBlock2Tab = 2069			PercentFraction = 6		PercentFractionTab = 2054	Point = 56			Point2 = 30				Point2Tab = 2078		Point3 = 3
   
   Point3Tab = 2051				Point4 = 22						Point4Tab = 2070		PointTab = 2104				Quat = 49					QuatTab = 2097			RadioButtonIndex = 13
   
   RadioButtonIndexTab = 2061	Ray = 50					RayTab = 2098				RefTarg = 18					RefTargTab = 2066	Rgb = 2							RgbTab = 2050
   
   Str = 57								StrTab = 2105					String = 8					StringTab = 2056			Texmap = 15				TexmapTab = 2063		TimeValue = 12
   
   TimeValueTab = 2060		Value = 64						ValueTab = 2112			Void = 46							VoidTab = 2094		World = 7						WorldTab = 2055



--Get the INDEX inside the Parent Anim Object
getParameterSubAnimNum
(ParamCollectorOps.getParameterParentAnim 1)[ParamCollectorOps.getParameterSubAnimNum 1].value
--RETURNS the value of the Length sub-animation track.
ex.
(ParamCollectorOps.getParameterParentAnim 1)[ParamCollectorOps.getParameterSubAnimNum 1].value = 10
--will set the value of the Box's length to 10 units and so on...

--"1" is the index of the parameter. You can get the index of a parameter by using 
ParamCollectorOps.getParameterIndex 1 1 1
--where the first argument is the collection index, the second is the rollout index in the collection, 
--the third is the parameter index inside the rollout. In the above case, the result would be 1 
--(first parameter in first rollout of the first collection)...






-- pymxs
--wrapper for the MAXScript engine, exposes virtually all the Interfaces, globals, and classes available in MAXScript
--see demoPyMXSTypeInterop.py example file in cloud 3ds scripts pymxs directory.


ex.
import pymxs
at = pymxs.attime
rt = pymxs.runtime
--create Teapot
t = rt.Teapot()

--animate it
with pymxs.animate(True):
with at(1):
    t.pos = rt.Point3(2,2,2)
with at(12):
    t.pos = rt.Point3(10, 10, 10)
with at(21):
    t.pos = rt.Point3(20,20,20)



ex.
import pymxs
rt = pymxs.runtime

--Create and visit a MaxScript Array
rt.execute(" gma = #(1,2,3)")
print rt.gma    
--#output: #(1,2,3)
len(rt.gma)    
--#output: 3
rt.gma[1] = 999
rt.Print(rt.gma[1])    
--#output: 999
l = list(rt.gma) #[1,999,3]
l[2] = 888
print l    
--#output: [1, 888, 3]
print rt.gma   
--# output: #(1, 999, 3)

--# Create a MaxScript Array via python sequence
ma = rt.Array(*(1, 2, 3))
print ma    
--#output: #(1,2,3)




--print in pymxs
pymxs.print_()





"EXTERNAL_FILES:__________________________________________________________________________"

-- Returns the filename path of the source file the function has been called from.
<filename>getSourceFileName() 


-- [run maxscript]
--fileIn will do the same as "run script" or evaluate all in the editor. 
--It can make a function available if it's globally declared
FileIn
ex.
fullPath = "O:\\Cloud\\____Graphics\\3ds Max\\Scripts\\macros\\tk_macroScript.ms"
FileIn fullPath


Include
-- Include actually takes the code from that file and injects it at that point. 
-- So if you have a large script and you want to organize things a bit better you can write 
-- certain functions in a separate file and include that function when the script get executed,
-- so that function would always accessible because it is included in that scope.








-- full path. (may be neccesarry to initialize python python.Init() )
fullPath = "%CLOUD%/____Graphics/3ds Max/Scripts/___Python_path/tk_setup.py"
python.ExecuteFile @fullPath


-- run python file FROM WINDOWS COMMAND LINE or batch file
3dsmax -U PythonHost "tk_setup.py" 









"dotNet___________________________________________________________________________________"

-- Operators:
== != 

sender


--query properties or events
ex.
ctrl = dotNetClass "System.Windows.Forms.Control"
showProperties ctrl
showEvents ctrl
showMethods ctrl
dotNet.showConstructors ctrl

dotNet.addEventHandler
-- takes 3 arguments:
-- a dotnetobject with a public event,
-- a string that is the name of the event,
-- and an maxscript function

ex.
ctrl = dotNetClass "System.Windows.Forms.Control"
dotnet.addeventhandler ctrl "KeyDown" keyDownFunction




"USER_INPUT:______________________________________________________________________________"

-- [hotkeys]



-- [.net System.Windows.Forms.Control]
-- Documentation
-- https://msdn.microsoft.com/en-us/library/system.windows.forms.control%28v=vs.110%29.aspx?f=255&MSPPError=-2147217396

ex.
control = dotNetClass "system.windows.forms.control"
showProperties control
showProperties control.keyDown
showProperties control.keyUp

on control.keyDown.x do
	(
	snapmode.setOSnapItemActive 4 1 (true);
	snapmode.setOSnapItemActive 4 2 (true);
	)
on control.keyUp.x do
	(
	snapmode.setOSnapItemActive 4 1 (false);
	snapmode.setOSnapItemActive 4 2 (false);
	)

-- if statement for above
if control.keyUp == control.keyUp.x do
		(
		---
		)

-- actions
KeyDown		--Occurs when a key is pressed while the control has focus.
KeyPress	--Occurs when a character. space or backspace key is pressed while the control has focus.
KeyUp			--Occurs when a key is released while the control has focus.
KeyEventArgs --Provides query data for the KeyDown or KeyUp event.
KeyPressEventArgs	--Provides query data for the KeyPress event.
ModifierKeys --Gets a value indicating which of the modifier keys (SHIFT, CTRL, and ALT) is in a pressed state.


MouseButtons --Gets a value indicating which of the mouse buttons is in a pressed state.
MousePosition	--Gets the position of the mouse cursor in screen coordinates.
MouseDown	--Occurs when the mouse pointer is over the control and a mouse button is pressed.
MouseEnter --Occurs when the mouse pointer enters the control.
MouseHover --Occurs when the mouse pointer rests on the control.
MouseLeave --Occurs when the mouse pointer leaves the control.
MouseMove --Occurs when the mouse pointer is moved over the control.
MouseUp		--Occurs when the mouse pointer is over the control and a mouse button is released.

-- microsoft keyboard key names:
-- https://msdn.microsoft.com/en-us/library/system.windows.forms.keys(v=vs.110).aspx


-- Create a DotNet TextBox
ex.
hTextBox = dotNetObject "System.Windows.Forms.TextBox"
hTextBox.size = dotNetObject "System.Drawing.Size" 160 25
hTextBox.location = dotNetObject "System.Drawing.Point" 20 20
-- Create a DotNet Form
hForm = dotNetObject "System.Windows.Forms.Form"
hForm.size = dotNetObject "System.Drawing.Size" 200 100
hForm.controls.add hTextBox
hForm.topmost = true
-- Create a DotNet Application to run the form
hApp = dotNetClass "System.Windows.Forms.Application"
hApp.run hForm



"SCRIPT_EDITOR:___________________________________________________________________________"

--MAXScript Editor Properties File - Quick Navigation:
--https://help.autodesk.com/view/3DSMAX/2018/ENU/?guid=__files_GUID_8588CAB1_7F4E_4A5E_9CD8_7F11F4DF9755_htm

--[defining keyboard shortcuts]

-- Tools > Open Global Options File menu item
-- Scroll down and locate the section remarked as

--  # User defined key commands
--	syntax: <shortcut>|<command>|\
--add a '\' at the end of each line except the last.
--The modifier keys are Ctrl, Shift, and Alt

-- The named keys are Left, Right, Up, Down, Insert, End, Home, Enter, Space, Tab, 
-- KeypadPlus, KeypadMinus, KeypadMultiply, KeypadDivide, Escape, Delete, PageUp, 
-- PageDown, Slash, Question, Equal, Win.

--Documentation: https://knowledge.autodesk.com/search-result/caas/CloudHelp/cloudhelp/2015/ENU/MAXScript-Help/files/GUID-BC77ED4A-66B5-4958-876D-DBBBBD486A52-htm.html
--Changes active after restart





-- [External Editor]

-- Sublime text: send to 3ds Max
-- file: Key Bindings - User file 

-- default MAXScript Listener keys:
{ "keys": ["ctrl+e"], "command": "send_file_to_max" },
{ "keys": ["shift+enter"], "command": "send_selection_to_max"},
{ "keys": ["ctrl+shift+e"], "command": "select_max_instance" },
{ "keys": ["f1"], "command" : "open_max_help"}


--MAXScript Editor - Defining Custom Keywords
-- https://knowledge.autodesk.com/search-result/caas/CloudHelp/cloudhelp/2015/ENU/MAXScript-Help/files/GUID-85AD190F-1A65-4BF2-8AE8-9688960B1ACC-htm.html

"Abbreviations files"
-- Abbreviations in Maxscript is one of the powerful tools in scripting, yet not all artists know about. 
-- Frankly it was found to make our scripting life much easier, have you ever thought of a short cut to 
-- your codes instead of writing them over and over again or at best case you would copy and paste from 
-- your collected library of codes.
-- Well the good news is that abbreviations in Maxscript was found for this exact reason, so instead of 
-- defining a Functions the old way why don't we just type fn and then hit Ctrl+Shift+A and it will throw 
-- us a full code:

FN _NAME =
(
 "Your code"
)

-- We can do it for loops or rollout templates etc.....
-- And to know how this magic works we are going to follow those simple steps:
 
-- 1- Create a new script and in Tools > Open abbreviations file, this will open an empty script for you 
-- (in case you didn't edit it before) were you can define your abbreviations.
 
-- 2- An abbreviation is defined in the form:
-- <AbbrevName>=<Expanded Form>
-- for example let's define a for loop

fordo=for i in 1 to 10 do ()
save it. Now open a new script and type fordo and hit Ctrl+Shift+A or go to Edit > Expand abbreviations. 

-- Voila! a for loop appeared.
 
-- 3- There are some rules you should follow here, AbbrevName is case sensitive and it detects spaces. So if 
-- you define it like:
-- For do =, when you want to call it the F should be capital and there is a space inbetween and after do.
 
-- 4- If you want to arrange the expanded forms to have tabs and on different lines then we have to use (\n) 
-- to move the following into another line and (\t) to add a tab, our loop example would change to be:
-- fordo=for i in 1 to 10 do \n(\n\t "your code" \n)
-- As simple as this. So when we call fordo it's gonna give us:

for i in 1 to 10 do 
(
  "your code" 
)

-- And here a couple of abbreviations you can add to your library:

fordo=for i in 1 to 10 do \n(\n\t "your code" \n)
rol=rollout _name "name" \n(\n \n)\n createdialog _name     
fn=fn NAME arg_a arg_b =\n(\n\tfnBody\n)
if=if ARG then\n(\n\tState\n)\nelse\n(\n\tState2\n)
sh=shellLaunch @"your file" ""
mfn=maxfilename
mfp=maxfilepath


-- [Abbreviations file]
/* COMMENTS */
header=/*HeaderStart***********\n:Created By:\t\t\tName:\n:Company:\t\t\t\t***********HeaderEnd*/
fnHeader=/*FnStart***********\n:Function: |\n:Usage: \n:Returns: \n:Todo: \n:Notes: \n***********FnEnd*/
fn=/*FnStart***********\n:Function |\n:Usage: \n:Returns: \n:Todo: \n:Notes: \n***********FnEnd*/
comment=/*CommentStart***********\n|\n***********CommentEnd*/

/* CODE STRUCTURES */
struct=struct |\n(\n\tfn,\n\t\n\tfn\n)\nNAME = NAME()
attributes=def = attributes NAME_D\n--redefine:def\n(\n\tlocal VAR = undefined\n\t\n\tparameters\n\n\trollout\n)
parameters=parameters NAME_Prm\n(\n\tPARAM type:#VAL\n)
for x=for x in ARRAY where ARG do\n(\n\tEXPR\n)
for i=for i = 1 to INTEGER where ARG do\n(\n\tEXPR\n)
if=if EXPR then\n(\n\tEXPR\n)\nelse\n(\n\tEXPR\n)
case=case EXPR of =\n(\n\tFACTOR: EXPR\n\tdefault: EXPR\n)

/* UI CONTROLS */
spinner=spinner NAME_Spin *CAPTION* range:[0,100,0] type:#float fieldWidth:spnW1 align:#right
slider=slider NAME_Sld *CAPTION* range:[0,100,0] type:#float ticks:2 align:#center
button=button NAME_Bt *CAPTION* width:w1 align:#center
checkbutton=checkbutton NAME_Cbt *CAPTION* align:#center
edittext=edittext NAME_Et *CAPTION* fieldWidth:w1 labelOnTop:true align:#left
checkbox=checkbox NAME_Cbx *CAPTION* align:#left
label=label NAME_Lbl *CAPTION* align:#center
group=group *CAPTION*\n(\n\tCONTROLS\n)

/* MAX WRAPPERS */
nodeTransformMonitor=nodeTransformMonitor node:| forwardTransformChangeMsgs:false

/* GENERAL */



-- MAXScript Editor - Defining And Using Abbreviations:
-- https://knowledge.autodesk.com/search-result/caas/CloudHelp/cloudhelp/2015/ENU/MAXScript-Help/files/GUID-7358FB2E-182A-4BB8-8208-3E74D28FC205-htm.html



-- query



"ERRORS:__________________________________________________________________________________"

--[Error Handling]

















--[Debugging: non-descript syntax errors and typos]



















