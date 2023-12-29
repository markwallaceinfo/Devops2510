
# rest_app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)

@app.route('/users/<int:user_id>', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_user_request(user_id):
    try:
        if request.method == 'POST':
            user_name = request.json.get('user_name')
            if User.query.get(user_id):
                return jsonify({"status": "error", "reason": "id already exists"}), 500
            new_user = User(id=user_id, user_name=user_name)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"status": "ok", "user_added": user_name}), 200

        elif request.method == 'GET':
            user = User.query.get(user_id)
            if user:
                return jsonify({"status": "ok", "user_name": user.user_name}), 200
            else:
                return jsonify({"status": "error", "reason": "no such id"}), 500

        elif request.method == 'PUT':
            user_name = request.json.get('user_name')
            user = User.query.get(user_id)
            if user:
                user.user_name = user_name
                db.session.commit()
                return jsonify({"status": "ok", "user_updated": user_name}), 200
            else:
                return jsonify({"status": "error", "reason": "no such id"}), 500

        elif request.method == 'DELETE':
            user = User.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return jsonify({"status": "ok", "user_deleted": user_id}), 200
            else:
                return jsonify({"status": "error", "reason": "no such id"}), 500

    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500