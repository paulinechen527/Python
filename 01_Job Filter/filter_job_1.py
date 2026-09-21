target_keyword = "中正區"

print(f"--- 開始篩選包含 [{target_keyword}] 的三行組職缺 ---")

with open("jobs.txt", "r", encoding="utf-8") as file:
    all_lines = file.readlines()

    for i in range(0, len(all_lines), 3):
        # 【關鍵安全防呆】：如果目前的編號 i，加上 2 之後，超過或等於總行數
        # 代表剩下的資料不夠 3 行了，那就用 break 立刻切斷迴圈，不要往下抓
        if i + 2 >= len(all_lines):
            break
            
        line1 = all_lines[i].strip()      
        line2 = all_lines[i+1].strip()    
        line3 = all_lines[i+2].strip()    
        
        full_job_info = f"{line1} {line2} {line3}"
        
        if target_keyword in full_job_info:
            print("【找到符合職缺】")
            print(f" 職稱：{line1}")
            print(f" 條件：{line2}")
            print(f" 薪資：{line3}")
            print("-" * 30)  

print("--- 篩選結束 ---")
