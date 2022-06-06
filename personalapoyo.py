from personal import Personal
class PersonaldeApoyo(Personal):
    __categoria=''
    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra,area,tipoInvestigacion,categoria,categoriaIncentivo='',extra=0.0):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra,area,tipoInvestigacion,categoria,categoriaIncentivo,extra)
        self.__categoria=categoria
    def getSueldo(self):
        return super().getSueldo()
    def getNombre(self):
        return super().getNombre()
    def getApellido(self):
        return super().getApellido()
    def getCaategoria(self):
        return self.__categoria
    def getCuil(self):
        return super().getCuil()
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldo=self.getSueldo(),
                antiguedad=self.getAntiguedad(),
                categoria=self.__categoria
                )
                )
        return d
