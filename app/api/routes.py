
from flask import Blueprint, jsonify, request

from app.models import MarvelHero, db

from .services import token_required

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/test', methods=['GET'])
def test():
    uverse = MarvelHero.query.all()[0]
    return jsonify(uverse.to_dict()), 200

# be able to read all data [GET]
# read a single heroes data [GET]
# create a animal? {POST}
# modify [POST]
# delete [DELETE]


@api.route('/marvel-heroes', methods=['GET'])
def marvel_heroes():
    """
    Getting all heroes from database and returning them as JSON data
    """

    heroes = MarvelHero.query.all()
    print(heroes)
    heroes = {a.id: a.to_dict() for a in heroes}
    return jsonify(heroes), 200


@api.route('/hero/<string:name>', methods=['GET'])
def getHeroName(name):
    print(name)
    hero = MarvelHero.query.filter_by(name=name.title()).first()
    if hero:
        return jsonify(hero.to_dict()), 200
    return jsonify({'error': f'No such animal with the name: {name.title()}'}), 404

@api.route('/create', methods=['POST'])
@token_required
def create_hero():
    """
    method: [POST]
    files nullable=false need to be included
    the rest are optional
    {
        "name":"Enrique Greene",
        "bio":"MMM"
    }
    """
    try:
        newdict = request.get_json()
        print(newdict)
        new_hero = MarvelHero(newdict)
        print(new_hero)
    except:
        return jsonify({'error': 'improper request or body data'}), 400
    try:
        db.session.add(new_hero)
        db.session.commit()
    except:
        return jsonify({'error': 'species already exists in the database'}), 400
    return jsonify({'created': new_hero.to_dict()}), 200



@api.route('/update/<string:id>')
@token_required
def updatedHero(id):
    try:
        newvals = request.get_json()
        hero = MarvelHero.query.get(id)
        hero.from_dict(newvals)
        db.session.commit()
        return jsonify({'Updated Hero': hero.to_dict()}), 200
    except:
        return jsonify({'Request failed': 'Invalid request or Hero-ID does not exist. '}), 400


@api.route('/delete/<string:id>', methods=['DELETE'])
@token_required
def removeHero(id):
    hero = MarvelHero.query.get(id)
    if not hero:
        return jsonify({'Remove failed': f'No animal with ID {id} in the database.'}), 400
    db.session.delete(hero)
    db.session.commit()
    return jsonify({'Removed hero': hero.to_dict()}), 200
