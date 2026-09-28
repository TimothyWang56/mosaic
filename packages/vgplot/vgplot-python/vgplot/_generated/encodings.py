# DO NOT EDIT. Generated from the Mosaic JSON schema by bin/generate-python-api.js.
# Regenerate with: pnpm run generate:python-api

from __future__ import annotations

from typing import Any

from .._types import UNSET, TransformArg


def _transform(
    name: str, args: tuple[Any, ...], options: dict[str, Any]
) -> dict[str, Any]:
    vals = [a for a in args if a is not UNSET]
    value: Any = vals[0] if len(vals) == 1 else vals or ""
    return {name: value, **options}


def abs(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the absolute value of a number."""
    return _transform("abs", (col,), options)


def add(a: TransformArg, b: TransformArg, **options: Any) -> dict[str, Any]:
    """Add two numbers (`a + b`)."""
    return _transform("add", (a, b), options)


def argmax(col: TransformArg, by: TransformArg, **options: Any) -> dict[str, Any]:
    """Find a value of the first column that maximizes the second column."""
    return _transform("argmax", (col, by), options)


def argmin(col: TransformArg, by: TransformArg, **options: Any) -> dict[str, Any]:
    """Find a value of the first column that minimizes the second column."""
    return _transform("argmin", (col, by), options)


def avg(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the average (mean) value of the given column."""
    return _transform("avg", (col,), options)


def bin(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Bin a continuous variable into discrete intervals."""
    return _transform("bin", (col,), options)


def ceil(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Round a number up to the nearest integer."""
    return _transform("ceil", (col,), options)


def centroid(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the 2D centroid of geometry-typed data."""
    return _transform("centroid", (col,), options)


def centroid_x(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the centroid x-coordinate of geometry-typed data."""
    return _transform("centroidX", (col,), options)


def centroid_y(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the centroid y-coordinate of geometry-typed data."""
    return _transform("centroidY", (col,), options)


def column(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Interpret a string or param-value as a column reference."""
    return _transform("column", (col,), options)


def count(col: TransformArg | UNSET = UNSET, **options: Any) -> dict[str, Any]:
    """Compute the count of records in an aggregation group."""
    return _transform("count", (col,), options)


def cume_dist(**options: Any) -> dict[str, Any]:
    """Compute the cumulative distribution value over an ordered window partition."""
    return {"cume_dist": None, **options}


def date_day(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Transform a Date value to a day of the month for cyclic comparison."""
    return _transform("dateDay", (col,), options)


def date_month(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Transform a Date value to a month boundary for cyclic comparison."""
    return _transform("dateMonth", (col,), options)


def date_month_day(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Transform a Date value to a month and day boundary for cyclic comparison."""
    return _transform("dateMonthDay", (col,), options)


def dense_rank(**options: Any) -> dict[str, Any]:
    """Compute the dense row rank (no gaps) over an ordered window partition."""
    return {"dense_rank": None, **options}


def div(a: TransformArg, b: TransformArg, **options: Any) -> dict[str, Any]:
    """Divide the first number by the second (`a / b`)."""
    return _transform("div", (a, b), options)


def exp(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the exponential function `e ** x`."""
    return _transform("exp", (col,), options)


def first(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Return the first column value found in an aggregation group."""
    return _transform("first", (col,), options)


def first_value(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Get the first value of the given column in the current window frame."""
    return _transform("first_value", (col,), options)


def floor(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Round a number down to the nearest integer."""
    return _transform("floor", (col,), options)


def geojson(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute a GeoJSON-formatted string from geometry-typed data."""
    return _transform("geojson", (col,), options)


def idiv(a: TransformArg, b: TransformArg, **options: Any) -> dict[str, Any]:
    """Integer-divide the first number by the second (`a // b`)."""
    return _transform("idiv", (a, b), options)


def lag(
    col: TransformArg,
    offset: TransformArg | UNSET = UNSET,
    default: TransformArg | UNSET = UNSET,
    **options: Any,
) -> dict[str, Any]:
    """Compute lagging values in a column."""
    return _transform("lag", (col, offset, default), options)


def last(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Return the last column value found in an aggregation group."""
    return _transform("last", (col,), options)


def last_value(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Get the last value of the given column in the current window frame."""
    return _transform("last_value", (col,), options)


def lead(
    col: TransformArg,
    offset: TransformArg | UNSET = UNSET,
    default: TransformArg | UNSET = UNSET,
    **options: Any,
) -> dict[str, Any]:
    """Compute leading values in a column."""
    return _transform("lead", (col, offset, default), options)


def ln(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the natural logarithm of a number."""
    return _transform("ln", (col,), options)


def log(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the base 10 logarithm of a number."""
    return _transform("log", (col,), options)


def max(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the maximum value of the given column."""
    return _transform("max", (col,), options)


def median(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the median value of the given column."""
    return _transform("median", (col,), options)


def min(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the minimum value of the given column."""
    return _transform("min", (col,), options)


def mod(a: TransformArg, b: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the remainder of dividing the first number by the second (`a % b`)."""
    return _transform("mod", (a, b), options)


def mode(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the mode value of the given column."""
    return _transform("mode", (col,), options)


def mul(a: TransformArg, b: TransformArg, **options: Any) -> dict[str, Any]:
    """Multiply two numbers (`a * b`)."""
    return _transform("mul", (a, b), options)


def nth_value(
    col: TransformArg, offset: TransformArg, **options: Any
) -> dict[str, Any]:
    """Get the nth value of the given column in the current window frame, counting from one."""
    return _transform("nth_value", (col, offset), options)


def ntile(buckets: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute an n-tile integer ranging from 1 to the provided argument (num_buckets), dividing the partition as equally as possible."""
    return _transform("ntile", (buckets,), options)


def percent_rank(**options: Any) -> dict[str, Any]:
    """Compute the percentage rank over an ordered window partition."""
    return {"percent_rank": None, **options}


def pow(a: TransformArg, b: TransformArg, **options: Any) -> dict[str, Any]:
    """Raise the first number to the power of the second (`a ** b`)."""
    return _transform("pow", (a, b), options)


def product(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the product of the given column."""
    return _transform("product", (col,), options)


def quantile(col: TransformArg, p: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the quantile value of the given column at the provided probability threshold."""
    return _transform("quantile", (col, p), options)


def rank(**options: Any) -> dict[str, Any]:
    """Compute the row rank over an ordered window partition."""
    return {"rank": None, **options}


def round(
    col: TransformArg, places: TransformArg | UNSET = UNSET, **options: Any
) -> dict[str, Any]:
    """Round a number to the given decimal places (second argument, default `0`)."""
    return _transform("round", (col, places), options)


def row_number(**options: Any) -> dict[str, Any]:
    """Compute the 1-based row number over an ordered window partition."""
    return {"row_number": None, **options}


def sign(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the sign of a number (-1, 0, or 1)."""
    return _transform("sign", (col,), options)


def sqrt(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the square root of a number."""
    return _transform("sqrt", (col,), options)


def stddev(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the sum of the given column."""
    return _transform("stddev", (col,), options)


def stddev_pop(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the sum of the given column."""
    return _transform("stddevPop", (col,), options)


def sub(a: TransformArg, b: TransformArg, **options: Any) -> dict[str, Any]:
    """Subtract the second number from the first (`a - b`)."""
    return _transform("sub", (a, b), options)


def sum(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the sum of the given column."""
    return _transform("sum", (col,), options)


def trunc(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Truncate a number toward zero."""
    return _transform("trunc", (col,), options)


def variance(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the sample variance of the given column."""
    return _transform("variance", (col,), options)


def var_pop(col: TransformArg, **options: Any) -> dict[str, Any]:
    """Compute the population variance of the given column."""
    return _transform("varPop", (col,), options)


__all__ = [
    "abs",
    "add",
    "argmax",
    "argmin",
    "avg",
    "bin",
    "ceil",
    "centroid",
    "centroid_x",
    "centroid_y",
    "column",
    "count",
    "cume_dist",
    "date_day",
    "date_month",
    "date_month_day",
    "dense_rank",
    "div",
    "exp",
    "first",
    "first_value",
    "floor",
    "geojson",
    "idiv",
    "lag",
    "last",
    "last_value",
    "lead",
    "ln",
    "log",
    "max",
    "median",
    "min",
    "mod",
    "mode",
    "mul",
    "nth_value",
    "ntile",
    "percent_rank",
    "pow",
    "product",
    "quantile",
    "rank",
    "round",
    "row_number",
    "sign",
    "sqrt",
    "stddev",
    "stddev_pop",
    "sub",
    "sum",
    "trunc",
    "var_pop",
    "variance",
]
