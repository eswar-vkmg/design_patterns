from strategy_pattern.request_handling_strategy import PerchRequestHandlingStrategy, LanternRequestHandlingStrategy
from strategy_pattern.request_backup_strategy import S3BackupStrategy

if __name__ == '__main__':
    agencies = ['Perch', 'Lantern']
    agency_wise_mapper = {
        'Perch': PerchRequestHandlingStrategy,
        'Lantern': LanternRequestHandlingStrategy
    }
    for agency in agencies:
        request_handling_obj = agency_wise_mapper[agency]()
        # request_handling_obj.request_backup_obj = S3BackupStrategy()
        request_handling_obj.perform_request_preparation()
        request_handling_obj.perform_request_backup()
        request_handling_obj.perform_request_upload()
        print()
