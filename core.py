import os
import json
import datetime

# 專案資料路徑，確保程式能找到 data 資料夾
DATA_PATH = os.path.join(os.path.dirname(__file__), "data/")

# 儲存天干地支的對應表
TIAN_GAN = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
DI_ZHI = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

# 天干寄宮表 (四維寄宮法)
GAN_TO_GONG = {
    '甲': '寅', '乙': '辰', '丙': '巳', '丁': '未',
    '戊': '辰', '己': '未', '庚': '申', '辛': '戌',
    '壬': '亥', '癸': '丑'
}

# 五行與天干地支對應表
FIVE_ELEMENTS = ['木', '火', '土', '金', '水']
ELEMENT_MAPPING = {
    '甲': '木', '乙': '木', '丙': '火', '丁': '火', '戊': '土', '己': '土',
    '庚': '金', '辛': '金', '壬': '水', '癸': '水',
    '寅': '木', '卯': '木', '巳': '火', '午': '火', '申': '金', '酉': '金',
    '亥': '水', '子': '水', '辰': '土', '戌': '土', '丑': '土', '未': '土'
}

# 五行相剋關係
FIVE_ELEMENT_KE = {
    '金': '木', '木': '土', '土': '水', '水': '火', '火': '金'
}

# 節氣與月將對應表 (簡化版)
JIE_QI_TO_YUE_JIANG = {
    "大雪": "子", "小寒": "丑", "立春": "寅", "驚蟄": "卯",
    "清明": "辰", "立夏": "巳", "芒種": "午", "小暑": "未",
    "立秋": "申", "白露": "酉", "寒露": "戌", "立冬": "亥"
}

# 根據地支找出對應的神將
def get_shen_jiang(tian_pan, di_pan, yue_jiang):
    SHEN_JIANG = ["貴人", "螣蛇", "朱雀", "六合", "勾陳", "青龍", "天空", "白虎", "太常", "玄武", "太陰", "天后"]
    
    gui_ren_start_index = 0
    
    shen_jiang_pan = {}
    for i, zhi in enumerate(di_pan):
        shen_jiang_pan[tian_pan[i]] = SHEN_JIANG[(i + gui_ren_start_index) % 12]
        
    return shen_jiang_pan

def get_user_input():
    pass

def calculate_chart(user_data):
    """
    學習型核心運算引擎。

    注意：
    目前實作採用簡化規則，並非完整傳統大六壬排盤法。
    特別是月將、天將起法與三傳推導仍屬原型階段。
    """
    
    # 步驟 1: 計算日干支
    date_obj = datetime.date(user_data['year'], user_data['month'], user_data['day'])
    base_date = datetime.date(1900, 1, 1) # 庚子日
    delta_days = (date_obj - base_date).days
    
    gan_index = (delta_days + 6) % 10 # 庚為第 6 個天干
    zhi_index = (delta_days + 0) % 12 # 子為第 0 個地支
    
    ri_gan = TIAN_GAN[gan_index]
    ri_zhi = DI_ZHI[zhi_index]
    ri_gan_zhi = f"{ri_gan}{ri_zhi}"
    
    # 步驟 2: 找出月將 (簡化版)
    yue_jiang = ""
    if user_data['month'] == 1: yue_jiang = "丑"
    elif user_data['month'] == 2: yue_jiang = "寅"
    elif user_data['month'] == 3: yue_jiang = "卯"
    elif user_data['month'] == 4: yue_jiang = "辰"
    elif user_data['month'] == 5: yue_jiang = "巳"
    elif user_data['month'] == 6: yue_jiang = "午"
    elif user_data['month'] == 7: yue_jiang = "未"
    elif user_data['month'] == 8: yue_jiang = "申"
    elif user_data['month'] == 9: yue_jiang = "酉"
    elif user_data['month'] == 10: yue_jiang = "戌"
    elif user_data['month'] == 11: yue_jiang = "亥"
    elif user_data['month'] == 12: yue_jiang = "子"

    
    # 步驟 3: 佈置天盤與地盤
    di_pan = DI_ZHI.copy()
    
    yue_jiang_index = DI_ZHI.index(yue_jiang)
    ri_zhi_index = DI_ZHI.index(ri_zhi)
    offset = (ri_zhi_index - yue_jiang_index + 12) % 12
    
    tian_pan = [DI_ZHI[(i + offset) % 12] for i in range(12)]
    
    # 步驟 4: 找出四課
    def get_shang_shen(di_zhi_name):
        di_zhi_index = di_pan.index(di_zhi_name)
        return tian_pan[di_zhi_index]

    ri_gan_gong = GAN_TO_GONG[ri_gan]
    ri_gan_shang_shen = get_shang_shen(ri_gan_gong)
    ri_zhi_shang_shen = get_shang_shen(ri_zhi)
    
    si_ke = [ri_gan, ri_gan_shang_shen, ri_zhi, ri_zhi_shang_shen]
    
    # 步驟 5: 推導三傳 (加入更複雜的推導方法)
    san_chuan = []
    
    # 方法一：賊剋法
    ke_relationships = []
    if FIVE_ELEMENT_KE[ELEMENT_MAPPING[ri_gan_shang_shen]] == ELEMENT_MAPPING[ri_gan]:
        ke_relationships.append(ri_gan_shang_shen)
    if FIVE_ELEMENT_KE[ELEMENT_MAPPING[ri_zhi_shang_shen]] == ELEMENT_MAPPING[ri_zhi]:
        ke_relationships.append(ri_zhi_shang_shen)

    if ke_relationships:
        chu_chuan = ke_relationships[0]
        zhong_chuan = get_shang_shen(chu_chuan)
        mo_chuan = get_shang_shen(zhong_chuan)
        san_chuan = [chu_chuan, zhong_chuan, mo_chuan]
    else:
        # 方法二：遙剋法
        # 尋找天盤剋地盤的關係
        yao_ke_list = []
        for i in range(12):
            tian_shen = tian_pan[i]
            di_zhi = di_pan[i]
            if FIVE_ELEMENT_KE[ELEMENT_MAPPING[tian_shen]] == ELEMENT_MAPPING[di_zhi]:
                yao_ke_list.append(tian_shen)
        
        if yao_ke_list:
            chu_chuan = yao_ke_list[0]
            zhong_chuan = get_shang_shen(chu_chuan)
            mo_chuan = get_shang_shen(zhong_chuan)
            san_chuan = [chu_chuan, zhong_chuan, mo_chuan]
        else:
            # 方法三：別責法
            if ri_gan in ['丁', '己', '癸']:
                if ri_gan_shang_shen == '亥':
                    san_chuan = ['亥', '申', '巳']
                elif ri_gan_shang_shen == '卯':
                    san_chuan = ['卯', '酉', '巳']
            
            # 方法四：昴星法
            elif ri_zhi == '酉':
                chu_chuan = '酉'
                zhong_chuan = get_shang_shen(chu_chuan)
                mo_chuan = get_shang_shen(zhong_chuan)
                san_chuan = [chu_chuan, zhong_chuan, mo_chuan]
                

    # 步驟 6: 找出神將
    shen_jiang_pan = get_shen_jiang(tian_pan, di_pan, yue_jiang)
    
    chart_data = {
        "ri_gan_zhi": ri_gan_zhi,
        "ri_gan": ri_gan,
        "ri_zhi": ri_zhi,
        "yue_jiang": yue_jiang,
        "di_pan": di_pan,
        "tian_pan": tian_pan,
        "si_ke": si_ke,
        "san_chuan": san_chuan,
        "shen_jiang_pan": shen_jiang_pan,
    }
    
    return chart_data

def normalize_question_type(question_type):
    mapping = {
        "工作": "問工作",
        "感情": "問感情",
        "財運": "問財運",
        "問工作": "問工作",
        "問感情": "問感情",
        "問財運": "問財運",
    }
    return mapping.get((question_type or "").strip(), (question_type or "").strip())


def get_interpretation(chart_data, question_type):
    """
    解讀模組：根據排盤結果與問題類型，從 JSON 資料中生成解讀。
    """
    
    try:
        with open(f"{DATA_PATH}chapter_3.json", 'r', encoding='utf-8') as f:
            chapter_3_data = json.load(f)
        with open(f"{DATA_PATH}chapter_4.json", 'r', encoding='utf-8') as f:
            chapter_4_data = json.load(f)
    except FileNotFoundError:
        return "錯誤：找不到 JSON 資料檔。請確認 'data' 資料夾和裡面的檔案都已存在且名稱正確。"

    shen_jiang_meanings = {d["name"]: d for d in chapter_3_data["sections"][0]["details"]}
    question_type = normalize_question_type(question_type)
    
    report_lines = []
    report_lines.append(f"--- 大六壬學習型原型：針對【{question_type}】的分析報告 ---")
    report_lines.append("注意：本結果使用簡化演算法，只適合作為程式學習、規則研究與介面原型。")
    
    # 報告基本盤面
    report_lines.append(f"\n【基本盤面】")
    report_lines.append(f"  日干支: {chart_data['ri_gan_zhi']}")
    report_lines.append(f"  月將: {chart_data['yue_jiang']}")
    report_lines.append(f"  四課: {chart_data['si_ke']}")
    
    # 報告三傳
    report_lines.append(f"\n【三傳分析】")
    if chart_data["san_chuan"]:
        san_chuan = chart_data["san_chuan"]
        
        # 初傳解讀
        chu_chuan_zhi = san_chuan[0]
        chu_chuan_shen = chart_data["shen_jiang_pan"].get(chu_chuan_zhi)
        chu_chuan_meaning = shen_jiang_meanings.get(chu_chuan_shen, {}).get("symbols", ["未知"])
        report_lines.append(f"\n【初傳】{chu_chuan_zhi}，所臨神將為【{chu_chuan_shen}】。")
        report_lines.append(f"  解讀：這代表事情的開端與【{'、'.join(chu_chuan_meaning)}】相關。")
        
        # 中傳解讀
        zhong_chuan_zhi = san_chuan[1]
        zhong_chuan_shen = chart_data["shen_jiang_pan"].get(zhong_chuan_zhi)
        zhong_chuan_meaning = shen_jiang_meanings.get(zhong_chuan_shen, {}).get("symbols", ["未知"])
        report_lines.append(f"\n【中傳】{zhong_chuan_zhi}，所臨神將為【{zhong_chuan_shen}】。")
        report_lines.append(f"  解讀：事情的發展過程可能會經歷【{'、'.join(zhong_chuan_meaning)}】。")
        
        # 末傳解讀
        mo_chuan_zhi = san_chuan[2]
        mo_chuan_shen = chart_data["shen_jiang_pan"].get(mo_chuan_zhi)
        mo_chuan_meaning = shen_jiang_meanings.get(mo_chuan_shen, {}).get("symbols", ["未知"])
        report_lines.append(f"\n【末傳】{mo_chuan_zhi}，所臨神將為【{mo_chuan_shen}】。")
        report_lines.append(f"  解讀：最終的結果可能與【{'、'.join(mo_chuan_meaning)}】相關。")

    else:
        report_lines.append("\n三傳推導失敗，此局勢較為複雜，難以用基礎方法判斷。")
    
    # 報告結論
    if question_type in [sec['name'] for sec in chapter_4_data['sections']]:
        for sec in chapter_4_data['sections']:
            if sec['name'] == question_type:
                report_lines.append(f"\n【針對 {question_type} 的專門解讀】")
                report_lines.append(sec['details'])

    report_lines.append("\n--------------------")
    
    return "\n".join(report_lines)

def display_result(report):
    pass

def main():
    pass

if __name__ == "__main__":
    pass