from typing import Any
from re import match as regex_match
from requests import get as requests_get
from GoogleNews import GoogleNews
import global_vars

def is_valid_date(date : str):
    return bool(regex_match(global_vars.VALID_DATE_REGEX, date))

def clean_entry(item : Any):
    cookies={'CONSENT': global_vars.CONSENT_STRING}
    try:
        item['link'] = requests_get(f"http://{item['link']}", cookies=cookies).url
    except:
        return "EXCEPTION"
    return item

def generate_news(phrases : list, lang : str, start : str, end : str):
    gn = GoogleNews(lang = lang, start = start, end = end)
    for phrase in phrases:
        gn.get_news(phrase)
    ret = []
    for entry in gn.results():
        cleaned_entry = clean_entry(entry)
        if(cleaned_entry == "EXCEPTION"):
            continue
        else:
            ret.append(cleaned_entry)
    return ret