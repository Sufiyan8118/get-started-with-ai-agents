import os
from azure.ai.agents import Agent
from tools.mosaic_tool import MosaicAITool

def build_agent():
    # Load config from environment
    mosaic_api_key = os.environ["MOSAIC_API_KEY"]
    mosaic_endpoint = os.environ["MOSAIC_API_ENDPOINT"]

    # Instantiate Mosaic Tool
    mosaic_tool = MosaicAITool(
        api_key=mosaic_api_key,
        endpoint=mosaic_endpoint,
    )

    # Register tools (add other tools as in original code)
    agent = Agent(
        tools=[mosaic_tool],
        # add your model/service config as per project
    )
    return agent
