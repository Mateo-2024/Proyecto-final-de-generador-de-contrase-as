# Proyecto-final-de-generador-de-contrase-as
                  UIDE
Nombre:Mateo Vasquez 
Fecha:22/12/2024

# Generador de Contraseñas Seguras

Este proyecto es un generador de contraseñas seguras escrito en Python. Proporciona una interfaz simple para que los usuarios creen contraseñas personalizadas según sus necesidades, con opciones para incluir letras mayúsculas, números y símbolos especiales.

## Características
- Genera contraseñas de longitud personalizada.
- Permite incluir o excluir letras mayúsculas, números y símbolos especiales.
- Copia la contraseña generada al portapapeles (requiere la biblioteca `pyperclip`).
- Asegura que la longitud mínima de la contraseña sea de 8 caracteres para mayor seguridad.

## Requisitos
Este proyecto requiere Python 3.6 o superior.

### Dependencias
Instala las dependencias necesarias con:
```bash
pip install pyperclip
```

## Uso
1. Clona este repositorio o descarga el archivo.
2. Ejecuta el programa:
   ```bash
   python generador_contraseñas.py
   ```
3. Sigue las instrucciones en la consola para generar tu contraseña:
   - Introduce la longitud deseada (mínimo 8 caracteres).
   - Especifica si deseas incluir letras mayúsculas, números y símbolos.
   - Decide si quieres copiar la contraseña generada al portapapeles.
     

## Ejemplo
```
=== Generador de Contraseñas Seguras ===
Introduce la longitud de la contraseña (mínimo 8): 12
¿Incluir letras mayúsculas? (s/n): s
¿Incluir números? (s/n): s
¿Incluir símbolos especiales? (s/n): n

Tu contraseña generada es: A1b2c3d4E5f6
¿Copiar al portapapeles? (s/n): s
¡Contraseña copiada al portapapeles!
¿Generar otra contraseña? (s/n): n
¡Gracias por usar el Generador de Contraseñas!
```

## Personalización
El programa se puede modificar fácilmente para adaptarse a necesidades específicas:
- Cambia el conjunto de caracteres permitidos (por ejemplo, para excluir ciertos símbolos).
- Ajusta la longitud mínima de la contraseña.




