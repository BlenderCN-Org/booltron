import bpy
from bpy.types import Panel


class ToolShelf(Panel):
	bl_category = 'Booltron'
	bl_label = 'Booltron'
	bl_idname = 'booltron_panel'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_context = 'objectmode'

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def draw(self, context):
		layout = self.layout
		layout.enabled = len(context.selected_objects) > 1

		col = layout.column(align=True)
		col.operator('booltron.union', text='Union')
		col.operator('booltron.difference', text='Difference')
		col.operator('booltron.intersect', text='Intersect')
		col.separator()

		sub = col.column(align=True)
		sub.enabled = len(context.selected_objects) == 2
		sub.operator('booltron.slice', text='Slice')
		sub.operator('booltron.subtract', text='Subtract')
