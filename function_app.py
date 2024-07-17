from opentelemetry.sdk.resources import Resource
from opentelemetry.semconv.resource import ResourceAttributes
from dynatrace.opentelemetry.tracing.api import configure_dynatrace
import azure.functions as func
import logging
from dynatrace.opentelemetry.azure.functions import wrap_handler

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Configure Dynatrace and log the connection status
try:
    tracer_provider = configure_dynatrace(
        resource=Resource.create({ResourceAttributes.SERVICE_NAME: "FunctionAppDemopython"})
    )
    logging.info("Successfully configured Dynatrace tracing.")
except Exception as e:
    logging.error(f"Failed to configure Dynatrace tracing: {e}")

# Define the function app
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Wrap the function handler
@wrap_handler
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        response_message = f"Hello, {name}. This HTTP triggered function executed successfully."
    else:
        response_message = (
            "Hence Python Demo Accomplished. Thanks team for giving such a nice task"
        )

    logging.info("Sending metrics to Dynatrace.")
    # Example: Log the metrics sending status (assuming you have some way to track this)
    # Here we just log that the metrics sending is attempted, in a real-world scenario you might want to log
    # the actual status from Dynatrace API or SDK if available
    try:
        # Simulate metrics sending logic
        send_metrics_to_dynatrace()
        logging.info("Metrics sent to Dynatrace successfully.")
    except Exception as e:
        logging.error(f"Failed to send metrics to Dynatrace: {e}")

    return func.HttpResponse(response_message, status_code=200)

def send_metrics_to_dynatrace():
    # Placeholder for the logic to send metrics to Dynatrace
    # Implement the actual logic to send metrics here
    pass
