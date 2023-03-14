# Z axis 방향으로 -20 ~ 25 구간에 모든 형상이 존재한다
#offset = -10
#Make Polygon and extrude each polygon
def AddPlane(offset,index1) :
	import FreeCAD, Draft, Drawing
	ZAxis = FreeCAD.Vector(0, 0, 1)
	p3 = FreeCAD.Vector(100, 100, offset)
	place3 = FreeCAD.Placement(p3, FreeCAD.Rotation(ZAxis, 0))
	Polygon3 = Draft.makePolygon(6, radius=300, placement=place3)
	f = FreeCAD.getDocument('Unnamed').addObject('Part::Extrusion', 'Extrude'+str(index1))
	f = App.getDocument('Unnamed').getObject('Extrude'+str(index1))
	f.Base = Polygon3
	f.DirMode = "Normal"
	f.DirLink = None
	f.LengthFwd = 5.000000000000000
	f.LengthRev = 0.000000000000000
	f.Solid = True
	f.Reversed = True
	f.Symmetric = False
	f.TaperAngle = 0.000000000000000
	f.TaperAngleRev = 0.000000000000000
	f.Base.ViewObject.hide()
	App.ActiveDocument.recompute()

for i in range(-3,6):
	AddPlane(i*5,i+3)

#Intersection of Boolean operation each Extrude with orgianl shape
for i in range(0,9):
	ex = App.ActiveDocument.getObject('Extrude'+str(i))
	App.activeDocument().addObject('Part::MultiCommon','Common'+str(i))
	App.activeDocument().getObject('Common'+str(i)).Shapes = [App.activeDocument().getObject('Extrude'+str(i)),App.activeDocument().Part__Feature,]
	Gui.activeDocument().getObject('Extrude'+str(i)).Visibility=False
	Gui.activeDocument().Part__Feature.Visibility=False
	App.ActiveDocument.recompute()
	#Or Drawing "Project Shape"
	#Vertor 값을 어떻게 정할 것이냐????


def ProjectCommon(i):
	import Drawing
	pro = App.ActiveDocument.getObject('Common'+str(i))
	FreeCAD.ActiveDocument.addObject('Drawing::FeatureProjection','Common_proj'+str(i))
	FreeCAD.ActiveDocument.ActiveObject.Direction=FreeCAD.Vector(0, 0, 1)
	FreeCAD.ActiveDocument.ActiveObject.Source=pro
	FreeCAD.ActiveDocument.ActiveObject.VCompound=True
	FreeCAD.ActiveDocument.ActiveObject.Rg1LineVCompound=True
	FreeCAD.ActiveDocument.ActiveObject.RgNLineVCompound=True
	FreeCAD.ActiveDocument.ActiveObject.OutLineVCompound=True
	FreeCAD.ActiveDocument.ActiveObject.IsoLineVCompound=True
	FreeCAD.ActiveDocument.ActiveObject.HCompound=False
	FreeCAD.ActiveDocument.ActiveObject.Rg1LineHCompound=False
	FreeCAD.ActiveDocument.ActiveObject.RgNLineHCompound=False
	FreeCAD.ActiveDocument.ActiveObject.OutLineHCompound=False
	FreeCAD.ActiveDocument.ActiveObject.IsoLineHCompound=False

for i in range (0,9):
	ProjectCommon(i)


import Draft
com0 = []
com1 = []
com2 = []
com3 = []
com4 = []
com5 = []
com6 = []
com7 = []
point0=[]
point1=[]
point2=[]
point3=[]
point4=[]
point5=[]
point6=[]
point7=[]
com0 = App.ActiveDocument.getObject('Common_proj0')
com1 = App.ActiveDocument.getObject('Common_proj1')
com2 = App.ActiveDocument.getObject('Common_proj2')
com3 = App.ActiveDocument.getObject('Common_proj3')
com4 = App.ActiveDocument.getObject('Common_proj4')
com5 = App.ActiveDocument.getObject('Common_proj5')
com6 = App.ActiveDocument.getObject('Common_proj6')
com7 = App.ActiveDocument.getObject('Common_proj7')
for j in range(0,len(com0.Shape.Edges)):
	if (type(com0.Shape.Edges[j].Curve) == Part.Line):
		for i in range(0,len(com0.Shape.Edges[j].Vertexes)):
			Draft.makePoint(com0.Shape.Edges[j].Vertexes[i].Point)
	#else (type(com6.Shape.Edges[j].Curve) == Part.Circle):
	else :
		Draft.makeCircle(com0.Shape.Edges[j], placement=None, face=None, startangle=None, endangle=None, support=None)

	for i in range(0,len(com0.Shape.Edges[j].Vertexes[i].Point)):
	point0.append(App.ActiveDocument.getObject.Point)
	Draft.makeWire(point0)
	#for i in range(0,len(com4.Shape.Edges[j].Vertexes)):
	#Circle6i = Draft.makePoint(com4.Shape.Edges[j].Vertexes[i].Point)
