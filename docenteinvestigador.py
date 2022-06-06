from docente import Docente
from investigador import Investigador
class DocenteInvestigador(Docente,Investigador):
    __categoriaIncentivo=''
    __extra=0.0
    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra,area,tipoInvestigacion,categoriaIncentivo,extra):
        #Docente.__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo,catedra)
        #Investigador.__init__(cuil, apellido, nombre, sueldoBasico, antiguedad,area, tipoInvestigacion)
        super().__init__( cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra,area,tipoInvestigacion)
        self.__categoriaIncentivo=categoriaIncentivo
        self.__extra=extra
    def getExtra(self):
        return self.__extra
    def getApellido(self):
        return super().getApellido()
    def getCategoria(self):
        return self.__categoriaIncentivo
    def getCargo(self):
        return Docente.getCargo()
    def getCarrera(self):
        return Docente.getCarrera()
    def getNombre():
        return super().getNombre()
    def getCuil(self):
        return super().getCuil()
    def __lt__(self,elemento):
        resultado=False
        if(self.getNombre()>elemento.getNombre()):
            resultado=True
        return resultado
    def getSueldo(self):
        return  super().getSueldo()
    def __str__(self):
        print('categoria:{}\n sueldo extra:{}'.format(self.__categoríaIncentivo,self.__extra))
        return super().__str__()
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                cuil=super().getCuil(),
                apellido=self.getApellido(),
                nombre=super().getNombre(),
                sueldo=super().getSueldo(),
                antiguedad=super().getAntiguedad(),
                cargo=super().getCargo(),
                catedra=super().getCatedra(),
                area=super().getArea(),
                tipoInvestigacion=super().getTipo(),
                categoriaInventivo=self.__categoriaIncentivo,
                extra=self.__extra
                )
                )
        return d
