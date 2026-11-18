class Documento:
    def __init__(self, nombre, apellido_materno, apellido_paterno, fecha_nacimiento, ubigeo, ciudad):
        self.nombre = nombre
        self.apellido_materno = apellido_materno
        self.apellido_paterno = apellido_paterno
        self.fecha_nacimiento = fecha_nacimiento
        self.ubigeo = ubigeo
        self.ciudad = ciudad

    def mostrar_informacion(self):
        print(f"Información del documento: {self.nombre} {self.apellido_paterno} {self.apellido_materno}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Ubigeo: {self.ubigeo}")
        print(f"Ciudad: {self.ciudad}")

    def actualizar_ubigeo(self, nuevo_ubigeo):
        self.ubigeo = nuevo_ubigeo

    def actualizar_ciudad(self, nueva_ciudad):
        self.ciudad = nueva_ciudad

    def retornar_edad(self, actual_year):
        birth_year = int(self.fecha_nacimiento.split('-')[0])
        return actual_year - birth_year

henry = Documento("Henry", "Ayala", "Vega", "1993-11-21", "150101", "Lima")
henry.mostrar_informacion()
henry.actualizar_ubigeo("150102")
henry.mostrar_informacion()
henry.actualizar_ciudad("Arequipa")
henry.retornar_edad(2026)
henry.mostrar_informacion()