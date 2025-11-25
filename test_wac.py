import subprocess
import os

def run_wac_on_xml(xml_file_path, wac_exe_path=r"D:\电脑管家迁移文件\windADK\Assessment and Deployment Kit\Windows Assessment Toolkit\x86\wac.exe"):
    """
    调用 wac.exe 解析指定的 XML 文件。

    参数:
        xml_file_path (str): 要解析的 XML 文件路径。
        wac_exe_path (str): wac.exe 的路径（默认为 "wac.exe"，假设已在 PATH 中）。

    返回:
        str: wac.exe 的标准输出。
    """
    if not os.path.isfile(xml_file_path):
        raise FileNotFoundError(f"XML 文件不存在: {xml_file_path}")
    
    try:
        # 调用 wac.exe 并捕获输出
        result = subprocess.run(
            [wac_exe_path, xml_file_path],
            capture_output=True,
            text=True,
            check=True  # 如果 wac.exe 返回非零退出码，会抛出异常
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("wac.exe 执行失败！")
        print("错误码:", e.returncode)
        print("标准错误输出:", e.stderr)
        raise
    except FileNotFoundError:
        raise FileNotFoundError(f"未找到 wac.exe，请检查路径: {wac_exe_path}")

# 示例使用
if __name__ == "__main__":
    xml_path = r"D:\0_JS-WERlog\0_Fast-Startup\JobResults_LAPTOP-HRS5HAE3_2025-0809_0814-56.417.xml"
    try:
        output = run_wac_on_xml(xml_path)
        print("解析结果:")
        print(output)
    except Exception as e:
        print("发生错误:", e)