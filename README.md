# Predicción de la función de proteínas utilizando aprendizaje profundo

Este proyecto utiliza aprendizaje profundo para predecir la función de proteínas desconocidas a partir de datos de secuencias de proteínas conocidas.

## Estructura del repositorio

- data/: Contiene archivos FASTA con secuencias de proteínas conocidas y desconocidas.
- src/: Contiene scripts de Python para preprocesar datos, entrenar el modelo y predecir la función de proteínas.
- models/: Contiene el modelo entrenado en formato HDF5.
- results/: Contiene las predicciones de función de proteínas en formato CSV.

## Cómo ejecutar el proyecto

1. Preprocesar los datos:
  python src/preprocess_data.py

2. Entrenar el modelo:
  python src/train_model.py
  
3. Predecir la función de proteínas desconocidas:
  python src/predict_function.py
  
