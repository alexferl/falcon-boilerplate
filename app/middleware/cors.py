from app.config import settings


class CrossDomain:
    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header("Access-Control-Allow-Origin",
                        settings.get("ACCESS_CONTROL_ALLOW_ORIGIN"))
        resp.set_header("Access-Control-Allow-Methods",
                        settings.get("ACCESS_CONTROL_ALLOW_METHODS"))
        resp.set_header("Access-Control-Allow-Credentials",
                        settings.get("ACCESS_CONTROL_ALLOW_CREDENTIALS"))
        resp.set_header("Access-Control-Allow-Headers",
                        settings.get("ACCESS_CONTROL_ALLOW_HEADERS"))
