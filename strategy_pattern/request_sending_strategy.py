from abc import ABC, abstractmethod


class RequestSendingStrategy(ABC):
    @abstractmethod
    def upload_request_object(self):
        pass


class SftpUploadStrategy(RequestSendingStrategy):
    def upload_request_object(self):
        print('SFTP sending')
