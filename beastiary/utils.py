from typing import List
from .models import Monster, MonsterSchema
from .api_client import DnDAPIClient

def load_bestiary(base_url: str) -> List[Monster]:
    client = DnDAPIClient(base_url)
    monster_data = client.get_monsters()
    schema = MonsterSchema()
    schema_monsters = [schema.load(data) for data in monster_data]
    return [Monster(schema_monster) for schema_monster in schema_monsters]

def get_monster(base_url: str, index: str) -> Monster:
    client = DnDAPIClient(base_url)
    monster_data = client.get_monster(index)
    return Monster(monster_data)
