from datetime import datetime


class PredictionsHistory:
    history = []

    def add_prediction_record(self, temperature: float, heart_rate: int, blood_pressure: int, prediction: str):
        """
        Agrega una predicción a la lista de historial de máximo 5 elementos.
        """

        if len(self.history) == 5:
            self.history.pop(0)

        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "temperature": temperature,
            "heart_rate": heart_rate,
            "blood_pressure": blood_pressure,
            "prediction": prediction,
        })


    def clear_history(self):
        self.history.clear()


    def get_predictions_history(self):
        return self.history

