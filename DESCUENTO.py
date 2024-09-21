def calcular_total_compra(productos, porcentaje_descuento=20):
    """
    Calcula el total de una compra.

    Parámetros:
    productos (lista): Lista de productos con cantidad, precio unitario y nombre.
    porcentaje_descuento (int, opcional): Porcentaje de descuento (default: 20).

    Retorna:
    float: Total de la compra.
    """
    subtotal = 0
    print("Factura:")
    for producto in productos:
        cantidad = producto[0]
        precio_unitario = producto[1]
        nombre_producto = producto[2]
        subtotal_producto = cantidad * precio_unitario
        subtotal += subtotal_producto
        print(f"Producto: {nombre_producto}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio Unitario: ${precio_unitario:.2f}")
        print(f"Subtotal: ${subtotal_producto:.2f}")
        print("")

    descuento = (subtotal / 100) * porcentaje_descuento
    total = subtotal - descuento

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento ({porcentaje_descuento}%): ${descuento:.2f}")
    print(f"Total: ${total:.2f}")

    return total

def main():
    # Ejemplo de productos
    productos = [
        [2, 1.99, "Azúcar"],
        [3, 2.49, "Arroz"],
        [1, 1.29, "Tallarín"]
    ]

    calcular_total_compra(productos)

if __name__ == "__main__":
    main()

#En este codigo:
#Lafunción calcular_total_compra calcula el subtotal de cada producto y suma al subtotal total.
#Se imprime la factura con detalles de cada producto y total final.
#Se calcula el descuento aplicando el porcentaje al subtotal total.

#imprimir el ahorro total del los tres productos azucar, arroz,tallarin
# Precios y cantidades de los productos
azucar_precio = 1.99
azucar_cantidad = 2
arroz_precio = 2.49
arroz_cantidad = 3
tallarin_precio = 1.29
tallarin_cantidad = 1

# Cálculo de subtotales
azucar_subtotal = azucar_precio * azucar_cantidad
arroz_subtotal = arroz_precio * arroz_cantidad
tallarin_subtotal = tallarin_precio * tallarin_cantidad

# Cálculo de descuentos (20%)
porcentaje_descuento = 20
azucar_descuento = azucar_subtotal * (porcentaje_descuento / 100)
arroz_descuento = arroz_subtotal * (porcentaje_descuento / 100)
tallarin_descuento = tallarin_subtotal * (porcentaje_descuento / 100)

# Cálculo de ahorro total
ahorro_total = azucar_descuento + arroz_descuento + tallarin_descuento

# Imprimir resultados
print("Ahorro total: $ {:.2f}".format(ahorro_total))
