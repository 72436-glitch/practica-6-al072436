import math

# ---- VALIDACIÓN ----
def validar(valor):
    if valor <= 0:
        raise ValueError("Todos los valores deben ser mayores que cero.")
    return valor


# ---- CÁLCULOS ----

def volumen_losa(largo, ancho, espesor):
    return validar(largo) * validar(ancho) * validar(espesor)


def volumen_zapata(largo, ancho, espesor):
    return validar(largo) * validar(ancho) * validar(espesor)


def volumen_columna_rect(lado1, lado2, altura):
    return validar(lado1) * validar(lado2) * validar(altura)


def volumen_columna_circ(diametro, altura):
    radio = validar(diametro) / 2
    return math.pi * (radio ** 2) * validar(altura)


# ---- PRUEBAS ----
def pruebas():
    assert round(volumen_losa(5, 4, 0.15), 2) == 3.00
    assert volumen_zapata(2, 2, 0.5) == 2.0
    assert volumen_columna_rect(0.3, 0.3, 3) == 0.27
    assert round(volumen_columna_circ(0.4, 3), 4) == round(math.pi * 0.2 * 0.2 * 3, 4)

    print("TODAS LAS PRUEBAS PASARON CORRECTAMENTE ✔")