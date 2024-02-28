import tkinter as tk
import os
from tkinter import ttk
import matlab.engine
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import time
#Colors
primary_color = "#003399"
secondary_color = "#66B2FF"
light_gray_color = "#E6E6E6"
white_color = "#FFFFFF"
light_green_color = "#66CC99"
accent_color = "#FF9900"
dark_gray_color = "#666666"
error_color = "#CC0000"


#Fonksiyonlar
mode=False
x=0
start_time=None
end_time=None
execution_time=None
eng = matlab.engine.start_matlab()
image_paths = []
def removeImage():
    print('Resimler Silindi')
    klasor_yolu = 'C:\\Users\\yagiz\\OneDrive\\Documents\\GitHub\\Python'
    dosyalar = os.listdir(klasor_yolu)
    for dosya in dosyalar:
     dosya_yolu = os.path.join(klasor_yolu, dosya)
     if dosya.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        os.remove(dosya_yolu)
        print(f"{dosya} silindi.")

class Option:
    def __init__(self, value, label):
        self.value = value
        self.label = label

    def __str__(self):
        return self.label
    
def on_select(event):
    global x
    selected_item = combobox.get()
    option = next((opt for opt in options if str(opt) == selected_item), None)
    if option:
        print("Seçilen öğe:", option.value)
        x=option.value
        print(x)
    else:
        print("Seçilen öğe bulunamadı.")

def darkmodSwicth():
   print('Tema Değişti')
   global mode
   if mode==False:
    myTiltle.config(fg='white',bg='#003399')
    form.configure(bg='black')
    mode=True
   else:
    myTiltle.config(fg='black',bg=primary_color)
    form.configure(bg='white')
    mode=False

def getScript():
      global start_time
      global end_time
      global execution_time
      start_time=time.time()
      if x == 0:
          script_path = "script0.png"
          if not os.path.exists(script_path):
              eng.eval("run('step0.m')", nargout=0)
              eng.eval("saveas(gcf, 'script0.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script0.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
      elif x == 1:
          script_path = "script1_2.png"
          if not os.path.exists(script_path):
              eng.eval("run('step1_2.m')", nargout=0)
              eng.eval("saveas(gcf, 'script1_2.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script1_2.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
          

      elif x == 2:
          script_path = "script3.png"
          if not os.path.exists(script_path):
              eng.eval("run('step3.m')", nargout=0)
              eng.eval("saveas(gcf, 'script3.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script3.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
         

      elif x == 3:
          script_path = "script4.png"
          if not os.path.exists(script_path):
              eng.eval("run('step4.m')", nargout=0)
              eng.eval("saveas(gcf, 'script4.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script4.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
          

      elif x == 4:
          script_path = "script5.png"
          if not os.path.exists(script_path):
              eng.eval("run('step5.m')", nargout=0)
              eng.eval("saveas(gcf, 'script5.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script5.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
          

      elif x == 5:
          script_path = "script6.png"
          if not os.path.exists(script_path):
              eng.eval("run('step6.m')", nargout=0)
              eng.eval("saveas(gcf, 'script6.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script6.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
          

      elif x == 6:
          script_path = "script7.png"
          if not os.path.exists(script_path):
              eng.eval("run('step7.m')", nargout=0)
              eng.eval("saveas(gcf, 'script7.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script7.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
          

      elif x == 7:
          script_path = "script8.png"
          if not os.path.exists(script_path):
              eng.eval("run('step8.m')", nargout=0)
              eng.eval("saveas(gcf, 'script8.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script8.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
          

      elif x == 8:
          script_path = "script9.png"
          if not os.path.exists(script_path):
              eng.eval("run('step9.m')", nargout=0)
              eng.eval("saveas(gcf, 'script9.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script9.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
          
          
      elif x == 9:
          script_path = "script10.png"
          if not os.path.exists(script_path):
              eng.eval("run('step10.m')", nargout=0)
              eng.eval("saveas(gcf, 'script10.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script10.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
         

      elif x == 10:
          script_path = "script11.png"
          if not os.path.exists(script_path):
              eng.eval("run('step11.m')", nargout=0)
              eng.eval("saveas(gcf, 'script11.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script11.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
          

      elif x == 11:
          script_path = "script12.png"
          if not os.path.exists(script_path):
              eng.eval("run('step12.m')", nargout=0)
              eng.eval("saveas(gcf, 'script12.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script12.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
         

      elif x == 12:
          script_path = "script13.png"
          if not os.path.exists(script_path):
              eng.eval("run('step13.m')", nargout=0)
              eng.eval("saveas(gcf, 'script13.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script13.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
         

      elif x == 13:
          script_path = "script14.png"
          if not os.path.exists(script_path):
              eng.eval("run('step14.m')", nargout=0)
              eng.eval("saveas(gcf, 'script14.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script14.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
         

      elif x == 14:
          script_path = "script15_16.png"
          if not os.path.exists(script_path):
              eng.eval("run('step15_16.m')", nargout=0)
              eng.eval("saveas(gcf, 'script15_16.png')", nargout=0)
          else:
              print("Resim var.")

          image = Image.open("script15_16.png")
          label_width = resultLabel.winfo_width()
          label_height = resultLabel.winfo_height()
          print(label_height)
          print(label_width)
          scaled_image = image.resize((label_width, label_height))
          result = ImageTk.PhotoImage(scaled_image)
          resultLabel.configure(image=result)
          resultLabel.image = result
      end_time=time.time()    
      testTime = end_time - start_time
      timeLabel.config(text=str(testTime)+'  -Saniye')
          
    
    
options = [
    Option(1, "COP Mean ML Coordinate"),
    Option(2, "COP Mean AP Coordinate"),
    Option(3, "COP Mean Distance"),
    Option(4, "COP Max"),
    Option(5, "COP RMS"),
    Option(6, "COP Range (Amplitude)"),
    Option(7, "COP and Sway Area"),
    Option(8, "Sway Direction Coeff"),
    Option(9, "Maximum Displacement"),
    Option(10, "COP Displacement and Sway Velocity"),
    Option(11, "COP Max Signal"),
    Option(12, "Sway Length ML"),
    Option(13, "Sway Length AP"),
    Option(14, "COP"),
    Option(15, "ML Time Series"),
    Option(16, "AP Time Series"),
] 

# GUI
form = tk.Tk()
form.title("My Application")
form.configure(bg="white")
form.geometry('1000x1100')
image_frame = tk.Frame(form)
image = tk.PhotoImage(file='indir.png')
myTiltle=tk.Label(form,text="Tiltle of Program",width=30,height=2,font='Helvetica 18 bold',fg='Black',bg=primary_color)
timeLabel=tk.Label(form,text=execution_time,width=30,height=2,font='Helvetica 18 bold',fg='Black')
myButton_1= tk.Button(form,text='Script 1',font='Helvetica 9 bold',bd=1 ,width=40,height=2,command=getScript)
myButton_3= tk.Button(form,text='Sil',font='Helvetica 9 bold',bd=1 ,width=40,height=2,command=removeImage)
myButton_2= tk.Button(form,text='DarkModButton',font='Helvetica 9 bold',bd=1 ,width=40,height=2,command=darkmodSwicth)
combobox = ttk.Combobox(form, values=[str(opt) for opt in options],width=50,height=150)
resultLabel = tk.Label(form, image=image,width=400,height=400)
tiltleLabel= tk.Label(form,text='All Grahps',font='Helvetica 18 bold',bg='white')
tiltleLabel.grid(column=3,row=0,columnspan=3,pady=10)
myTiltle.grid(column=0,row=0,columnspan=3,pady=10)
timeLabel.grid(column=0,row=5 ,columnspan=3, pady=10)
myButton_2.grid(column=0,row=4 ,columnspan=3, pady=10)
myButton_3.grid(column=0,row=6 ,columnspan=3, pady=10)
resultLabel.grid(column=0,row=1,columnspan=3,pady=10,padx=40 )
myButton_1.grid(column=0,row=3 ,columnspan=3, pady=10)
image_frame.grid(column=4,row=1,columnspan=3,pady=10)
for image_path in image_paths:
    image = Image.open(image_path)
    image = image.resize((300, 300))  # Adjust the size as per your needs
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(image_frame, image=photo)
    image_label.image = photo
    image_label.pack(side=tk.LEFT)
combobox.grid(column=0,columnspan=3,row=2 , pady=10)
combobox.bind("<<ComboboxSelected>>",  on_select)
# Pencereyi göster
tk.mainloop()
eng.quit()