class Personal:
    __cuil=''
    __apellido=''
    __nombre=''
    __sueldoBasico=0.0
    __antiguedad=0
    def __init__(self,cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra,area,tipoInvestigacion,categoria,categoriaIncentivo,extra):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldoBasico=sueldoBasico
        self.__antiguedad=antiguedad
    def getAntiguedad(self):
        return self.__antiguedad
    def getSueldo(self):
        return self.__sueldoBasico
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def __str__(self):
        return ('cuil:{}\napellido:{}\nnombre:{}\nsueldo basico:{}\nantiguedad:{}'.format(self.__cuil,self.__apellido,self.__nombre,self.__sueldoBasico,self.__antiguedad))
    def getCuil(self):
        return self.__cuil
