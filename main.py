from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from io import BytesIO
from PIL import Image, ImageTk

root = Tk(className='画图')
root.geometry('700x500')
root.state('zoomed')

change_size_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0f\x00\x00\x00\x0e\x08\x06\x00\x00\x00\xf0\x8aF\xef\x00\x00\
\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\
\x01\xc7o\xa8d\x00\x00\x01rIDAT8O\x85R\xbfK\xc3P\x10\xbe\x86\xe0RhP\x1c\x8atpqP\'\xa9\xbb\xe9h\xfdO\x9c\xd4]-\xb8\xb8\xf9\x87\x88\
\x8b\x83 *vs\xd0\x82 \xb5ZqQ\xab\x16+m\x9aZ[\x9b\xe4\xbc{?\xd2\x94\x08~\xef}\xb9\xbb\x97\xfb\xde]\xdeK\x02"\x98Z\xdd/l\xe4\xe7\xb6\
\x11h\xa0\\\x0b\xc8\xea\x98-\xc7\x97\x8f\r\xd8\xb2\xad\x9c)S\x86X\xcf\xcfJ\x01e\xfbd\x03\xb2L_\xdb\x80\xdf\x01\xb8ns\xc9P\x9a\x10\
\xff\t\xc5\x1aw\x10\x04\x10\x13\xb3\x907\xd0BM-\xe4\x8dh\n\xfcYYW\xd2\xc9Q![\x1e\x84DL\x1c\x13\xaa.\xa2\xeb4\x05L{\xe7\xf8|&\x9d"\
\x17\xa1\xfc\xe2LG\x85\xa2}z\xe85I\xce\x940W\x162\xf6\xda2\x9f0\xc2\xdeQEX-\xf4\x95pXUv\xc1\xe7\xc2\xa0\xb6\x87\t<nk\x0eT\x14\xef^\
\x99m\xb8\x0f\xe9@\x95l\xa7\xe7\t\xb1)*\xb0\x98\x1c{>\r\xcf\x9f_\xf2\x80h\xa3b\xf9\x1d2\xf8\xd12\xcc\xb1\x96\xc8V\x98$&\x93\xe3-\
\xd8=\xbcA\xb7?\xc0f\xef\x07\x1b\xdd>\xd6;=\xac\xb9\xdf\xf8\xe4tq\xf3\xe0\x1aON\xcf\nR\x12\x87\x11\xad\xcc\xf4\xb4\xcf\x9fA4\x8c\
\xd8\x85\x840/\xaau\x18x^x\x10\xd4\xb1\xb8\n\xf6\x1f\xde\xda\x90\x9b\x18\xf9\xfdG\x90\xb8*\x95l\xc7i\xdb*\x8e\xc1\xb2R\xc5\xc5l\
\xb6\xa8\xc2\x08\x00~\x01\xe7\x1an\xc6\xc0\n\x98,\x00\x00\x00\x00IEND\xaeB`\x82'

change_size_bytesio = BytesIO(change_size_bytes)

change_size_img = ImageTk.PhotoImage(Image.open(change_size_bytesio))

h_pixel_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00\x1d\x08\x06\x00\x00\x00\xcb\x9en\x87\x00\x00\x00\x01\
sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x1d\x86\x00\x00\x1d\x86\x01]\
\xa2\x13\x81\x00\x00\x00\xe2IDATHK\xed\x96A\n\x830\x10EgJ\xf7Z\xbaq\xe9\x91<\x8ax\x08\xf1\x88^\xa2Tw.J\xa6\xf9\xc5\x14\x11M\xdaT\
\xb4\x8by \x81\xe0\x9f\xf93\x191\xdcu\x9d\x90\x87G\x92\xd0\x95\x99\xee"t\xea\xfbq\xd7\x8f\xb1\x9a\x8b\xd5\xdc\xac\xe6\x1c\xd0\x9c\
\xc6u\x11\x97<\x16h\x11\xc3\xc7j\x07\xe6\xc9Q\x8d\xd7\xed\x04c\x9f\xb9v\xad\x13\x8b\x06\\\x0b\xb7d\xed\x08\xff\xb3\x03\x8e\xa9\x89\
\x98!\x04\xa1A\xf4\x16\x05!\x02\xc4\x12J\x0e\x82]E\x80o\xaa\x07x\x17\x9aPr\xc0\xc6\x98\xf8\x12\x7f\x84\xed1qUUb\xe7`\xdc\xda\x8f,\
\xcb\xa8\xaek\xa2\xb2,\xe5\x08\xda\xb6E\xe7\xe5\xd3/ks\x86ax\xad\x87\x19p\xa8\x015\xa0\x06\xd4\x80\x1aP\x03j\x80\x9b\xa6\x91\xa2(\
\xde\xff\xe7\xbd\xc8\xf3\x9c\xd24%\xdc\x9d\x0f\xbb\x13\x12\x11=\x01n\x15\xee\xeb)\xfdCe\x00\x00\x00\x00IEND\xaeB`\x82'

h_pixel_bytesio = BytesIO(h_pixel_bytes)

h_pixel_img = ImageTk.PhotoImage(Image.open(h_pixel_bytesio))

v_pixel_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x1e\x00\x00\x00 \x08\x06\x00\x00\x00\x05@\xc8\x7f\x00\x00\x00\x01\
sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x1d\x86\x00\x00\x1d\x86\x01]\
\xa2\x13\x81\x00\x00\x01\x05IDATXG\xed\x97\xbf\n\x830\x10\x87/\xd2]K\x17GG\x1f\xc7Gqttt\xf3\xf9|\x88R\xdd\x1cJ\xd3\xfcl\x0e$X\x88\
\x7f.\x85\xe2\x07\xc7\xe5n\xf0\x83D/\xa8\xea\xba\xd6}\xdf\xd3^\xd24\xa5\xaa\xaaHkM\xc30\xd8\xeewTY\x96\xbam[[n\xa7\xeb:\xca\xf3\xdc\
[\x1c\xd9\xbc\x9bq\x1c\xed\xca\x8f\xc3\xc4k\xf9\x7f\xf1+\x8e\xed\xeaC\x10\xf1\xd3H\xafJM\x99\x11\x17Cv3R\x80\xccrQ\xf1\\\xca\xb0\\L\
\x8c3u\xa5\x0c\xfab\xe2\xc8\x0c\x91\x87\x19&\x88\xbb\t\x80\xcc=\xd1\xad\x86|\n\xae\x11N/8\xa78\x18\xa78\x18\xa7\xf8P0\xaf\xa7\xe0\
\x1aa{bb<\x1cw0\x82/\x0bd\xee\x89\x891\x8f\xf9rpA_t\xab/\x0br\xd4\xe8\x8b\xbf\\s9K\x81\xb8\x18@\x86;\x98\xa5 \x88\x18\xe0\xcc\xe7\
\x04\x13\xbb\xfcL\xac\x9a\xa6\xd1EQ\xac\xfe\xf7q\xc9\xb2\x8c\x92$\xf1\xff[4\xb1\xfc\xb1m\xc4OL\xf4\x06\x86\xae\x80a(\x8b\xe3s\x00\
\x00\x00\x00IEND\xaeB`\x82'

v_pixel_bytesio = BytesIO(v_pixel_bytes)

v_pixel_img = ImageTk.PhotoImage(Image.open(v_pixel_bytesio))

o_angle_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00\x1b\x08\x06\x00\x00\x00\x1d\xc7\x8d\x9a\x00\x00\x00\
\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x1d\x86\x00\x00\x1d\x86\x01\
]\xa2\x13\x81\x00\x00\x016IDATHK\xcd\x96M\x0e\x820\x10F\xa7\xc65`\xdc\xb0\xe42,Yr\r\x0e\xc0\x01\xb8\x10KN\xc3\x8e\x8d\x11\xf6\xc6\
\xda\x8f\x14\xe2\x0f\xb40R\xf4%D\xd38}_\xc7\x11\x11m\xdbJ2p\xf3}:\x0bAW)\xe9\xd0uz\xd5\xcc]\xd5\x9cT\xcdE\xd5\x1c-5\x07\xfd:\xc9 \
\xe7\x82Z\xecab\xb6\x03\xefr\x9c\xc6\x98\xf6\x89\xbb\xba\xdek\xe7:1\x19`h\xe1\x96\xcc}\x85\xff\xd9\x81\x81\xe7\x10\x9c!\x04\xb6A4\
\x1e\n\x85\xd8\x80\x8bM\x0e\xac]\xc5\x06kN\x0f\xf0Y\xd4\xd8\xe4\xc0z\x1fp\xcdW\x01<\xcf\xd3\xefx\x085\'\xec\x00\xbe\x1a\xb44M\xd9!\
\xc20\xa4\xa2(x\x01 \x8f\xe3\x98\xaa\xaa\xd2+\xeb\xe9\xd4|\x04A\xb0\xf8\xa7=\xb2\x85\xbc\xae\xeb^.1\xdczm\x11[\xc9\xa3(\xea\xe5\xe8\
\xc2\xe2\x00.\xe4`Q\x00Wr`\r\xe0R\x0e\x8c\x01\\\xcb\xc1l\x80=\xe4`2\xc0^r\xf0\x11`O9x\t\xb0\xb7\x1c\x8c\x01~!\x07}\x80_\xc9\x81P\
\x052I\x12*\xcbR/\xad\x87+\x07"\xcfs\x99e\x195M\xa3\x97\xd6\x81\xbfU\\\x1c9\xc0\x93\xe3\xd7OD\\9\x11\xd1\x03\xb0\xcd\'\xe6U%\x98J\
\x00\x00\x00\x00IEND\xaeB`\x82'

o_angle_bytesio = BytesIO(o_angle_bytes)

o_angle_img = ImageTk.PhotoImage(Image.open(o_angle_bytesio))

e_angle_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x17\x00\x00\x00 \x08\x06\x00\x00\x00\xf9U\xe3\xb5\x00\x00\x00\x01\
sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x1d\x86\x00\x00\x1d\x86\x01]\
\xa2\x13\x81\x00\x00\x01CIDATHK\xed\x951n\x840\x10E\x07+\x05\x15\x10\xa5\xa1\xa4\xe4"\x94\x9c\x82\x9e\x0b\xd0s!JNCG\xb3Z\xe8\xa3\
\x10\x7f\xcb\xb3\x81\xc5\x80a\x9d*y\xd2\xc8\xf8\x83\xdeH\xbbf\xf0\x86a\x98\xc8\x820\x0c\xa9\xaa*\xaa\xeb\x9a\xa6i\xa2q\x1c\xf5\x9dm\
\x84^w\x818\xcfs*\xcbR\'v\x1c\xca!\xce\xb2\x8c\x9a\xa6\xa1\xbe\xefuj\xc7\xae\x9c\xc5m\xdb\xead\x9f/\xf9\xfc\x9cM\xf9Y\xf1\xa7|\xfe\
\xdd\xf3\xd4\xca\x18\xe5W\xc4\x1fR\x0c\xb0r\x83\x95\xfc\x151\xc3\r\x16\xf2+\xbf\xf1\xb3\x98A\xfe\x90\x9f\x15\x03!\xcf\xfa]\x9ey\xd4\
M\x16\xc0\xca\x99\x92_\x113h\xa0\x8a\xf7(\xce^\x11\x1f!\x8a\xa2\xf8\x151\x10A\x10\xe8K\xf7,N\x8bk\xfe\xe5F\xfe\x88<\x8ec}\xf5\x03\
\xe6\x8b*\xde\xa3tf-\xef\xbaN\xc9\xe7\xdfO\x080\xc3Q<\xc0\xb0rf%\x878I\x92\xd5\x87\x19\xf3\x83\x07\xd63\xc8\x0f\xe5[b\xe6\xcd\xd0\
\x00{\xe4\xbb\xf2#13o\xc0b\xb0)\xb7\x153\x10b\x86\xb3\x18\x18\xe5g\xc5\x0c\xfe\x839+\xf9U\xb1\x89\x85\xdc\xa5\x18<\xe4\xae\xc5@\xf8\
\xbe\xafd\xae\xc5@\xa4iJQ\x149\x17\x03\xbc\xb3\xd2\xeb^LD\xf4\ri\xa1\xe8"\xf4&\xe2\xde\x00\x00\x00\x00IEND\xaeB`\x82'

e_angle_bytesio = BytesIO(e_angle_bytes)

e_angle_img = ImageTk.PhotoImage(Image.open(e_angle_bytesio))

def set(p):
    global paint
    paint = p
    if p == 'text':
        cv['cursor'] = 'xterm'
    else:
        cv['cursor'] = 'tcross'

def config_widthheight():
    window = Toplevel(root)
    window.geometry('267x380')
    window.focus_set()
    def exitwindow():
        root.attributes('-disabled', False)
        window.destroy()
    root.attributes('-disabled', True)
    window.title('调整大小和扭曲')
    window.transient(root)
    window.resizable(False, False)
    window.protocol('WM_DELETE_WINDOW', exitwindow)

    def wrap_button(btn):
        def set_focus1(event):
            nonlocal focus_in_btn
            focus_in_btn = True
        def set_focus2(event):
            nonlocal focus_in_btn
            focus_in_btn = False
        btn.bind('<ButtonPress-1>', set_focus1)
        btn.bind('<ButtonRelease-1>', set_focus2)

    sizefrm = ttk.LabelFrame(window, text='重新调整大小')
    sizefrm.place(x=14, y=13, width=242, height=173)
    focus_in_btn = False
    Label(sizefrm, text='依据(B):').place(x=15, y=6)
    intvar = IntVar()
    intvar.set(1)
    def setvalue1():
        strvar1.set('100')
        strvar2.set('100')
    def setvalue2():
        strvar1.set(str(cvwidth))
        strvar2.set(str(cvheight))
    rb1 = ttk.Radiobutton(sizefrm, text='百分比', value=1, variable=intvar, command=setvalue1)
    wrap_button(rb1)
    rb1.place(x=80, y=6)
    rb2 = ttk.Radiobutton(sizefrm, text='像素', value=2, variable=intvar, command=setvalue2)
    wrap_button(rb2)
    rb2.place(x=155, y=6)

    def testvar1(content):
        valid = False
        if content.startswith('0'):
            content = content[1:]
            strvar1.set(content)
        if content.isdigit():
            valid = True
        elif not content:
            strvar1.set('0')
            valid = True
        if valid:
            if checked.get():
                if intvar.get() == 1:
                    strvar2.set(content if content else '0')
                else:
                    strvar2.set(str(int(cvheight * int(content if content else '0') / cvwidth)))
            return True
        else:
            window.bell()
            return False
    def testvar2(content):
        valid = False
        if content.startswith('0'):
            content = content[1:]
            strvar2.set(content)
        if content.isdigit():
            valid = True
        elif not content:
            strvar2.set('0')
            valid = True
        if valid:
            if intvar.get() == 1:
                if checked.get():
                    strvar1.set(content if content else '0')
            return True
        else:
            window.bell()
            return False
    testvar1 = window.register(testvar1)
    testvar2 = window.register(testvar2)

    lb = Label(sizefrm, image=h_pixel_img)
    lb.place(x=15, y=35)
    Label(sizefrm, text='水平(H):').place(x=77, y=45)
    strvar1 = StringVar()
    entry1 = ttk.Entry(sizefrm, textvariable=strvar1, validate='key', validatecommand=(testvar1, '%P'))
    strvar1.set('100')
    entry1.place(x=161, y=45, width=61, height=23)

    Label(sizefrm, image=v_pixel_img).place(x=15, y=77)
    Label(sizefrm, text='垂直(V):').place(x=77, y=87)
    strvar2 = StringVar()
    entry2 = ttk.Entry(sizefrm, textvariable=strvar2, validate='key', validatecommand=(testvar2, '%P'))
    strvar2.set('100')
    entry2.place(x=161, y=87, width=61, height=23)

    checked = IntVar()
    checked.set(1)
    checkbtn = ttk.Checkbutton(sizefrm, text='保持纵横比(M)', variable=checked)
    wrap_button(checkbtn)
    checkbtn.place(x=15, y=120)

    tiltfrm = ttk.LabelFrame(window, text='倾斜(角度)')
    tiltfrm.place(x=14, y=198, width=242, height=128)

    def testvar3(content):
        valid = False
        if content.startswith('0'):
            content = content[1:]
            strvar3.set(content)
        if content.isdigit():
            valid = True
        elif not content:
            strvar3.set('0')
            valid = True
        if valid:
            return True
        else:
            window.bell()
            return False
    def testvar4(content):
        valid = False
        if content.startswith('0'):
            content = content[1:]
            strvar4.set(content)
        if content.isdigit():
            valid = True
        elif not content:
            strvar4.set('0')
            valid = True
        if valid:
            return True
        else:
            window.bell()
            return False
    testvar3 = window.register(testvar3)
    testvar4 = window.register(testvar4)

    Label(tiltfrm, image=o_angle_img).place(x=15, y=8)
    Label(tiltfrm, text='水平(O):').place(x=77, y=18)
    strvar3 = StringVar()
    entry3 = ttk.Entry(tiltfrm, textvariable=strvar3, validate='key', validatecommand=(testvar3, '%P'))
    strvar3.set('0')
    entry3.place(x=161, y=18, width=61, height=23)

    Label(tiltfrm, image=e_angle_img).place(x=15, y=58)
    Label(tiltfrm, text='垂直(E):').place(x=77, y=68)
    strvar4 = StringVar()
    entry4 = ttk.Entry(tiltfrm, textvariable=strvar4, validate='key', validatecommand=(testvar4, '%P'))
    strvar4.set('0')
    entry4.place(x=161, y=68, width=61, height=23)

    def ok():
        global cvwidth, cvheight
        if intvar.get() == 1:
            cvwidth = int(int(cvwidth) * int(strvar1.get()) / 100)
            cvheight = int(int(cvheight) * int(strvar2.get()) / 100)
        else:
            ordwidth = cvwidth
            ordheight = cvheight
            cvwidth = int(strvar1.get()) or ordwidth
            cvheight = int(strvar2.get()) or ordheight
        cv.place_configure(width=cvwidth, height=cvheight)
        exitwindow()
    def cancel():
        exitwindow()

    okbtn = ttk.Button(window, text='确定', default='active', command=ok)
    wrap_button(okbtn)
    cancelbtn = ttk.Button(window, text='取消', command=cancel)
    wrap_button(cancelbtn)
    okbtn.place(x=75, y=340)
    cancelbtn.place(x=170, y=340)
    
    while True:
        try:
            if focus_in_btn:
                lb.focus_set()
            window.update()
        except TclError:
            return

def choosebgcolor():
    color = colorchooser.askcolor()[1]
    if color is not None:
        global bgcolor
        bgcolor = color

def setbg():
    global bgcolor
    bgcolor = ''

def choosefgcolor():
    color = colorchooser.askcolor()[1]
    if color is not None:
        global fgcolor
        fgcolor = color

menu = Menu(root)
drawmenu = Menu(menu, tearoff=False)
menu.add_cascade(label='画图(D)', menu=drawmenu)
colormenu = Menu(drawmenu, tearoff=False)
drawmenu.add_cascade(label='颜色(C)', menu=colormenu)
colormenu.add_command(label='选择背景颜色(C)...', command=choosebgcolor)
colormenu.add_command(label='设置背景色为透明(S)', command=setbg)
colormenu.add_command(label='选择前景颜色(C)...', command=choosefgcolor)
drawmenu.add_separator()
drawmenu.add_command(label='直线(L)', command=lambda: set('line'))
drawmenu.add_command(label='椭圆(O)', command=lambda: set('oval'))
drawmenu.add_command(label='矩形(R)', command=lambda: set('rect'))
drawmenu.add_command(label='写字(W)', command=lambda: set('write'))
drawmenu.add_command(label='文字(T)', command=lambda: set('text'))
canvasmenu = Menu(menu, tearoff=False)
menu.add_cascade(label='画布(C)', menu=canvasmenu)
canvasmenu.add_command(label='调整大小(S)', command=config_widthheight, image=change_size_img, compound='left')
root['menu'] = menu

startx = None
starty = None
nowpainting = None
paint = 'line'
shiftdown = False
bgcolor = 'white'
fgcolor = 'black'

def getstart(event):
    global startx, starty, nowpainting
    startx = event.x
    starty = event.y
    if paint == 'line':
        nowpainting = cv.create_line(startx, starty, event.x, event.y, width=2, fill=fgcolor, smooth=True)
    elif paint == 'oval':
        nowpainting = cv.create_oval(startx, starty, event.x, event.y, width=2, outline=fgcolor, fill=bgcolor)
    elif paint == 'rect':
        nowpainting = cv.create_rectangle(startx, starty, event.x, event.y, width=2, outline=fgcolor, fill=bgcolor)
    elif paint == 'write':
        nowpainting = cv.create_line(startx, starty, event.x, event.y, width=2, fill=fgcolor, smooth=True)
    elif paint == 'text':
        if nowpainting:
            txt = nowpainting[0].get()
            cv.focus_set()
            cv.delete(nowpainting[1])
            cv.create_text(nowpainting[2][0] + 3, nowpainting[2][1], text=txt, fill=fgcolor, justify='left', anchor='w')
            nowpainting = None
        else:
            xy = (startx, starty)
            etr = ttk.Entry(cv)
            etr.focus_set()
            win = cv.create_window(startx, starty, window=etr, anchor='w')
            nowpainting = (etr, win, xy)

def changeabsvalue(x, n):
    return n if x >= 0 else -n

def painting(event):
    global startx, starty, nowpainting
    if nowpainting is not None:
        if shiftdown:
            if paint == 'line':
                relx = abs(event.x - startx)
                rely = abs(event.y - starty)
                if relx >= rely:
                    cv.coords(nowpainting, startx, starty, event.x, starty)
                else:
                    cv.coords(nowpainting, startx, starty, startx, event.y)
            elif paint == 'write':
                nowpainting = cv.create_line(startx, starty, event.x, event.y, width=2, fill=fgcolor, smooth=True)
                startx = event.x
                starty = event.y
            elif paint != 'text':
                relx = event.x - startx
                rely = event.y - starty
                rel = min(abs(relx), abs(rely))
                relx = changeabsvalue(relx, rel)
                rely = changeabsvalue(rely, rel)
                cv.coords(nowpainting, startx, starty, startx + relx, starty + rely)
        else:
            if paint == 'write':
                nowpainting = cv.create_line(startx, starty, event.x, event.y, width=2, fill=fgcolor)
                startx = event.x
                starty = event.y
            elif paint != 'text':
                cv.coords(nowpainting, startx, starty, event.x, event.y)

def endpaint(event):
    global startx, starty, nowpainting
    startx = None
    starty = None
    if paint != 'text':
        nowpainting = None

def onshiftdown(event):
    global shiftdown
    shiftdown = True

def onshiftup(event):
    global shiftdown
    shiftdown = False

bg = Canvas(root, bg='#d2dcea', highlightthickness=0)

cv = Canvas(root, bg='white', highlightthickness=1, cursor='tcross')
cv.bind('<1>', getstart)
cv.bind('<Motion>', painting)
cv.bind('<ButtonRelease-1>', endpaint)
cv.bind('<KeyPress-Shift_L>', onshiftdown)
cv.bind('<KeyRelease-Shift_L>', onshiftup)
cv.bind('<KeyPress-Shift_R>', onshiftdown)
cv.bind('<KeyRelease-Shift_R>', onshiftup)
cv.focus_set()
cvwidth = 600
cvheight = 400
cv.place(x=5, y=5, width=cvwidth, height=cvheight)

bg.pack(fill='both', expand=True)

root.mainloop()
