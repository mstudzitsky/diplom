from flask_injector import inject
from services.models import Models
from services.cleartext import ClearText


@inject
def predict_service_id(model: Models, clear: ClearText,  search_string) -> tuple:
    clear_text = clear.clear_text(search_string)
    service_id, service_name = model.predict(clear_text)
    return {
                'service_id': int(service_id),
                'service_name': service_name
           }, 200
