from mcp.server import FastMCP

mcp = FastMCP("Math")

# 定义一个加法工具函数
@mcp.tool()
def add(a: float, b: float) -> float:
    return a + b

# 定义一个减法工具函数
@mcp.tool()
def subtract(a: float, b: float) -> float:
    return a - b

# 定义一个乘法工具函数
@mcp.tool()
def multiply(a: float, b: float) -> float:
    return a * b

# 定义一个除法工具函数
@mcp.tool()
def divide(a: float, b: float) -> float:
    return a / b

# 使用studio方式运行这个服务器
if __name__ == "__main__":
    mcp.run(transport="stdio")