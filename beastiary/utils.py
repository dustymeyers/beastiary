from typing import List
from .models import Monster
from .api_client import DnDAPIClient

def load_bestiary(base_url: str) -> List[Monster]:
    client = DnDAPIClient(base_url)
    monster_data = client.get_monsters()
    return [Monster(data) for data in monster_data]

def get_monster(base_url: str, index: str) -> Monster:
    client = DnDAPIClient(base_url)
    monster_data = client.get_monster(index)
    return Monster(monster_data)
