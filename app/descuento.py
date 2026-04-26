def aplicar_descuento(precio, edad, cupon, intentos):
    if intentos >= 3:
        return "Bloqueado: Por exceso de intentos fallidos."
    
    if edad < 21:
        return "Error: Debes tener 21 años o mas para usar el cupon."
    
    if cupon != "DESCUENTO20":
        return "Error: Cupon invalido."
    
    precio_final = precio - precio * 0.20
    return precio_final