from funasr import AutoModel
import re

# 加载带时间戳的中文通用模型（适配FunASR 1.2.9）
model = AutoModel(
    model="paraformer-zh",
    vad_model="fsmn-vad",
    punc_model="ct-punc",
    disable_update=True,
    device="cpu",
    model_revision="v2.0.4"
)

# 处理音频文件
result = model.generate(
    input=r"D:\video\2025年06月六级听力音频第2套.mp3",
    batch_size=16,
    return_timestamps=True,
    timestamp_type="word",
    word_level=True
)

# 辅助函数：统一时间戳格式
def get_word_timestamps(timestamp_item):
    if isinstance(timestamp_item, (list, tuple)):
        if len(timestamp_item) == 2 and isinstance(timestamp_item[1], (list, tuple)):
            return [int(timestamp_item[1][0]), int(timestamp_item[1][1])]
        elif len(timestamp_item) >= 2:
            return [int(timestamp_item[0]), int(timestamp_item[1])]
    return [0, 100]

# 辅助函数：转换毫秒到SRT时间格式 (00:00:00,000)
def ms_to_srt_time(ms):
    seconds = ms // 1000
    minutes = seconds // 60
    hours = minutes // 60
    remaining_seconds = seconds % 60
    remaining_minutes = minutes % 60
    remaining_ms = ms % 1000
    return f"{hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d},{remaining_ms:03d}"

# 生成SRT内容
srt_content = []
srt_index = 1  # SRT序号从1开始

for seg_idx, segment in enumerate(result):
    full_text = segment.get("text", "").strip()
    word_timestamp_list = segment.get("timestamp", [])
    if not full_text or not word_timestamp_list:
        continue

    # 拆分文本为词列表
    text_parts = re.findall(r"([^，。！？；：\s]+|[，。！？；：])", full_text)
    word_list = [part for part in text_parts if part.strip()]

    # 对齐词和时间戳长度
    min_length = min(len(word_list), len(word_timestamp_list))
    word_list = word_list[:min_length]
    word_timestamp_list = word_timestamp_list[:min_length]

    # 按句子合并生成SRT条目
    current_sentence = []
    current_start_ms = None
    
    for word, ts_item in zip(word_list, word_timestamp_list):
        start_ms, end_ms = get_word_timestamps(ts_item)
        
        if current_start_ms is None:
            current_start_ms = start_ms
        
        current_sentence.append(word)
        
        # 遇到句末标点，生成SRT条目
        if word in ["。", "！", "？", "；"]:
            # 转换时间格式
            start_srt = ms_to_srt_time(current_start_ms)
            end_srt = ms_to_srt_time(end_ms)
            # 拼接句子文本
            sentence_text = "".join(current_sentence)
            # 添加SRT条目
            srt_content.append(f"{srt_index}")
            srt_content.append(f"{start_srt} --> {end_srt}")
            srt_content.append(sentence_text)
            srt_content.append("")  # 空行分隔条目
            # 更新序号和缓存
            srt_index += 1
            current_sentence = []
            current_start_ms = None
    
    # 处理最后一句（无句末标点）
    if current_sentence:
        start_ms = current_start_ms if current_start_ms else 0
        last_start_ms, last_end_ms = get_word_timestamps(word_timestamp_list[-1])
        start_srt = ms_to_srt_time(start_ms)
        end_srt = ms_to_srt_time(last_end_ms)
        sentence_text = "".join(current_sentence)
        # 添加最后一句的SRT条目
        srt_content.append(f"{srt_index}")
        srt_content.append(f"{start_srt} --> {end_srt}")
        srt_content.append(sentence_text)
        srt_content.append("")
        srt_index += 1

# 保存SRT文件
with open("六级听力_202506_第2套.srt", "w", encoding="utf-8") as f:
    f.write("\n".join(srt_content))

print("✅ SRT文件已生成完成！")





# from funasr import AutoModel

# # 加载带时间戳的中文通用模型（适配FunASR 1.2.9，指定模型版本避免格式差异）
# model = AutoModel(
#     model="paraformer-zh",
#     vad_model="fsmn-vad",
#     punc_model="ct-punc",
#     disable_update=True,
#     device="cpu",
#     model_revision="v2.0.4"  # 锁定稳定版本，避免时间戳格式波动
# )

# # 处理音频文件：同时获取文本和词级时间戳
# result = model.generate(
#     input=r"D:\video\2025年06月六级听力音频第2套.mp3",
#     batch_size=16,
#     return_timestamps=True,
#     timestamp_type="word",  # 词级时间戳（仅含时间，无文本）
#     word_level=True  # 显式开启词级输出，确保文本可按词拆分
# )

# # 辅助函数：统一时间戳格式（提取[start_ms, end_ms]）
# def get_word_timestamps(timestamp_item):
#     """从时间戳项中提取标准的[start_ms, end_ms]"""
#     if isinstance(timestamp_item, (list, tuple)):
#         # 情况1：嵌套格式 [start_ms, end_ms] 或 [其他信息, [start_ms, end_ms]]
#         if len(timestamp_item) == 2 and isinstance(timestamp_item[1], (list, tuple)):
#             return [int(timestamp_item[1][0]), int(timestamp_item[1][1])]
#         # 情况2：扁平格式 [start_ms, end_ms]
#         elif len(timestamp_item) >= 2:
#             return [int(timestamp_item[0]), int(timestamp_item[1])]
#     # 异常情况：返回默认时间（避免崩溃）
#     return [0, 100]

# print("识别结果+时间戳（按词/短句分段）：")
# for seg_idx, segment in enumerate(result):
#     # 1. 获取核心数据：完整文本（带标点）和词级时间戳列表
#     full_text = segment.get("text", "").strip()  # 完整中文文本（关键！）
#     word_timestamp_list = segment.get("timestamp", [])  # 仅含时间的词级列表
#     if not full_text or not word_timestamp_list:
#         print(f"\n=== 片段{seg_idx+1} ===")
#         print("⚠️  无有效文本或时间戳数据")
#         continue

#     # 2. 按词拆分完整文本（基于标点和空格，确保与时间戳数量匹配）
#     # 先按标点分割为短句，再按空格分割为词（FunASR默认词间用空格分隔）
#     import re
#     # 步骤1：分割标点与文本（如“你好，世界”→["你好", "，", "世界"]）
#     text_parts = re.findall(r"([^，。！？；：\s]+|[，。！？；：])", full_text)
#     # 步骤2：过滤空字符，得到纯净词列表
#     word_list = [part for part in text_parts if part.strip()]

#     # 3. 确保词列表与时间戳列表长度一致（避免错位）
#     min_length = min(len(word_list), len(word_timestamp_list))
#     word_list = word_list[:min_length]
#     word_timestamp_list = word_timestamp_list[:min_length]

#     # --------------------------
#     # 方案1：按词输出（中文词+对应时间）
#     # --------------------------
#     print(f"\n=== 片段{seg_idx+1}（按词拆分）===")
#     for word_idx, (word, ts_item) in enumerate(zip(word_list, word_timestamp_list)):
#         start_ms, end_ms = get_word_timestamps(ts_item)
#         start_s = start_ms / 1000
#         end_s = end_ms / 1000
#         print(f"词{word_idx+1}：[{start_s:.2f}s - {end_s:.2f}s] → {word}")

#     # --------------------------
#     # 方案2：按句子输出（合并带标点的完整句）
#     # --------------------------
#     print(f"\n=== 片段{seg_idx+1}（按句子合并）===")
#     current_sentence = []
#     current_start_ms = None  # 句子起始时间（取第一个词的时间）
    
#     for word, ts_item in zip(word_list, word_timestamp_list):
#         start_ms, end_ms = get_word_timestamps(ts_item)
        
#         # 初始化句子起始时间
#         if current_start_ms is None:
#             current_start_ms = start_ms
        
#         # 添加当前词到句子
#         current_sentence.append(word)
        
#         # 遇到句末标点，输出完整句子
#         if word in ["。", "！", "？", "；"]:
#             start_s = current_start_ms / 1000
#             end_s = end_ms / 1000
#             sentence_text = "".join(current_sentence)
#             print(f"句子：[{start_s:.2f}s - {end_s:.2f}s] → {sentence_text}")
#             # 重置缓存
#             current_sentence = []
#             current_start_ms = None
    
#     # 输出最后一句（无句末标点的情况）
#     if current_sentence:
#         start_s = current_start_ms / 1000 if current_start_ms else 0
#         # 取最后一个词的结束时间
#         last_start_ms, last_end_ms = get_word_timestamps(word_timestamp_list[-1])
#         end_s = last_end_ms / 1000
#         sentence_text = "".join(current_sentence)
#         print(f"句子：[{start_s:.2f}s - {end_s:.2f}s] → {sentence_text}")