import tkinter as tk
import random

def generate_random_number():
    min_value = int(min_entry.get())
    max_value = int(max_entry.get())

    if min_value >= max_value:
        result_label.config(text="Lỗi: Min phải nhỏ hơn Max")
    else:
        random_number = random.randint(min_value, max_value)
        result_label.config(text=f"Con số may mắn của bạn là: {random_number}",fg="purple")

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Random Number Generator")

# Label
instruction_label = tk.Label(window, text="Random Number", fg="red", font=("Times New Roman",15))
instruction_label.pack()
# Label
instruction_label = tk.Label(window, text="Nhập khoảng số random bạn muốn")
instruction_label.pack(pady=10)

#Tạo và cấu hình khung chứa nội dung
content_frame = tk.Frame(window,padx=20, pady=20)
content_frame.pack(expand=True,fill = "both")

#Label và Entry cho Min
min_label = tk.Label(content_frame, text="Min:")
min_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
min_entry = tk.Entry(content_frame, width=10)
min_entry.grid(row=0, column=1, padx=5, pady=5)

#Label và Entry cho Max
max_label = tk.Label(content_frame, text="Max:")
max_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
max_entry = tk.Entry(content_frame, width=10)
max_entry.grid(row=0, column=3, padx=5, pady=5)

# Button để tạo số ngẫu nhiên
generate_button = tk.Button(window, text="Random", command=generate_random_number)
generate_button.pack()

# Label hiển thị kết quả
result_label = tk.Label(window, text="", font=("Times New Roman", 16))
result_label.pack(pady=20)

# Button để thoát ứng dụng
exit_button = tk.Button(window, text="Thoát", command=window.quit)
exit_button.pack()

# Khởi chạy ứng dụng
window.mainloop()