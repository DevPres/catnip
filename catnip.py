from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel
from datetime import datetime, date
from .feeder import get_news


@tool
def get_latest_news(tool_input, cat):
    """"use this tool to respond to requests like 'give me good news' ecc.."""
    n = get_news()

    return cat.llm(
        f"""
        These are a list of articles.
        {print(n)}

        Leave in this list ONLY the articles that bring joy.
        """
    )

