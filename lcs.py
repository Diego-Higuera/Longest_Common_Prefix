class Solution:
    def longestCommonPrefix(self, palabras: List[str]) -> str:  #enunciado
        res = ''                                                #resultado inicializado vacio
        if len(palabras) == 0:                                  #si el tamaño (len) de palabras es 0
            return res                                          #se devuelve el resultado
        palabra_corta = min(palabras, key = len)                #busca la palabra de menor(min) tamaño (key = len)
        for i in range(len(palabra_corta)):                     #
            for s in palabras:                                  #recorre las palabras por caracter (s)
                 if s[i] != palabras[0][i]:                     #si el caracter (s[i]) no coincide con el caracter de la primera palabra[0])
                     return res                                 #devuelve el resultado
            res += s[i]                                         #si coincide los añade al resultado
        return res                                              #devuelve el resultado
                