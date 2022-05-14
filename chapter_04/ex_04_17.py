def busca(lista, valor):
    navegar = lista.head

    while navegar and navegar.data != valor:
        navegar = navegar.nextItem

    return navegar
