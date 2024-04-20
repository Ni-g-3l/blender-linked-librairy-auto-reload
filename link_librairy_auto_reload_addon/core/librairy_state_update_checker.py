import os

from link_librairy_auto_reload_addon.core.update_time_watcher import OsUpdateTimeWatcher

class LibrairyStateUpdateChecker:

    update_time_watcher = OsUpdateTimeWatcher

    LIBRAIRIES = {}

    @classmethod
    def reload_needed(cls, librairy_path):
        if librairy_path not in cls.LIBRAIRIES:
            cls.LIBRAIRIES[librairy_path] = cls.update_time_watcher.get_update_time(librairy_path)
            return False
        
        last_update_time = cls.LIBRAIRIES.get(librairy_path)
        current_update_time = cls.update_time_watcher.get_update_time(librairy_path)

        if current_update_time > last_update_time:
            cls.LIBRAIRIES[librairy_path] = current_update_time
            return True
        return False

    @classmethod
    def reset(cls):
        cls.LIBRAIRIES.clear()