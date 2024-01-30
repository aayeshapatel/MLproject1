    
import sys
import logging
import traceback  # Import traceback for more detailed error information if needed
from src.logger import logging

def error_message_detail(error, error_details):
    # Unpack the exc_info tuple
    _, _, exc_tb = error_details
    # Get the filename and line number from the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message

class Custom_exception(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        # Correctly call error_message_detail with unpacked exc_info
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         # Get the current exception's exc_info
#         exc_type, exc_value, exc_traceback = sys.exc_info()
#         # Log the error
#         logging.info("Divide by zero error")
#         # Pass the exc_info tuple to Custom_exception
#         raise Custom_exception(e, (exc_type, exc_value, exc_traceback))
    
