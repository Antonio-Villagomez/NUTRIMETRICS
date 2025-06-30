from datetime import date
from typing import List, Dict
from collections import Counter

# Clase estudiante
class Estudiante:

    def __init__(self, nombre: str, edad: int, genero: str, areaEstudio: str):
        self.nombre: str = nombre
        self.edad: int = edad
        self.genero: str = genero
        self.areaEstudio: str = areaEstudio

    def __str__(self) -> str:
        return f"Estudiante(Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Área: {self.areaEstudio})"

# Clase alimento
class Alimento:

    def __init__(self, nombre: str, tipo: str, carbohidrato: float, proteina: float, fibra: float, otro: float, porcion: str):
        self.nombre: str = nombre
        self.tipo: str = tipo
        self.carbohidrato: float = carbohidrato
        self.proteina: float = proteina
        self.fibra: float = fibra
        self.otro: float = otro # Otros nutrientes o calorías no detalladas
        self.porcion: str = porcion # Descripción de la porción

    def __str__(self) -> str:
        return f"Alimento(Nombre: {self.nombre}, Tipo: {self.tipo}, Porción: {self.porcion})"

# Clase ingesta
class Ingesta:

    def __init__(self, estudiante: Estudiante, alimento: Alimento, fecha: date, cantidad: float):
        self.estudiante: Estudiante = estudiante
        self.alimento: Alimento = alimento
        self.fecha: date = fecha
        self.cantidad: float = cantidad # Cantidad en porciones

    def __str__(self) -> str:
        return (f"Ingesta(Estudiante: {self.estudiante.nombre} consumió {self.cantidad} "
                f"de {self.alimento.nombre} el {self.fecha})")

# Clase reporte
class ReporteAnalisis:

    def __init__(self, promedioCarbohidratos: float, promedioProteinas: float, promedioFibra: float, alimentosMasConsumidos: Dict[str, int]):
        self.promedioCarbohidratos: float = promedioCarbohidratos
        self.promedioProteinas: float = promedioProteinas
        self.promedioFibra: float = promedioFibra
        self.alimentosMasConsumidos: Dict[str, int] = alimentosMasConsumidos
        self.total_carbohidratos: float = 0.0
        self.total_proteinas: float = 0.0
        self.total_fibra: float = 0.0
        self.total_nutrientes: float = 0.0 # Suma total de carbohidratos, proteínas y fibra

    def generarReporte(self) -> str:
        reporte_str = "--- Reporte de Análisis Nutricional ---\n"
        reporte_str += f"Promedio de Carbohidratos por ingesta: {self.promedioCarbohidratos:.2f} g\n"
        reporte_str += f"Promedio de Proteínas por ingesta: {self.promedioProteinas:.2f} g\n"
        reporte_str += f"Promedio de Fibra por ingesta: {self.promedioFibra:.2f} g\n"
        
        # Calcular porcentajes si hay nutrientes totales para evitar división por cero
        if self.total_nutrientes > 0:
            porcentaje_carbohidratos = (self.total_carbohidratos / self.total_nutrientes) * 100
            porcentaje_proteinas = (self.total_proteinas / self.total_nutrientes) * 100
            porcentaje_fibra = (self.total_fibra / self.total_nutrientes) * 100
            reporte_str += f"\nPorcentaje de Carbohidratos en el total: {porcentaje_carbohidratos:.2f}%\n"
            reporte_str += f"Porcentaje de Proteínas en el total: {porcentaje_proteinas:.2f}%\n"
            reporte_str += f"Porcentaje de Fibra en el total: {porcentaje_fibra:.2f}%\n"
        else:
            reporte_str += "\nNo hay datos nutricionales para calcular porcentajes.\n"

        reporte_str += "\n--- Alimentos Consumidos (Frecuencia de Ingesta) ---\n"
        if self.alimentosMasConsumidos:
            for alimento, count in sorted(self.alimentosMasConsumidos.items(), key=lambda item: item[1], reverse=True):
                reporte_str += f"- {alimento}: {count} {'vez' if count == 1 else 'veces'}\n"
        else:
            reporte_str += "No hay datos de consumo de alimentos para mostrar.\n"
        return reporte_str

# Clase del analizador de alimentacion
class AnalizadorAlimentacion:

    def __init__(self):
        pass

    def analizarIngesta(self, ingestas: List[Ingesta]) -> ReporteAnalisis:
        if not ingestas:
            # Si no hay ingestas, retorna un reporte vacío
            return ReporteAnalisis(0.0, 0.0, 0.0, {})

        total_carbohidratos_consumidos = 0.0
        total_proteinas_consumidas = 0.0
        total_fibra_consumida = 0.0
        nombres_alimentos_consumidos = []

        for ingesta_actual in ingestas:
            # Multiplica los nutrientes por la cantidad de porciones consumidas
            total_carbohidratos_consumidos += ingesta_actual.alimento.carbohidrato * ingesta_actual.cantidad
            total_proteinas_consumidas += ingesta_actual.alimento.proteina * ingesta_actual.cantidad
            total_fibra_consumida += ingesta_actual.alimento.fibra * ingesta_actual.cantidad
            nombres_alimentos_consumidos.append(ingesta_actual.alimento.nombre)

        num_total_de_ingestas = len(ingestas)
        # Calcula promedios, asegurando no dividir por cero
        promedio_carbs = total_carbohidratos_consumidos / num_total_de_ingestas if num_total_de_ingestas > 0 else 0.0
        promedio_proteinas = total_proteinas_consumidas / num_total_de_ingestas if num_total_de_ingestas > 0 else 0.0
        promedio_fibra = total_fibra_consumida / num_total_de_ingestas if num_total_de_ingestas > 0 else 0.0
        
        # Cuenta la frecuencia de cada alimento
        frecuencia_alimentos = Counter(nombres_alimentos_consumidos)

        # Crea el objeto ReporteAnalisis y asigna los totales para el cálculo de porcentajes
        reporte = ReporteAnalisis(
            promedioCarbohidratos=promedio_carbs,
            promedioProteinas=promedio_proteinas,
            promedioFibra=promedio_fibra,
            alimentosMasConsumidos=dict(frecuencia_alimentos)
        )
        reporte.total_carbohidratos = total_carbohidratos_consumidos
        reporte.total_proteinas = total_proteinas_consumidas
        reporte.total_fibra = total_fibra_consumida
        # El total de nutrientes es la suma de los tres macronutrientes principales
        reporte.total_nutrientes = total_carbohidratos_consumidos + total_proteinas_consumidas + total_fibra_consumida
        return reporte

# Función para pedir datos del estudiante al usuario
def input_datos_estudiante() -> Estudiante:
    print("\n--- Ingreso de tus datos de Estudiante ---")
    nombre = input("Ingresa tu nombre completo: ").strip()
    
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad <= 0:
                print("La edad debe ser un número positivo. Intenta de nuevo.")
            else:
                break
        except ValueError:
            print("Edad inválida. Por favor, ingresa un número entero.")
            
    while True:
        genero = input("Ingresa tu género (Masculino/Femenino/Otro): ").strip().capitalize()
        if genero in ["Masculino", "Femenino", "Otro"]:
            break
        else:
            print("Género inválido. Por favor, ingresa 'Masculino', 'Femenino' o 'Otro'.")

    while True:        
        area_estudio = input("Ingresa tu carrera de ESCOM(ISC, IA, LCD): ").strip()
        if area_estudio in ["ISC", "IA", "LCD"]:
            break
        else:
            print("Carrera invalida. Ingresa un valor correcto por favor")
    
    return Estudiante(nombre, edad, genero, area_estudio)


# Función para que el usuario ingrese alimentos
def input_ingestas_usuario(estudiante: Estudiante) -> List[Ingesta]:
    ingestas_usuario: List[Ingesta] = []
    print(f"\n--- Ingreso de comidas para {estudiante.nombre} ---")
    print("Introduce los alimentos consumidos. Escribe 'fin' para terminar.")

    # Simular una base de datos de alimentos con valores nutricionales
    alimentos_disponibles = {
        "manzana": Alimento("Manzana", "Fruta", 25.0, 0.5, 4.0, 0.2, "1 pieza mediana (aprox. 180g)"),
        "pechuga de pollo": Alimento("Pechuga de Pollo", "Carne", 0.0, 31.0, 0.0, 2.0, "100g cocida"),
        "arroz blanco": Alimento("Arroz Blanco", "Cereal", 28.0, 2.7, 0.4, 0.1, "1/2 taza cocida (aprox. 75g)"),
        "lentejas": Alimento("Lentejas", "Legumbre", 20.0, 9.0, 8.0, 1.0, "1/2 taza cocida (aprox. 100g)"),
        "pan integral": Alimento("Pan Integral", "Cereal", 15.0, 3.0, 2.5, 0.5, "1 rebanada (aprox. 30g)"),
        "aguacate": Alimento("Aguacate", "Fruta", 9.0, 2.0, 7.0, 15.0, "1/2 unidad (aprox. 100g)"),
        "salmon": Alimento("Salmón", "Pescado", 0.0, 20.0, 0.0, 13.0, "100g"),
        "brocoli": Alimento("Brócoli", "Vegetal", 7.0, 2.8, 5.0, 0.4, "1 taza (aprox. 90g)"),
        "huevo": Alimento("Huevo", "Proteína", 0.6, 6.0, 0.0, 5.0, "1 unidad grande"),
        "yogur griego": Alimento("Yogur Griego", "Lácteo", 5.0, 10.0, 0.0, 0.5, "100g"),
        "pasta": Alimento("Pasta", "Cereal", 30.0, 5.0, 2.0, 0.5, "1 taza cocida"),
        "atun enlatado": Alimento("Atún enlatado", "Pescado", 0.0, 25.0, 0.0, 8.0, "100g"),
        "papa cocida": Alimento("Papa Cocida", "Vegetal", 20.0, 2.0, 2.0, 0.1, "1 papa mediana (aprox. 170g)"),
        "leche entera": Alimento("Leche Entera", "Lácteo", 12.0, 8.0, 0.0, 8.0, "1 vaso (240ml)"),
        "quinoa": Alimento("Quinoa", "Cereal", 21.0, 4.0, 3.0, 0.5, "1/2 taza cocida"),
        "almendras": Alimento("Almendras", "Fruto Seco", 20.0, 20.0, 12.0, 50.0, "100g"),
    }

    # --- Mostrar la base de datos de alimentos al inicio ---
    print("\n--- Base de Datos de Alimentos Disponibles ---")
    # Ordenar los alimentos alfabéticamente para una mejor visualización
    sorted_alimentos = sorted(alimentos_disponibles.items(), key=lambda item: item[0])
    for nombre_key, alimento_obj in sorted_alimentos:
        print(f"- {alimento_obj.nombre.capitalize()} (Porción: {alimento_obj.porcion})")
    print("-------------------------------------------\n")

    while True:
        nombre_alimento = input("Nombre del alimento (o 'fin' para terminar): ").strip()
        if nombre_alimento.lower() == 'fin':
            break
        
        alimento_encontrado = alimentos_disponibles.get(nombre_alimento.lower())

        if alimento_encontrado:
            try:
                cantidad = float(input(f"Cantidad consumida de {alimento_encontrado.nombre} (en porciones): "))
                if cantidad <= 0:
                    print("La cantidad debe ser un número positivo. Intenta de nuevo.")
                    continue
                ingestas_usuario.append(Ingesta(estudiante, alimento_encontrado, date.today(), cantidad))
                print(f"'{alimento_encontrado.nombre}' añadido.")
            except ValueError:
                print("Cantidad inválida. Por favor, ingresa un número.")
        else:
            print(f"El alimento '{nombre_alimento}' no está en nuestra base de datos. Por favor, intenta con otro o revisa la escritura.")
            # Se omite la lista de disponibles aquí para evitar repetirla en cada error.

    return ingestas_usuario

# Ejemplo de Uso (Bloque principal de ejecución)
if __name__ == "__main__":
    analizador = AnalizadorAlimentacion() # Instancia del analizador

    # --- Interacción completa con el usuario ---
    print("\n" + "="*60 + "\n")
    print("--- ¡Bienvenido al Analizador Nutricional Interactivo! ---")
    
    # 1. El usuario ingresa sus datos como estudiante
    estudiante_actual = input_datos_estudiante()
    print(f"\n¡Hola, {estudiante_actual.nombre}! Tus datos han sido registrados.")

    # 2. El usuario ingresa sus comidas, viendo los alimentos disponibles
    ingestas_del_usuario = input_ingestas_usuario(estudiante_actual)
    
    # 3. Generar y mostrar el reporte de las comidas del usuario
    if ingestas_del_usuario:
        print(f"\n--- Reporte Nutricional para {estudiante_actual.nombre} ({date.today()}) ---")
        reporte_personal = analizador.analizarIngesta(ingestas_del_usuario)
        print(reporte_personal.generarReporte())
    else:
        print("No se ingresaron comidas para generar un reporte hoy para ti.")

    print("\n" + "="*60 + "\n")
    print("¡Gracias por usar el Analizador Nutricional!")