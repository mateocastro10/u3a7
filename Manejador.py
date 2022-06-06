from docente import Docente
from docenteinvestigador import DocenteInvestigador
from investigador import Investigador
from nodo import Nodo
from personalapoyo import PersonaldeApoyo
class Manejador:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def insertarElemento(self,posicion,elemento):
        aux=self.__comienzo
        band=True
        j=0
        nodo = Nodo(elemento)
        if(posicion==0):
            nodo.setSiguiente(aux)
            self.__comienzo=nodo
            self.__actual=nodo
            self.__tope+=1
            print('Insertado al comienzo!')
        else:
            while(band):
                if(j==posicion):
                    nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(nodo)
                    band=False
                    print('insertado')
                aux=aux.getSiguiente()
                j+=1
    def agregarElemento(self,elemento):
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def mostrarElemento(self):
        id=int(input('Ingrese posicion de el elemento que desea encontrar:'))
        aux = self.__comienzo
        i=1
        while aux!=None:
            if(i==id):
                print(aux.getDato())
                aux=None
            else:
                i+=1
                aux=aux.getSiguiente()
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            personales=[personal.toJSON() for personal in self]
            )
        return d
    def punto1(self):
        a=input('ingrese cuil:')
        b=input('ingrese apellido:')
        c=input('ingrese nombre:')
        d=input('ingrese sueldoBasico:')
        e=input('ingrese antiguedad:')
        f=input('ingrese carrera:')
        g=input('ingrese cargo')
        h=input('ingrese catedra:')
        undocente=Docente(a,b,c,d,e,f,g,h)
        pos=int(input('ingrese posicion:'))
        self.insertarElemento(pos,undocente)
    def punto2(self):
        op=input('Que desea agregar?(1.Docente|2.Investigador|3.Docente investigador|4.Personal de apoyo)')
        a=input('ingrese cuil:')
        b=input('ingrese apellido:')
        c=input('ingrese nombre:')
        d=input('ingrese sueldoBasico:')
        e=input('ingrese antiguedad:')
        if(op=='1'):
            f=input('ingrese carrera:')
            g=input('ingrese cargo')
            h=input('ingrese catedra:')
            unpersonal=Docente(a,b,c,d,e,f,g,h)
        elif(op=='2'):
            f=input('ingrese area:')
            g=input('ingrese tipo de investigacion')
            unpersonal=Investigador(a,b,c,d,e,'','','',f,g)
        elif(op=='3'):
            f=input('ingrese carrera:')
            g=input('ingrese cargo')
            h=input('ingrese catedra:')
            i=input('ingrese area:')
            j=input('ingrese tipo de investigacion')
            k=input('ingrese Incentivo(I,II,II): ')
            l=float(input('ingrese sueldo extra:'))
            unpersonal=DocenteInvestigador(a,b,c,d,e,f,g,h,i,j,'',k,l)
        elif(op=='4'):
            f=input('ingrese categoria:')
            unpersonal=PersonaldeApoyo(a,b,c,d,e,'','','','','',f)
    def punto3(self):
        self.mostrarElemento()
    def punto4(self):
        lista=[]
        elemento=input('Ingrese nombre de una carrera:')
        for i in self:
            if(type(i)==DocenteInvestigador and i.getCarrera().lower()==elemento):
                lista.append(i)
        lista.sort()
        for i in lista:
            print(i.getNombre())
    def punto5(self):
        j=0
        k=0
        elemento=input('Ingrese area de investigacion:')
        for i in self:
            if(type(i)==Investigador):
                j+=1
            if(type(i)==DocenteInvestigador):
                k+=1
        print('la cantidad de Investigadores son:{}\nla cantidad de Docentes Investigadores son:{}'.format(j,k))
    def sueldodocente(self,i):
        sueldo= i.getSueldo()
        cargo= i.getCargo().lower()
        antiguedad=i.getAntiguedad()
        sueldo=sueldo+(sueldo*antiguedad/100)
        if(cargo == 'simple'):
            sueldo=sueldo+(sueldo+10/100)
        if(cargo == 'semiexclusivo'):
            sueldo=sueldo+(sueldo+20/100)
        if(cargo == 'exclusivo'):
            sueldo=sueldo+(sueldo+50/100)
        return sueldo
    def sueldoInvestigador(self,i):
        sueldo= i.getSueldo()
        antiguedad=i.getAntiguedad()
        sueldo=sueldo+(sueldo*antiguedad/100)
    def sueldopersonal(self,i):
        sueldo= i.getSueldo()
        cat= i.getCategoria()
        antiguedad=i.getAntiguedad()
        sueldo=sueldo+(sueldo*antiguedad/100)
        if(cat<=10 and cat>1):
            sueldo=sueldo+(sueldo+10/100)
        if(cat>=11 and cat<=20):
            sueldo=sueldo+(sueldo+20/100)
        if(cat>=21 and cat<=22):
            sueldo=sueldo+(sueldo+30/100)
        return sueldo
    def punto6(self):
        self.sort()
        for i in self:
            if(type(i)==Docente):
                sueldo=self.sueldodocente(i)
            if(type(i)==Investigador):
                sueldo=self.sueldoInvestigador(i)
            if(type(i)==PersonaldeApoyo):
                sueldo=self.sueldopersonal(i)
            print('nombre:{} apellido:{}\n tipo:{}\sueldo:{}'.format(i.getNombre(),i.getApellido(),i.getTipo(),sueldo))
    def punto7(self):
        extra=0
        cat=input('ingrese categoria(I,II,III,IV):')
        for i in self:
            if(type(i)==DocenteInvestigador and cat==i.getCategoria()):
                print('apellido:{} nombre:{} extra={}'.format(i.getApellido(),i.getNombre(),i.getExtra()))
                extra+=i.getExtra()
