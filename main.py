import math

from fastmcp import FastMCP


mcp = FastMCP("calculator")


def _validate_operands(a: float, b: float) -> None:
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("operands must be finite numbers")


def _validate_result(result: float) -> float:
    if not math.isfinite(result):
        raise ValueError("result is outside the supported numeric range")
    return result


@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    _validate_operands(a, b)
    return _validate_result(a + b)


@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    _validate_operands(a, b)
    return _validate_result(a - b)


@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    _validate_operands(a, b)
    return _validate_result(a * b)


@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    _validate_operands(a, b)
    if b == 0:
        raise ValueError("cannot divide by zero")
    return _validate_result(a / b)


if __name__ == "__main__":
    mcp.run()
