import bpy
from bpy.props import FloatProperty
from .. import LuxCoreNodeTexture
from ... import utils
from .. import COLORDEPTH_DESC

class LuxCoreNodeTexColorAtDepth(LuxCoreNodeTexture):
    bl_label = "Color at depth"
    bl_width_min = 200
    
    color_depth = FloatProperty(name="Absorption Depth", default=1.0, subtype="DISTANCE", unit="LENGTH",
                               description=COLORDEPTH_DESC)

    def init(self, context):
        self.add_input("LuxCoreSocketColor", "Absorption", (1, 1, 1))
        self.outputs.new("LuxCoreSocketColor", "Color")

    def draw_buttons(self, context, layout):
        layout.prop(self, "color_depth")
    
    def export(self, props, luxcore_name=None):
        abs_col = self.inputs["Absorption"].export(props)

        definitions = {
            "type": "colordepth",
            "kt": abs_col,
            "depth": self.color_depth,
        }
        
        return self.base_export(props, definitions, luxcore_name)