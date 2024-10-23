from flask import Flask, request

from ip_manager import add_ip, get_ip, get_all_ips, delete_ip, delete_all_ips

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Lista Abuse</h1>"


@app.route("/ip", methods=["POST"])
def create_ip():
    """Adiciona um novo IP."""
    data = request.json
    return add_ip(
        data["value"], data["type"], data["risk"], data["notes"], data["list"]
    )


@app.route("/ip/<ip_address>", methods=["GET"])
def read_ip(ip_address):
    """Busca um IP específico."""
    return get_ip(ip_address)


@app.route("/ips", methods=["GET"])
def read_all_ips():
    """Retorna todos os IPs com paginação."""
    page = int(request.args.get("page", 1))
    return get_all_ips(page)


@app.route("/ip/<ip_address>", methods=["DELETE"])
def remove_ip(ip_address):
    """Deleta um IP específico."""
    return delete_ip(ip_address)


@app.route("/ips", methods=["DELETE"])
def remove_all_ips():
    """Deleta todos os IPs."""
    return delete_all_ips()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
