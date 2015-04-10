"""
Tienda de gadgets 
Informatica VI 
David Vazquez Sanchez
Grupo: 2296

"""
import cPickle # biblioteca que seializa datos

# se declara la clase de los nodos
class Nodo:
    def __init__(self):
        self.id = 0
        self.name = None
        self.description = None
        self.price = 0
        self.next = None
#  Aqui va la clase estructura la cual incluye todos los metodos que  dan la funcionalidad.
class Lista:
    def __init__(self):
        self.root = Nodo()

#agrega un nodo a la lista
    def add(self,nodo):
        if self.root.id == 0 :
            self.root = nodo

        else :
             aux = self.root
             while True :
                if aux.next == None:
                    aux.next = nodo
                    break
                else :
                    aux = aux.next   



#consulta los datos que  se capturan en memoria principal                            
    def  consult(self):
        aux = self.root
        if aux.id == 0:
             print "Lista vacia"
        else :
            print aux.id
            print aux.name
            print aux.description
            print aux.price
            while aux.next != None:
                aux = aux.next
                print aux.id
                print aux.name
                print aux.description
                print aux.price 

#Cambia  datos de nodos que ya existen se puede apreciar los cambios en la serializacion.
    def change(self):
        aux = self.root
        aux2 = self.root
        if aux.id == 0:
            print "No hay elementos que se desen cambiar"
        else:
            element = input("Escribe el id a cambiar: ")
            if aux.id == element :
                if aux.next == None:
                    self.root = Nodo()
                    nodo = Nodo()
                    nodo.id = input("Escribe el nuevo id: ")
                    nodo.name = raw_input("Escribe el  nuevo nombre del producto: ")
                    nodo.description = raw_input("Escribe  la nueva breve descripcion del producto: ")
                    nodo.price = input("Escribe el nuevo precio: $ ")
                    if self.root.id == 0 :
                       self.root = nodo
                    else :
                       aux = self.root  
                       while True :
                             if aux.next == None:
                                 aux.next = nodo
                                 break
                             else :
                                 aux = aux.next    


                    
                else :
                    self.root = aux.next
                    
            else:
                t = True
                while aux.next != None and t:
                    aux = aux.next
                    if aux.id == element :
                        aux2.next = aux.next
                        aux = None
                        t = False
                        break
                    aux2 = aux2.next
                if t==True:
                    print "Id no encontrado" 
                       

# Borra un nodo de la lista
    def delete(self):
        aux = self.root
        aux2 = self.root
        if aux.id == 0:
            print "No hay elementos que se puedan eliminar"
        else:
            element = input("Escribe el id a eliminar: ")
            if aux.id == element :
                if aux.next == None:
                    self.root = Nodo()
                else :
                    self.root = aux.next

                  
            else:
                t = True
                while aux.next != None and t:
                    aux = aux.next
                    if aux.id == element :
                        aux2.next = aux.next
                        aux = None
                        t = False
                        break
                    aux2 = aux2.next
                    
                if t==True:
                    print "Id no encontrado"       


#se declara toda las operaciones  de la clases de mis articulos  que heredan de la clase lista.   
class tablet(Lista):
    
    def maintablet(self,tablet):
         tablet = tablet()
        
         while True:
                 print "***Menu de las Tablets ***"
                 print "1.- Insertar una tablet"
                 print "2.- Consultar una tablet "
                 print "3.- Eliminar una tablet "
                 print "4.- Cambiar una tablet"
                 print "5.- Salir al menu de articulos"
                 print "-----------------------------"
                 try:
                     opcion = input("Elige tu opcion: ")
                     if opcion == 1: 
                          
                          nodo = Nodo()
                          nodo.id = input("Escribe el id: ")
                         
                          nodo.name = raw_input("Escribe el nombre del producto: ")
                          nodo.description = raw_input("Escribe  una breve descripcion del producto: ")
                          nodo.price = input("Escribe el precio: $ ")
                          tablet.add(nodo)
                          outtablet= open('tablets.txt', 'w')# se genera un archivo que serializa los datos que se capturan1
                          cPickle.dump(tablet, outtablet)
                          outtablet.close( )
                                             
                     elif opcion == 2:
                          tablet.consult()    
                     elif opcion == 3:
                          tablet.delete()
                          outtablet= open('tablets.txt', 'w')
                          cPickle.dump(tablet, outtablet)
                          outtablet.close( )
                     elif opcion == 4:
                          tablet.change()
                          outtablet= open('tablets.txt', 'w')
                          cPickle.dump(tablet, outtablet)
                          outtablet.close( )     
                     elif opcion == 5:
                          break
                 except Exception as e:
                     print "Ocurrio un error"
                     print e      
                                 


class cell(Lista):
     def maincell(self,cell):
       cell = cell()
       while True:
                 print "***Menu de  los celulare ***"
                 print "1.- Insertar un celular"
                 print "2.- Consultar un celular "
                 print "3.- Eliminar un celular "
                 print "4.- Cambiar datos de un celular"
                 print "5.-Salir al menu de articulos"
                 print "-----------------------------"
                 try:
                     opcion = input("Elige tu opcion: ")
                     if opcion == 1:
                          nodo = Nodo()
                          nodo.id = input("Escribe el id: ")
                          nodo.name = raw_input("Escribe el nombre del producto: ")
                          nodo.description = raw_input("Escribe  una breve descripcion del producto: ")
                          nodo.price = input("Escribe el precio: $ ")
                          cell.add(nodo)
                          outcell= open('cell.txt', 'w')
                          cPickle.dump(cell, outcell)
                          outcell.close( )
                     elif opcion == 2:
                          cell.consult()
                     elif opcion == 3:
                          cell.delete()
                          outcell= open('cell.txt', 'w')
                          cPickle.dump(cell, outcell)
                          outcell.close( )
                     elif opcion == 4:
                          cell.change()
                          outcell= open('cell.txt', 'w')
                          cPickle.dump(cell, outcell)
                          outcell.close( )
                     elif opcion == 5:
                          break     
                 except Exception as e:
                     print "Ocurrio un error"
                     print e  
         
class laptop(Lista):
    def mainlaptop(self,laptop):
      laptop = laptop()
      while True:
                 print "***Menu de  las laptos ***"
                 print "1.- Insertar una laptop"
                 print "2.- Consultar una laptop "
                 print "3.- Eliminar una laptop "
                 print "4.- Cambiar datos de una laptop"
                 print "5.-Salir al menu de articulos"
                 print "-----------------------------"
                 try:
                     opcion = input("Elige tu opcion: ")
                     if opcion == 1:
                          nodo = Nodo()
                          nodo.id = input("Escribe el id: ")
                          nodo.name = raw_input("Escribe el nombre del producto: ")
                          nodo.description = raw_input("Escribe  una breve descripcion del producto: ")
                          nodo.price = input("Escribe el precio: $ ")
                          laptop.add(nodo)
                          outlaptop= open('laptop.txt', 'w')
                          cPickle.dump(cell, outlaptop)
                          outlaptop.close( )
                     elif opcion == 2:
                          laptop.consult()
                     elif opcion == 3:
                          laptop.delete()
                          outlaptop= open('laptop.txt', 'w')
                          cPickle.dump(cell, outlaptop)
                          outlaptop.close( )
                     elif opcion == 4:
                          laptop.change()
                          outlaptop= open('laptop.txt', 'w')
                          cPickle.dump(cell, outlaptop)
                          outlaptop.close( )
                     elif opcion == 5:
                          break     
                 except Exception as e:
                     print "Ocurrio un error"
                     print e       
     


class desktop(Lista): 
     def maindesktop(self,desktop):
       desktop = desktop()
       while True:
                 print "*** Menu de  las Desktop ***"
                 print "1.- Insertar una desktop"
                 print "2.- Consultar una desktop "
                 print "3.- Eliminar una desktop "
                 print "4.- Cambiar los datos de una desktop"
                 print "5.-Salir al menu de articulos"
                 print "-----------------------------"
                 try:
                     opcion = input("Elige tu opcion: ")
                     if opcion == 1:
                          nodo = Nodo()
                          nodo.id = input("Escribe el id: ")
                          nodo.name = raw_input("Escribe el nombre del producto: ")
                          nodo.description = raw_input("Escribe  una breve descripcion del producto: ")
                          nodo.price = input("Escribe el precio: $ ")
                          desktop.add(nodo)
                          outdesktop= open('desktop.txt', 'w')
                          cPickle.dump(cell, outdesktop)
                          outdesktop.close( )
                     elif opcion == 2:
                          desktop.consult()
                     elif opcion == 3:
                          desktop.delete()
                          outdesktop= open('desktop.txt', 'w')
                          cPickle.dump(cell, outdesktop)
                          outdesktop.close( )
                     elif opcion == 4:
                          desktop.change()
                          outdesktop= open('desktop.txt', 'w')
                          cPickle.dump(cell, outdesktop)
                          outdesktop.close( )
                     elif opcion == 5: 
                          break
                 except Exception as e:
                     print "Ocurrio un error"
                     print e       
      


   
                                              
# se crea el menu principal y se llama  las funciones  de las clases de los articulos para que se implementen los menus de cada uno.
class main():

    loop = 1

    while loop == 1:
        print " ***Bienvenido a la tienda de gadgets *** "
        print " ***Tus articulos son: *** "
        print "***************************"
        print "1) Tablet"
        print "2) Celular"
        print "3) Laptop"
        print "4) Desktop"
        print "5) Salir"
        print "***************************"
        choise = input("Seleciona tu opcion: ") 
        choise = int(choise)

        if choise == 1:
            #tablet = tablet
          t =tablet()
          t.maintablet(tablet)

        elif choise == 2:
          c = cell()
          c.maincell(cell)
            
        elif choise == 3:
          l = laptop()
          l.mainlaptop(laptop)
                        
        elif choise == 4:
          d = desktop()
          d.maindesktop(desktop)
                        
        elif choise == 5:
            break              
"""
NOTA:  Hice una serializacion en archivos pero no puedo leer sobre la serializacion
solo se puede escribir y los datos que capturas en memoria si se guardan en el archivo se puede consultar.

"""



        


        
    
        
               
