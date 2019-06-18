from flask_injector import inject
from services.cleartext import ClearText


@inject
def lemmatize(clear: ClearText, search_string) -> tuple:
    result = clear.clear_text(search_string)
    return {'lemma': result}, 200
