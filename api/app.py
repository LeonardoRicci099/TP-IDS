from flask import Flask, jsonify
from sqlalchemy.exc import SQLAlchemyError

import reservas

app = Flask(__name__)


@app.route("/api/v1/reservas", methods=["GET"])
def get_reservas():
    try:
        result = reservas.reservas_all()
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    response = []
    for row in result:
        response.append(
            jsonify(
                {
                    "ReservaID": row[0],
                    "Creacion": row[1],
                    "Desde": row[2],
                    "Hasta": row[3],
                    "CantNiños": row[4],
                    "CantAdultos": row[5],
                    "PrecioTotal": row[6],
                    "HabID": row[7],
                    "UsuarioID": row[8],
                }
            )
        )

    return jsonify(response), 200


@app.route("/api/v1/reservas/<int:res_id>", methods=["GET"])
def get_reservas_by_id(res_id):
    try:
        result = reservas.reservas_by_id(res_id)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

    if len(result) == 0:
        return jsonify({"error": "No se encontró ninguna reserva"}), 404

    result = result[0]
    return (
        jsonify(
            {
                "ReservaID": result[0],
                "Creacion": result[1],
                "Desde": result[2],
                "Hasta": result[3],
                "CantNiños": result[4],
                "CantAdultos": result[5],
                "PrecioTotal": result[6],
                "HabID": result[7],
                "UsuarioID": result[8],
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(port="5001", debug=True)
