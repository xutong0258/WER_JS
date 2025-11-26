from base.AdvancedXMLParser import AdvancedXMLParser
from base.fileOP import dump_file
from utils.logger_util import *
from base.contants import *

def get_value_by_key_detail_secnod_layer(file, target_name="Firmware POST Duration"):
    vaule_list = []
    # 使用高级解析器


    advanced_parser = AdvancedXMLParser()
    result2 = advanced_parser.parse(file)

    # print(result2)
    AssessmentResults_dict = result2.get("AssessmentResults")
    # logger.info(f'AssessmentResults_dict:{AssessmentResults_dict}')

    # file_name = r'D:\01_AssessmentResults_dict.yaml'
    # dump_file(file_name, AssessmentResults_dict)

    AssessmentResult_dict = AssessmentResults_dict.get("AssessmentResult")
    # logger.info(f'AssessmentResult_dict:{AssessmentResult_dict}')

    # file_name = r'D:\02_AssessmentResult_dict.yaml'
    # dump_file(file_name, AssessmentResult_dict)

    Iteration_dict = AssessmentResult_dict.get("Iterations").get("Iteration")
    # logger.info(f'Iteration_dict:{Iteration_dict}')

    file_name = f'./Iteration_dict.yaml'
    # dump_file(file_name, Iteration_dict)
    break_flag = False
    for idx, item in enumerate(Iteration_dict):
        # logger.info(f'item:{item}')
        # if idx == name_idx:
        cell_list = item.get("TestCases")
        if cell_list is not None:
            cell_list = cell_list.get("TestCase")
        if cell_list is None:
            continue
        for cell in cell_list:
            Name_dict = cell.get("Name")
            name = Name_dict.get("#text")
            # logger.info(f'name:{name}')
            if name == target_name:
                value_list = cell.get("MetricValues").get("MetricValue")
                logger.info(f'value_list:{value_list}')

                vaule_text = value_list[0].get("Value").get("#text")
                # logger.info(f'vaule_text:{vaule_text}')
                # file_name = f'./{idx}_{name}.yaml'
                # dump_file(file_name, cell)
                vaule_list.append(vaule_text)

    return vaule_list

def get_value_by_key_first_layer(file, target_name='Total Boot'):
    vaule_list = []
    # 使用高级解析器

    advanced_parser = AdvancedXMLParser()
    result2 = advanced_parser.parse(file)

    # print(result2)
    AssessmentResults_dict = result2.get("AssessmentResults")
    # logger.info(f'AssessmentResults_dict:{AssessmentResults_dict}')

    # file_name = r'D:\01_AssessmentResults_dict.yaml'
    # dump_file(file_name, AssessmentResults_dict)

    AssessmentResult_dict = AssessmentResults_dict.get("AssessmentResult")
    # logger.info(f'AssessmentResult_dict:{AssessmentResult_dict}')

    # file_name = r'D:\02_AssessmentResult_dict.yaml'
    # dump_file(file_name, AssessmentResult_dict)

    Iteration_dict = AssessmentResult_dict.get("Iterations").get("Iteration")
    # logger.info(f'Iteration_dict:{Iteration_dict}')

    file_name = f'./Iteration_dict.yaml'
    # dump_file(file_name, Iteration_dict)
    break_flag = False
    for idx, item in enumerate(Iteration_dict):
        # logger.info(f'item:{item}')
        # if idx == name_idx:
        cell_list = item.get("TestCases")
        if cell_list is not None:
            cell_list = cell_list.get("TestCase")
        if cell_list is None:
            continue
        for cell in cell_list:
            Name_dict = cell.get("Name")
            name = Name_dict.get("#text")
            # logger.info(f'name:{name}')
            if target_name in name:
                value_list = cell.get("MetricValues").get("MetricValue")
                # logger.info(f'value_list:{value_list}')

                vaule_text = value_list[0].get("Value").get("#text")
                # logger.info(f'vaule_text:{vaule_text}')
                # file_name = f'./{idx}_{name}.yaml'
                dump_file(file_name, cell)
                vaule_list.append(vaule_text)
                break
    return vaule_list

if __name__ == '__main__':
    file = r'D:\0_JS-WERlog\0_Fast-Startup\JobResults_LAPTOP-HRS5HAE3_2025-0809_0814-56.417.xml'

    vaule_list = get_value_by_key_detail_secnod_layer(file, target_name="Post On/Off")
    logger.info(f'vaule_list:{vaule_list}')
