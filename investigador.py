from personal import Personal
class Investigador(Personal):
    __area=''
    __tipoInvestigacion=''
    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera='', cargo='', catedra='',area='',tipoInvestigacion='',categoria='',categoriaIncentivo='',extra=''):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra,area,tipoInvestigacion,categoria,categoriaIncentivo,extra)
        self.__area=area
        self.__tipoInvestigacion=tipoInvestigacion
    def getApellido(self):
        return super().getApellido()
    def getTipo(self):
        return self.__tipoInvestigacion
    def getArea(self):
        return self.__area
    def getSueldo(self):
        return super().getSueldo()
    def getCuil(self):
        return super().getNombre()
    def getCuil(self):
        return super().getCuil()
    def __str__(self):
        print('area de investigacion:{}\ntipo de investigacion:{}'.format(self.__area,self.__tipoInvestigacion))
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
                area=self.__area,
                tipoInvestigacion=self.__tipoInvestigacion
                )
                )
        return d
