import os


class OsUpdateTimeWatcher:

    @staticmethod
    def get_update_time(file_path):
        return os.path.getmtime(file_path) 