import random
import string
import pyperclip  

def generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    """
    Genera una contraseña segura según los parámetros especificados.
    """
    caracteres = string.ascii_lowercase  # Minúsculas
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if len(caracteres) == 0:
        return "Error: Selecciona al menos un tipo de carácter."
    
    # Generar contraseña con la longitud y los caracteres especificados
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    """
    Interfaz de usuario para generar contraseñas seguras.
    """
    print("=== Generador de Contraseñas Seguras ===")
    while True:
        try:
            # Solicitar longitud de la contraseña
            longitud = int(input("Introduce la longitud de la contraseña (mínimo 8): "))
            if longitud < 8:
                print("Error: La longitud debe ser al menos 8 caracteres.")
                continue
            
            # Solicitar configuraciones
            incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").strip().lower() == 's'
            incluir_numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
            incluir_simbolos = input("¿Incluir símbolos especiales? (s/n): ").strip().lower() == 's'
            
            # Generar la contraseña
            contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
            
            # Mostrar la contraseña generada
            if "Error" not in contraseña:
                print(f"\nTu contraseña generada es: {contraseña}")
                copiar = input("¿Copiar al portapapeles? (s/n): ").strip().lower() == 's'
                if copiar:
                    pyperclip.copy(contraseña)
                    print("¡Contraseña copiada al portapapeles!")
            else:
                print(contraseña)

            # Preguntar si desea generar otra contraseña
            repetir = input("\n¿Generar otra contraseña? (s/n): ").strip().lower()
            if repetir != 's':
                print("¡Gracias por usar el Generador de Contraseñas!")
                break
        except ValueError:
            print("Error: Introduce un número válido para la longitud.")

if __name__ == "__main__":
    main()
