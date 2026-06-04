# 如果之前已经克隆过仓库，这一步可以跳过。如果没有，请运行这行：
# !git clone https://github.com/digital-era/NorthStar.git

import os
import re

target_dir = "NorthStar/Quantum Guardians"

def count_words_mixed(text):
    """
    精确统计中英文混合文本的字数：
    - 每个中文字符计为 1 个字
    - 每个英文单词/数字序列计为 1 个字
    """
    # 1. 统计中文字符数 (CJK 字符区间)
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
    chinese_count = len(chinese_chars)
    
    # 2. 移除中文字符后，统计英文单词和数字
    text_without_chinese = re.sub(r'[\u4e00-\u9fff]', ' ', text)
    # 匹配英文单词、数字、带连字符或单引号的词
    english_words = re.findall(r'\b[a-zA-Z0-9_\-\']+\b', text_without_chinese)
    english_count = len(english_words)
    
    return chinese_count + english_count

def count_words_in_md_files(directory):
    if not os.path.exists(directory):
        print(f"未找到目录: {directory}")
        return

    files = os.listdir(directory)
    
    # 使用正则表达式精确匹配 "QGR" + 数字 + ".md" 的格式
    # 例如：QGR01.md, QGR12.md 等，会过滤掉带有 Prompt 的文件
    file_pattern = re.compile(r"^QGR\d+\.md$")
    qgr_files = [f for f in files if file_pattern.match(f)]
    
    if not qgr_files:
        print("未找到符合条件（形如 QGR02.md）的文件。")
        return

    # 按文件名排序
    qgr_files.sort()

    print(f"找到 {len(qgr_files)} 个标准格式文件。开始统计字数：\n")
    print(f"{'文件名':<50} | {'字数 (Word Count)':<15}")
    print("-" * 70)

    total_words = 0
    for file_name in qgr_files:
        file_path = os.path.join(directory, file_name)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                word_count = count_words_mixed(content)
                total_words += word_count
                print(f"{file_name:<50} | {word_count:<15}")
        except Exception as e:
            print(f"读取文件 {file_name} 时发生错误: {e}")
            
    print("-" * 70)
    print(f"{'总计':<50} | {total_words:<15}")

# 执行统计
count_words_in_md_files(target_dir)
