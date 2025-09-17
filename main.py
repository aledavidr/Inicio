
from ast import Return
from errno import EEXIST
from logging import exception
from tempfile import tempdir
from tkinter import E, EXCEPTION
from turtle import color
from typing import Literal
from fastapi import FastAPI
from xml.dom import minidom
from fastapi.responses import FileResponse

from PIL import Image, ImageFont, ImageDraw
app = FastAPI()
@app.get ('/pr')
async def pr(nombre: str,nombreb: str,enc_id: str):
    try:
        doc = minidom.parse("./xml/" + enc_id +  ".xml")  
        cf1=0   
        cf2=0   
        cf3=0   
       
        fuente = leevalorxml("font",doc)
        tamanio = leevalorxml("tamanio",doc)
        scf1 = leevalorxml("cf1",doc)
        scf2 = leevalorxml("cf2",doc)
        scf3 = leevalorxml("cf3",doc)
        ejex = leevalorxml("x",doc)
        ejey = leevalorxml("y",doc)
        titulo1 = leevalorxml("titulo",doc)
        titulo2 = leevalorxml("titulo2",doc)
        fmayusculas = leevalorxml("forzarmayusculas",doc)       
        
        cf1=string_to_int(scf1) 
        cf2=string_to_int(scf2) 
        cf3=string_to_int(scf3) 
        
        espacios = 24-len(nombre) 
                
        my_image = Image.open("./imagenes/" + enc_id  +  ".jpg")    
                
        title_font = ImageFont.truetype('./fuentes/' + fuente + '.ttf', int(tamanio))   
        title_text = nombre     

        title_text = nombre.center(espacios) + '\n' +  titulo1 + '\n' + titulo2          

        if enc_id =='35' or enc_id =='36':
            espacios = espacios - 5  
            title_text = nombre.center(espacios) + '\n' +  titulo1 + '\n' +  titulo2 + '\n' + nombreb + '?'  

        if enc_id =='27' or enc_id =='31':  
            nombreb=''
            nombre = nombre + ','
            espacios = espacios -4
            title_text = nombre.center(espacios) +  '\n' +  titulo1 + '\n' +  titulo2 + '\n' + nombreb    


        if fmayusculas=='-1':   
            title_text= title_text.upper()  


        image_editable = ImageDraw.Draw(my_image)   
        if enc_id == 33 or enc_id == 34:    
            title_text=''   
        else:   
            image_editable.text((int(ejex) ,int(ejey)), title_text   , (cf1,cf2,cf3), font=title_font,align='center')   
            my_image.save("./imagenes/result.jpg")  
    
        return FileResponse ("./imagenes/result.jpg")
    except FileNotFoundError as e:
        return ('error el cuento '+ str(enc_id) + '  no existe')

def string_to_int(s):
    try:
        temp = int(eval(str(s)))
        if type(temp) == int:
            return temp
    except:
        return
def leevalorxml(campo, sdoc):
    dato = sdoc.getElementsByTagName(campo)[0]  
    tmp = dato.firstChild.data  
    return tmp

