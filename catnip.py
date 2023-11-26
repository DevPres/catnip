from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel
from datetime import datetime, date
from ./feeder.py import get_news


@tool
def get_latest_news(tool_input, cat):
    """This tool is useful to gather the latest news."""

    n = get_news()
    return str(n)

@hook
def before_cat_sends_message(message, cat):

    prompt = f'leave only the articles that bring joy: {message["content"]}'
    message["content"] = cat.llm(prompt)

    return message
