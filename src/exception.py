import sys
import logging
import sys

def eroor_message_detail(error,error_detail:sys):
   _,_,exc_tb= error_detail.exe_info()
   file_name=exc_tb.tb_frame.f_code.co_file_name
   error_message="Error Ocuured in Python Script Name [{0}] line numeber [{1}] error message [{2}]".format(
    file_name.exc_tb.tb_lineno,str(error))

    
   return error_message

   


class CustomException(Exception):
    def __intit__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=eroor_message_detail(error_message,error_detail=error_detail)

        
    def __str__(self):
        return self.eroor_message
    
    
