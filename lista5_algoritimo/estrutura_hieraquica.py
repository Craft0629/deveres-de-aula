empresa = {
    "TI": {
        "Desenvolvimento": {},
        "Infraestrutura": {}
    },

    "RH": {
        "Recrutamento": {},
        "Treinamento": {}
    }
}


def mostrar_departamentos(departamento):

    for chave in departamento:

        print(chave)

        mostrar_departamentos(departamento[chave])


mostrar_departamentos(empresa)