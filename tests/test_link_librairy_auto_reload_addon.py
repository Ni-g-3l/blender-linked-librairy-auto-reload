import unittest

from link_librairy_auto_reload_addon.core.librairy_state_update_checker import LibrairyStateUpdateChecker


class FakeOlderUpdateTimeWatcher:

    @staticmethod
    def get_update_time(file_path):
        return 0

class FakeYoungerUpdateTimeWatcher:

    @staticmethod
    def get_update_time(file_path):
        return 100

class Test_link_librairy_auto_reload_addon(unittest.TestCase):

    def tearDown(self):
        LibrairyStateUpdateChecker.reset()

    def test_check_update_state_on_new_librairy(self):
        LibrairyStateUpdateChecker.update_time_watcher = FakeOlderUpdateTimeWatcher
        self.assertFalse(LibrairyStateUpdateChecker.reload_needed("new_librairy_file.blend"))

    def test_check_update_state_on_new_librairy_multiple_time_without_update(self):
        LibrairyStateUpdateChecker.update_time_watcher = FakeOlderUpdateTimeWatcher
        self.assertFalse(LibrairyStateUpdateChecker.reload_needed("new_librairy_file.blend"))
        self.assertFalse(LibrairyStateUpdateChecker.reload_needed("new_librairy_file.blend"))

    def test_check_update_state_on_new_librairy_multiple_time_with_update(self):
        LibrairyStateUpdateChecker.update_time_watcher = FakeOlderUpdateTimeWatcher
        self.assertFalse(LibrairyStateUpdateChecker.reload_needed("new_librairy_file.blend"))
        LibrairyStateUpdateChecker.update_time_watcher = FakeYoungerUpdateTimeWatcher
        self.assertTrue(LibrairyStateUpdateChecker.reload_needed("new_librairy_file.blend"))

if __name__ == '__main__':
    unittest.main()