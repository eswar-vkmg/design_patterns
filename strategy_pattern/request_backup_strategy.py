from abc import ABC, abstractmethod


class RequestBackupStrategy(ABC):
    @abstractmethod
    def backup_request_object(self):
        pass


class S3BackupStrategy(RequestBackupStrategy):
    def backup_request_object(self):
        print('Using S3 for backup')


class GlacierBackupStrategy(RequestBackupStrategy):
    def backup_request_object(self):
        print('Using Glacier for backup')
