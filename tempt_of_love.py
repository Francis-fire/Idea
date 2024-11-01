from tkinter import Tk,Label,Button,messagebox,Message,PhotoImage
import random
# from PIL import Image,ImageTk
import sys
import os
root = Tk()
root.geometry('900x730')
root.resizable(0,0)
root.title("爱心扫雷")
# image = Image.open("bg.png")
# image = image.resize((900,730))
# photo = ImageTk.PhotoImage(image)
#迷惑值
love = 0
#清醒值
awake = 50
#块中内容
block_names = ['甲','乙','丙','丁','戊','已','庚','辛','壬','癸',
               '亲','密','激','情','承','诺',
               '艳','遇','佳','人','一','红','花','迷','恋','情','深','无','所','傻',
               '海','誓','山','盟','白','头','偕','老',
               '情','投','意','合','情','意','绵','绵',
               '双','鱼','生','水','中','朝','暮','不','相','离',
               '两','心','知','永','相','随',
               '包','容','守','护']
#10个增加迷惑值的字
block_love = {''}
#5个增加清醒值的字
block_awake = {''}

# bg = Label(root, image=photo).place(x=0, y=0, relwidth=1, relheight=1)
score = Label(root, text=f'清醒值:{awake}%', font=('微软雅黑',20),bg='#98FB98')
score.grid(row=0, column=0)
sex = Label(root, text=f'迷惑值:{love}0%', font=('微软雅黑',20), bg='#EE82EE')
sex.grid(row=1, column=0)
# accomplishment = Label(root, text='成就:', font='微软雅黑', bg='#FFFF00')
# accomplishment.grid(row=20, column=0)
message = Message(root, text='游戏规则:.\
                  1.每局会刷新5个增加清醒的块和10个增加昏迷的块.\
                  2.清醒块:清醒值+10,迷惑值-10.\
                  3.迷惑块:清醒值-10,迷惑值+10.\
                  4.清醒值达到100时为胜利.\
                  5.清醒值等于0或迷惑值等于100,游戏失败.', font='微软雅黑')
message.grid(row=21, column=0)

#随机选出10个增加迷惑值的字
def new_love(num):
    num = 10 - num
    for i in range(0,num):
        block_love.add(random.choice(block_names))
#随机选出5个增加清醒值的字
def new_awake(num):
    num = 5 - num
    for i in range(0,num):
        block_awake.add(random.choice(block_names))
#确保清醒值和迷惑值的大小合适
def block_len_is_normal():
    if len(block_awake) < 5:
        new_awake(len(block_awake))
    if len(block_love) < 10:
        new_love(len(block_love))
    return True
#确保清醒值和迷惑值中没有空值
def block_null_is_false():
    for w in block_awake.copy(): 
        if w == '':
            block_awake.remove(w)
    if len(block_awake) < 5:
        new_awake(len(block_awake))
    for l in block_love.copy():    
        if l == '':
            block_love.remove(l)
    if block_len_is_normal() == True:
        return True
#判断迷惑字与清醒字是否相同
def alternative():
    for l in block_love.copy():
        for w in block_awake.copy():
            if l == w:
                block_awake.remove(w)
    if block_len_is_normal() == True and block_null_is_false() == True:
        return True
z = 0
while z <= 10:
    z += 1
    if alternative() == True and block_len_is_normal() == True and block_null_is_false() == True:
        continue
      

#结束
def boom():
    messagebox.showwarning(title='游戏结束', message="您已被爱情迷惑,游戏结束")
    s = messagebox.askokcancel("哈哈哈","是否再来一局")
    if s == True:
        print('睡了睡了')
    if s == False:
        sys.exit()
#胜利
def win():
    messagebox.showinfo(title='胜利', message='您的理智战胜了爱情的迷惑,游戏胜利')
    s = messagebox.askokcancel("哈哈哈","是否再来一局")
    if s == True:
        print('睡了睡了')
    if s == False:
        sys.exit()
        
#胜利
def balance():
    messagebox.showinfo(title='胜利', message='您是一个意志坚定非常感性的人,游戏胜利')
    s = messagebox.askokcancel("哈哈哈","是否再来一局")
    if s == True:
        print('睡了睡了')
    if s == False:
        sys.exit()
#删除块
def del_block(block_name):
    globals()[block_name].grid_forget()
    root.update()
#对选择的块判断是否使迷惑字，使 迷惑值 或 清醒值 增加
def range_num(name):
    global love
    global awake
    global block_love
    global block_names
    #globals把存储在name中的字符变为变量名字，利用.cget()提取按钮中的文本
    block_text_get = globals()[name].cget('text')
    block_names.remove(block_text_get)
    if len(block_names) == 0:
        balance()
    #删除已经按下的按钮块
    del_block(name)
    #判断点击的按钮块是否与选择出 增加迷惑值的按钮 或 增加清醒值的按钮相同
    for l in block_love:
        if block_text_get == l:
            #增加迷惑值:
            if love < 100:
                love += 10
            if awake > 0:
                awake -= 10
            score.config(text=f'清醒值:{awake}%')
            sex.config(text=f'迷惑值:{love}%')
            root.update()
            #当迷惑值到达100,醒值降低到0 时触发失败对话框
            if love == 100 or awake == 0:
                boom()
    for b in block_awake:
        if block_text_get == b:
            if awake < 100:
                awake += 10
                
            if love > 0:
                love -= 10
            score.config(text=f'清醒值:{awake}%')
            sex.config(text=f'迷惑值:{love}%')
            root.update()
            #清醒值到达100触发胜利对话框
            if awake == 100:
                win()
        
o_block = Button(root, text='甲', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='o_block'))
o1_block = Button(root, text='亲', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='o1_block'))
o2_block = Button(root, text='密', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='o2_block'))
t_block = Button(root, text='乙', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='t_block'))
th_block = Button(root, text='丙', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='th_block'))
fh_block = Button(root, text='丁', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='fh_block'))
fr_block = Button(root, text='戊', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='fr_block'))
block_1 = Button(root, text='已', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_1'))
block_011 = Button(root, text='情', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_011'))
block_012 = Button(root, text='意', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_012'))
block_013 = Button(root, text='绵', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_013'))
block_014 = Button(root, text='绵', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_014'))
block_2 = Button(root, text='庚', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_2'))
block_22 = Button(root, text='激', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_22'))
block_23 = Button(root, text='情', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_23'))
block_3 = Button(root, text='辛', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_3'))
block_4 = Button(root, text='壬', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_4'))
block_5 = Button(root, text='癸', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_5'))

block_6 = Button(root, text='迷', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_6'))
block_7 = Button(root, text='恋', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_7'))
block_8 = Button(root, text='情', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_8'))
block_9 = Button(root, text='深', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_9'))
block_10 = Button(root, text='无', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_10'))
block_11 = Button(root, text='所', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_11'))
block_12 = Button(root, text='傻', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_12'))

block_13 = Button(root, text='艳', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_13'))
block_131 = Button(root, text='情', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_131'))
block_132 = Button(root, text='投', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_132'))
block_133 = Button(root, text='意', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_133'))
block_134 = Button(root, text='合', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_134'))
block_14 = Button(root, text='遇', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_14'))
block_141 = Button(root, text='双', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_141'))
block_142 = Button(root, text='鱼', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_142'))
block_143 = Button(root, text='生', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_143'))
block_144 = Button(root, text='水', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_144'))
block_145 = Button(root, text='中', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_145'))
block_146 = Button(root, text='朝', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_146'))
block_147 = Button(root, text='暮', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_147'))
block_148 = Button(root, text='不', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_148'))
block_149 = Button(root, text='相', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_149'))
block_1410 = Button(root, text='离', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_1410'))
block_15 = Button(root, text='佳', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_15'))
block_151 = Button(root, text='海', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_151'))
block_152 = Button(root, text='誓', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_152'))
block_153 = Button(root, text='山', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_153'))
block_154 = Button(root, text='盟', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_154'))
block_155 = Button(root, text='白', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_155'))
block_156 = Button(root, text='头', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_156'))
block_157 = Button(root, text='偕', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_157'))
block_158 = Button(root, text='老', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_158'))
block_16= Button(root, text='人', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_16'))
block_161= Button(root, text='两', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_161'))
block_162= Button(root, text='心', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_162'))
block_163= Button(root, text='知', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_163'))
block_164= Button(root, text='永', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_164'))
block_165= Button(root, text='相', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_165'))
block_166= Button(root, text='随', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_166'))
block_17 = Button(root, text='一', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_17'))
block_171 = Button(root, text='包', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_171'))
block_172 = Button(root, text='容', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_172'))
block_173 = Button(root, text='守', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_173'))
block_174 = Button(root, text='护', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_174'))
block_18 = Button(root, text='红', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_18'))
block_181 = Button(root, text='承', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_181'))
block_182 = Button(root, text='诺', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_182'))
block_19 = Button(root, text='花', width=5, height=2, bg='#FF3030', command=lambda: range_num(name='block_19'))

t_block.grid(row=2, column=5)
th_block.grid(row=2, column=6)
block_3.grid(row=2, column=11)
block_4.grid(row=2, column=12)
block_2.grid(row=3, column=10)
block_22.grid(row=3, column=11)
block_23.grid(row=3, column=12)

o_block.grid(row=3, column=4)
o1_block.grid(row=3, column=5)
o2_block.grid(row=3, column=6)
fh_block.grid(row=3, column=7)
block_5.grid(row=3, column=13)

block_13.grid(row=4, column=3)
block_131.grid(row=4, column=4)
block_132.grid(row=4, column=5)
block_133.grid(row=4, column=6)
block_134.grid(row=4, column=7)
fr_block.grid(row=4, column=8)
block_1.grid(row=4, column=9)
block_011.grid(row=4, column=10)
block_012.grid(row=4, column=11)
block_013.grid(row=4, column=12)
block_014.grid(row=4, column=13)
block_6.grid(row=4, column=14)

block_14.grid(row=5, column=3)
block_141.grid(row=5, column=4)
block_142.grid(row=5, column=5)
block_143.grid(row=5, column=6)
block_144.grid(row=5, column=7)
block_145.grid(row=5, column=8)
block_146.grid(row=5, column=9)
block_147.grid(row=5, column=10)
block_148.grid(row=5, column=11)
block_149.grid(row=5, column=12)
block_1410.grid(row=5, column=13)
block_7.grid(row=5, column=14)

block_15.grid(row=6, column=4)
block_151.grid(row=6, column=5)
block_152.grid(row=6, column=6)
block_153.grid(row=6, column=7)
block_154.grid(row=6, column=8)
block_155.grid(row=6, column=9)
block_156.grid(row=6, column=10)
block_157.grid(row=6, column=11)
block_158.grid(row=6, column=12)
block_8.grid(row=6, column=13)


block_16.grid(row=7, column=5)
block_161.grid(row=7, column=6)
block_162.grid(row=7, column=7)
block_163.grid(row=7, column=8)
block_164.grid(row=7, column=9)
block_165.grid(row=7, column=10)
block_166.grid(row=7, column=11)
block_9.grid(row=7, column=12)

block_17.grid(row=8, column=6)
block_171.grid(row=8, column=7)
block_172.grid(row=8, column=8)
block_173.grid(row=8, column=9)
block_174.grid(row=8, column=10)
block_10.grid(row=8, column=11)

block_18.grid(row=9, column=7)
block_181.grid(row=9, column=8)
block_182.grid(row=9, column=9)
block_11.grid(row=9, column=10)

block_19.grid(row=10, column=8)
block_12.grid(row=10, column=9)

root.mainloop()