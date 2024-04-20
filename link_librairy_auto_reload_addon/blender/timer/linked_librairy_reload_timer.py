import bpy
from bpy.app.handlers import persistent

@persistent
def check_librairy_to_reload_every_2_seconds():
    bpy.ops.librairy.reload_updated_librairy()
    return 2.0


def register_timer():
    if not bpy.app.timers.is_registered(check_librairy_to_reload_every_2_seconds):
        bpy.app.timers.register(check_librairy_to_reload_every_2_seconds)

def unregister_timer():
    bpy.app.timers.unregister(check_librairy_to_reload_every_2_seconds)