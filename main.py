import tkinter as tk
from tkinter import ttk, scrolledtext
from core import calculate_chart, get_interpretation

def create_gui():
    """建立並運行 GUI 介面"""

    # 主視窗設定
    window = tk.Tk()
    window.title("大六壬學習型排盤原型 v1.0")
    window.geometry("800x700")
    window.configure(bg="#f0f0f0")

    # 樣式設定
    style = ttk.Style()
    style.configure("TLabel", background="#f0f0f0", font=("Microsoft YaHei UI", 12))
    style.configure("TButton", font=("Microsoft YaHei UI", 12), padding=10)
    style.configure("TEntry", font=("Microsoft YaHei UI", 12))

    # 主框架
    main_frame = ttk.Frame(window, padding="15")
    main_frame.pack(fill="both", expand=True)

    # 輸入區
    input_frame = ttk.Frame(main_frame, padding="15", relief="groove")
    input_frame.pack(pady=10, fill="x")

    labels = ["年 (例如: 2025):", "月 (例如: 9):", "日 (例如: 17):", "時 (24小時制, 例如: 19):", "分 (例如: 2):", "問事類型:"]
    entries = {}

    for i, text in enumerate(labels):
        ttk.Label(input_frame, text=text).grid(row=i, column=0, padx=5, pady=5, sticky="w")
        entry = ttk.Entry(input_frame)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
        entries[text] = entry

    entries["年 (例如: 2025):"].insert(0, "2025")
    entries["月 (例如: 9):"].insert(0, "9")
    entries["日 (例如: 17):"].insert(0, "17")
    entries["時 (24小時制, 例如: 19):"].insert(0, "21")
    entries["分 (例如: 2):"].insert(0, "15")
    entries["問事類型:"].insert(0, "問工作")

    # 占卜結果顯示區
    result_frame = ttk.Frame(main_frame, padding="15")
    result_frame.pack(fill="both", expand=True)
    result_display = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, font=("Microsoft YaHei UI", 10))
    result_display.pack(fill="both", expand=True)

    def run_calculation():
        """執行計算並顯示結果的函式"""
        try:
            user_data = {
                "year": int(entries["年 (例如: 2025):"].get()),
                "month": int(entries["月 (例如: 9):"].get()),
                "day": int(entries["日 (例如: 17):"].get()),
                "hour": int(entries["時 (24小時制, 例如: 19):"].get()),
                "minute": int(entries["分 (例如: 2):"].get()),
                "question_type": entries["問事類型:"].get()
            }

            result_display.delete("1.0", tk.END)
            result_display.insert(tk.END, "[運算中] 正在依目前簡化規則產生學習用盤面...\n\n")
            
            # 使用 update_idletasks 讓訊息即時顯示
            window.update_idletasks()

            chart_data = calculate_chart(user_data)
            
            report = get_interpretation(chart_data, user_data.get("question_type"))
            
            result_display.insert(tk.END, report)

        except Exception as e:
            result_display.delete("1.0", tk.END)
            result_display.insert(tk.END, f"發生錯誤：{e}\n請確認您的輸入格式正確。")
    
    # 占卜按鈕
    run_button = ttk.Button(main_frame, text="開始占卜", command=run_calculation)
    run_button.pack(pady=10)

    # 啟動主迴圈
    window.mainloop()

if __name__ == "__main__":
    create_gui()