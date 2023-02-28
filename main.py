import tkinter as tk
import MemberDB

# 버튼 클릭 이벤트 함수
def on_button_click():
    input1 = entry1.get()
    input2 = entry2.get()
    print("입력1: {}, 입력2: {}".format(input1, input2))
    logindata = MemberDB.loginId(input1,input2)

    # 로그인 시도
    if len(logindata) > 0 :
        # 로그인 성공 메시지 표시
        empty_label.config(text="로그인 성공!")

        # 새로운 윈도우 생성
        new_window = tk.Toplevel(root)
        new_window.geometry("500x600")

        menu_bar = tk.Menu(new_window)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        data_menu = tk.Menu(menu_bar, tearoff=0)
        data_menu.add_command(label="Import")
        data_menu.add_command(label="Export")

        user_menu = tk.Menu(menu_bar, tearoff=0)
        user_menu.add_command(label="Login")
        user_menu.add_command(label="Logout")

        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Data", menu=data_menu)
        menu_bar.add_cascade(label="User", menu=user_menu)

        new_window.config(menu=menu_bar)

        # 라벨 추가
        label3 = tk.Label(new_window, text="환영합니다!")
        label3.pack()

        # 버튼
        button2 = tk.Button(new_window, text="로그아웃", command=new_window.destroy)
        button2.pack()
    else:
        # 로그인 실패 메시지 표시
        empty_label.config(text="로그인 실패!")

def signup_btn():
    # 기존 내용 지우기
    for widget in root.winfo_children():
        widget.destroy()

    # 아이디 입력창 추가
    id_label = tk.Label(root, text="아이디:")
    id_label.pack()
    id_entry = tk.Entry(root)
    id_entry.pack()

    # 비밀번호 입력창 추가
    password_label = tk.Label(root, text="비밀번호:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # 이름 입력창 추가
    name_label = tk.Label(root, text="이름:")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    # 회원가입 버튼 추가
    register_button = tk.Button(root, text="회원가입")
    register_button.pack()

# 메인 윈도우 생성
root = tk.Tk()

# 화면 크기 설정
root.geometry("200x150")

# 첫 번째 입력창
label1 = tk.Label(root, text="아이디")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

# 두 번째 입력창
label2 = tk.Label(root, text="비밀번호")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# 빈 라벨 추가
empty_label = tk.Label(root, text="")
empty_label.pack()

# 버튼
button = tk.Button(root, text="로그인", command=on_button_click)
button.pack()

# 빈 라벨 추가
empty_label = tk.Label(root, text="")
empty_label.pack()

# 버튼
button = tk.Button(root, text="회원가입", command=signup_btn)
button.pack()



# 메인 루프 실행
root.mainloop()