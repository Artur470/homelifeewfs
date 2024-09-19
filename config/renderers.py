from rest_framework.renderers import JSONRenderer
import json


class PrettyJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Если данные пусты, возвращаем стандартный ответ
        if data is None:
            return super().render(data, accepted_media_type, renderer_context)

        # Используем базовый рендерер для получения JSON-строки
        json_data = super().render(data, accepted_media_type, renderer_context)

        # Форматируем JSON с отступами
        return json.dumps(json.loads(json_data), indent=4, ensure_ascii=False).encode('utf-8')
