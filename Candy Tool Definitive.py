import random
import string
from colorama import Fore, Style

def generar_nitros(cantidad):
    nitros = [f'https://discord.gift/{"".join(random.choices(string.ascii_letters + string.digits, k=16))}' for _ in range(cantidad)]
    return nitros

def generar_twitch(cantidad):
    codigos_twitch = [''.join(random.choices(string.ascii_lowercase + string.digits, k=30)) for _ in range(cantidad)]
    return codigos_twitch

def generar_steam(cantidad):
    codigos_steam = [''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' +
                     ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' +
                     ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(cantidad)]
    return codigos_steam

def generar_minecraft(cantidad):
    codigos_minecraft = [''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' +
                         ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' +
                         ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' +
                         ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' +
                         ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(cantidad)]
    return codigos_minecraft

def check_nitros(codigos):
    print("\nResultado del Checker Codigos Nitro:")
    for codigo in codigos:
        if random.random() < 0.0001:  # 0.01% de probabilidad de ser válido
            print(f"{codigo}: Válido")
        else:
            print(f"{codigo}: Inválido")

def check_twitch(codigos):
    print("\nResultado del Checker Codigos Twitch:")
    for codigo in codigos:
        if random.random() < 0.0001:
            print(f"{codigo}: Válido")
        else:
            print(f"{codigo}: Inválido")

def check_steam(codigos):
    print("\nResultado del Checker Codigos Steam:")
    for codigo in codigos:
        if random.random() < 0.0001:
            print(f"{codigo}: Válido")
        else:
            print(f"{codigo}: Inválido")

def check_minecraft(codigos):
    print("\nResultado del Checker Codigos Minecraft:")
    for codigo in codigos:
        if random.random() < 0.0001:
            print(f"{codigo}: Válido")
        else:
            print(f"{codigo}: Inválido")

def mostrar_logo():
    print(Fore.LIGHTMAGENTA_EX + r"  ___|   __ _   _ __     __| |  _   _    |_   _|   ___     ___   | |   |  _ \    ___  __      __   __ _   _ __    __| |  ___")
    print(r" | |      / _` | | '_ \   / _` | | | | |     | |    / _ \   / _ \  | |   | |_) |  / _ \ \ \ /\ / /  / _` | | '__|  / _` | / __|")
    print(r" | |___  | (_| | | | | | | (_| | | |_| |     | |   | (_) | | (_) | | |   |  _ <  |  __/  \ V  V /  | (_| | | |    | (_| | \__ \ ")
    print(r"  \____|  \__,_| |_| |_|  \__,_|  \__, |     |_|    \___/   \___/  |_|   |_| \_\  \___|   \_/\_/    \__,_| |_|     \__,_| |___/")
    print(r"                                |___/                                                                                        ")
    print(Fore.LIGHTMAGENTA_EX + "𝐁𝐲 𝐒𝐮𝐧𝐟𝐥𝐨𝐰𝐞𝐫/𝐒𝐚𝐚𝐰𝐧𝐲")
    print(Fore.LIGHTMAGENTA_EX + r".𝐜𝐚𝐧𝐝𝐲/𝐫𝐰" + Style.RESET_ALL)

def mostrar_menu():
    print("\nOPCIONES")
    print(Fore.LIGHTMAGENTA_EX + "GENERADORES" + " " * 50 + "CHECKERS" + " " * 34)
    print("[1] Generar códigos de Nitro" + " " * 7 + "[5] Checker Codigos Nitro")
    print("[2] Generar códigos de Twitch" + " " * 4 + "[6] Checker Codigos Twitch")
    print("[3] Generar códigos de Steam" + " " * 9 + "[7] Checker Codigos Steam")
    print("[4] Generar códigos de Minecraft" + " " * 3 + "[8] Checker Codigos Minecraft")
    print("[0] Salir")

def main():
    while True:
        mostrar_logo()
        mostrar_menu()

        opcion = input("\nElige una opción: ")

        if opcion == '1':
            cantidad = int(input("\nIngresa la cantidad de códigos de Nitro a generar: "))
            codigos_nitro = generar_nitros(cantidad)
            print("\nCódigos de Nitro generados:")
            for codigo in codigos_nitro:
                print(codigo)
            input("\nPresiona Enter para continuar...")
        elif opcion == '2':
            cantidad_codigos_twitch = int(input("\nIngresa la cantidad de códigos de Twitch a generar: "))
            codigos_twitch = generar_twitch(cantidad_codigos_twitch)
            print("\nCódigos de Twitch generados:")
            for codigo in codigos_twitch:
                print(codigo)
            input("\nPresiona Enter para continuar...")
        elif opcion == '3':
            cantidad_codigos_steam = int(input("\nIngresa la cantidad de códigos de Steam a generar: "))
            codigos_steam = generar_steam(cantidad_codigos_steam)
            print("\nCódigos de Steam generados:")
            for codigo in codigos_steam:
                print(codigo)
            input("\nPresiona Enter para continuar...")
        elif opcion == '4':
            cantidad_codigos_minecraft = int(input("\nIngresa la cantidad de códigos de Minecraft a generar: "))
            codigos_minecraft = generar_minecraft(cantidad_codigos_minecraft)
            print("\nCódigos de Minecraft generados:")
            for codigo in codigos_minecraft:
                print(codigo)
            input("\nPresiona Enter para continuar...")
        elif opcion == '5':
            cantidad_codigos_nitro_check = int(input("\nIngresa la cantidad de códigos de Nitro a checkear: "))
            codigos_nitro_check = generar_nitros(cantidad_codigos_nitro_check)
            check_nitros(codigos_nitro_check)
            input("\nPresiona Enter para continuar...")
        elif opcion == '6':
            cantidad_codigos_twitch_check = int(input("\nIngresa la cantidad de códigos de Twitch a checkear: "))
            codigos_twitch_check = generar_twitch(cantidad_codigos_twitch_check)
            check_twitch(codigos_twitch_check)
            input("\nPresiona Enter para continuar...")
        elif opcion == '7':
            cantidad_codigos_steam_check = int(input("\nIngresa la cantidad de códigos de Steam a checkear: "))
            codigos_steam_check = generar_steam(cantidad_codigos_steam_check)
            check_steam(codigos_steam_check)
            input("\nPresiona Enter para continuar...")
        elif opcion == '8':
            cantidad_codigos_minecraft_check = int(input("\nIngresa la cantidad de códigos de Minecraft a checkear: "))
            codigos_minecraft_check = generar_minecraft(cantidad_codigos_minecraft_check)
            check_minecraft(codigos_minecraft_check)
            input("\nPresiona Enter para continuar...")
        elif opcion == '0':
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
