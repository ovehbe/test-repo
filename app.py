import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

GREETINGS = {
    "en": "Hello",
    "es": "Hola",
    "fr": "Bonjour",
    "de": "Hallo",
    "ar": "مرحبا",
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        lang = self.path.strip("/") or "en"
        greeting = GREETINGS.get(lang, GREETINGS["en"])
        logging.info("Request: lang=%s greeting=%s", lang, greeting)

        payload = json.dumps({"language": lang, "greeting": greeting})

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(payload.encode())


def main():
    server = HTTPServer(("localhost", 8000), Handler)
    print("Serving on http://localhost:8000")
    server.serve_forever()


if __name__ == "__main__":
    main()
