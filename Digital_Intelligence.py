from tkinter import *
from tkinter import ttk
#============================================================================================================
#Creación de la raíz aplicando algunos atributos
root=Tk()
root.title("Digital Intelligence v1.0")
root.resizable(False,False)
root.iconbitmap("img/cobra_kai.ico")
root.config(cursor="hand2")
root.geometry("1200x600")
root.config(bg="skyblue")
root.config(relief="groove")
root.config(bd="30")
#============================================================================================================




#============================================================================================================
#Creación del frame principal aplicando algunos atributos y elementos
main_frame=Frame(root,width="650",height="430")
main_frame.pack()
main_frame.config(bg="MidnightBlue")
main_frame.config(bd="20")
main_frame.config(relief="groove")
main_frame.config(cursor="hand2")
#Label del titulo del frame principal
Label(main_frame,text="DIGITAL INTELLIGENCE",fg="old lace",font=("Comic Sans MS",30),bg="MidnightBlue").place(x=60,y=20)
#Label que contendrá una imagen del logo principal y el botón de inicio
logo_image=PhotoImage(file="img/dip.png")
Label(main_frame,image=logo_image,bg="MidnightBlue").place(x=170,y=80)
#Botón para iniciar la aplicación
principal_Button=Button()
principal_Button.config(text="Iniciar", width="25",height="1",bg="MidnightBlue",fg="old lace",font=("Comic Sans MS",20))
principal_Button.pack()
#============================================================================================================




#============================================================================================================
#Creación del frame con todas las funciones 
master_frame=Frame(root,width="650",height="10")
master_frame.config(bg="old lace")
master_frame.config(bd="20")
master_frame.config(relief="groove")
master_frame.config(cursor="hand2")
#Creación del boton "machine_upload_button" mediante el cuál se cargaran los archivos de máquina
machine_upload_button=Button(master_frame,text="Archivo de Máquina",font=("Comic Sans MS",10),bg="black",fg="yellow")
machine_upload_button.grid(row=0,column=0,padx=10)
#Creación del botón "simulation_upload_Button" mediante el cuál se cargarán los archivos de simulación
simulation_upload_Button=Button(master_frame,text="Archivo de Simulación",font=("Comic Sans MS",10),bg="black",fg="yellow")
simulation_upload_Button.grid(row=0,column=1,padx=10)
#Creación del botón "reports_Button" mediante el cuál se harán los reportes
reports_Button=Button(master_frame,text="Reportes",font=("Comic Sans MS",10),bg="black",fg="yellow")
reports_Button.grid(row=0,column=2,padx=10)
#Creación del botón "information_Button", el cuál proporcionará información del fundador de la aplicación
information_Button=Button(master_frame,text="Información",font=("Comic Sans MS",10),bg="black",fg="yellow")
information_Button.grid(row=0,column=3,padx=10)
#Creación del botón "exit_Button" el cúal será el encargado de darle fin a a la ejecución de la aplicación.
exit_Button=Button(master_frame,text=" Salir",font=("Comic Sans MS",10),bg="black",fg="yellow")
exit_Button.grid(row=0,column=4,padx=10)
#============================================================================================================




#============================================================================================================
#Creación del frame donde se muestran todos los items
selection_frame=Frame(root,width="200",height="100")
selection_frame.config(bg="skyblue")
selected_item = StringVar()
item_selector=ttk.Combobox(selection_frame,textvariable=selected_item,values=["0","1","2"],state="readonly",width="20",height="20")
#============================================================================================================




#============================================================================================================
#Creación del frame donde se muestran el proceso
process_frame=Frame(root,width="600",height="400")
process_frame.config(bg="old lace")
process_frame.config(bd="20")
process_frame.config(relief="groove")
process_frame.config(cursor="hand2")
#============================================================================================================








#============================================================================================================
#Creación del frame donde se muestra la tabla de procesos
table_frame=Frame(root,width="600",height="430",padx=0)
table_frame.config(bg="old lace")
table_frame.config(bd="20")
table_frame.config(relief="groove")
table_frame.config(cursor="hand2")
#============================================================================================================




#============================================================================================================
#Función encargada de iniciar la aplicación
def master_mind_window():
    main_frame.destroy()
    principal_Button.destroy()
    root.geometry("1400x600")
    master_frame.grid(row=0,column=10)
    selection_frame.grid(row=0,column=0)
    table_frame.grid(row=1,column=10)
    process_frame.grid(row=1,column=0,padx=50)
#Con este botón inicializamos esta función
principal_Button.config(command=master_mind_window)
#============================================================================================================    



#============================================================================================================
#Función que termina con la ejecución de la aplicación
def exit_application():
    exit()
exit_Button.config(command=exit_application)
#============================================================================================================




#============================================================================================================
#La útlima instrucción de la raíz, ejecutará todo lo que esté arriba de este método
root.mainloop()
#============================================================================================================