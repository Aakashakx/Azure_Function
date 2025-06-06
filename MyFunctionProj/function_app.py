import azure.functions as func
import requests
import logging
import json
from datetime import datetime, timedelta

app = func.FunctionApp()

@app.route(route="GetUSDINRHistory", auth_level=func.AuthLevel.FUNCTION)
def GetUSDINRHistory(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Fetching last 10 days USD to INR exchange rates.')

    try:
        end_date = datetime.today()
        start_date = end_date - timedelta(days=10)

        url = (
            f"https://api.exchangerate.host/timeseries"
            f"?start_date={start_date.date()}&end_date={end_date.date()}"
            f"&base=USD&symbols=INR"
        )

        response = requests.get(url)
        data = response.json()

        if not data.get("success"):
            raise Exception("API returned failure")

        rates = data.get("rates", {})

        return func.HttpResponse(
            json.dumps(rates, indent=2),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error fetching exchange rate history: {e}")
        return func.HttpResponse("Failed to retrieve exchange rate history.", status_code=500)
