import requests
from mcp.server.mcpserver import MCPServer

DICE_API_URL = "http://127.0.0.1:5001"
mcp = MCPServer("DiceRoller")


@mcp.tool()
def roll_dice(num_dice: int = 1, num_sides: int = 6) -> dict:
    """Roll one or more polyhedral dice and return each individual roll and the total.

    Args:
        num_dice: Number of dice to roll (1 to 100).
        num_sides: Number of sides per die (e.g., 6 for d6, 20 for d20).
    """
    resp = requests.post(
        f"{DICE_API_URL}/roll",
        json={"num_dice": num_dice, "num_sides": num_sides},
        timeout=5,
    )
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    mcp.run()
