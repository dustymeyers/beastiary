from typing import Any, Dict, List
from flask import jsonify, request
from . import bp
from .utils import load_bestiary, get_monster

base_url = "https://www.dnd5eapi.co/api"
bestiary = load_bestiary(base_url)

@bp.route('/', methods=['GET'])
def get_bestiary() -> List[Dict[str, Any]]:
    return jsonify([monster.to_dict() for monster in bestiary])

@bp.route('/<string:index>', methods=['GET'])
def get_monster_by_index(index) -> Dict[str, Any]:
    monster = get_monster(base_url, index)
    if monster:
        return jsonify(monster.to_dict())
    else:
        return jsonify({"error": "Monster not found"}), 404
