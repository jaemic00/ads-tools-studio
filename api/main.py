#Imports
import global_vars
from fastapi import FastAPI, HTTPException
from ojrson_response import ORJSONResponse
from modules.news_functions import generate_news, is_valid_date

api = FastAPI(default_response_class=ORJSONResponse)

@api.get("/")
async def root():
    raise HTTPException(status_code=401, detail="Requests for root are not supported!")

@api.get("/articles/")
async def read_item(phrases : str = "",
                    lang: str = global_vars.DEFAULT_LANG,
                    start: str = global_vars.DEFAULT_START,
                    end : str = global_vars.DEFAULT_END):
    phrases = phrases.split(sep=",")
    if len(phrases) == 1 and phrases[0] == "":
        raise HTTPException(status_code=410, detail=f"Please provide at least one phrase.")
    if not (lang in global_vars.ISO_LANGUAGE_CODES):
        raise HTTPException(status_code=410, detail=f"Lang {lang} is invalid. Please provide a correct ISO 639-1 language code.")
    if not is_valid_date(start):
        raise HTTPException(status_code=410, detail=f"Startdate {start} is invalid. Please provide a correct date in dd/mm/rrrr format.")
    if not is_valid_date(end):
        raise HTTPException(status_code=410, detail=f"Enddate {end} is invalid. Please provide a correct date in dd/mm/rrrr format.")
    return generate_news(phrases, lang, start, end)
