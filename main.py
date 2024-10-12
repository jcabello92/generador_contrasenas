##### IMPORTACIONES #####
import random





##### VARIABLES GLOBALES #####
MINUSCULAS_INFERIOR = 97
MINUSCULAS_SUPERIOR = 122

MAYUSCULAS_INFERIOR = 65
MAYUSCULAS_SUPERIOR = 90

NUMEROS_INFERIOR = 48
NUMEROS_SUPERIOR = 57

ESPECIALES_1_INFERIOR = 33
ESPECIALES_1_SUPERIOR = 47
ESPECIALES_2_INFERIOR = 58
ESPECIALES_2_SUPERIOR = 64
ESPECIALES_3_INFERIOR = 91
ESPECIALES_3_SUPERIOR = 96
ESPECIALES_4_INFERIOR = 123
ESPECIALES_4_SUPERIOR = 126

ESPACIO = 32

MINUSCULAS = []
MAYUSCULAS = []
NUMEROS = []
ESPECIALES = []

FINAL = []

CONTRASENA = []





##### FUNCIONES #####
def inicializar_listas():
    C = MINUSCULAS_INFERIOR
    while(C <= MINUSCULAS_SUPERIOR):
        MINUSCULAS.append(C)
        C = C + 1

    C = MAYUSCULAS_INFERIOR
    while(C <= MAYUSCULAS_SUPERIOR):
        MAYUSCULAS.append(C)
        C = C + 1

    C = NUMEROS_INFERIOR
    while(C <= NUMEROS_SUPERIOR):
        NUMEROS.append(C)
        C = C + 1

    C = ESPECIALES_1_INFERIOR
    while(C <= ESPECIALES_1_SUPERIOR):
        ESPECIALES.append(C)
        C = C + 1

    C = ESPECIALES_2_INFERIOR
    while(C <= ESPECIALES_2_SUPERIOR):
        ESPECIALES.append(C)
        C = C + 1

    C = ESPECIALES_3_INFERIOR
    while(C <= ESPECIALES_3_SUPERIOR):
        ESPECIALES.append(C)
        C = C + 1

    C = ESPECIALES_4_INFERIOR
    while(C <= ESPECIALES_4_SUPERIOR):
        ESPECIALES.append(C)
        C = C + 1



def definir_lista_final(VALIDACION_MINUSCULAS, VALIDACION_MAYUSCULAS, VALIDACION_NUMEROS, VALIDACION_ESPECIALES, VALIDACION_ESPACIO):
    if(VALIDACION_MINUSCULAS):
        C = 0
        while(C < len(MINUSCULAS)):
            FINAL.append(MINUSCULAS[C])
            C = C + 1

    if(VALIDACION_MAYUSCULAS):
        C = 0
        while(C < len(MAYUSCULAS)):
            FINAL.append(MAYUSCULAS[C])
            C = C + 1

    if(VALIDACION_NUMEROS):
        C = 0
        while(C < len(NUMEROS)):
            FINAL.append(NUMEROS[C])
            C = C + 1

    if(VALIDACION_ESPECIALES):
        C = 0
        while(C < len(ESPECIALES)):
            FINAL.append(ESPECIALES[C])
            C = C + 1

    if(VALIDACION_ESPACIO):
        FINAL.append(ESPACIO)



def generar_contrasena(LONGITUD, VALIDACION_MINUSCULAS, VALIDACION_MAYUSCULAS, VALIDACION_NUMEROS, VALIDACION_ESPECIALES, VALIDACION_ESPACIO):
    inicializar_listas()
    definir_lista_final(VALIDACION_MINUSCULAS, VALIDACION_MAYUSCULAS, VALIDACION_NUMEROS, VALIDACION_ESPECIALES, VALIDACION_ESPACIO);
  
    C = 0
    while(C < LONGITUD):
        CONTRASENA.append(random.choice(FINAL))
        C = C + 1

    C = 0
    while(C < len(CONTRASENA)):
        if(C == 0):
            print('\nContraseña: ', end = "")
        print(chr(CONTRASENA[C]), end = "")
        C = C + 1
    print()





##### SISTEMA PRINCIPAL #####
print('\n')
print("GENERADOR DE CONTRASEÑAS...\n")

VALIDACION_AUX_LONGITUD = input("Longitud = ")

VALIDACION_AUX_MINUSCULAS = False
VALIDACION_MINUSCULAS = input("Minúsculas = ")
if(VALIDACION_MINUSCULAS == "1"):
    VALIDACION_AUX_MINUSCULAS = True

VALIDACION_AUX_MAYUSCULAS = False
VALIDACION_MAYUSCULAS = input("Mayúsculas = ")
if(VALIDACION_MAYUSCULAS == "1"):
    VALIDACION_AUX_MAYUSCULAS = True

VALIDACION_AUX_NUMEROS = False
VALIDACION_NUMEROS = input("Números = ")
if(VALIDACION_NUMEROS == "1"):
    VALIDACION_AUX_NUMEROS = True

VALIDACION_AUX_ESPECIALES = False
VALIDACION_ESPECIALES = input("Especiales = ")
if(VALIDACION_ESPECIALES == "1"):
    VALIDACION_AUX_ESPECIALES = True

VALIDACION_AUX_ESPACIOS = False
VALIDACION_ESPACIOS = input("Espacios = ")
if(VALIDACION_ESPACIOS == "1"):
    VALIDACION_AUX_ESPACIOS = True

generar_contrasena(int(VALIDACION_AUX_LONGITUD), VALIDACION_AUX_MINUSCULAS, VALIDACION_AUX_MAYUSCULAS, VALIDACION_AUX_NUMEROS, VALIDACION_AUX_ESPECIALES, VALIDACION_AUX_ESPACIOS)