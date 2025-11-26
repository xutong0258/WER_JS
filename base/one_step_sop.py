import os
import sys
from utils.logger_util import *
from base.fileOP import *
from base.folder_file import *
from base.xml_help import *
from base.list_help import *

path_dir = os.path.dirname(__file__)

rule_config_file = os.path.join(CONFIG_PATH, 'check_rule.yaml')
rule_dict = read_file_dict(rule_config_file)

# Total_Boot_Duration
def one_process_run_FastStartup(rule_config_dict, *args, **kwargs):
    file = kwargs.get('file', None)
    logger.info(f'file:{file}')

    Total_Boot_Duration = rule_config_dict.get('Total_Boot_Duration', 18)*1000
    # logger.info(f'Total_Boot_Duration:{Total_Boot_Duration}')

    Main_Path_Boot_Duration = rule_config_dict.get('Main_Path_Boot_Duration', 10)*1000
    # logger.info(f'Main_Path_Boot_Duration:{Main_Path_Boot_Duration}')

    Boot_Manager_Duration = rule_config_dict.get('Boot_Manager_Duration', 0.5)*1000

    Hiberfile_Read_Boot_Duration = rule_config_dict.get('Hiberfile_Read_Boot_Duration', 2.5) * 1000
    Resume_Device_Boot_Duration = rule_config_dict.get('Resume_Device_Boot_Duration', 3) * 1000

    Winlogon_Resume_Boot_Duration = rule_config_dict.get('Winlogon_Resume_Boot_Duration', 1) * 1000
    Explorer_Intialization_Duration = rule_config_dict.get('Explorer_Intialization_Duration', 3) * 1000

    Post_On_Off_Duration = rule_config_dict.get('Post_On_Off_Duration', 18)*1000
    # logger.info(f'Post_On_Off_Duration:{Post_On_Off_Duration}')

    # # Total_Boot_Duration_flag
    Total_Boot_list = get_value_by_key_first_layer(file, target_name="Total Boot")
    logger.info(f'Total_Boot_list:{Total_Boot_list}')

    Total_Boot_Duration_flag = False
    for item in Total_Boot_list:
        if float(item) > Total_Boot_Duration:
            Total_Boot_Duration_flag = True
            break
    logger.info(f'Total_Boot_Duration_flag:{Total_Boot_Duration_flag}')

    max_delta_dict = {}

    # Boot_Manager_Duration
    Duration_list = get_value_by_key_detail_secnod_layer(file, target_name='Boot Manager')
    logger.info(f'Duration_list:{Duration_list}')

    max_delta = get_list_max_delta(Duration_list, Boot_Manager_Duration)
    if max_delta > 0:
        max_delta_dict['Boot_Manager_Duration'] = max_delta
    logger.info(f'max_delta_dict:{max_delta_dict}')

    # Hiberfile_Read_Boot
    Duration_list = get_value_by_key_detail_secnod_layer(file, target_name='Hiberfile Read')
    logger.info(f'Duration_list:{Duration_list}')

    max_delta = get_list_max_delta(Duration_list, Hiberfile_Read_Boot_Duration)
    if max_delta > 0:
        max_delta_dict['Hiberfile_Read_Boot_Duration'] = max_delta
    logger.info(f'max_delta_dict:{max_delta_dict}')

    # Resume_Device_Boot_Duration
    Duration_list = get_value_by_key_detail_secnod_layer(file, target_name='Resume Devices')
    logger.info(f'Duration_list:{Duration_list}')

    max_delta = get_list_max_delta(Duration_list, Resume_Device_Boot_Duration)
    if max_delta > 0:
        max_delta_dict['Resume_Device_Boot_Duration'] = max_delta
    logger.info(f'max_delta_dict:{max_delta_dict}')

    # Winlogon_Resume_Boot_Duration
    Duration_list = get_value_by_key_detail_secnod_layer(file, target_name='Winlogon Resume')
    logger.info(f'Duration_list:{Duration_list}')

    max_delta = get_list_max_delta(Duration_list, Winlogon_Resume_Boot_Duration)
    if max_delta > 0:
        max_delta_dict['Winlogon_Resume_Boot_Duration'] = max_delta
    logger.info(f'max_delta_dict:{max_delta_dict}')

    # Explorer_Intialization_Duration
    Duration_list = get_value_by_key_detail_secnod_layer(file, target_name='Explorer Initialization')
    logger.info(f'Duration_list:{Duration_list}')

    max_delta = get_list_max_delta(Duration_list, Explorer_Intialization_Duration)
    if max_delta > 0:
        max_delta_dict['Explorer_Intialization_Duration'] = max_delta
    logger.info(f'max_delta_dict:{max_delta_dict}')

    dict_len = len(max_delta_dict)
    logger.info(f'dict_len:{dict_len}')

    check_flag_2 = False
    if dict_len >= 1:
        check_flag_2 = True

    # Post_On_Off_Duration_flag
    Post_On_Off_Duration_flag = False

    Post_On_Off_Duration_list = get_value_by_key_first_layer(file, target_name="Total Boot")
    logger.info(f'Post_On_Off_Duration_list:{Post_On_Off_Duration_list}')


    for item in Post_On_Off_Duration_list:
        if float(item) > Post_On_Off_Duration:
            Post_On_Off_Duration_flag = True
            break
    logger.info(f'Post_On_Off_Duration_flag:{Post_On_Off_Duration_flag}')

    if Total_Boot_Duration_flag == True and Post_On_Off_Duration_flag == True and check_flag_2 == True:
        result_dict = rule_dict.get('check_rule_FastStartup')
        logger.info(f'result_dict:{result_dict}')

        result_yaml_file = 'result.yaml'
        result_yaml_file = os.path.join(path_dir, result_yaml_file)

        dump_file(result_yaml_file, result_dict)
    return