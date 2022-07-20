listaPrecios = [49100,51000,166600,140200,63100,75600,74600,15600,40800,80800]
listaResultante = []
i = 0
while i <= len(listaPrecios):
    if i % 2 != 0:
        listaResultante += [listaPrecios[i]]
    i += 1
print(listaResultante)
