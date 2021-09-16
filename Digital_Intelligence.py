from Line_Linked_List import Line_Linked_list
from Production_Line import Production_Line
from Product import Product
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from xml.dom import minidom
import re
from tkinter.filedialog import askopenfilename
from Line_Linked_List import Line_Linked_list
from Product_Linked_List import Product_Linked_List
production_lines_counter=0
line_linked_list_handler = Line_Linked_list()
product_linked_list_handler=Product_Linked_List()

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
item_combobox=Combobox(selection_frame,width="50",state="readonly")
item_combobox.grid(row=0,column=0)
product_search_button=Button(selection_frame,text="Buscar Producto",font=("Comic Sans MS",10),bg="black",fg="yellow")
product_search_button.grid(row=1,column=0,pady=10)

product_delete_button=Button(selection_frame,text="Vaciar datos",font=("Comic Sans MS",10),bg="black",fg="yellow")
product_delete_button.grid(row=2,column=0,pady=10)

#============================================================================================================




#============================================================================================================
#Creación del frame donde se muestran el proceso
process_frame=Frame(root,width="600",height="400")
process_frame.config(bg="MidnightBlue")
process_frame.config(bd="20")
process_frame.config(relief="groove")
process_frame.config(cursor="hand2")
item_name=Label(process_frame,text="Producto:",fg="old lace",font=("Comic Sans MS",30),bg="MidnightBlue").place(x=10,y=20)
item_components=Label(process_frame,text="Componentes:",fg="old lace",font=("Comic Sans MS",30),bg="MidnightBlue").place(x=10,y=100)
item_process=Label(process_frame,text="Bar:",fg="old lace",font=("Comic Sans MS",30),bg="MidnightBlue").place(x=10,y=180)


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
#Función que muestra información del estudiante
def student_information():
    messagebox.showinfo(title="Digital Intelligence V1.0",message="Master Mind: Erwin Vásquez\n IPC2 Sección 'E'\n Proyecto ||")
information_Button.config(command=student_information)
#============================================================================================================


#============================================================================================================
#Función que muestra información del estudiante
def machine_upload_file():
    global item_combobox
    route = askopenfilename()
    if route.endswith("xml"):
        archive = open(route,"r")
        archive.close()
        machine_file(route)
        item_combobox.config(values=product_linked_list_handler.collected_names.split(","))
        messagebox.showinfo(title="Digital Intelligence V1.0",message="El archivo de máquina fue cargado con éxito al sistema!!")
    else:
        messagebox.showerror(title="Digital Intelligence V1.0",message="No es un archivo con extensión 'xml', intenta de nuevo!!")
        machine_upload_file()
    
machine_upload_button.config(command=machine_upload_file)
#============================================================================================================

#============================================================================================================
def machine_file(route):
    global production_lines_counter


    #=============================================PARSEO XML==================================================
    machine_xml = minidom.parse(route)
    #==========================================================================================================

    #===========================================VARIABLES IMPORTANTES==========================================
    products = machine_xml.getElementsByTagName('Producto')
    production_lines_amount=machine_xml.getElementsByTagName('CantidadLineasProduccion')
    production_lines=machine_xml.getElementsByTagName('LineaProduccion')
    production_lines_buffer=""
    #==========================================================================================================

    #==================================NO. LINEAS DE PRODUCCIÓN================================================
    for production_line in production_lines_amount:
        for c in production_line.firstChild.data:
            if c.isdigit():
                production_lines_buffer+=c
    #==========================================================================================================

    #==================================DATOS LINEAS DE PRODUCCIÓN==============================================
    #Variables temporables, que irán almacenando la información de las lineas de producción
    #Posteriormente estos datos se almacenarán en la lista enlazada.
    production_line_number=""
    production_line_component=""
    production_line_time=""
    #Ciclo donde de manera rápida se recorre el arreglo de las lineas de producción
    for production_line in production_lines:
        production_line_number= production_line.getElementsByTagName("Numero")[0].childNodes[0].data
        production_line_component=production_line.getElementsByTagName("CantidadComponentes")[0].childNodes[0].data
        production_line_time=production_line.getElementsByTagName("TiempoEnsamblaje")[0].childNodes[0].data
        #Variable temporal donde se guardarán los datos escenciales de la linea de producción actual
        temp_line=Production_Line(int(production_line_number),int(production_line_component),int(production_line_time))
        #Inserción de un nuevo nodo a la lista enlazada de lineas de producción
        line_linked_list_handler.insert_line(temp_line)
    #==========================================================================================================


    #========================================DATOS PRODUCTOS===================================================
    #Ciclo donde de manera rápida se recorre el arreglo de los productos
    #Posteriormente estos datos se almacenarán en la lista enlazada de productos.
    for product in products:
        #Variables temporables, que irán almacenando la información de los productos
        product_name=""
        product_elaboration=""
        name_error= product.getElementsByTagName("nombre")[0].childNodes[0].data
        elaboration_error=product.getElementsByTagName("elaboracion")[0].childNodes[0].data
        for a in name_error:
            if re.search('[a-z]', a) or re.search('[A-Z]', a) or a.isdigit() or a==" ":
                product_name+=a
        for b in elaboration_error:
            if re.search('[a-z]', b) or re.search('[A-Z]', b) or b.isdigit() or b==" ":
                product_elaboration+=b
        #Variable temporal donde se guardarán los datos escenciales de la linea de producción actual
        temp_product=Product(product_name,product_elaboration)
        #Inserción de un nuevo nodo a la lista enlazada de lineas de producción
        product_linked_list_handler.insert_product(temp_product)
    #==========================================================================================================
    production_lines_counter=int(production_lines_buffer)
    print("Lineas de producción:",production_lines_counter)
    line_linked_list_handler.travel()
    print("")
    product_linked_list_handler.travel()
    product_linked_list_handler.product_name_list_collector()
    #============================================================================================================

#============================================================================================================
bar=StringVar()
name=StringVar()
components=StringVar()
def product_information():

    global item_combobox,name,bar,components
    temp_components=""
    temp_bar=""
    
    components_collected=""
    bar_collected=""
    state=0
    state_=0
    buffer=""
    name.set(item_combobox.get())
    temp_bar=product_linked_list_handler.product_elaboration(item_combobox.get())
    temp_components=product_linked_list_handler.product_component(item_combobox.get())
    temp_components.replace(" ",",")
    temp_components+="("
    temp_bar+="("

    

    for g in temp_components:
        if state==0:
            if g=="C":
                state=1
            elif g=="L":
                buffer+=g
                buffer=""
            elif g=="(":
                break
        if state==1:
            if g=="C" or g.isdigit() or g==",":
                components_collected+=g
            else:
                components_collected+=","
                state=0
    for f in temp_bar:
        if state_==0:
            if f=="L":
                state_=1
            elif f=="(":
                break
        if state_==1:
            if f =="L" or f.isdigit() or f=="C":
                bar_collected+=f
            else:
                bar_collected+="=>"
                state_=0
    bar.set(bar_collected)
    components.set(components_collected)
    Label(process_frame,textvariable=name,fg="old lace",font=("Comic Sans MS",30),bg="MidnightBlue").place(x=200,y=20)
    Label(process_frame,textvariable=components,fg="old lace",font=("Comic Sans MS",10),bg="MidnightBlue").place(x=270,y=140)
    Label(process_frame,textvariable=bar,fg="old lace",font=("Comic Sans MS",10),bg="MidnightBlue").place(x=100,y=220)



product_search_button.config(command=product_information)


#============================================================================================================



#============================================================================================================
def delete_information():
    global name,components,bar
    name.set("")
    bar.set("")
    components.set("")

product_delete_button.config(command=delete_information)
#============================================================================================================




#============================================================================================================
#La útlima instrucción de la raíz, ejecutará todo lo que esté arriba de este método
root.mainloop()
#============================================================================================================