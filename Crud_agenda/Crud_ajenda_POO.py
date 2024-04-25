import cx_Oracle;
from os import system 
system('cls')

class Agenda(): 
    def __init__(self):
        self.BDconexion1=cx_Oracle.connect(
            user="U1DAVID",
            password="654321",
            dsn="localhost/xe"       
        );
        self.AA = self.BDconexion1.cursor();
        print("\n---------------------------------------------------------")
        print(" . . . . . . Conexion Establecida a la Base de Datos  . . . . . . ")
        print("---------------------------------------------------------\n")
    
    def Menu(self):
        c=0
        while True:
            menu=input('\n:::: Agenda :::: \n[1].Anadir contacto \n[2].Lista de contactos \n[3].Buscar \n[4].Editar \n[5].Eliminar \n[6].Salir \n\nEscoje una opcion: ')
            
            if menu=='1':
                self.anadir()
            elif menu=='2':
                self.listar()
            elif menu=='3':
                self.buscar()
            elif menu=='4':
                self.editar()
            elif menu=='5':
                self.eliminar()
            elif menu=='6':
                self.salir()
            else: 
                print('\n**** Opcion no es valida ****\n')
                c+=1
                if c==4:
                    print(':::::: Superaste el numero de intentos permitidos ::::::\n')
                    break

    def anadir(self):
        try:
            nom=input('Nombre: ').title(); telf=input('Telefono: '); corr=input('Email: ')

            self.AA.execute('''INSERT INTO AjendaDG(Nombre,Telefono,Email)VALUES('{}','{}','{}')'''.format(nom,telf,corr))
            self.BDconexion1.commit()
            print('')
            print('..... Datos insertados .....')

        except Exception:
            print('')
            print('..... Error al grabar los datos .....')
            
    def listar(self):
        self.AA.execute('select * from AjendaDG')
        Busque=self.AA.fetchall()
        print('- - - - - - - - - - - -')
        print(len(Busque),'Contactos guardados')
        print('- - - - - - - - - - - -')
        Busque.sort()

        for i in Busque:
            print('')
            print('Nombre .... : ',i[0])
            print('Telefono .. : ',i[1])
            print('Email ..... : ',i[2])
        
    def buscar(self):
        self.AA.execute('select * from AjendaDG')
        Busque=self.AA.fetchall()
        buscar=input('Buscar nombre: ').title()

        for x in Busque: 
            if buscar in x[0]:
                print('')
                print('Nombre .... : ',x[0])
                print('Telefono .. : ',x[1])
                print('Email ..... : ',x[2])

    def editar(self):
        nomm=input('Buscar nombre: ').title()
        eddit=input('\n¿Que quieres editar? \n[1].Nombre \n[2].Telefono \n[3].Correo \n[4].volver al menu \n\nIngresa una opcion: ')
 
        if eddit=='1':
            try:
                self.AA.execute('select * from AjendaDG')
                Busque=self.AA.fetchall()
                nom=input('Nuevo nombre: ').title()

                for i in Busque:
                    if nomm == i[0]:
                        actualizar=("Update AjendaDG Set NOMBRE = '{}' where NOMBRE = '{}' ")
                        self.AA.execute(actualizar.format(nom,nomm))
                        self.BDconexion1.commit()
                        print('. . . . . . . . . . . . . . . .')
                        print('      Datos actualizados ')
                        print('. . . . . . . . . . . . . . . .')
            except Exception:
                print('')
                print(' Error en la actualizacion de datos')  

        elif eddit=='2':
            try:
                self.AA.execute('select * from AjendaDG')
                Busque=self.AA.fetchall()
                telf=input('Nuevo numero de telefono: ')

                for i in Busque:
                    if nomm == i[0]:
                        actualizar=("Update AjendaDG Set TELEFONO = '{}' where NOMBRE = '{}' ")
                        self.AA.execute(actualizar.format(telf,nomm))
                        self.BDconexion1.commit()
                        print('. . . . . . . . . . . . . . . .')
                        print('      Datos actualizados ')
                        print('. . . . . . . . . . . . . . . .')
            except Exception:
                print('')
                print(' Error en la actualizacion de datos')  
     
        elif eddit=='3':
            try:
                self.AA.execute('select * from AjendaDG')
                Busque=self.AA.fetchall()
                correo=input('Nuevo correo: ')

                for i in Busque:
                    if nomm == i[0]:
                        actualizar=("Update AjendaDG Set EMAIL = '{}' where NOMBRE = '{}' ")
                        self.AA.execute(actualizar.format(correo,nomm))
                        self.BDconexion1.commit()
                        print('. . . . . . . . . . . . . . . .')
                        print('      Datos actualizados ')
                        print('. . . . . . . . . . . . . . . .')
            except Exception:
                print('')
                print(' Error en la actualizacion de datos') 

        elif eddit=='4':
            self.Menu()
        else:
            print('\n**** Opcion no es correcta ****')
        
        
    def eliminar(self):
        try:
            self.AA.execute('select * from AjendaDG')
            Busque=self.AA.fetchall()
            nomm=input('Nombre: ').title()
            for i in Busque: 
                if nomm == i[0]: 
                    self.AA.execute("delete from AjendaDG where Nombre = '"+nomm+ "'" )    
                    self.BDconexion1.commit()
                    print('. . . . . . . . . . . . . . . .')
                    print('      Datos eliminados ')
                    print('. . . . . . . . . . . . . . . .')
        except Exception:
                    print('')
                    print(' Error en la eliminacion de datos ')
                    print('')

    def salir(self):
        print('Saliendo...')
        exit()

Agenda1 = Agenda()    
Agenda1.Menu()

        

