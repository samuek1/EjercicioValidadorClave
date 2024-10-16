from abc import ABC, abstractmethod


class ReglaValidacion(ABC):

    def init(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    @abstractmethod
    def es_valida(self):
        pass

    def _validar_longitud(self, clave):
        count_1 = 0
        for i in clave:
            count_1 += 1

        if count_1 > self._longitud_esperada:
            return True

    def _contiene_mayuscula(self, clave):
        for item in clave:
            if item.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave):
        for item in clave:
            if item.islower():
                return True
        return False

    def _contiene_numero(self, clave):
        for item in clave:
            if item.isdigit():
                return True
        return False


class ReglaValidacionGanimedes(ReglaValidacion):

    def init(self, longitud_esperada: int):
        super().init(longitud_esperada)


    def contiene_caracter_especial(self, clave):
        counter = 0
        for item in clave:
            if item == "@" or "_" or "#" or "$" or "%":
                counter += 1

            if counter >= 1:
                return True
            else:
                return False

    def es_valida(self, clave: str):
        ReglaValidacion._validar_longitud()


class ReglaValidacionCalisto(ReglaValidacion):

    def init(self, longitud_esperada: int):
        super().init(longitud_esperada)

    def contiene_calisto(self, clave):
        if "calisto" in clave.lower():
            counter = 0
            for item in clave:
                if item in "CALISTO":
                    counter += 1

            if 2 <= counter < 7:
                return True

        return False


class Validador:

    def init(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)
