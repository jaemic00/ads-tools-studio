from orjson import dumps as orjson_dumps
from fastapi.responses import JSONResponse
from typing import Any
class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        return orjson_dumps(content)