from insercion import Insercion

def main():
    Lista = [6,5,3,1,8,7,2,4]
    ord = Insercion(Lista)
    print("Lista desordenada \t", Lista)
    print("Lista ordenada    \t", ord.insercion())
    #print("Lista ordenadaRec \t", ord.insercionRec(0))


if __name__ == main():
    main()
