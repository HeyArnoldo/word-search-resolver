# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.patches import Rectangle

# Configuración de colores y estilo
COLOR_FONDO = (1, 1, 1, 1)        # Blanco
COLOR_TEXTO_NORMAL = (0.2, 0.2, 0.2, 1)  # Gris oscuro
COLOR_BORDE = (0.8, 0.8, 0.8, 1)  # Gris claro
GROSOR_BORDE = 0.3
TAMANO_FUENTE = 14
TAMANO_CELDA = 1.2

# Sopa de letras con longitudes de fila desiguales:
sopa = [
    "OCITIVELEASDVBSACINORCAREMIRPP",
    "ILNUMEROSTITOIPCMEDMPZRWOGULFE",
    "AOUMERARDECAAGNEHEMIASEDMRTAIS",
    "MDMAIDOBRLIMSOIOPSOMLASEUUEMLT",
    "ISESOEDIAICOARPNEHCHAUGUNBNEHO",
    "JOBAGOOASCRFMIESSAONIRESSECNOT",
    "GBOTELXPATAHOKGMSRMHTURAIRATDI",
    "ORCONIEIJONASLDTAUDICDAMSZOAEM",
    "LEISEVOCGRILANAGOAIMHEIOEACCDU",
    "AMORSALASACINORCADNUGESUYCF1EN",
    "HELIICELNAODAROISARAOSPOEAMOUO",
    "IRAISHEIENSSAESOERASNDEPRRSNSM",
    "PRIMERAREYESEAIGESJULIORAIAELE",
    "DREBRUNSISAIDEUTERONOMIODAPSES",
    "AOASACINORCADNUGESEBRGUVNSAJIM",
    "NMNAESTERFALARACPELEAALEURLEAA",
    "IADENIVDIOEUSOJJOLEADMARGUVRAL",
    "ENRMALACUQUEJSESDHAGEORBETMEBA",
    "LOEPFIJUECESDASAEOISOAAISIUMIQ",
    "PSITFOIEAEJERMUIGDTIPSPOERHIBU",
    "CASAMAAGOCFTAISAMIQUEASSUOAALI",
    "TIAOCIBINASSECASAECOLMOSSQNSIA",
    "RNMSEMDNTAIAGUTEJEREMIASNAOMAS",
    "AOITLUIHAJEIAENIADGARQJIPACASA",
    "EFCANTARESGSFGHRTYJYVUACIAROMA",
    "IOJTIGSGOIAEOLEUMASADNUGESPERU",
    "OSGUDEBAIOGLTPCGACOMOICIDIENAG",
    "TATILIANAMECILEIUQEZEJCDPAMRAP",
    "CAOHABACUCMEPPRIMERASAMUELFAGI"
]

# Palabras a buscar
palabras = [
    "genesis",
    "exodo",
    "levitico",
    "numeros",
    "deuteronomio",
    "josue",
    "jueces",
    "rut",
    "primerasamuel",
    "segundasamuel",
    "primerareyes",
    "segundareyes",
    "primeracronicas",
    "segundacronicas",
    "esdras",
    "nehemias",
    "ester",
    "job",
    "salmos",
    "proverbios",
    "eclesiastes",
    "cantares",
    "isaias",
    "jeremias",
    "lamentaciones",
    "ezequiel",
    "daniel",
    "oseas",
    "joel",
    "amos",
    "abdias",
    "jonas",
    "miqueas",
    "nahum",
    "habacuc",
    "sofonias",
    "hageo",
    "zacarias",
    "malaquias"
]

# Direcciones posibles (dx, dy):
direcciones = [
    (0, 1),   # derecha
    (0, -1),  # izquierda
    (1, 0),   # abajo
    (-1, 0),  # arriba
    (1, 1),   # diagonal abajo-derecha
    (1, -1),  # diagonal abajo-izquierda
    (-1, 1),  # diagonal arriba-derecha
    (-1, -1)  # diagonal arriba-izquierda
]

def palabra_en_posicion(sopa, palabra, fila_inicial, col_inicial, dx, dy):
    """Verifica si 'palabra' está en 'sopa' comenzando en (fila_inicial, col_inicial)
    y avanzando en la dirección (dx, dy)."""
    filas = len(sopa)
    longitud = len(palabra)
    
    for i in range(longitud):
        fila_actual = fila_inicial + i * dx
        col_actual = col_inicial + i * dy
        
        # Verifica límites
        if fila_actual < 0 or fila_actual >= filas:
            return False
        if col_actual < 0 or col_actual >= len(sopa[fila_actual]):
            return False
        
        # Compara carácter
        if sopa[fila_actual][col_actual].lower() != palabra[i].lower():
            return False
    
    return True

def buscar_palabra(sopa, palabra):
    """Busca todas las apariciones de 'palabra' en 'sopa' y retorna una lista
    de tuplas (fila_inicial, col_inicial, fila_final, col_final)."""
    filas = len(sopa)
    resultados = []
    
    for fila in range(filas):
        for col in range(len(sopa[fila])):
            for dx, dy in direcciones:
                if palabra_en_posicion(sopa, palabra, fila, col, dx, dy):
                    fila_final = fila + (len(palabra) - 1) * dx
                    col_final = col + (len(palabra) - 1) * dy
                    resultados.append((fila, col, fila_final, col_final))
    
    return resultados

def marcar_palabra(sopa_lista, colores, palabra, fila_inicial, col_inicial, dx, dy, color):
    """Marca la palabra en la matriz de sopa_lista y asigna el color en 'colores'."""
    for i in range(len(palabra)):
        f = fila_inicial + i * dx
        c = col_inicial + i * dy
        sopa_lista[f][c] = sopa_lista[f][c].upper()
        colores[f][c] = color

def crear_imagen_sopa(sopa_lista, colores, nombre_imagen="sopa_resuelta.png"):
    """
    Dibuja la sopa de letras con las palabras resaltadas y la guarda como imagen.
    """
    filas = len(sopa_lista)
    columnas = max(len(fila) for fila in sopa_lista)
    
    fig = plt.figure(figsize=(columnas * 0.22, filas * 0.22), dpi=150)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    plt.axis('off')
    
    # Dibujar celdas y texto de la sopa
    for fila in range(filas):
        for col in range(len(sopa_lista[fila])):
            rect = Rectangle(
                (col - TAMANO_CELDA / 2, fila - TAMANO_CELDA / 2),
                TAMANO_CELDA, TAMANO_CELDA,
                facecolor=COLOR_FONDO,
                edgecolor=COLOR_BORDE,
                linewidth=GROSOR_BORDE
            )
            ax.add_patch(rect)
            
            letra = sopa_lista[fila][col]
            ax.text(
                col, fila, letra,
                fontsize=TAMANO_FUENTE,
                ha='center',
                va='center',
                color=colores[fila][col],
                weight='bold'
            )
    
    ax.set_xlim(-TAMANO_CELDA / 2, columnas)
    ax.set_ylim(filas, -TAMANO_CELDA / 2)
    plt.tight_layout()
    
    plt.savefig(nombre_imagen, bbox_inches='tight', pad_inches=0.2, dpi=300)
    plt.close()
    
    imagen = Image.open(nombre_imagen)
    imagen = imagen.resize((1920, int(1920 * (filas / columnas))), Image.Resampling.LANCZOS)
    imagen.save(nombre_imagen)

def crear_imagen_leyenda(legend_info, nombre_imagen="leyenda.png", max_columns=3):
    """
    Crea una imagen con la leyenda de las palabras y sus colores.
    Se organiza en varias columnas (wrap) para ocupar solo lo necesario.
    Cada entrada muestra un cuadrado con el color asignado y la palabra en mayúsculas.
    """
    n = len(legend_info)
    columns = min(n, max_columns)
    rows = math.ceil(n / columns)
    
    # Tamaño asignado a cada entrada (en unidades de "datos")
    entry_width = 2    # espacio horizontal por entrada
    entry_height = 0.5  # espacio vertical por entrada
    margin_x = 0.2
    margin_y = 0.2
    
    total_width = columns * entry_width + 2 * margin_x
    total_height = rows * entry_height + 2 * margin_y
    
    fig, ax = plt.subplots(figsize=(total_width, total_height))
    ax.set_xlim(0, total_width)
    ax.set_ylim(0, total_height)
    ax.axis("off")
    
    for i, (palabra, color) in enumerate(legend_info):
        col_index = i % columns
        row_index = rows - 1 - (i // columns)  # para que la primera entrada quede arriba
        cell_x = margin_x + col_index * entry_width
        cell_y = margin_y + row_index * entry_height
        
        # Dibujar cuadrado de color
        square_size = 0.3
        rect = Rectangle((cell_x, cell_y + (entry_height - square_size) / 2),
                         square_size, square_size,
                         facecolor=color, edgecolor="black")
        ax.add_patch(rect)
        
        # Escribir la palabra al lado del cuadrado, con wrap activado
        text_x = cell_x + square_size + 0.1
        text_y = cell_y + entry_height / 2
        ax.text(text_x, text_y, palabra.upper(), va="center", ha="left",
                fontsize=10, wrap=True)
    
    plt.tight_layout()
    plt.savefig(nombre_imagen, dpi=300, bbox_inches="tight", pad_inches=0.2)
    plt.close()

def combinar_imagenes(imagen_superior, imagen_inferior, nombre_final="sopa_completa.png"):
    """
    Combina dos imágenes (la leyenda en la parte superior y el pupiletras abajo)
    en una sola imagen final.
    """
    img_sup = Image.open(imagen_superior)
    img_inf = Image.open(imagen_inferior)
    
    ancho = max(img_sup.width, img_inf.width)
    alto = img_sup.height + img_inf.height
    
    img_final = Image.new("RGB", (ancho, alto), "white")
    img_final.paste(img_sup, (0, 0))
    img_final.paste(img_inf, (0, img_sup.height))
    img_final.save(nombre_final)

def main():
    # Convertir cada fila de la sopa en una lista para modificar caracteres
    sopa_lista = [list(fila) for fila in sopa]
    colores_matriz = [[COLOR_TEXTO_NORMAL for _ in fila] for fila in sopa]
    
    # Generar colores únicos para cada palabra usando un colormap
    cmap = plt.get_cmap("tab10")
    colores_palabras = [cmap(i / len(palabras)) for i in range(len(palabras))]
    
    # Buscar y marcar cada palabra en la sopa
    for idx, palabra in enumerate(palabras):
        ubicaciones = buscar_palabra(sopa, palabra)
        if ubicaciones:
            color = colores_palabras[idx]
            for (fi, ci, ff, cf) in ubicaciones:
                dx = 0 if ff == fi else (1 if ff > fi else -1)
                dy = 0 if cf == ci else (1 if cf > ci else -1)
                marcar_palabra(sopa_lista, colores_matriz, palabra, fi, ci, dx, dy, color)
    
    legend_info = list(zip(palabras, colores_palabras))
    
    crear_imagen_sopa(sopa_lista, colores_matriz, nombre_imagen="sopa_resuelta.png")
    crear_imagen_leyenda(legend_info, nombre_imagen="leyenda.png", max_columns=3)
    combinar_imagenes("leyenda.png", "sopa_resuelta.png", nombre_final="sopa_completa.png")
    print("¡Sopa de letras completa guardada como 'sopa_completa.png'!")

if __name__ == "__main__":
    main()
