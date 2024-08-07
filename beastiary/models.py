from typing import Any, Dict, Optional
from typing import List


class Monster:

    # {
    # 'index': 'commoner', 
    # 'url': '/api/monsters/commoner',
    # 'name': 'Commoner',
    #
    # 'desc': 'Commoners include peasants, serfs, slaves, servants, pilgrims, merchants, artisans, and hermits.',
    # 'size': 'Medium', 'type': 'humanoid', 'subtype': 'any race', 'alignment': 'any alignment', 
    # 'armor_class': [{...}], 'hit_points': 4, 'hit_dice': '1d8', 'hit_points_roll': '1d8', 
    # 'speed': {'walk': '30 ft.'}, 'strength': 10, 'dexterity': 10, 'constitution': 10, 
    # 'intelligence': 10, 'wisdom': 10, 'charisma': 10, 'proficiencies': [], 'damage_vulnerabilities': [], 
    # 'damage_resistances': [], 'damage_immunities': [], 'condition_immunities': [], 
    # 'senses': {'passive_perception': 10}, 
    # 'languages': 'any one language (usually Common)', 'challenge_rating': 0, 'proficiency_bonus': 2, 'xp': 10, 
    # 'actions': [{...}],  'legendary_actions': [], 'special_abilities': []
    # }


    def __init__(self, data: Dict[str, Any]):
        self.index = data['index']
        self.url = data['url']
        self.name = data['name']
        self.desc: Optional[str] = data.get('desc')
        self.size: Optional[str] = data.get('size')
        self.type: Optional[str] = data.get('type')
        self.subtype: Optional[str] = data.get('subtype')
        self.alignment: Optional[str] = data.get('alignment')
        self.armor_class: Optional[Dict[str, Any]] = data.get('armor_class')
        self.hit_points: Optional[int] = data.get('hit_points')
        self.hit_dice: Optional[str] = data.get('hit_dice')
        self.hit_points_roll: Optional[str] = data.get('hit_points_roll')
        self.speed: Optional[Dict[str, str]] = data.get('speed')
        self.strength: Optional[int] = data.get('strength')
        self.dexterity: Optional[int] = data.get('dexterity')
        self.constitution: Optional[int] = data.get('constitution')
        self.intelligence: Optional[int] = data.get('intelligence')
        self.wisdom: Optional[int] = data.get('wisdom')
        self.charisma: Optional[int] = data.get('charisma')
        self.proficiencies: Optional[List[str]] = data.get('proficiencies')
        self.damage_vulnerabilities: Optional[List[str]] = data.get('damage_vulnerabilities')
        self.damage_resistances: Optional[List[str]] = data.get('damage_resistances')
        self.damage_immunities: Optional[List[str]] = data.get('damage_immunities')
        self.condition_immunities: Optional[List[str]] = data.get('condition_immunities')
        self.senses: Optional[Dict[str, str]] = data.get('senses')
        self.languages: Optional[str] = data.get('languages')
        self.challenge_rating: Optional[int] = data.get('challenge_rating')
        self.proficiency_bonus: Optional[int] = data.get('proficiency_bonus')
        self.xp: Optional[int] = data.get('xp')
        self.actions: Optional[List[Dict[str, Any]]] = data.get('actions')
        self.legendary_actions: Optional[List[Dict[str, Any]]] = data.get('legendary_actions')
        self.special_abilities: Optional[List[Dict[str, Any]]] = data.get('special_abilities')









    def to_dict(self) -> Dict[str, Any]:
        return {
            'index': self.index,
            'url': self.url,
            'name': self.name,
            'desc': self.desc,
            'size': self.size,
            'type': self.type,
            'subtype': self.subtype,
            'alignment': self.alignment,
            'armor_class': self.armor_class,
            'hit_points': self.hit_points,
            'hit_dice': self.hit_dice,
            'hit_points_roll': self.hit_points_roll,
            'speed': self.speed,
            'strength': self.strength,
            'dexterity': self.dexterity,
            'constitution': self.constitution,
            'intelligence': self.intelligence,
            'wisdom': self.wisdom,
            'charisma': self.charisma,
            'proficiencies': self.proficiencies,
            'damage_vulnerabilities': self.damage_vulnerabilities,
            'damage_resistances': self.damage_resistances,
            'damage_immunities': self.damage_immunities,
            'condition_immunities': self.condition_immunities,
            'senses': self.senses,
            'languages': self.languages,
            'challenge_rating': self.challenge_rating,
            'proficiency_bonus': self.proficiency_bonus,
            'xp': self.xp,
            'actions': self.actions,
            'legendary_actions': self.legendary_actions,
            'special_abilities': self.special_abilities
        }