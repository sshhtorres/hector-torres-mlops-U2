from services.predictions_history import PredictionsHistory


class TestPredictionsHistory:

    def test_add_prediction_record(self):
        expected_max_len = 5

        record =  {
            "temperature": 36,
            "heart_rate": 120,
            "blood_pressure": 90,
            "prediction": "NO ENFERMO",
        }

        client = PredictionsHistory()
        for n in range(expected_max_len):
            client.add_prediction_record(**record)

        preds = client.get_predictions_history()
        assert len(preds) == expected_max_len, f"Expected {expected_max_len} records, got {len(preds)}"

        for n in range(expected_max_len):
            assert preds[n]["temperature"] == record["temperature"], f"Expected {record['temperature']}, got {preds[n]['temperature']}"
            assert preds[n]["heart_rate"] == record["heart_rate"], f"Expected {record['heart_rate']}, got {preds[n]['heart_rate']}"
            assert preds[n]["blood_pressure"] == record["blood_pressure"], f"Expected {record['blood_pressure']}, got {preds[n]['blood_pressure']}"
            assert preds[n]["prediction"] == record["prediction"], f"Expected {record['prediction']}, got {preds[n]['prediction']}"


    def test_clear_history(self):
        client = PredictionsHistory()
        
        record =  {
            "temperature": 36,
            "heart_rate": 120,
            "blood_pressure": 90,
            "prediction": "NO ENFERMO",
        }
        client.add_prediction_record(**record)

        client.clear_history()
        preds = client.get_predictions_history()
        assert len(preds) == 0, f"Expected 0 records, got {len(preds)}"


    def test_get_predictions_history(self):
        client = PredictionsHistory()

        record =  {
            "temperature": 36,
            "heart_rate": 120,
            "blood_pressure": 90,
            "prediction": "NO ENFERMO",
        }
        client.add_prediction_record(**record)

        preds = client.get_predictions_history()
        assert len(preds) == 1, f"Expected 1 record, got {len(preds)}"
