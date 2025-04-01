import tkinter as tk
from datetime import datetime

def time_delta():
    # 取得開始時間和結束時間
    start_hour = int(start_time_var.get().split(":")[0])
    start_minute = int(start_time_var.get().split(":")[1])
    end_hour = int(end_time_var.get().split(":")[0])
    end_minute = int(end_time_var.get().split(":")[1])

    # 計算時間差
    total_minutes = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)
    hours = total_minutes // 60
    minutes = total_minutes % 60

    # 輸出結果
    result_label.config(text=f"時間差為 {hours} 小時 {minutes} 分鐘")

# 建立主視窗
root = tk.Tk()
root.title("時間跨度器")

# 建立大型時間選擇按鈕
start_time_var = tk.StringVar()
start_time_var.set("09:00")
end_time_var = tk.StringVar()
end_time_var.set("18:00")

start_time_btn = tk.Button(root, text="開始時間", font=("Arial", 20), command=lambda: select_time(start_time_var))
start_time_btn.grid(row=0, column=0, padx=20, pady=20)
end_time_btn = tk.Button(root, text="結束時間", font=("Arial", 20), command=lambda: select_time(end_time_var))
end_time_btn.grid(row=0, column=1, padx=20, pady=20)

def select_time(time_var):
    # 顯示時間選擇視窗
    time_window = tk.Toplevel(root)
    time_window.title("選擇時間")

    # 建立時間選擇 Spinbox
    hour_var = tk.StringVar(value=time_var.get().split(":")[0])
    minute_var = tk.StringVar(value=time_var.get().split(":")[1])
    hour_spinbox = tk.Spinbox(time_window, from_=0, to=23, width=2, textvariable=hour_var, font=("Arial", 20))
    minute_spinbox = tk.Spinbox(time_window, from_=0, to=59, width=2, textvariable=minute_var, font=("Arial", 20))
    hour_spinbox.grid(row=0, column=0, padx=10, pady=10)
    tk.Label(time_window, text=":", font=("Arial", 20)).grid(row=0, column=1, padx=10, pady=10)
    minute_spinbox.grid(row=0, column=2, padx=10, pady=10)

    # 確認按鈕
    confirm_btn = tk.Button(time_window, text="確認", font=("Arial", 20), command=lambda: set_time(time_var, hour_var, minute_var, time_window))
    confirm_btn.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

def set_time(time_var, hour_var, minute_var, time_window):
    # 更新時間選擇變數
    time_var.set(f"{hour_var.get()}:{minute_var.get()}")
    time_window.destroy()

# 計算時間差按鈕
calculate_btn = tk.Button(root, text="計算時間差", font=("Arial", 20), command=time_delta)
calculate_btn.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

# 顯示時間差
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()