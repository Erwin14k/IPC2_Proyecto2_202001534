from Line_Linked_List import Line_Linked_list
from Production_Line import Production_Line
from Line_Linked_List import Line_Components_List
import xml.etree.ElementTree as ET
from Product import Product
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from xml.dom import minidom
import re
import math
from tkinter.filedialog import askopenfilename
from Line_Linked_List import Line_Linked_list
from Product_Linked_List import Product_Linked_List,Elaboration_Linked_List
production_lines_counter=0
line_linked_list_handler = Line_Linked_list()
product_linked_list_handler=Product_Linked_List()
elaboration_handler=Elaboration_Linked_List()
import sys
import os
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
reports_Button=Button(master_frame,text="Reporte HTML",font=("Comic Sans MS",10),bg="black",fg="yellow")
reports_Button.grid(row=0,column=2,padx=10)

graphviz_Button=Button(master_frame,text="Graphviz",font=("Comic Sans MS",10),bg="black",fg="yellow")
graphviz_Button.grid(row=0,column=3,padx=10)
#Creación del botón "information_Button", el cuál proporcionará información del fundador de la aplicación
information_Button=Button(master_frame,text="Información",font=("Comic Sans MS",10),bg="black",fg="yellow")
information_Button.grid(row=0,column=4,padx=10)
#Creación del botón "exit_Button" el cúal será el encargado de darle fin a a la ejecución de la aplicación.
exit_Button=Button(master_frame,text=" Salir",font=("Comic Sans MS",10),bg="black",fg="yellow")
exit_Button.grid(row=0,column=5,padx=10)
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


assemble_product_button=Button(process_frame,text="Ensamblar Producto",font=("Comic Sans MS",10),bg="old lace",fg="MidnightBlue")
assemble_product_button.place(x=210,y=300)


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
    root.geometry("1500x670")
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
#Función para cargar el archivo de máquina
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
    components_counter=0
    bar_counter=0
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
                components_counter+=1
                if components_counter==14 or components_counter==28:
                    components_collected+="\n"
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
            elif f==" ":
                bar_collected+="=>"
                bar_counter+=1
            else:
                if bar_counter==10 or bar_counter==20 or bar_counter==30 or bar_counter==40:
                    bar_collected+="\n"
                state=0
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
def grapviz_creator():
    global item_combobox
    product_name=item_combobox.get()
    text=""
    f = open('bb.dot','w')
    text+="""digraph G {
	subgraph cluster_0 {
		style=filled;
		color=lightgrey;
		node [style=filled,color=white];
		label = "process #1";
	}"""
    text+=product_name+"""->"""
    current2 = elaboration_handler.first
    while current2 and current2.product_name == product_name:
        if current2.product_name == product_name:
            text+=current2.elaboration
            text+="""->"""
            current2=current2.next_one
        else:
            current2=current2.next_one
    text+="""End_Product_Process;
    """+product_name+"""[shape=Mdiamond];
	End_Product_Process [shape=Mdiamond];
    }"""

    
    f.write(text)
    f.close()
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
    os.system('dot -Tpng bb.dot -o grafo2.png')
    os.startfile("grafo2.png")
graphviz_Button.config(command=grapviz_creator)
#============================================================================================================




#============================================================================================================
def machine_file(route):
    global production_lines_counter
    machine_xml=ET.parse(route)
    """machine_xml2=ET.tostring(machine_xml).decode()
    machine_xml2.lower()
    machine_xml=ET.parse(machine_xml2)"""
    machine_xml_rooot = machine_xml.getroot()
    for i in machine_xml_rooot:
        for j in i:
            for number in j.findall('Numero'):
                for components_ammount in j.findall('CantidadComponentes'):
                    for time in j.findall('TiempoEnsamblaje'):
                        temp_line=Production_Line(int(number.text),int(components_ammount.text),int(time.text))
                        line_linked_list_handler.insert_line(temp_line)
    for i in machine_xml_rooot:
            for j in i:
                for name_error in j.findall('nombre'):
                    for elaboration_error in j.findall('elaboracion'):
                        product_name=""
                        product_elaboration=""
                        for a in name_error.text:
                            if re.search('[a-z]', a) or re.search('[A-Z]', a) or a.isdigit() or a==" ":
                                product_name+=a
                        for b in elaboration_error.text:
                            if b=="L" or b=="C" or b.isdigit() or b==" ":
                                product_elaboration+=b
                        temp_product=Product(product_name,product_elaboration)
                        product_linked_list_handler.insert_product(temp_product)
    product_linked_list_handler.product_name_list_collector()
    line_linked_list_handler.travel()
    product_linked_list_handler.travel()
    
#============================================================================================================





def product_assembly():
    global item_combobox
    product_name=""
    product_name=item_combobox.get()
    current=""
    current2=""
    initial_elaboration=""
    temp_name=""
    current = product_linked_list_handler.first
    #Se valida que el producto exista
    while current and current.product.name != product_name:
        current = current.next_one
    #Una vez validado se procede a obtener sus atributos
    temp_name=product_name
    initial_elaboration=current.product.elaboration
    #Con esta variable recolectaremos las líneas utilizadas en n producto
    product_lines=""
    #Con esta variable calcularemos la cantidad de filas en n producto
    product_lines_counter=0
    state=0
    buffer=""
    for g in initial_elaboration:
        if state==0:
            if g=="C":
                buffer+=g
                buffer=""
                    
            elif g=="L":
                state=1
            elif g=="(":
                break
            else:
                buffer+=g
                buffer=""
        if state==1:
            if g=="L" or g.isdigit():
                buffer+=g
            else:
                if product_lines.count(buffer) >=1:
                    buffer=""
                    state=0
                else:
                    product_lines+=buffer
                    product_lines+=","
                    buffer=""
                    state=0
    product_lines_counter=((len(product_lines))/2)-1
    print("Producto: ",product_name,"||","Lineas de producción: ",product_lines,"||","Cantidad de lineas: ",product_lines_counter)
    elaboration_nodes=""
    elaboration_nodes+=initial_elaboration+")"
    state_node=0
    node_buffer=""
    for f in elaboration_nodes:
        if state_node==0:
            if f=="L":
                state_node=1
            elif f==")":
                break
            else:
                node_buffer+=f
                node_buffer=""
        if state_node==1:
            if f =="L" or f.isdigit() or f=="C":
                node_buffer+=f
            else :
                print("hola")
                print(node_buffer)
                elaboration_handler.insert_elaboration(node_buffer,temp_name)
                node_buffer=""
                state_node=0      
    elaboration_handler.travel()
    f = open('REPORTES/Reporte'+product_name+'.html','w')
    assembly_html ="""<html>
    <head></head>
    <body bgcolor=#BF85DD>
    <center>
    <h1>ENSAMBLAJE DEL PRODUCTO:  """+product_name+""" </h1>
    </center>
    <style type="text/css" media="all">
    h1, h2 {display: inline;}
    </style>
    <hr />
    <center>
    <table width="700" border="2" cellpadding="5" >
    <tr>"""
    counter=1
    th_buffer=""
    component_counter=1
    assembly_html +="""<th bgcolor= "#39BBC4" scope="row">SEGUNDO NO.</th>"""
    for a in product_lines :
        if a=="L" or a.isdigit():
            th_buffer+=a
        else:
            assembly_html +="""<th id="""+th_buffer+""" bgcolor= "#39BBC4">"""+th_buffer+"""</th>"""
            th_buffer=""
    assembly_html +="""</tr>"""
    assembly_html+="""
            <tr>
            <td bgcolor= "#38E42F" >"""+str(counter)+"""</td>"""
    for a in product_lines :
        if a=="L" or a.isdigit():
            pass
        else:
            assembly_html +="""<th bgcolor= "#39BBC4">Mover al componente C"""+str(component_counter)+"""</th>"""

    current2 = elaboration_handler.first
    actual_component=1
    line_number=""
    while current2 !=None :
        print("que pasa aquí?")
        if current2.product_name == temp_name:
            print("empezamos el recorrido")
            sentinel=False
            state_elaboration=0
            component_assembly=""
            for c in current2.elaboration:
                if state_elaboration==0:
                    if c =="C":
                        state_elaboration=1
                    else:
                        component_assembly+=c
                        component_assembly=""
                if state_elaboration==1:
                    if c =="C":
                        component_assembly+=c
                        component_assembly=""
                    elif c.isdigit():
                        component_assembly+=c
                    else:
                        state_elaboration=0
            #Buscamos el tiempo de ensamblaje en base al número de línea
            for c in current2.elaboration:
                if state_elaboration==0:
                    if c =="L":
                        state_elaboration=1
                if state_elaboration==1:
                    if c =="L":
                        line_number+=c
                        line_number=""
                    elif c.isdigit():
                        line_number+=c
                    else:
                        break
            assembly_time=line_linked_list_handler.time_by_line(int(line_number))
            print("llegamos a este while")
            while sentinel==False:
                if int(component_assembly)>actual_component:
                    actual_component+=1
                    counter+=1
                    assembly_html +="""<tr>
                    <td bgcolor= "#38E42F" >"""+str(counter)+"""</td><td bgcolor= "#EAC325">MOVER AL COMPONENTE C"""+str(actual_component)+"""</td></tr>"""
                elif int(component_assembly) < actual_component:
                    actual_component-=1
                    counter+=1
                    assembly_html +="""<tr><td bgcolor= "#38E42F" >"""+str(counter)+"""</td><td bgcolor= "#EAC325">MOVER AL COMPONENTE C"""+str(actual_component)+"""</td></tr>"""
                elif int(component_assembly) == actual_component:
                    sentinel=True
                    for h in range(int(assembly_time)):
                        counter+=1
                        assembly_html +="""<tr><td bgcolor= "#38E42F" >"""+str(counter)+"""</td><td bgcolor= "#23B6EF">ENSAMBLAR COMPONENTE  """+str(current2.elaboration)+"""</td></tr>"""
            current2 = current2.next_one
        else:
            current2 = current2.next_one
    
    assembly_html+="""
    </table>
    </body>
    </html>"""
    f.write(assembly_html)
    f.close()
    messagebox.showinfo(title="Digital Intelligence V1.0",message="El Producto: "+product_name+" Ha sido ensamblado con éxito!!")

assemble_product_button.config(command=product_assembly)
#===========================================================================================================

#============================================================================================================
#Función para cargar el archivo de máquina
def simulation_upload_file():
    route2 = askopenfilename()
    if route2.endswith("xml"):
        archive = open(route2,"r")
        archive.close()
        messagebox.showinfo(title="Digital Intelligence V1.0",message="El archivo de Simulación fue cargado con éxito al sistema!!")
        simulation_file(route2)
    else:
        messagebox.showerror(title="Digital Intelligence V1.0",message="No es un archivo con extensión 'xml', intenta de nuevo!!")
        machine_upload_file()
    
simulation_upload_Button.config(command=simulation_upload_file)
#============================================================================================================





#============================================================================================================
def simulation_file(route):

    simulation_xml=ET.parse(route)
    simulation_xml_rooot = simulation_xml.getroot()
    simulation_name=""
    show_text=""
    show_text+="La simulación con los productos: \n"
    for x in simulation_xml_rooot:
        if len(x.text)>=3:
            simulation_name=x.text
            print(simulation_name)
        for j in x:                
            show_text+="--"+j.text+"\n"
    show_text+="Comenzará en breve!!!!!"
    messagebox.showinfo(title="Digital Intelligence V1.0",message=show_text)
    for x in simulation_xml_rooot:
        for j in x:                
            product_assembly_2(j.text,simulation_name)
    
#============================================================================================================



def product_assembly_2(name,simulation_name):
    product_name=""
    product_name=name
    current=""
    current2=""
    initial_elaboration=""
    temp_name=""
    current = product_linked_list_handler.first
    #Se valida que el producto exista
    while current and current.product.name != product_name:
        current = current.next_one
    #Una vez validado se procede a obtener sus atributos
    temp_name=product_name
    initial_elaboration=current.product.elaboration
    #Con esta variable recolectaremos las líneas utilizadas en n producto
    product_lines=""
    #Con esta variable calcularemos la cantidad de filas en n producto
    product_lines_counter=0
    state=0
    buffer=""
    for g in initial_elaboration:
        if state==0:
            if g=="C":
                buffer+=g
                buffer=""
                    
            elif g=="L":
                state=1
            elif g=="(":
                break
            else:
                buffer+=g
                buffer=""
        if state==1:
            if g=="L" or g.isdigit():
                buffer+=g
            else:
                if product_lines.count(buffer) >=1:
                    buffer=""
                    state=0
                else:
                    product_lines+=buffer
                    product_lines+=","
                    buffer=""
                    state=0
    product_lines_counter=((len(product_lines))/2)-1
    print("Producto: ",product_name,"||","Lineas de producción: ",product_lines,"||","Cantidad de lineas: ",product_lines_counter)
    """elaboration_nodes=""
    elaboration_nodes+=initial_elaboration+")"
    state_node=0
    node_buffer=""
    for f in elaboration_nodes:
        if state_node==0:
            if f=="L":
                state_node=1
            elif f==")":
                break
            else:
                node_buffer+=f
                node_buffer=""
        if state_node==1:
            if f =="L" or f.isdigit() or f=="C":
                node_buffer+=f
            else :
                print("hola")
                print(node_buffer)
                elaboration_handler.insert_elaboration(node_buffer,temp_name)
                node_buffer=""
                state_node=0      
    elaboration_handler.travel()"""
    f = open('REPORTES/SIMULACION'+product_name+'.html','w')
    assembly_html ="""<html>
    <head></head>
    <body bgcolor=#BF85DD>
    <center>
    <h1>ENSAMBLAJE DEL PRODUCTO:  """+product_name+""" </h1>
    </center>
    <style type="text/css" media="all">
    h1, h2 {display: inline;}
    </style>
    <hr />
    <center>
    <table width="700" border="2" cellpadding="5" >
    <tr>"""
    counter=1
    th_buffer=""
    component_counter=1
    assembly_html +="""<th bgcolor= "#39BBC4" scope="row">SEGUNDO NO.</th>"""
    for a in product_lines :
        if a=="L" or a.isdigit():
            th_buffer+=a
        else:
            assembly_html +="""<th id="""+th_buffer+""" bgcolor= "#39BBC4">"""+th_buffer+"""</th>"""
            th_buffer=""
    assembly_html +="""</tr>"""
    assembly_html+="""
            <tr>
            <td bgcolor= "#38E42F" >"""+str(counter)+"""</td>"""
    for a in product_lines :
        if a=="L" or a.isdigit():
            pass
        else:
            assembly_html +="""<th bgcolor= "#39BBC4">Mover al componente C"""+str(component_counter)+"""</th>"""

    current2 = elaboration_handler.first
    actual_component=1
    line_number=""
    while current2 !=None :
        print("que pasa aquí?")
        if current2.product_name == temp_name:
            print("empezamos el recorrido")
            sentinel=False
            state_elaboration=0
            component_assembly=""
            for c in current2.elaboration:
                if state_elaboration==0:
                    if c =="C":
                        state_elaboration=1
                    else:
                        component_assembly+=c
                        component_assembly=""
                if state_elaboration==1:
                    if c =="C":
                        component_assembly+=c
                        component_assembly=""
                    elif c.isdigit():
                        component_assembly+=c
                    else:
                        state_elaboration=0
            #Buscamos el tiempo de ensamblaje en base al número de línea
            for c in current2.elaboration:
                if state_elaboration==0:
                    if c =="L":
                        state_elaboration=1
                if state_elaboration==1:
                    if c =="L":
                        line_number+=c
                        line_number=""
                    elif c.isdigit():
                        line_number+=c
                    else:
                        break
            assembly_time=line_linked_list_handler.time_by_line(int(line_number))
            print("llegamos a este while")
            while sentinel==False:
                if int(component_assembly)>actual_component:
                    actual_component+=1
                    counter+=1
                    assembly_html +="""<tr>
                    <td bgcolor= "#38E42F" >"""+str(counter)+"""</td><td bgcolor= "#EAC325">MOVER AL COMPONENTE C"""+str(actual_component)+"""</td></tr>"""
                elif int(component_assembly) < actual_component:
                    actual_component-=1
                    counter+=1
                    assembly_html +="""<tr><td bgcolor= "#38E42F" >"""+str(counter)+"""</td><td bgcolor= "#EAC325">MOVER AL COMPONENTE C"""+str(actual_component)+"""</td></tr>"""
                elif int(component_assembly) == actual_component:
                    sentinel=True
                    for h in range(int(assembly_time)):
                        counter+=1
                        assembly_html +="""<tr><td bgcolor= "#38E42F" >"""+str(counter)+"""</td><td bgcolor= "#23B6EF">ENSAMBLAR COMPONENTE  """+str(current2.elaboration)+"""</td></tr>"""
            current2 = current2.next_one
        else:
            current2 = current2.next_one
    
    assembly_html+="""
    </table>
    </body>
    </html>"""
    f.write(assembly_html)
    f.close()
    xml_creator(product_name,simulation_name,counter)
    messagebox.showinfo(title="Digital Intelligence V1.0",message="El Producto: "+product_name+" Ha sido ensamblado con éxito!!")






def xml_creator(name,simulation_name,time):
        route="SALIDAS/salidaSimulacion"+name+".xml" 
        s="Reporte XML\n"
        exits= ET.Element("SalidaSimulacion")
        sim_name= ET.SubElement(exits,"Nombre")
        sim_name.text=simulation_name
        product_list=ET.SubElement(exits,"ListadoProductos")
        product=ET.SubElement(product_list,"Producto")
        product_name=ET.SubElement(product,"Nombre")
        product_name.text=name
        time_total= ET.SubElement(product,"Tiempo")
        time_total.set("noSegundo",str(time))
        mydata= ET.tostring(exits)
        mydata=str(mydata)
        tree=ET.ElementTree(exits)
        tree.write(route,encoding="UTF-8",xml_declaration=True)












#La útlma instrucción de la raíz, ejecutará todo lo que esté arriba de este método
root.mainloop()
#===========================================================================================================