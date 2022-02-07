from random import randint
from datetime import date

DATE_V = "%Y%m%d"
CONSENT_STRING = f"YES+cb.{date.today().strftime(DATE_V)}-17-p0.en-GB+FX+{randint(100, 999)}"
VALID_DATE_REGEX = r"^(?:(?:31(\/)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$"
LANGUAGES = [('vi', 'Vietnamese'), ('ku', 'Kurdish'), ('ne', 'Nepali'), ('te', 'Telugu'), ('ru', 'Russian'), ('ar', 'Arabic'), ('ta', 'Tamil'), ('lv', 'Latvian'), ('el', 'Greek'), ('az', 'Azerbaijani'), ('hy', 'Armenian'), ('pa', 'Panjabi; Punjabi'), ('fr', 'French'), ('cy', 'Welsh'), ('bo', 'Tibetan'), ('ms', 'Malay'), ('sl', 'Slovenian'), ('bs', 'Bosnian'), ('tl', 'Tagalog'), ('tr', 'Turkish'), ('eu', 'Basque'), ('lt', 'Lithuanian'), ('en', 'English'), ('fi', 'Finnish'), ('sq', 'Albanian'), ('cs', 'Czech'), ('cv', 'Chuvash'), ('de', 'German'), ('Ga', 'Georgian'), ('ga', 'Irish'), ('hu', 'Hungarian'), ('rm', 'Romansh'), ('no', 'Norwegian'), ('th', 'Thai'), ('be', 'Belarusian'), ('fa', 'Persian'), ('uz', 'Uzbek'), ('sr', 'Serbian'), ('sw', 'Swahili'), ('zh', 'Chinese'), ('pl', 'Polish'), ('hr', 'Croatian'), ('pt', 'Portuguese'), ('af', 'Afrikaans'), ('ko', 'Korean'), ('nl', 'Dutch; Flemish'), ('it', 'Italian'), ('sv', 'Swedish'), ('my', 'Burmese'), ('is', 'Icelandic'), ('mk', 'Macedonian'), ('sk', 'Slovak'), ('es', 'Spanish'), ('ja', 'Japanese'), ('ro', 'Romanian'), ('bg', 'Bulgarian'), ('he', 'Hebrew'), ('eo', 'Esperanto'), ('uk', 'Ukrainian'), ('id', 'Indonesian'), ('ka', 'Georgian'), ('hi', 'Hindi'), ('mr', 'Marathi'), ('et', 'Estonian'), ('da', 'Danish'), ('ca', 'Catalan; Valencian'), ('mn', 'Mongolian')]
ISO_LANGUAGE_CODES = [item[0] for item in LANGUAGES]

DEFAULT_START = '01/01/2000'
DEFAULT_END = date.today().strftime("%d/%m/%Y")
DEFAULT_LANG = 'en'