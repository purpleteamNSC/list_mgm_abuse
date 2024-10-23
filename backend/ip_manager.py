from pymongo import MongoClient
from flask import jsonify
import os

# Inicializando o cliente MongoDB
client = MongoClient(
    "mongo",
    27017,
    username=os.getenv("ME_CONFIG_MONGODB_ADMINUSERNAME"),
    password=os.getenv("ME_CONFIG_MONGODB_ADMINPASSWORD"),
)
db = client["abuse"]  # Nome do banco de dados


def add_ip(value, type, risk, notes, list):
    """Adiciona um IP único no banco de dados."""
    if db.ips.find_one({"value": value}):
        return jsonify({"error": "IP já existe"}), 409
    db.ips.insert_one(
        {
            "value": value,
            "type": type,
            "risk": risk,
            "notes": notes,
            "list": list,
        }
    )
    return jsonify({"message": "IP adicionado com sucesso"}), 201


def get_ip(value):
    """Busca um IP no banco de dados."""
    ip = db.ips.find_one({"value": value})
    if ip:
        ip["_id"] = str(ip["_id"])  # Converter ObjectId para string
        return jsonify(ip)
    return jsonify({"error": "IP não encontrado"}), 404


def get_all_ips(page=1, limit=100):
    """Pega todos os IPs com paginação."""
    ips = list(db.ips.find().skip((page - 1) * limit).limit(limit))
    if len(ips) != 0:
        # Converter ObjectId para string
        for ip in ips:
            ip["_id"] = str(ip["_id"])
        return jsonify(ips)
    return jsonify({"error": "Não existe IPs"}), 404


def delete_ip(value):
    """Deleta um IP do banco de dados."""
    result = db.ips.delete_one({"value": value})
    print(result)
    if result.deleted_count > 0:
        return jsonify({"message": "IP deletado com sucesso"}), 200
    return jsonify({"error": "IP não encontrado"}), 404


def delete_all_ips():
    """Deleta todos os IPs do banco de dados."""
    db.ips.delete_many({})
    return jsonify({"message": "Todos os IPs deletados com sucesso"}), 204
