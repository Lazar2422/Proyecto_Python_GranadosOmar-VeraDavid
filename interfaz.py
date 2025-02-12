import json

def abrirJSONr(ruta):
    dicFinal={}
    with open(f"./{ruta}.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(ruta,dic):
    with open(f"./{ruta}.json",'w') as outFile:
        json.dump(dic,outFile)
f=True
perfil={}
while f==True:
    print("Seleccion el perfil")
    print("1 para estudiantes || 2 para trainers || 3 para coordinador || 4 para salir")
    x=int(input(": "))
    if x==1:
        ## funciones de campers
        ## funciones de campers
        ## funciones de campers
        ## funciones de campers
        rta="estudiantes"
        perfil=(abrirJSONr(rta))
        lie=True
        while lie==True:
            ## Interfaz inicio de sesion
            registro=input("1 para iniciar sesión || 2 para registrarse")
            if registro=="1":
                perfil=abrirJSONr(rta)
                nam=input("Ingrese el usuario (nombre): ")
                id=(input("Ingrese su ID: "))
                for i in range (len(perfil[rta])):
                    nome=(perfil[rta][i]["Nombre"])
                    idn=perfil[rta][i]["ID"]
                    if (nam==nome) & (id==idn):
                        tru=True
                        z=i
                        break
                    else:
                        tru=False
                if tru==True:
                    print("Bienvenido/a ", nam)
                    while tru==True:
                        print("Presione 1 para ver tu informacion || 2 para ver tus notas || 3 para salir")
                        inf=int(input(": "))
                        if inf==1:
                            ## informacion del camper
                            ape=perfil[rta][z]["Apellido"]
                            dir=perfil[rta][z]["direccion"]
                            acu=perfil[rta][z]["acudiente"]
                            cel=perfil[rta][z]["celular"]
                            fijo=perfil[rta][z]["fijo"]
                            est=perfil[rta][z]["estado"]
                            ries=perfil[rta][z]["riesgo"]
                            rutaa=perfil[rta][z]["ruta"]
                            print("ID:",id,"Nombre:",nome,"Apellido:",ape,"Direccion:",dir,"Acudiente:",acu,"Celular:",cel,"Telefono fijo:",fijo,"Estado:",est,"Riesgo:",ries,"Ruta:",rutaa)
                        elif inf==2:
                            ## notas del camper
                            rta2="notas"
                            notas={}
                            notas=abrirJSONr(rta2)
                            for i in range (len(notas[rta2])):
                                nombrecito=notas[rta2][i]["Nombre"]
                                if nombrecito==nome:
                                    proyec=notas[rta2][i]["Proyecto"]
                                    filtro=notas[rta2][i]["Filtro"]
                                    traba=notas[rta2][i]["Trabajos"]
                                    print("Nota proyecto:",proyec,"Nota filtro:",filtro,"Nota trabajos.",traba)
                                    break
                        elif inf==3:
                            ## sale de interfaz de usuario y vuelve a seleccionar el perfil
                            tru=False
                            lie=False
            elif registro=="2":
                rta2="estudiantes"
                mostrar={}
                ru=abrirJSONr("rutas")
                mostrar=abrirJSONr(rta2)
                nombe=input("Ingrese el nombre: ")
                ape=input("Ingrese el apellido: ")
                dir=input("Ingrese la direccion: ")
                acu=input("Ingrese el nombre del acudiente: ")
                cel=input("Ingrese el telefono celular: ")
                fijo=input("Ingrese el telefono fijo: ")
                ries="Nulo"
                rutaaa=input("Ingrese la ruta a estudiar: ")
                idd=str((len(mostrar[rta2]))+1)
                print("su ID: ",idd)
                if rutaaa=="1":
                    rutaa="Java"
                elif rutaaa=="2":
                    rutaa="NodeJS"
                elif rutaaa=="3":
                    rutaa=".Net"
                mostrar[rta2].append({"ID":idd,"Nombre":nombe,"Apellido":ape,"direccion":dir,"acudiente":acu,"celular":cel,"fijo":fijo,"estado":"Nuevo ingreso","riesgo":ries,"ruta":rutaa})
                guardarJSON("estudiantes",mostrar)
    elif x==2:
        ## funciones de trainers
        ## funciones de trainers
        ## funciones de trainers
        ## funciones de trainers
        rta="trainers"
        perfil=(abrirJSONr(rta))
        lie=True
        while lie==True:
            nam=input("Ingrese el usuario (nombre): ")
            id=(input("Ingrese su ID: "))
            for i in range (len(perfil[rta])):
                nome=str(perfil[rta][i]["Nombre"])
                idn=perfil[rta][i]["ID"]
                if (nam==nome) & (id==idn):
                    tru=True
                    z=i
                    break
                else:
                    tru=False
            if tru==True:
                print("Bienvenido ", nome)
                while tru==True:
                    print("Que te gustaria hacer?")
                    print("1 para ver tu informaicon || 2 para ver tus grupos || 3 para ver estudiantes || 4 para calificar estudiantes || 5 para salir")
                    inf=int(input(": "))
                    if inf==1:
                        ape=perfil[rta][z]["Apellido"]
                        ruta=perfil[rta][z]["Ruta"]
                        print("ID:",id,"Nombre:", nome,"Apellido:",ape,"Ruta:", ruta)
                    elif inf==3:
                        rta2="estudiantes"
                        mostrar={}
                        mostrar=abrirJSONr(rta2)
                        for i in range (len(mostrar[rta2])):
                            iddd=mostrar[rta2][i]["ID"]
                            nombre=mostrar[rta2][i]["Nombre"]
                            ape=mostrar[rta2][i]["Apellido"]
                            dir=mostrar[rta2][i]["direccion"]
                            acu=mostrar[rta2][i]["acudiente"]
                            cel=mostrar[rta2][i]["celular"]
                            fijo=mostrar[rta2][i]["fijo"]
                            est=mostrar[rta2][i]["estado"]
                            ries=mostrar[rta2][i]["riesgo"]
                            print("Estudiante ",i," ID:",iddd,"Nombre:",nombre,"Apellido:","Direccion:",dir,ape,"Acudiente:",acu,"Celular:",cel,"Telefono fijo:",fijo,"Estado:",est,"Riesgo:",ries)
                    elif inf==5:
                        tru=False
                        lie=False
                    elif inf==4:
                        rta1="notas"
                        notas={}
                        notas=abrirJSONr(rta1)
                        estu=input("Ingrese el ID del estudiante a calificar: ")
                        for i in range(len(notas[rta1])):
                            confirmar=notas[rta1][i]["ID"]
                            if confirmar==estu:
                                for q in range(len(notas[rta1][i]["notas"])):
                                    b=notas[rta1][i]["notas"][q]
                                    print("Presione ",q+1, " para calificar ",b)
                                s=i
                                break
                        nota=(int(input(": ")))
                        match nota:
                            case 1:
                                mod="Intro"
                            case 2:
                                mod="Python"
                            case 3:
                                mod="HTML/CSS"
                            case 4:
                                mod="Scrum"
                            case 5:
                                mod="Git"
                            case 6:
                                mod="JavaScript"
                            case 7:
                                mod="Intro Back"
                            case 8:
                                mod="Intro BBDD"
                            case 9:
                                mod="MySQL"
                            case 10:
                                mod="Java"
                            case 11:
                                mod="PostgreSQL"
                            case 12:
                                mod="SpringBoot"
                        proyec=int(input("Nota del proyecto: "))
                        filtro=int(input("Nota del filtro: "))
                        traba=int(input("Nota del trabajos: "))
                        ## arreglar mod con pedro
                        notas[rta1][s]["notas"][nota][mod][0]["Proyecto"]=proyec
                        notas[rta1][s]["notas"][nota][mod][0]["Filtro"]=filtro
                        notas[rta1][s]["notas"][nota][mod][0]["Trabajos"]=traba
    elif x==3:
        ## funciones de coordinador
        ## funciones de coordinador
        ## funciones de coordinador
        ## funciones de coordinador
        rta="coordinador"
        perfil=(abrirJSONr(rta))
        lie=True
        while lie==True:
            nam=input("Ingrese el usuario (nombre): ")
            id=(input("Ingrese su ID: "))
            for i in range (len(perfil[rta])):
                nome=str(perfil[rta][i]["Nombre"])
                idn=perfil[rta][i]["ID"]
                if (nam==nome) & (id==idn):
                    tru=True
                    z=i
                    break
                else:
                    tru=False
            if tru==True:
                while tru==True:
                    print("Bienvenido/a ", nome)
                    print("Que desea hacer?")
                    print("1 para ver informacion || 2 para editar informacion || 3 para añadir informacion || 4 para grupos || 5 para salir")
                    inf=int(input(": "))
                    if inf==1:
                        print("De cual perfil quiere ver la informacion?")
                        print("1 para camper || 2 para trainers || 3 para coordinadores")
                        infor=int(input(": "))
                        if infor==1:
                            rta2="estudiantes"
                            mostrar={}
                            mostrar=abrirJSONr(rta2)
                            for i in range (len(mostrar[rta2])):
                                iddd=mostrar[rta2][i]["ID"]
                                nombre=mostrar[rta2][i]["Nombre"]
                                ape=mostrar[rta2][i]["Apellido"]
                                dir=mostrar[rta2][i]["direccion"]
                                acu=mostrar[rta2][i]["acudiente"]
                                cel=mostrar[rta2][i]["celular"]
                                fijo=mostrar[rta2][i]["fijo"]
                                est=mostrar[rta2][i]["estado"]
                                ries=mostrar[rta2][i]["riesgo"]
                                print("Estudiante ",i," ID:",iddd,"Nombre:",nombre,"Apellido:","Direccion:",dir,ape,"Acudiente:",acu,"Celular:",cel,"Telefono fijo:",fijo,"Estado:",est,"Riesgo:",ries)
                        if infor==2:
                            rta2="trainers"
                            mostrar={}
                            mostrar=abrirJSONr(rta2)
                            for i in range (len(mostrar[rta2])):
                                iddd=mostrar[rta2][i]["ID"]
                                nombre=mostrar[rta2][i]["Nombre"]
                                ape=mostrar[rta2][i]["Apellido"]
                                rutaa=mostrar[rta2][i]["Ruta"]
                                print("Trainer ",i," ID:", iddd,"Nombre:",nombre,"Apellido:",ape,"Ruta:",rutaa)
                        if infor==3:
                            rta2="coordinador"
                            mostrar={}
                            mostrar=abrirJSONr(rta2)
                            for i in range (len(mostrar[rta2])):
                                iddd=mostrar[rta2][i]["ID"]
                                nombre=mostrar[rta2][i]["Nombre"]
                                print("Coordinador ",i," ID:",iddd,"Nombre:",nombre)
                    elif inf==2:
                        print("De cual perfil quiere editar informacion?")
                        print("1 para camper || 2 para trainers || 3 para coordinadores")
                        infor=int(input(": "))
                        if infor==1:
                            rta2="estudiantes"
                            mostrar={}
                            mostrar=abrirJSONr(rta2)
                            iddd=input("Ingrese el ID del estudiante a editar: ")
                            for i in range (len(mostrar[rta2])):
                                confirmar=mostrar[rta2][i]["ID"]
                                if confirmar==iddd:
                                    nombe=input("Ingrese el nombre: ")
                                    ape=input("Ingrese el apellido: ")
                                    dir=input("Ingrese la direccion: ")
                                    acu=input("Ingrese el nombre del acudiente: ")
                                    cel=input("Ingrese el telefono celular: ")
                                    fijo=input("Ingrese el telefono fijo: ")
                                    estado=input("Ingrese el estado del estudiante: ")
                                    ries=input("Ingrese el riesgo del estudiante: ")
                                    rutaa=input("Ingrese la ruta del estudiante: ")
                                    mostrar[rta2][i]["Nombre"]=nombe
                                    mostrar[rta2][i]["Apellido"]=ape
                                    mostrar[rta2][i]["direccion"]=dir
                                    mostrar[rta2][i]["acudiente"]=acu
                                    mostrar[rta2][i]["celular"]=cel
                                    mostrar[rta2][i]["fijo"]=fijo
                                    mostrar[rta2][i]["estado"]=estado
                                    mostrar[rta2][i]["riesgo"]=ries
                                    mostrar[rta2][i]["Ruta"]=rutaa
                                    guardarJSON(rta2,mostrar)
                        elif infor==2:
                            rta2="trainers"
                            mostrar={}
                            mostrar=abrirJSONr(rta2)
                            iddd=input("Ingrese el ID del trainer a editar: ")
                            for i in range (len(mostrar[rta2])):
                                confirmar=mostrar[rta2][i]["ID"]
                                if confirmar==iddd:
                                    nome=input("Ingrese el nombre: ")
                                    ape=input("Ingrese el apellido: ")
                                    rutaa=input("Ingrese la ruta: ")
                                    mostrar[rta2][i]["Nombre"]=nombe
                                    mostrar[rta2][i]["Apellido"]=ape
                                    mostrar[rta2][i]["Ruta"]=rutaa
                        elif infor==3:
                            rta2="coordinador"
                            mostrar={}
                            mostrar=abrirJSONr(rta2)
                            iddd=input("Ingrese el ID del coordinador a editar: ")
                            for i in range (len(mostrar[rta2])):
                                confirmar=mostrar[rta2][i]["ID"]
                                if confirmar==iddd:
                                    nome=input("Ingrese el nombre: ")
                                    mostrar[rta2][i]["Nombre"]=nome
                    elif inf==3:
                        print("De cual perfil quiere añadir informacion?")
                        print("1 para camper || 2 para trainers || 3 para coordinadores")
                        infor=int(input(": "))
                        if infor==1:
                            rta2="estudiantes"
                            mostrar={}
                            mostrar=abrirJSONr(rta2)
                            nombe=input("Ingrese el nombre: ")
                            ape=input("Ingrese el apellido: ")
                            dir=input("Ingrese la direccion: ")
                            acu=input("Ingrese el nombre del acudiente: ")
                            cel=input("Ingrese el telefono celular: ")
                            fijo=input("Ingrese el telefono fijo: ")
                            estado=input("Ingrese el estado del estudiante: ")
                            ries=input("Ingrese el riesgo del estudiante: ")
                            rutaa=input("Ingrese la ruta del estudiante: ")
                            idd=(len(mostrar[rta2]))+1
                            mostrar[rta2].append({"ID":idd,"Nombre":nombe,"Apellido":ape,"direccion":dir,"acudiente":acu,"celular":cel,"fijo":fijo,"estado":estado,"riesgo":ries,"ruta":rutaa})
                            guardarJSON(rta2,mostrar)
                        if infor==2:
                            rta2="trainers"
                            mostrar={}
                            mostrar=abrirJSONr(rta2)
                            nombe=input("Ingrese el nombre: ")
                            ape=input("Ingrese el apellido: ")
                            rutaa=input("Ingrese la ruta del docente: ")
                            idd=len(mostrar[rta2])+1
                            mostrar[rta2].append({"ID":idd,"Nombre":nombe,"Apellido":ape,"ruta":rutaa})
                            guardarJSON(rta2,mostrar)
                        if infor==3:
                            rta2="coordinador"
                            mostrar={}
                            mostrar=abrirJSONr(rta2)
                            nombe=input("Ingrese el nombre: ")
                            idd=len(mostrar[rta2])+1
                            mostrar[rta2].append({"ID":idd,"Nombre":nombe})
                            guardarJSON(rta2,mostrar)
                    elif inf==4:
                        verdad=True
                        while verdad:
                            rta2="grupo"
                            mostrar={}
                            mostrar=abrirJSONr(rta2)
                            print("Presione 1 para ver la información || 2 para editar || 3 para añadir || 4 para asignar estudiantes || 5 para salir")
                            infor=int(input(": "))
                            if infor==1:
                                for i in range (len(mostrar[rta2])):
                                    salon=mostrar[rta2][i]["salon"]
                                    trainer=mostrar[rta2][i]["trainer"]
                                    horario=mostrar[rta2][i]["horario"]
                                    rutaa=mostrar[rta2][i]["ruta"]
                                    print("Grupo ",i+1," Salon:",salon,"Trainer:",trainer,"Horario:",horario,"Ruta:",rutaa)
                                    print("Estudiantes: ")
                                    for q in range(len(mostrar[rta2][i]["estudiantes"])):
                                        estu=mostrar[rta2][i]["estudiantes"][q]["Nombre"]
                                        print("Estudiante ",i+1," ",estu)
                            elif infor==2:
                                print("Ingrese el numero del grupo a editar")
                                edit=int(input(": "))
                                edic=edit-1
                                nombe=input("Ingrese el nombre del salón asignado: ")
                                trainer=input("Ingrese el nombre del trainer asigando: ")
                                ## debatir el editar estudiante
                                horario=input("Ingrese el numero del horario asignado: ")
                                rutaa=input("Ingrese el numero de la ruta asignada: ")
                                mostrar[rta2][edic]["salon"]=nombe
                                mostrar[rta2][edic]["trainer"]=trainer
                                mostrar[rta2][edic]["horario"]=horario
                                mostrar[rta2][edic]["ruta"]=rutaa
                                guardarJSON(rta2,mostrar)
                            elif infor==3:
                                rta3="salones"
                                salo={}
                                trai=abrirJSONr("trainers")
                                salo=abrirJSONr(rta3)
                                for i in range(len(salo[rta3])):
                                    a=salo[rta3][i]["Nombre"]
                                    print(" 1 para salon",a)
                                nombe=int(input())
                                nombre=salo[rta3][nombe]["Nombre"]
                                train=input("Ingrese el id del trainer: ")
                                for i in range(len(trai["trainers"])):
                                    verificar=trai["trainers"][i]["ID"]
                                    if verificar==train:
                                        trainer=trai["trainers"][i]["Nombre"]
                                horario=input("Ingrese el numero del horario: ")
                                rutaaa=input("Ingrese el numero de la ruta: ")
                                if rutaaa=="1":
                                    rutaa="Java"
                                elif rutaaa=="2":
                                    rutaa="NodeJS"
                                elif rutaaa=="3":
                                    rutaa=".Net"
                                estudiantes=[]
                                mostrar[rta2].append({"salon":nombre,"trainer":trainer,"estudiantes":estudiantes,"horario":horario,"ruta":rutaa})
                                guardarJSON(rta2,mostrar)
                            elif infor==4:
                                sal={}
                                sal=abrirJSONr("grupo")
                                camper={}
                                camper=abrirJSONr("estudiantes")
                                ingreso=input("Ingrese el ID del estudiante a añadir")
                                sa=int(input("Ingrese numero del grupo"))
                                for i in range (len(camper["estudiantes"])):
                                    verificar=camper["estudiantes"][i]["ID"]
                                    if verificar==ingreso:
                                        nombre=camper["estudiantes"][i]["Nombre"]
                                        iden=i-1
                                        añadir=sal["grupo"][iden]["estudiantes"]
                                        añadir.append({"Nombre":nombre})
                                guardarJSON("grupo",sal)
                            elif infor==5:
                                verdad=False
                    elif inf==5:
                        tru=False
                        lie=False
    elif x==4:  
        f=False 