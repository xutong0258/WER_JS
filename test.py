import os
import sys


from base.fileOP import *
from base.list_help import *

if __name__ == '__main__':
    file = r'D:\11.xml'
    log_lines = get_file_content_list(file)
    text = 'AssessmentResults'
    index = get_list_text_line_first_index(log_lines, text)
    logger.info(f'index: {index}')
    first_part = log_lines[0:index]
    logger.info(f'first part: {first_part}')

    text = '/AssessmentResults'
    index = get_list_text_line_first_index(log_lines, text)
    logger.info(f'index: {index}')
    second_part = log_lines[index+1:]
    logger.info(f'second_part: {second_part}')

    result_list = first_part + second_part

    file_name = r'D:\12.xml'
    content = ''.join(result_list)
    wrtie_file(file_name, content)
    pass
