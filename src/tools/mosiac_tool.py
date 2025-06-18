import requests
from azure.ai.agents import Tool

class MosaicAITool(Tool):
    def __init__(self, api_key, endpoint):
        super().__init__(
            name="MosaicAI",
            description="Call Mosaic AI's LLM API for completion",
            parameters={
                "prompt": {"type": "string", "description": "The prompt to complete."}
            }
        )
        self.api_key = api_key
        self.endpoint = endpoint

    def call(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {"prompt": prompt}
        response = requests.post(self.endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("completion", "")
