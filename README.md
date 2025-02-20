# Sopa de Letras - Solución Visual

Este proyecto consiste en un script de Python que resuelve una sopa de letras y genera una imagen final en la que se destacan las palabras encontradas, junto con una leyenda que muestra el color asignado a cada una.

---

## Descripción

El script realiza las siguientes acciones:

- **Definición del Puzzle:**  
  Se especifica la sopa de letras en una lista de cadenas (cada cadena es una fila), la cual puede tener longitudes de fila desiguales.

- **Búsqueda de Palabras:**  
  Se busca un conjunto de palabras (en este caso, libros de la Biblia) en la sopa en 8 direcciones posibles: horizontal (izquierda y derecha), vertical (arriba y abajo) y en las cuatro diagonales.

- **Resaltado y Creación de Imágenes:**  
  Cada palabra encontrada se marca en la sopa con un color único obtenido de un colormap de Matplotlib. Se generan dos imágenes:
  - Una imagen con la sopa de letras en la que se resaltan las palabras.
  - Una imagen de leyenda que asocia cada palabra con su color.
  
- **Combinación de Imágenes:**  
  Finalmente, ambas imágenes se combinan en una imagen final llamada `sopa_completa.png`.

---

## Requisitos

Para ejecutar este script, necesitas tener instalado Python (versión 3.6 o superior) y las siguientes librerías:

- **matplotlib** (para la visualización y creación de imágenes)  
- **numpy**  
- **Pillow (PIL)**

Puedes instalar estas librerías utilizando pip:

```bash
pip install matplotlib numpy Pillow
```

*Nota:* Aunque el código utiliza también módulos estándar como `math`, estos vienen incluidos en Python.

---

## Uso

1. **Guardar el Código:**  
   Guarda el código en un archivo, por ejemplo, `sopa_de_letras.py`.

2. **Ejecutar el Script:**  
   Abre una terminal o consola en el directorio donde se encuentra el archivo y ejecuta:

   ```bash
   python sopa_de_letras.py
   ```

3. **Ver el Resultado:**  
   Al finalizar la ejecución, se generará un archivo llamado `sopa_completa.png` en el mismo directorio. Esta imagen contiene la sopa de letras con las palabras resaltadas y la leyenda correspondiente.

---

## Personalización

- **Modificar la Sopa de Letras:**  
  Puedes editar la variable `sopa` para definir tu propio puzzle.

- **Cambiar las Palabras a Buscar:**  
  Actualiza la lista `palabras` con las palabras que deseas encontrar en la sopa.

- **Ajustar Estilos y Colores:**  
  Las variables `COLOR_FONDO`, `COLOR_TEXTO_NORMAL`, `COLOR_BORDE`, `TAMANO_FUENTE`, etc., permiten personalizar la apariencia de la imagen final.

- **Direcciones de Búsqueda:**  
  La lista `direcciones` define las 8 posibles direcciones en las que se buscan las palabras. Puedes modificarla si deseas cambiar la lógica de búsqueda.

---

## Créditos

Este código se desarrolló con la contribución e inspiración de **Joao Souza**.  

---