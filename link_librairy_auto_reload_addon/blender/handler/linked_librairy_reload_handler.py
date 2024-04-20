import bpy
from bpy.app.handlers import persistent

from link_librairy_auto_reload_addon.core.librairy_state_update_checker import LibrairyStateUpdateChecker
from link_librairy_auto_reload_addon.blender.timer.linked_librairy_reload_timer import register_timer, unregister_timer

@persistent
def reset_librairy_update_state_checker(_):
    LibrairyStateUpdateChecker.reset()
    register_timer()


def register_handler():
    bpy.app.handlers.load_post.append(reset_librairy_update_state_checker)

def unregister_handler():
    bpy.app.handlers.load_post.remove(reset_librairy_update_state_checker)
    unregister_timer()