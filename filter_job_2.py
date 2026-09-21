target_keyword = "中正區"

print(f"--- 開始篩選包含 [{target_keyword}] 的三行組職缺 ---")

with open("jobs.txt", "r", encoding="utf-8") as file:
    # 核心觀念：一次把所有行數讀進來，變成一個「行列表 (List)」
    all_lines = file.readlines()

    # 使用迴圈，每次跳 3 行 (i = 0, 3, 6, 9...)
    for i in range(0, len(all_lines), 3):
        # 透過索引值 [i]，一次抓出同一組的三行資料
        line1 = all_lines[i].strip()      # 職缺名稱
        line2 = all_lines[i+1].strip()    # 公司名稱
        line3 = all_lines[i+2].strip()    # 條件
        
        # 把這三行組合成一個大字串，方便一起檢查
        full_job_info = f"{line1} {line2} {line3}"
        
        # 檢查這整組資料裡，有沒有包含我們要的關鍵字
        if target_keyword in full_job_info:
            if "2年" in full_job_info:
                print("【找到符合職缺】")
                print(f" 職稱：{line1}")
                print(f" 公司名稱：{line2}")
                print(f" 條件：{line3}")
                print("-" * 30)  # 印出分隔    

print("--- 篩選結束 ---")

