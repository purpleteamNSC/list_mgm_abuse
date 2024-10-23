from flask import Flask

app = Flask(__name__)

dados = {
    "meta": {"generatedAt": "2020-09-24T19:54:11+00:00"},
    "data": [
        {
            "ipAddress": "5.188.10.179",
            "abuseConfidenceScore": 100,
            "lastReportedAt": "2020-09-24T19:17:02+00:00",
        },
        {
            "ipAddress": "185.222.209.14",
            "abuseConfidenceScore": 100,
            "lastReportedAt": "2020-09-24T19:17:02+00:00",
        },
        {
            "ipAddress": "191.96.249.183",
            "abuseConfidenceScore": 100,
            "lastReportedAt": "2020-09-24T19:17:01+00:00",
        },
    ],
}


@app.route("/")
def home():
    return dados['data']


@app.route("/ip/<ip>")
def abuse(ip):
    ips = ["1.1.1.1"]
    if ip in ips:
        return "IP ja existe"

    return f"IP Adicionado: {ip}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
