"""Servidor local para CuidAM Frames. Detener con Ctrl+C."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    handler = partial(SimpleHTTPRequestHandler, directory=str(root))
    with ThreadingHTTPServer(("0.0.0.0", 8766), handler) as server:
        print("CuidAM Frames: http://localhost:8766")
        print("En otro equipo: http://IP_LOCAL_DEL_SERVIDOR:8766")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")
