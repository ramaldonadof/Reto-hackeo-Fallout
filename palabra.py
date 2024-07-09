class Palabra:
    
    def __init__(self, palabra: str, coincidencia: int):
        self.palabra = palabra
        self.coincidencia = coincidencia

    @property
    def palabra(self) -> str:
        return self._palabra
    
    @palabra.setter
    def palabra(self, word: str) -> None:
        self._palabra = word
    
    @property
    def coincidencia(self) -> int:
        return self._coincidencia
    
    @coincidencia.setter
    def coincidencia(self, coinci: int) -> None:
        self._coincidencia = coinci