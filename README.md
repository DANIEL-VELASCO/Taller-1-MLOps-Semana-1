🐧 Taller 1 - MLOps
API de Clasificación de Penguins con FastAPI y Docker

Este proyecto fue desarrollado como parte del Taller 1 de MLOps.
Se entrena un modelo de Machine Learning utilizando el dataset palmerpenguins y se expone mediante una API construida con FastAPI, la cual es desplegada dentro de un contenedor Docker.

📂 Estructura del Proyecto
TALLER_1/
│
├── app/
│   ├── main.py
│   ├── penguins_species_model.pkl
│   └── requirements
│
├── Dockerfile
└── README.md

📌 Descripción de los componentes

main.py → Contiene la implementación de la API con FastAPI.

penguins_species_model.pkl → Modelo entrenado para clasificación de especies.

requirements → Archivo de dependencias del proyecto.

Dockerfile → Archivo de configuración para crear la imagen Docker.

README.md → Documentación del proyecto.

⚙️ Entrenamiento del Modelo

El modelo fue entrenado previamente utilizando el dataset palmerpenguins.

El archivo serializado generado es:

penguins_species_model.pkl


Este archivo es cargado por la API para realizar predicciones.

🚀 Ejecución Local (sin Docker)

Desde la carpeta app, instalar dependencias:

pip install -r requirements


Luego ejecutar:

uvicorn main:app --reload --port 8989


Abrir en el navegador:

http://localhost:8989/docs

🐳 Ejecución con Docker

Desde la raíz del proyecto (donde está el Dockerfile):

Construir la imagen:
docker build -t penguin-api .

Ejecutar el contenedor:
docker run -p 8989:8989 penguin-api


La API quedará disponible en:

http://localhost:8989/docs

📡 Endpoint Principal
POST /predict

Recibe las siguientes variables:

bill_length_mm

bill_depth_mm

flipper_length_mm

body_mass_g

Ejemplo de entrada JSON:

{
  "bill_length_mm": 50,
  "bill_depth_mm": 15,
  "flipper_length_mm": 200,
  "body_mass_g": 4000
}


Retorna:

Especie predicha del pingüino

🧠 Tecnologías Utilizadas

Python 3.10

FastAPI

Uvicorn

Scikit-learn

Docker

🎯 Objetivo del Proyecto

Aplicar conceptos fundamentales de MLOps:

Serialización de modelos

Creación de API para inferencia

Contenerización con Docker

Exposición del servicio en puerto 8989

👨‍💻 Autor

Daniel Velasco
Maestría en Inteligencia Artificial