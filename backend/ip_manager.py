from pymongo import MongoClient
from flask import jsonify
import os
from datetime import datetime


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
    data = datetime.now().strftime("%d-%m-%Y- %H:%M:%S")
    if db.ips.find_one({"value": value}):
        return jsonify({"message": "dado ja existe"}), 409
    db.ips.insert_one(
        {
            "value": value,
            "type": type,
            "risk": risk,
            "notes": notes,
            "list": list,
            "date_sent": str(data) 
        }
    )
    return jsonify({"message": "ip adicionado"}), 201


def get_ip(value):
    """Busca um IP no banco de dados."""
    ip = db.ips.find_one({"value": value})
    if ip:
        ip["_id"] = str(ip["_id"])  # Converter ObjectId para string
        return jsonify(ip)
    return jsonify({"message": "sem dados"}), 404


def get_all_ips(page=1, limit=100):
    """Pega todos os IPs com paginação."""
    ips = list(db.ips.find().skip((page - 1) * limit).limit(limit))
    if len(ips) != 0:
        # Converter ObjectId para string
        for ip in ips:
            ip["_id"] = str(ip["_id"])
        return jsonify(ips)
    return jsonify({"message": "sem dados"}), 404


def delete_ip(value):
    """Deleta um IP do banco de dados."""
    result = db.ips.delete_one({"value": value})
    if result.deleted_count > 0:
        return jsonify({"message": "ip deletado com sucesso"}), 200
    return jsonify({"message": "sem dados"}), 404


def delete_all_ips():
    """Deleta todos os IPs do banco de dados."""
    db.ips.delete_many({})
    return jsonify({"message": "todos os dados deletados com sucesso"}), 200
