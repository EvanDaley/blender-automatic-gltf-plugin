bl_info = {
    "name": "AutoGLTF",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import os
import shutil

bpy.ops.wm.save_mainfile() 


class ObjectAutoExportGltf(bpy.types.Operator):
    """My Object Exporting Script"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.autoexport"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Export to GLTF"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.
        # The original script
        # scene = context.scene
        filepath = os.path.join(export_path, name)
        # filepath = bpy.path.ensure_ext(filepath, ".x3d")

        bpy.ops.export_scene.gltf(

        )
        # for obj in scene.objects:
            # obj.location.x += 1.0
            

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

def menu_func(self, context):
    self.layout.operator(ObjectAutoExportGltf.bl_idname)

def register():
    bpy.utils.register_class(ObjectAutoExportGltf)
    bpy.types.VIEW3D_MT_object.append(menu_func)  # Adds the new operator to an existing menu.

def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_func)  # Removes the new operator from an existing menu.
    bpy.utils.unregister_class(ObjectAutoExportGltf)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()