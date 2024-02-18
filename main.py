
from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import filedialog





# Choose a baseimage
def choose_picture():
    global pic1, img
    f_types = [('PNG Files','*.png'),('JPEG','*.jpg')]
    pic1 = filedialog.askopenfilename(filetypes=f_types,title='Choose a picture')
    picture_open = Image.open(pic1)
    resized_img = picture_open.resize((225,225))
    img = ImageTk.PhotoImage(resized_img)
    frame_img(img)
    return img

# Choose a watermark image
def choose_watermark():
    global pic2, water_mark, resized_img
    f_types = [('PNG Files','*.png'),('JPEG','*.jpg')]
    pic2 = filedialog.askopenfilename(filetypes=f_types,title='Choose a watermark')
    picture_open = Image.open(pic2)
    resized_img = picture_open.resize((50, 50))
    water_mark = ImageTk.PhotoImage(resized_img)

# Add watermark
def insert_watermark(checkmark1, checkmark2):
    if checkmark1 == True:
        add_watermark()
    elif checkmark2 == True:
        add_textmark()




# Add image watermark
def add_watermark():
    new_img = water_mark
    label = Label(image=new_img)
    label.place(x=300,y=80)


#Add text watermark
def add_textmark():
    new_image = create_image_text()
    resized_img = new_image.resize((225, 225))
    resized_img.show()


# Create image with image watermark
def create_image_pic():
    global baseImage
    position = (0,0)
    baseImage = Image.open(pic1).convert('RGBA')
    watermark = resized_img.convert('RGBA')
    baseImage.paste(watermark, position, mask=watermark)
    return baseImage

# Create image with text watermark
def create_image_text():
    global image, word, draw, pic
    image = Image.open(pic1)
    draw = ImageDraw.Draw(image)
    font_size = int(225/6)
    font = ImageFont.truetype('arial.ttf', font_size)
    x, y = int(225/2), int(225/2)
    word = e.get()
    draw.text((x,y), text=word, font=font,stroke_width=5,stroke_fill='#222', fill='#FFF', anchor='ms')
    return image

#Save watermark
def save_image():
    f_types = [('PNG Files','*.png'),('JPEG','*.jpg')]
    if e.get() != '':
        pic = create_image_text()
        filename = filedialog.asksaveasfile(mode='wb', filetypes=f_types, title='Save Picture', defaultextension=".png")
        pic.save(filename)
    else:
        baseImage1 = create_image_pic()
        filename = filedialog.asksaveasfile(mode='wb', filetypes=f_types, title='Save Picture', defaultextension=".png")
        baseImage1.save(filename)

    reset()

# Reset
def reset():
    check_button1.set(False)
    check_button2.set(False)
    e.delete(0, 'end')
    





# Create a tkinter window
root = Tk()
root.title('Image Watermarker')
root.geometry('600x400')
root.configure(bg='#26867c')

# Create input and label
e = Entry(root, width= 17)
e.place(x=190, y=290)


label = Label(root, text= 'Watermark Text', bg='#26867c')
label.place(x=95, y=290)


# Open image
picture_open = Image.open('empty.jpg')
resized_img1 = picture_open.resize((225,225))
img = ImageTk.PhotoImage(resized_img1)

# Create frame
def frame_img(image):
    frame = Frame(root,width=390, height=380)
    frame.pack()
    frame.place(anchor='nw', relx=0.5, rely=0.2)

    # Create label
    label = Label(frame, image=image)
    label.pack()



frame_img(img)


# Create buttons

check_button1 = BooleanVar()
check_button2 = BooleanVar()

b1 = Button(bg='#39c9bb',text='Choose a Picture',height=1,width=20,command= lambda : choose_picture())
b1.place(x=90,y=90)
b2 = Button(bg='#39c9bb',text='Choose a Watermark',height=1,width=20, command= lambda : choose_watermark())
b2.place(x=90,y=190)
b3 = Button(bg='#39c9bb',text='Add Watermark',height=1,width=14,
            command= lambda : insert_watermark(check_button1.get(), check_button2.get()))
b3.place(x=110,y=350)
b4 = Button(bg='#39c9bb',text='Save Picture',height=1,width=14, command= lambda : save_image())
b4.place(x=360,y=350)
b5 = Checkbutton(root, text= 'Picture Watermark',variable=check_button1,
                 onvalue=1,
                 offvalue=0,
                 bg='#26867c')
b5.place(x=90, y=140)
b6 = Checkbutton(root, text='Text Watermark',variable=check_button2,
                 onvalue=1,
                 offvalue=0,
                 bg='#26867c'
                 )
b6.place(x=90, y=250)


root.mainloop()

