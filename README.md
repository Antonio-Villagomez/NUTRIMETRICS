
# Analizador Nutricional para Estudiantes

## 📄 Descripción del Proyecto

Este es un **Analizador Nutricional** simple pero efectivo, diseñado para estudiantes. Permite al usuario ingresar sus datos personales y las comidas consumidas a lo largo del día. A partir de esta información, la aplicación calcula y presenta un reporte detallado del promedio de **carbohidratos, proteínas y fibra** por ingesta, así como el porcentaje de cada uno en la dieta total y la frecuencia de los alimentos consumidos.

Es una herramienta útil para obtener una visión rápida del perfil nutricional de la dieta diaria y fomentar hábitos alimenticios conscientes.

-----

## ✨ Características Principales

  * **Registro de Datos del Estudiante:** Permite al usuario ingresar su nombre, edad, género y área de estudio.
  * **Base de Datos de Alimentos:** Incluye una selección predefinida de alimentos con sus valores nutricionales (carbohidratos, proteínas, fibra) y porciones de referencia.
  * **Ingreso Interactivo de Comidas:** El usuario puede añadir los alimentos que consume junto con la cantidad en porciones, de forma interactiva a través de la terminal.
  * **Visualización de Alimentos Disponibles:** Al iniciar el registro de comidas, se muestra una lista clara de los alimentos que se pueden ingresar, junto con sus porciones recomendadas.
  * **Análisis Nutricional Detallado:** Calcula:
      * Promedio de carbohidratos, proteínas y fibra por ingesta.
      * **Porcentaje de carbohidratos, proteínas y fibra** respecto al total de estos tres macronutrientes.
      * Frecuencia de consumo de cada alimento.
  * **Reportes Claros:** Genera un resumen fácil de leer con todos los datos nutricionales.

-----

## 🚀 Cómo Ejecutar el Código

Sigue estos sencillos pasos para poner en marcha el analizador nutricional en tu máquina:

1.  **Guarda el Código:**

      * Copia todo el código fuente y pégalo en un archivo de texto.
      * Guarda este archivo con la extensión `.py` (por ejemplo, `analizador_nutricional.py`).

2.  **Abre una Terminal:**

      * **Windows:** Busca "CMD" o "PowerShell" en el menú de inicio.
      * **macOS/Linux:** Abre la aplicación "Terminal".

3.  **Navega al Directorio del Archivo:**

      * Usa el comando `cd` para ir a la carpeta donde guardaste `analizador_nutricional.py`.
          * Ejemplo: `cd C:\Usuarios\TuUsuario\Documentos\MiProyecto`
          * Ejemplo: `cd ~/Escritorio/AnalizadorNutricional`

4.  **Ejecuta el Script de Python:**

      * Una vez en el directorio correcto, ejecuta el programa con el siguiente comando:
        ```bash
        python analizador_nutricional.py
        ```
      * (Si tienes varias versiones de Python, podrías necesitar `python3 analizador_nutricional.py`).

5.  **Interactúa con la Aplicación:**

      * El programa te pedirá primero tus datos personales (nombre, edad, género, área de estudio).
      * Luego, te mostrará la lista de alimentos disponibles y te pedirá que ingreses los alimentos consumidos y sus cantidades. Escribe `fin` cuando hayas terminado de registrar tus comidas.
      * Finalmente, verás el reporte nutricional personalizado en la terminal.

-----

## 🛠️ Tecnologías Utilizadas

  * **Python 3.x**

-----

## 📂 Estructura del Código

El proyecto está organizado en las siguientes clases y funciones principales:

  * **`Estudiante`**: Almacena los datos personales del usuario.
  * **`Alimento`**: Define las propiedades nutricionales de cada alimento y su porción de referencia.
  * **`Ingesta`**: Registra un consumo específico de un alimento por un estudiante en una fecha dada.
  * **`ReporteAnalisis`**: Contiene los resultados del análisis nutricional y la lógica para formatear el reporte.
  * **`AnalizadorAlimentacion`**: La clase central que procesa las ingestas y calcula los promedios y frecuencias.
  * **`input_datos_estudiante()`**: Función para solicitar y validar los datos del usuario.
  * **`input_ingestas_usuario()`**: Función interactiva para que el usuario registre sus alimentos, mostrando la base de datos disponible.

-----

## 🤝 Contribuciones

Si tienes ideas para mejorar este analizador (como añadir más alimentos a la base de datos, implementar persistencia de datos, o nuevas métricas), ¡no dudes en proponerlas\!

-----

## ✒️ Autores

  * **\<Antonio Leon Villagomez/Antonio-Villagomez y Alexis Antonio Lopez Perez\>**

----
## Gracias por leer
