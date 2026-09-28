# Numeric Functions

SQL numeric function expressions.

## abs

`abs(expression)`

Returns a function expression for the absolute value of the input _expression_.

## sign

`sign(expression)`

Returns a function expression for the sign of the input _expression_: `-1` for negative values, `0` for zero, and `1` for positive values.

## sqrt

`sqrt(expression)`

Returns a function expression for the square root of the input _expression_.

## exp

`exp(expression)`

Returns a function expression that computes `e` raised to the power of the input _expression_.

## ln

`ln(expression)`

Returns a function expression for the natural logarithm of the input _expression_.

## log

`log(expression)`

Returns a function expression for the base 10 logarithm of the input _expression_.

## ceil

`ceil(expression)`

Returns a function expression that rounds the input _expression_ up to the nearest integer.

## floor

`floor(expression)`

Returns a function expression that rounds the input _expression_ down to the nearest integer.

## round

`round(expression, places)`

Returns a function expression that rounds the input _expression_ to the given number of decimal _places_ (default `0`).
Negative _places_ values round to tens, hundreds, and so on.

## trunc

`trunc(expression)`

Returns a function expression that truncates the input _expression_ toward zero.

## greatest

`greatest(...expressions)`

Returns a function expression that selects the largest value among the input _expressions_.

## least

`least(...expressions)`

Returns a function expression that selects the smallest value among the input _expressions_.

## isNaN

`isNaN(expression)`

Returns a function expression that is true if the floating point input _expression_ is not a number (NaN), false otherwise.

## isFinite

`isFinite(expression)`

Returns a function expression that is true if the floating point input _expression_ is finite, false otherwise.

## isInfinite

`isInfinite(expression)`

Returns a function expression that is true if the floating point input _expression_ is infinite, false otherwise.
