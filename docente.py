from personal import Personal
class Docente(Personal):
    __carrera=''
    __cargo=''
    __catedra=''
    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra,area='',tipoInvestigacion='',categoria='',categoriaIncentivo='',extra=0.0):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra,area,tipoInvestigacion,categoria,categoriaIncentivo,extra)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
    def getCatedra(self):
        return self.__catedra
    def getCuil(self):
        super().getCuil()
    def getAntiguedad(self):
        super().getAntiguedad()
    def getCargo(self):
        return self.__cargo
    def getSueldo(self):
        return super().getSueldo()
    def getNombre(self):
        return super().getNombre()
    def getApellido(self):
        return super().getApellido()
    def getCarrera(self):
        return self.__carrera
    def __str__(self):
        print('carrera:{} cargo:{} catedra:{}'.format(self.__carrera,self.__cargo,self.__catedra))
        return super().__str__()
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldo=self.getSueldo(),
                antiguedad=self.getAntiguedad(),
                cargo=self.__cargo,
                catedra=self.__catedra
                )
                )
        return d
