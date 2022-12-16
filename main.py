from google.cloud import translate
from decouple import config

project_id = config("PROJECT_ID")
assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient()

sample_text = "Hello world!"
target_language_code = "tr"

response = client.translate_text(
    contents=[sample_text],
    target_language_code=target_language_code,
    parent=parent,
)

for translation in response.translations:
    print(translation.translated_text)