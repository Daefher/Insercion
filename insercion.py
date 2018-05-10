class Insercion(object):
    Lista = None
    tam_lista = 0
    def __init__(self,Lista):
        self.Lista = Lista
        self.tam_lista = len(Lista)

    def insercion(self):
        i = 0
        while i < self.tam_lista: #[5][4][3][2][1]
            j = i #1
            while j > 0 and self.Lista[j-1] > self.Lista[j]: # [5] y [4]
                tmp = self.Lista[j] # [4]
                self.Lista[j] =  self.Lista[j - 1]  #[5] [5]
                self.Lista[j-1] = tmp #[4] [5]
                j -=1
            i += 1
        return self.Lista

    def insercionRec(self,tam):
        if tam >= self.tam_lista:
            return self.Lista
        else:
            j = tam
            while j > 0 and self.Lista[j-1] > self.Lista[j]: # [5] y [4]
                tmp = self.Lista[j] # [4]
                self.Lista[j] =  self.Lista[j - 1]  #[5] [5]
                self.Lista[j-1] = tmp #[4] [5]
                j -=1
            print("Lista: ", self.Lista)
            return self.insercionRec(tam+1)
