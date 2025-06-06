import azure.functions as func
import requests
import logging
import json

app = func.FunctionApp()

@app.route(route="GetUSDtoINR", auth_level=func.AuthLevel.FUNCTION)
def GetUSDtoINR(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Fetching USD to INR exchange rate.')

    try:
        # Free exchange rate API (you can use your API key for higher limits)
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        inr_rate = data["rates"]["INR"]

        return func.HttpResponse(
            json.dumps({"Today rate of 1 USD_to_INR": inr_rate}),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        logging.error(f"Error fetching exchange rate: {e}")
        return func.HttpResponse("Failed to retrieve exchange rate.", status_code=500)
