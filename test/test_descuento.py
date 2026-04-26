from app.descuento import aplicar_descuento

# 1 . Caso de exito
def test_descuento_exitoso():
    assert aplicar_descuento(1000, 21, "DESCUENTO20", 1) == 800

# 2 .  Caso de error
def test_descuento_error_edad():
    assert aplicar_descuento(1000, 20, "DESCUENTO20", 1) == "Error: Debes tener 21 años o mas para usar el cupon."

# 2 . 1.  Caso de error
def test_descuento_error_cupon():
    assert aplicar_descuento(1000, 21, "DESCUENTO10", 1) == "Error: Cupon invalido."

# 3 . Caso border 
def test_descuento_error_bloqueo():
    assert aplicar_descuento(1000, 21, "DESCUENTO20", 4) == "Bloqueado: Por exceso de intentos fallidos."