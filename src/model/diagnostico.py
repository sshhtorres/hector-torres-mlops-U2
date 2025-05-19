CATS = {
    0: "NO ENFERMO",
    1: "ENFERMEDAD LEVE",
    2: "ENFERMEDAD AGUDA",
    3: "ENFERMEDAD CRÓNICA",
    4: "ENFERMEDAD TERMINAL",
}


def predict(temperature: float, heart_rate: int, blood_pressure: int) -> str:
    """
    predecir las siguientes categorías de condición de enfermedad de un paciente a partir de la temperatura, el ritmo cardiaco, y la presión sanguínea:
    - "NO ENFERMO"
    - "ENFERMEDAD LEVE"
    - "ENFERMEDAD AGUDA"
    - "ENFERMEDAD CRÓNICA"
    - "ENFERMEDAD TERMINAL"

    NOTA: LA SIGUIENTE ES UNA FUNCIÓN SIN NINGÚN SUSTENTO MÉDICO, SOLO ES UN MOCK DE UN MODELO DE CLASIFICACIÓN.
    """

    if temperature < 35.0 and heart_rate < 60 and blood_pressure < 90:
        return CATS[4]
    elif temperature < 35.0 or heart_rate < 60 or blood_pressure < 90:
        return CATS[3]
    elif temperature > 38.0 and heart_rate > 100:
        return CATS[2]
    elif temperature > 37.0 and heart_rate > 90:
        return CATS[1]
    elif blood_pressure > 140:
        return CATS[3]
    else:
        return CATS[0]
