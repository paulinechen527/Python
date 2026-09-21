# 1. 把兩個條件分開設定
cond1 = "中正區"
cond2 = "2年" 
cond3 = "0~5 人應徵"

print(f"--- 開始篩選：符合 [{cond1}] 且 經驗要求 [{cond2}] 的職缺 ---")

with open("jobs.txt", "r", encoding="utf-8") as file:
    all_lines = file.readlines()

    for i in range(0, len(all_lines), 3):
        if i + 2 >= len(all_lines):
            break
            
        line1 = all_lines[i].strip()      
        line2 = all_lines[i+1].strip()    
        line3 = all_lines[i+2].strip()    
        
        full_job_info = f"{line1} {line2} {line3}"
        
        # 【關鍵改動】：用小寫的 and 把兩個條件連起來
        if (cond1 in full_job_info) and (cond2 in full_job_info) and (cond3 in full_job_info):
            print("【找到符合職缺】")
            print(f" 職稱/公司：{line1} / {line2}")
            print(f" 條件：{line3}")
            print("-" * 30)  

print("--- 篩選結束 ---")