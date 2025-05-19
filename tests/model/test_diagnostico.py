from model.diagnostico import predict


def test_predict():
    test_cases = [
        (36, 120, 90, "NO ENFERMO"),
        (34.9, 59, 89, "ENFERMEDAD TERMINAL"),
        (34.9, 120, 90, "ENFERMEDAD CRÓNICA"),
        (36, 59, 90, "ENFERMEDAD CRÓNICA"),
        (36, 120, 89, "ENFERMEDAD CRÓNICA"),
        (38.5, 120, 90, "ENFERMEDAD AGUDA"),
        (38, 120, 90, "ENFERMEDAD LEVE"),
        # (38, 120, 90, "ERROR EN PRUEBAS"),  # error intencional para comprobar el manejo de errores
    ]

    for temperature, heart_rate, blood_pressure, expected in test_cases:
        result = predict(temperature, heart_rate, blood_pressure)
        assert result == expected, f"Expected {expected}, but got {result} for input ({temperature}, {heart_rate}, {blood_pressure})"
