from base.AdvancedXMLParser import AdvancedXMLParser
from base.fileOP import dump_file
from utils.logger_util import *


# 使用高级解析器
file = r'D:\0_JS-WERlog\0_Fast-Startup\JobResults_LAPTOP-HRS5HAE3_2025-0809_0814-56.417.xml'

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

for idx, item in enumerate(Iteration_dict):
    if idx == 2:
        cell_list = item.get("TestCases").get("TestCase")
        for cell in cell_list:
            Name_dict = cell.get("Name")
            name = Name_dict.get("#text")
            logger.info(f'name:{name}')
            if name == "Firmware POST Duration":
                file_name = f'./{idx}_{name}.yaml'
                dump_file(file_name, cell)
