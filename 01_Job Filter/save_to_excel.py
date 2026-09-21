import pandas as pd  # 1. 第一步：先引入工具箱

# 2. 設定篩選條件
cond1 = "中正區"
cond2 = "2年"

print(f"--- 開始篩選並匯出 Excel ---")

# 3. 準備一個大箱子裝資料
matched_jobs = []

# 4. 開始讀取檔案並篩選（記得確認 jobs.txt 已經把最後一行空行刪除囉！）
with open("jobs.txt", "r", encoding="utf-8") as file:
    all_lines = file.readlines()

    for i in range(0, len(all_lines), 3):
        if i + 2 >= len(all_lines):
            break
            
        line1 = all_lines[i].strip()      # 今天 + 職稱
        line2 = all_lines[i+1].strip()    # 公司名稱
        line3 = all_lines[i+2].strip()    # 地點與年資
        
        full_job_info = f"{line1} {line2} {line3}"
        
        # 如果同時符合「中正區」與「2年」
        if (cond1 in full_job_info) and (cond2 in full_job_info):
            
            # 把資料整理成乾淨的欄位
            job_data = {
                "職稱": line1.replace("今天\t", ""), 
                "公司名稱": line2,
                "詳細資訊": line3
            }
            # 丟進大箱子
            matched_jobs.append(job_data)

# 5. 檢查大箱子，如果裡面有東西，就叫 Pandas 秘書做成 Excel
if len(matched_jobs) > 0:
    df = pd.DataFrame(matched_jobs)   # 變成表格
    df.to_excel("result.xlsx", index=False)  # 存成 Excel 檔
    print(f"🎉 成功！已篩選出 {len(matched_jobs)} 筆職缺，並儲存為 result.xlsx")
else:
    print("❌ 沒有找到符合條件的職缺，因此未產生 Excel 檔案。")
