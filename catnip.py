from cat.mad_hatter.decorators import tool, hook, plugin
from datetime import datetime, date
from .feeder import get_news


@tool
def get_latest_news(tool_input, cat):
    """"use this tool to respond to requests like 'give me good news' ecc.."""
    try:
        n = get_news()
        return n
    except Exception as e:
        print(e)
        return "Oops, nothing good today!"  


@hook(priority=1)
def before_cat_sends_message(final_output, cat):
    
    print(final_output)
    prompt = 
        "Filter from the list all message that are not a extremely POSITIVE \n" +
        f"This is the list: {final_output}"
    
    return cat.llm(prompt)

