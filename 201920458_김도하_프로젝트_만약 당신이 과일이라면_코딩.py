import tkinter as tk
import tkinter.font
from tkinter import messagebox
from tkinter import simpledialog

def ace() :
    '오렌지'
def acf() :
    '토마토'
def ade() :
    '복숭아'
def adf() :
    '자몽'
def bce() :
    '딸기'
def bcf() :
    '석류'
def bde() :
    '그린 키위'
def bdf() :
    '사과'


fruit_pre_type = {"ace": "오렌지", 
"acf": "토마토",
"ade": "복숭아",
"adf": "자몽",
"bce": "딸기",
"bcf": "석류",
"bde": "그린 키위",
"bdf": "사과"}

fruit_type = {"오렌지": "향기나는 과일, 그래 바로 나", 
"토마토": "내 얼굴이 빨갛게 익어갈수록, 의사들 얼굴은 파랗게 질려간다지?",
"복숭아": "물렁한 게 좋아 딱딱한 게 좋아? 난 뭐든지 할 수 있어",
"자몽": "묘한 매력, 빠져들면 못 헤어나올걸",
"딸기": "맛과 건강, 나처럼 챙길 수 있어?",
"석류": "미녀만? 아니 미남도 좋아하지",
"그린 키위": "겉까지 알찬 나, 버릴게 하나도 없다고",
"사과": "하루에 한 번 정도는 우리 얼굴 보자?"}

fruit_recipe = {"오렌지": "오렌지 소르베, 오렌지 주스, 오렌지 마멀레이드", 
"토마토": "토마토 달걀 볶음, 토마토 설탕 절임, 토마토 케찹",
"복숭아":"복숭아 타르트, 복숭아 스무디, 복숭아 아이스티",
"자몽": "자몽 에이드, 자몽차, 자몽청",
"딸기": "딸기 주스, 딸기 탕후루, 딸기 우유",
"석류": "석류 화채, 석류 샐러드, 석류 식초",
"그린 키위": "키위 소스, 키위 드레싱, 키위 스무디",
"사과": "애플 파이, 사과 젤리, 사과 잼"}

fruit_detail = {"오렌지": "상쾌한 맛이 나는 오렌지, 감기예방과 피부미용에 좋아요!", 
"토마토": "비타민 c,e,k가 풍부해서 여드름 억제에 좋아요!",
"복숭아":"흡수가 빠른 각종 당류 및 비타민과 무기질 등이 풍부하여 피로회복에 도움이 돼요!",
"자몽": "골다공증과 동맥경화, 지방 분해 효과 덕분에 다이어트에 좋아요!",
"딸기": "실제 당 함유량도 적고 칼로리도 낮아서 고혈압, 당뇨, 비만, 심혈관 질환같은 성인병에 좋아요!",
"석류": "여성에게는 생리불순에 효과가 있고 남성의 경우에는 발기부전 호전에 도움이 돼요!",
"그린 키위": "식이섬유로 꽉찬 영양 덩어리 과일, 껍질까지 먹으면 더 좋아요!",
"사과": "사과에 함유된 케세틴은 폐기능을 강하게 하여 오염물질로부터 폐를 보호해줘요!"}

fruit_good = {
"오렌지": "토마토", 
"토마토": "오렌지", 
"복숭아": "자몽", 
"자몽": "복숭아", 
"딸기": "석류", 
"석류": "딸기", 
"그린 키위": "사과", 
"사과": "그린 키위"}


def check():
    global sms_result
    #print("no1 : {} {} {}".format(radio_var1.get(), radio_var2.get(), radio_var3.get()))

    ans1 = ""
    ans2 = ""
    ans3 = ""

    if radio_var1.get() == 1: ans1 = 'a'
    elif radio_var1.get() == 2: ans1 = 'b'
    if radio_var2.get() == 1: ans2 = 'c'
    elif radio_var2.get() == 2: ans2 = 'd'
    if radio_var3.get() == 1: ans3 = 'e'
    elif radio_var3.get() == 2: ans3 = 'f'
    
    if radio_var1.get() and radio_var2.get() and radio_var3.get():
        result = ans1 + ans2 + ans3
        re_result = fruit_pre_type[ans1 + ans2 + ans3]
        
        my_type = "["+re_result + "]" + fruit_type[re_result]
        my_detail = fruit_detail[re_result]
        my_recipe = fruit_recipe[re_result]
        my_good = fruit_good[re_result]
      

        label_10['text'] = my_type
        label_11['text'] = my_detail
        label_12['text'] = my_recipe
        label_13['text'] = my_good

window = tk.Tk()
window.title("만약 당신이 과일이라면")
window.geometry("1920x1080") #창크기

answer = messagebox.showinfo("만약 당신이 과일이라면","눈을 떠보니, 만약 당신이 과일이라면?")
answer = messagebox.showinfo("만약 당신이 과일이라면","START!")
name = simpledialog.askstring("입력", "이름을 입력해주세요.", parent=window)

answer = messagebox.showinfo("만약 당신이 과일이라면","'흐음...' \n\n '흐음냐..'")
answer = messagebox.showinfo("만약 당신이 과일이라면","'야...! 어서 눈을 떠!!' \n\n '응?'")
answer = messagebox.showinfo("만약 당신이 과일이라면","'뭐, 뭐야 이거?' \n\n 옆의 파인애플은 엄청나게 다급하다는 듯이 내게 말을 걸었다. \n\n '인간이 우릴 먹으려 한다고..!!' \n\n '그러게.. 너무 무서워 나..' \n\n 옆에 체리도 오두방정을 떨면서 울먹거렸다.")
answer = messagebox.showinfo("만약 당신이 과일이라면","...잠만 \n\n 이거 이상하잖아? \n\n 왜 과일이 내게 말을 거는 거지?!")
answer = messagebox.showinfo("만약 당신이 과일이라면","'어이. 신참. 정신 똑바로 차려.' \n\n 나이를 지긋하게 먹어 얼굴 곳곳에 갈색 기미가 드리운 바나나가 담담하게 말했다. \n\n '이러다.. 우리.. 다 죽어!!!!!!!!!!!!!!!!!' ")
answer = messagebox.showinfo("만약 당신이 과일이라면","'예?'")
answer = messagebox.showwarning("만약 당신이 과일이라면","미션: 나를 먹으려 하는 인간을 피해라..!!")

font=tkinter.font.Font(family="맑은 고딕", size=18)
font2=tkinter.font.Font(family="맑은 고딕", size=11)

tk.Label(window, text="만약 당신이 과일이라면?", fg="orange", font=font).pack()

frame1 = tk.Frame(window)
frame1.pack()

label_sinsang = tk.Label(frame1, text=name+'님', anchor="w", width="100", font=font2, fg="green")
label_0 = tk.Label(frame1, text="\n ※ 각 문항에 대해 원하는 답을 클릭해주세요", anchor="w", width="100", font=font2)

label_sinsang.grid(row=0, column=0, padx=10, pady=5)
label_0.grid(row=1, column=0, padx=10, pady=5)

frame2 = tk.Frame(window)
frame2.pack()

label_1 = tk.Label(frame1, text="1. 인간..! 인간이다..!! 과일이 된 나보다 몇 배나 큰 인간은 과일 친구들과 당신을 들고는 물줄기에 씻으려 한다. 이때의 당신은?", anchor='w', width="100", font=font2)

label_1.grid(row=2, column=0, padx=10, pady=5)

frame3 = tk.Frame(window)
frame3.pack()

frame4 = tk.Frame(window)
frame4.pack()

radio_var1 = tk.IntVar()

radio_1 = tk.Radiobutton(frame3, text="액션 영화처럼 떼굴떼굴 굴러서 물줄기를 피한다.", value="1", variable=radio_var1, command=check, font=font2)
radio_2 = tk.Radiobutton(frame4, text="목욕재계? 오히려 좋아 샤워를 즐긴다. ", value="2", variable=radio_var1, command=check, font=font2)

radio_1.grid(row=3, column=1, padx=10, pady=5)
radio_2.grid(row=4, column=1, padx=10, pady=5)

frame5 = tk.Frame(window)
frame5.pack()

label_2 = tk.Label(frame5, text="2. 인간이 나를 뽀득이 씻기고 뾰족-!한 칼날을 들어 껍질을 벗길 준비를 한다. 날카로운 칼날이 내 살갗에 닿고.. 어이 멈춰..!!", anchor='w', width="100", font=font2)

label_2.grid(row=5, column=0, padx=10, pady=5)

frame6 = tk.Frame(window)
frame6.pack()

frame7 = tk.Frame(window)
frame7.pack()

radio_var2 = tk.IntVar()

radio_3 = tk.Radiobutton(frame6, text="신체발부 수지부모. 복수의 칼날을 간다. ", value="1", variable=radio_var2, command=check, font=font2)
radio_4 = tk.Radiobutton(frame7, text="요즘엔 힙스터가 대세지. 민머리? 힙합으로 받아들인다.", value="2", variable=radio_var2, command=check, font=font2)

radio_3.grid(row=6, column=1, padx=10, pady=5)
radio_4.grid(row=7, column=1, padx=10, pady=5)

frame8 = tk.Frame(window)
frame8.pack()

label_3 = tk.Label(frame8, text="3. 어느새 조각나버린 친구들과 같이 접시에 담긴 나. 인간은 삼지창의 포크를 들고 당신을 찍어버리려고 하는데.. ", anchor='w', width="100", font=font2)

label_3.grid(row=8, column=0, padx=10, pady=5)

frame9 = tk.Frame(window)
frame9.pack()

frame10 = tk.Frame(window)
frame10.pack()

radio_var3 = tk.IntVar()

radio_5 = tk.Radiobutton(frame9, text="'넌 꽤 괜찮은 과일이었지..' 옆에 친구를 대신 밀어버린다.", value="1", variable=radio_var3, command=check, font=font2)
radio_6 = tk.Radiobutton(frame10, text="접시 위에서 트위스트 춤을 추며 포크를  피해 미끄러진다.", value="2", variable=radio_var3, command=check, font=font2)

radio_5.grid(row=9, column=1, padx=10, pady=5)
radio_6.grid(row=10, column=1, padx=10, pady=5)

tk.Label(window, text="").pack()

frame11 = tk.Frame(window)
frame11.pack()

label_blank = tk.Label(frame2, text="")
label_5 = tk.Label(frame11, text="타입", width=10, height=1, anchor="w", font=font2, fg="blue")
label_6 = tk.Label(frame11, text="상세", width=10, height=1, anchor="w", font=font2, fg="blue")
label_7 = tk.Label(frame11, text="레시피", width=10, height=1, anchor="w", font=font2, fg="blue")
label_8 = tk.Label(frame11, text="환상의궁합", width=10, height=1, anchor="w", font=font2, fg="blue")

label_10 = tk.Label(frame11, text="", width=65, height=1, anchor="w", fg="blue", font=font2)
label_11 = tk.Label(frame11, text="", width=65, height=1, anchor="w", fg="skyblue", font=font2)
label_12 = tk.Label(frame11, text="", width=65, height=1, anchor="w", fg="skyblue", font=font2)
label_13 = tk.Label(frame11, text="", width=65, height=1, anchor="w", fg="skyblue", font=font2)

label_5.grid(row=0, column=0, padx=10, pady=1)
label_6.grid(row=1, column=0, padx=10, pady=1)
label_7.grid(row=2, column=0, padx=10, pady=1)
label_8.grid(row=3, column=0, padx=10, pady=1)

label_10.grid(row=0, column=1, padx=10, pady=1)
label_11.grid(row=1, column=1, padx=10, pady=1)
label_12.grid(row=2, column=1, padx=10, pady=1)
label_13.grid(row=3, column=1, padx=10, pady=1)
label_blank.grid(row=4, column=0, padx=10, pady=1)

window.mainloop()