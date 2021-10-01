from strategy_pattern.request_formation_strategy import ExcelFormationStrategy
from strategy_pattern.request_backup_strategy import S3BackupStrategy, GlacierBackupStrategy
from strategy_pattern.request_sending_strategy import SftpUploadStrategy


class RequestHandlingStrategy:
    def __init__(self):
        self.request_prep_obj = None
        self.request_backup_obj = None
        self.request_upload_obj = None

    def perform_request_preparation(self):
        self.request_prep_obj.prepare_request_object()

    def perform_request_backup(self):
        self.request_backup_obj.backup_request_object()

    def perform_request_upload(self):
        self.request_upload_obj.upload_request_object()


class PerchRequestHandlingStrategy(RequestHandlingStrategy):
    def __init__(self):
        super(PerchRequestHandlingStrategy, self).__init__()
        self.request_prep_obj = ExcelFormationStrategy()
        self.request_backup_obj = S3BackupStrategy()
        self.request_upload_obj = SftpUploadStrategy()


class LanternRequestHandlingStrategy(RequestHandlingStrategy):
    def __init__(self):
        super(LanternRequestHandlingStrategy, self).__init__()
        self.request_prep_obj = ExcelFormationStrategy()
        self.request_backup_obj = GlacierBackupStrategy()
        self.request_upload_obj = SftpUploadStrategy()
