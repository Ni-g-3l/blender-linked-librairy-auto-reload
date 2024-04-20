import bpy

from link_librairy_auto_reload_addon.core.librairy_state_update_checker import LibrairyStateUpdateChecker

class LIBRAIRY_OT_reload_new_updated_librairy(bpy.types.Operator):

    bl_idname = "librairy.reload_updated_librairy"
    bl_label = "Reload updated librairy"

    def execute(self, _):
        for lib in bpy.data.libraries:
            if LibrairyStateUpdateChecker.reload_needed(bpy.path.abspath(lib.filepath)):
                self.report({"INFO"}, f"Librairy '{lib.name}' reloaded")
                lib.reload()
        return {"FINISHED"}