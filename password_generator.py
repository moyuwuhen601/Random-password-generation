import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip  # 复制功能

# 生成随机密码
def generate_password():
    try:
        password_length = int(length_entry.get())
        if password_length < 6:
            messagebox.showwarning("警告", "密码长度不能小于 6 位！")
            return
    except ValueError:
        messagebox.showwarning("警告", "请输入有效的数字！")
        return

    special_chars = "@!.?[]*#%"
    similar_chars = "0oO1lI"

    use_special = special_var.get()
    use_similar = similar_var.get()

    characters = string.ascii_letters + string.digits
    if use_special:
        characters += special_chars

    password = [
        random.choice(string.ascii_uppercase),  # 确保至少一个大写字母
        random.choice(string.ascii_lowercase),  # 确保至少一个小写字母
        random.choice(string.digits)            # 确保至少一个数字
    ]

    if use_special:
        password.append(random.choice(special_chars))

    if use_similar:
        # 选择两个不同的相似字符
        similar_pair = random.sample(similar_chars, 2)
        password.extend(similar_pair)

    # 计算还需要补充的字符数
    remaining_length = password_length - len(password)
    if remaining_length > 0:
        password += [random.choice(characters) for _ in range(remaining_length)]

    # 打乱密码顺序
    random.shuffle(password)

    # 生成最终密码
    final_password = "".join(password)
    password_var.set(final_password)

# 复制密码到剪贴板
def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("提示", "密码已复制到剪贴板！")

# 创建主窗口
root = tk.Tk()
root.title("随机密码生成器")
root.geometry("400x300")
root.resizable(False, False)

# 密码长度输入
tk.Label(root, text="密码长度（至少 6 位）：").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # 默认长度

# 复选框：是否包含特殊字符
special_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="包含特殊字符 (@!.?[]*#%)", variable=special_var).pack()

# 复选框：是否包含相似字符
similar_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="包含相似字符 (0oO1lI)", variable=similar_var).pack()

# 生成密码按钮
tk.Button(root, text="生成密码", command=generate_password).pack(pady=10)

# 显示密码
password_var = tk.StringVar()
password_label = tk.Entry(root, textvariable=password_var, state="readonly", width=30, font=("Arial", 14))
password_label.pack(pady=5)

# 复制密码按钮
tk.Button(root, text="复制密码", command=copy_to_clipboard).pack()

# 运行 GUI
root.mainloop()
