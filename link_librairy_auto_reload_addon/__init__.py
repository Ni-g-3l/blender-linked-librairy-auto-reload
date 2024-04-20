bl_info = {
    "name": "Linked Librairy Auto Reloader",
    "author": "Ni-g-3l",
    "version": (0, 1, 0),
    "blender": (3, 5, 1),
    "location": "System",
    "description": "Auto reload linked librairy",
    "warning": "",
    "doc_url": "",
    "category": "System",
}
import bpy

from link_librairy_auto_reload_addon.blender.operator.reload_update_librairy_operator import LIBRAIRY_OT_reload_new_updated_librairy
from link_librairy_auto_reload_addon.blender.timer.linked_librairy_reload_timer import register_timer, unregister_timer
from link_librairy_auto_reload_addon.blender.handler.linked_librairy_reload_handler import register_handler, unregister_handler

def register():
    bpy.utils.register_class(LIBRAIRY_OT_reload_new_updated_librairy)
    register_handler()


def unregister():
    bpy.utils.unregister_class(LIBRAIRY_OT_reload_new_updated_librairy)
    unregister_handler()
