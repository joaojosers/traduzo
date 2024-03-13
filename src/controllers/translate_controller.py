from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET"])
def index():
    languages = LanguageModel.list_dicts()
    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


# translate_controller = Blueprint("translate", __name__)
@translate_controller.route("/", methods=["POST"])
def translate_text():
    # Receber parâmetros do corpo da solicitação
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    # Realizar a tradução do texto
    translated_text = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    # Retornar o texto traduzido
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated_text,
    )


# @translate_controller.route("/", methods=["POST"])
# def translate_text():
#     # Receber parâmetros do corpo da solicitação
#     text_to_translate = request.form.get("text_to_translate")
#     translate_from = request.form.get("translate_from")
#     translate_to = request.form.get("translate_to")

#     # Realizar a tradução do texto
#     translated_text = GoogleTranslator(
#         source=translate_from, target=translate_to
#     ).translate(text_to_translate)

#     # Retornar o texto traduzido
#     # return jsonify({"translated": translated_text})
#     return render_template(
#         "index.html",
#         text_to_translate=text_to_translate,
#         translate_from=translate_from,
#         translate_to=translate_to,
#         translated=translated_text
#         # languages = LanguageModel.list_dicts()
#     )
