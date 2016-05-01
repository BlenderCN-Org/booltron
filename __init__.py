bl_info = {
	"name": "Booltron",
	"author": "Mikhail Rachinskiy (jewelcourses.com)",
	"version": (2000,),
	"blender": (2,7,4),
	"location": "3D View → Tool Shelf",
	"description": "Booltron—super add-on for super fast booleans.",
	"wiki_url": "https://github.com/mrachinskiy/blender-addon-booltron",
	"tracker_url": "https://github.com/mrachinskiy/blender-addon-booltron/issues",
	"category": "Mesh"}

if "bpy" in locals():
	from importlib import reload
	reload(utility)
	reload(operators)
	reload(ui)
	del reload
else:
	import bpy
	from . import (operators, ui)


classes = (
	ui.ToolShelf,

	operators.UNION,
	operators.DIFFERENCE,
	operators.INTERSECT,
	operators.SLICE,
	operators.SUBTRACT,
)


def register():
	for cls in classes:
		bpy.utils.register_class(cls)


def unregister():
	for cls in classes:
		bpy.utils.unregister_class(cls)


if __name__ == "__main__":
	register()
