## File: app/routes.py

from .models import Event
from .extensions import db
from flask import Blueprint, request, jsonify

api_bp = Blueprint('api', __name__, template_folder='../templates')


@api_bp.route('/')
def index():
    from flask import render_template
    return render_template('index.html')


@api_bp.route('/api/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([e.to_dict() for e in events])

@api_bp.route('/api/events', methods=['POST'])
def create_event():
    data = request.get_json()
    if not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400

    new_event = Event(title=data['title'], description=data.get('description'))
    db.session.add(new_event)
    db.session.commit()
    return jsonify(new_event.to_dict()), 201

@api_bp.route('/api/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    data = request.get_json()

    event.title = data.get('title', event.title)
    event.description = data.get('description', event.description)

    db.session.commit()
    return jsonify(event.to_dict())

@api_bp.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return '', 204