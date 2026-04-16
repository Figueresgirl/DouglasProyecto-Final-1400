import json
import time
import sys

COSTO_POR_HORA = 25
COSTO_RECOGIDA = 10
COSTO_URGENTE = 20
ARCHIVO = "datos.json"


class CentroDeRecepcionST:
    def __init__(self):
        self.cliente = ""

    def iniciar(self):
        self.cliente = input("[Centro de Recepcion ST]: Ingrese su nombre: ").strip()

        if not self.cliente:
            self.cliente = "Cliente"

        while True:
            try:
                opcion = self.menu()

                if opcion == "1":
                    self.revisar()
                elif opcion == "2":
                    self.reparar()
                elif opcion == "3":
                    self.donar()
                elif opcion == "4":
                    print(f"[Centro de Recepcion ST]: Gracias por su visita, {self.cliente}")
                    sys.exit()
                else:
                    print("[Centro de Recepcion ST]: Opción no válida")

            except Exception as e:
                print("[Centro de Recepcion ST]: Error controlado:", e)

    def menu(self):
        print("\n=== Centro de Recepcion ST ===")
        print(f"[Centro de Recepcion ST]: Bienvenido/a {self.cliente}")
        print("[Centro de Recepcion ST]: Seleccione una opción")
        print("1. Revisar")
        print("2. Reparar")
        print("3. Donar")
        print("4. Salir")
        return input(f"[{self.cliente}]: ").strip()

    def continuar(self):
        opcion = input(
            f"\n[Centro de Recepcion ST]: {self.cliente}, ¿desea algo más? (s/n): "
        ).strip().lower()

        if opcion != "s":
            print(f"[Centro de Recepcion ST]: Gracias por su visita, {self.cliente}")
            return False
        return True

    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje).strip())
            except ValueError:
                print("[Centro de Recepcion ST]: Ingrese un número válido.")

    def pedir_año(self):
        while True:
            año = self.pedir_entero(f"{self.cliente}, ingrese el año del dispositivo: ")
            if 1980 <= año <= 2100:
                return año
            print("[Centro de Recepcion ST]: Ingrese un año razonable.")

    def generar_ticket(self):
        return f"T-{int(time.time())}"

    def pedir_metodo_entrega(self, permitir_urgente=True):
        print(f"\n[Centro de Recepcion ST]: {self.cliente}, seleccione el método de entrega")
        print("1. Llevar equipo (Gratis)")
        print("2. Recogida a domicilio ($10)")
        if permitir_urgente:
            print("3. Servicio urgente ($20)")

        opciones_validas = ["1", "2", "3"] if permitir_urgente else ["1", "2"]

        while True:
            opcion = input(f"{self.cliente}, seleccione una opción: ").strip()
            if opcion in opciones_validas:
                break
            print("[Centro de Recepcion ST]: Opción inválida")

        if opcion == "1":
            return {
                "metodo_entrega": "Cliente lleva el equipo",
                "costo_entrega": 0,
                "fecha_servicio": input(f"{self.cliente}, indique la fecha de entrega: ").strip()
            }
        elif opcion == "2":
            return {
                "metodo_entrega": "Recogida a domicilio",
                "costo_entrega": COSTO_RECOGIDA,
                "fecha_servicio": input(f"{self.cliente}, indique la fecha de recogida: ").strip(),
                "direccion_recogida": input(f"{self.cliente}, indique la dirección de recogida: ").strip()
            }
        else:
            return {
                "metodo_entrega": "Servicio urgente",
                "costo_entrega": COSTO_URGENTE,
                "fecha_servicio": input(f"{self.cliente}, indique la fecha del servicio urgente: ").strip(),
                "direccion_recogida": input(f"{self.cliente}, indique la dirección: ").strip()
            }

    def guardar(self, datos):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                contenido = json.load(archivo)
                if not isinstance(contenido, list):
                    contenido = []
        except (FileNotFoundError, json.JSONDecodeError):
            contenido = []

        contenido.append(datos)

        with open(ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(contenido, archivo, indent=4, ensure_ascii=False)

    def informe(self, datos):
        print("\n--- INFORME / TICKET ---")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")

    # -------------------------
    # REVISAR
    # -------------------------
    def revisar(self):
        print(f"\n[Centro de Recepcion ST]: {self.cliente}, vamos a registrar la revisión de su dispositivo.")

        tipo = input(f"{self.cliente}, ingrese el tipo de dispositivo: ").strip()
        marca = input(f"{self.cliente}, ingrese la marca: ").strip()
        modelo = input(f"{self.cliente}, ingrese el modelo: ").strip()
        año = self.pedir_año()
        problema = input(f"{self.cliente}, describa el problema: ").strip()

        entrega = self.pedir_metodo_entrega(permitir_urgente=False)

        ticket = self.generar_ticket()
        costo_total = COSTO_POR_HORA + entrega["costo_entrega"]

        datos = {
            "ticket": ticket,
            "cliente": self.cliente,
            "servicio": "Revisión",
            "tipo": tipo,
            "marca": marca,
            "modelo": modelo,
            "año": año,
            "problema": problema,
            "horas_estimadas": 1,
            "costo_por_hora": COSTO_POR_HORA,
            "metodo_entrega": entrega["metodo_entrega"],
            "costo_entrega": entrega["costo_entrega"],
            "fecha_servicio": entrega["fecha_servicio"],
            "costo_total": costo_total
        }

        if "direccion_recogida" in entrega:
            datos["direccion_recogida"] = entrega["direccion_recogida"]

        self.guardar(datos)
        self.informe(datos)

        print(f"\n[Centro de Recepcion ST]: {self.cliente}, se recomienda proceder con la reparación si el diagnóstico lo confirma.")
        print("[Centro de Recepcion ST]: El costo final puede variar según la evaluación técnica.")

        continuar_reparacion = input(
            f"{self.cliente}, ¿desea continuar con la reparación? (s/n): "
        ).strip().lower()

        if continuar_reparacion == "s":
            self.reparar()
            return

        if not self.continuar():
            sys.exit()

    # -------------------------
    # REPARAR
    # -------------------------
    def reparar(self):
        print(f"\n[Centro de Recepcion ST]: {self.cliente}, seleccione el tipo de reparación")
        print("1. Pantalla")
        print("2. Batería")
        print("3. Sistema")
        print("4. No enciende")

        while True:
            opcion = input(f"{self.cliente}, seleccione una opción: ").strip()
            if opcion in ["1", "2", "3", "4"]:
                break
            print("[Centro de Recepcion ST]: Opción inválida")

        if opcion == "1":
            problema, horas = "Pantalla", 2
        elif opcion == "2":
            problema, horas = "Batería", 1.5
        elif opcion == "3":
            problema, horas = "Sistema", 2
        else:
            problema, horas = "No enciende", 3

        entrega = self.pedir_metodo_entrega(permitir_urgente=True)

        costo_total = (horas * COSTO_POR_HORA) + entrega["costo_entrega"]
        ticket = self.generar_ticket()

        datos = {
            "ticket": ticket,
            "cliente": self.cliente,
            "servicio": "Reparación",
            "problema": problema,
            "horas_estimadas": horas,
            "costo_por_hora": COSTO_POR_HORA,
            "metodo_entrega": entrega["metodo_entrega"],
            "costo_entrega": entrega["costo_entrega"],
            "fecha_servicio": entrega["fecha_servicio"],
            "costo_estimado": costo_total
        }

        if "direccion_recogida" in entrega:
            datos["direccion_recogida"] = entrega["direccion_recogida"]

        self.informe(datos)

        confirmar = input(
            f"{self.cliente}, ¿desea confirmar la reparación? (s/n): "
        ).strip().lower()

        if confirmar != "s":
            print(f"[Centro de Recepcion ST]: Operación cancelada, {self.cliente}")
            if not self.continuar():
                sys.exit()
            return

        self.guardar(datos)
        print(f"\n[Centro de Recepcion ST]: Reparación registrada con ticket {ticket}.")

        if not self.continuar():
            sys.exit()

    # -------------------------
    # DONAR
    # -------------------------
    def donar(self):
        print(f"\n[Centro de Recepcion ST]: Gracias {self.cliente} por considerar la donación de su equipo.")

        tipo = input(f"{self.cliente}, ingrese el tipo de dispositivo: ").strip()
        marca = input(f"{self.cliente}, ingrese la marca: ").strip()
        modelo = input(f"{self.cliente}, ingrese el modelo: ").strip()
        año = self.pedir_año()
        estado = input(f"{self.cliente}, describa el estado del equipo: ").strip()

        print(f"\n[Centro de Recepcion ST]: ¿Qué planea hacer con el equipo?")
        print("1. Donarlo para que otra persona lo use")
        print("2. Reciclarlo")
        print("3. Evaluar si puede actualizarse para nuevo uso")
        print("4. No estoy seguro/a, necesito recomendación")

        while True:
            destino = input(f"{self.cliente}, seleccione una opción: ").strip()
            if destino in ["1", "2", "3", "4"]:
                break
            print("[Centro de Recepcion ST]: Opción inválida")

        if destino == "1":
            plan_equipo = "Donarlo para reutilización"
        elif destino == "2":
            plan_equipo = "Reciclar el equipo"
        elif destino == "3":
            plan_equipo = "Evaluar actualización para nuevo uso"
        else:
            plan_equipo = "Solicita recomendación técnica"

        print(f"\n[Centro de Recepcion ST]: ¿Desea servicio de recogida para la donación?")
        print("1. Entregar personalmente")
        print("2. Solicitar recogida a domicilio")

        while True:
            opcion_entrega = input(f"{self.cliente}, seleccione una opción: ").strip()
            if opcion_entrega in ["1", "2"]:
                break
            print("[Centro de Recepcion ST]: Opción inválida")

        if opcion_entrega == "1":
            metodo_entrega = "Entrega en local"
            costo_entrega = 0
            fecha_servicio = input(f"{self.cliente}, indique la fecha de entrega: ").strip()
            direccion_recogida = ""
        else:
            metodo_entrega = "Recogida a domicilio"
            costo_entrega = COSTO_RECOGIDA
            fecha_servicio = input(f"{self.cliente}, indique la fecha de recogida: ").strip()
            direccion_recogida = input(f"{self.cliente}, indique la dirección de recogida: ").strip()

        desea_borrado = input(
            f"{self.cliente}, ¿desea borrado seguro de datos? (s/n): "
        ).strip().lower()
        borrado_datos = "Sí" if desea_borrado == "s" else "No"

        ticket = self.generar_ticket()

        datos = {
            "ticket": ticket,
            "cliente": self.cliente,
            "servicio": "Donación",
            "tipo": tipo,
            "marca": marca,
            "modelo": modelo,
            "año": año,
            "estado": estado,
            "plan_para_el_equipo": plan_equipo,
            "metodo_entrega": metodo_entrega,
            "costo_entrega": costo_entrega,
            "fecha_servicio": fecha_servicio,
            "borrado_seguro_datos": borrado_datos
        }

        if direccion_recogida:
            datos["direccion_recogida"] = direccion_recogida

        self.guardar(datos)
        self.informe(datos)

        print(f"\n[Centro de Recepcion ST]: Donación registrada con ticket {ticket}.")

        if plan_equipo == "Reciclar el equipo":
            print("[Centro de Recepcion ST]: Su equipo será procesado de manera responsable para minimizar el impacto ambiental.")
        elif plan_equipo == "Evaluar actualización para nuevo uso":
            print("[Centro de Recepcion ST]: Evaluaremos su equipo para extender su vida útil mediante actualización tecnológica.")
        elif plan_equipo == "Donarlo para reutilización":
            print("[Centro de Recepcion ST]: Su equipo podrá tener una segunda vida útil ayudando a otra persona.")

        print("[Centro de Recepcion ST]: Gracias por preocuparse por la sostenibilidad y la salud del planeta.")

        if not self.continuar():
            sys.exit()


if __name__ == "__main__":
    app = CentroDeRecepcionST()
    app.iniciar()
