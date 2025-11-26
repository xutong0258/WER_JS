import os
import sys

file_path = os.path.abspath(__file__)
path_dir = os.path.dirname(file_path)

root_dir = os.path.join(path_dir, '../')
sys.path.append(root_dir)

from base.one_step_sop import *

path_dir = os.path.dirname(__file__)


if __name__ == '__main__':
    rule_config_dict = {}
    Total_Boot_Duration = 18

    file = r'D:\0_JS-WERlog\0_Fast-Startup\JobResults_LAPTOP-HRS5HAE3_2025-0809_0814-56.417.xml'
    rule_config_dict['Total_Boot_Duration'] = 18
    rule_config_dict['Main_Path_Boot_Duration'] = 10

    rule_config_dict['Boot_Manager_Duration'] = 0.5
    rule_config_dict['Hiberfile_Read_Boot_Duration'] = 2.5
    rule_config_dict['Resume_Device_Boot_Duration'] = 3
    rule_config_dict['Winlogon_Resume_Boot_Duration'] = 1
    rule_config_dict['Explorer_Intialization_Duration'] = 3

    rule_config_dict['Post_On_Off_Duration'] = 5

    one_process_run_FastStartup(rule_config_dict=rule_config_dict,   file=file)
    pass