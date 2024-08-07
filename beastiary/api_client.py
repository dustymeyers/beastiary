import requests
from .logger import logger
from typing import Any, Dict, List

class DnDAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_monsters(self) -> List[Dict[str,Any]]:
        url = f"{self.base_url}/monsters"
        try:
            response = requests.get(url)
            response.raise_for_status()
            logger.info(f"Successfully fetched monsters from {url}")
            return response.json()['results']
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching monsters from {url}: {e}")
            raise

    def get_monster(self, index: str) -> Dict[str, Any]:
        url = f"{self.base_url}/monsters/{index}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching monster {index} from {url}: {e}")
            raise
