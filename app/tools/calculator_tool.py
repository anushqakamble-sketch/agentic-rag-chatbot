from langchain_core.tools import Tool

def calculator(expression: str):
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "Invalid math expression"


calculator_tool = Tool(
    name="calculator",
    func=calculator,
    description="Use this tool to solve math expressions like '45 * 23'"
)