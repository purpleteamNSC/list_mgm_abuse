from pymongo import MongoClient
from flask import jsonify
import os

# Inicializando o cliente MongoDB
client = MongoClient('mongo', 27017, username=os.getenv('ME_CONFIG_MONGODB_ADMINUSERNAME'), password=os.getenv('ME_CONFIG_MONGODB_ADMINPASSWORD'))
db = client['myDatabase']  # Nome do banco de dados

def add_ip(ip_address):
    """Adiciona um IP único no banco de dados."""
    if db.ips.find_one({"ip": ip_address}):
        return jsonify({"error": "IP já existe"}), 409
    db.ips.insert_one({"ip": ip_address})
    return jsonify({"message": "IP adicionado com sucesso"}), 201

def get_ip(ip_address):
    """Busca um IP no banco de dados."""
    ip = db.ips.find_one({"ip": ip_address})
    return jsonify(ip) if ip else jsonify({"error": "IP não encontrado"}), 404

def get_all_ips(page=1, limit=100):
    """Pega todos os IPs com paginação."""
    ips = list(db.ips.find().skip((page - 1) * limit).limit(limit))
    return jsonify(ips)

def delete_ip(ip_address):
    """Deleta um IP do banco de dados."""
    result = db.ips.delete_one({"ip": ip_address})
    if result.deleted_count > 0:
        return jsonify({"message": "IP deletado com sucesso"}), 204
    return jsonify({"error": "IP não encontrado"}), 404

def delete_all_ips():
    """Deleta todos os IPs do banco de dados."""
    db.ips.delete_many({})
    return jsonify({"message": "Todos os IPs deletados com sucesso"}), 204
