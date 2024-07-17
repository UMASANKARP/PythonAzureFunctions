from opentelemetry.sdk.resources import Resource
from opentelemetry.semconv.resource import ResourceAttributes

from dynatrace.opentelemetry.tracing.api import configure_dynatrace

tracer_provider = configure_dynatrace(
    resource=Resource.create({"my.resource.attribute": "My Resource"})
)

#Importing other modules

import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

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
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Hence Python Demo Accomplished. Thanks team for giving such an nice task",
             status_code=200
        )
