# file_path = r"D:\Personal\OrangeHRM\config\logs\test_permission.log"
# try:
#     with open(file_path, 'w') as f:
#         f.write("Test log file to check permissions.\n")
#     print(f"Test file created successfully: {file_path}")
# except Exception as e:
#     print(f"Failed to create file: {e}")
import logging


def simple_logger_test():
    logging.basicConfig(filename=r"D:\Personal\OrangeHRM\config\logs\simple_test.log", level=logging.DEBUG)
    logging.debug("This is a debug message.")
    print(f"Log file created at: D:\\Personal\\OrangeHRM\\config\\logs\\simple_test.log")