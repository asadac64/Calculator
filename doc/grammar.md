# Grammar for the calculator

## Version 0
The arithmetic expression is only a number.

```
Arithmetic Expression (AE) = Number
```

## Version 1: Factorial
Add the factorial expression.

```
Arithmetic Expression (AE) = FactExpr
FactExpr = Number {!}

```

## Version 2: Power
Add the power expression.

```
Arithmetic Expression (AE) = PowerExpr
PowerExpr = FactExpr {"^" PowerExpr}
FactExpr = Number {!}

```

## Version 3: Unary
Add the unary -/+ expression.

```
Arithmetic Expression (AE) = UnaryExpr
UnaryExpr = [- | +] PowerExpr
PowerExpr = FactExpr {"^" PowerExpr}
FactExpr = Number {!}

```

## Version 4: Multiplication
Add the Multiplication expression.

```
Arithmetic Expression (AE) = MulExpr
MulExpr = UnaryExpr { ("*" | "/" | "%") UnaryExpr}
UnaryExpr = [- | +] PowerExpr
PowerExpr = FactExpr {"^" PowerExpr}
FactExpr = Number {!}

```
## Version 5: Addition
Add the Addition expression.

```
Arithmetic Expression (AE) = AddExpr
AddExpr = mulExpr { ("+" | "-" ) mulExpr}
MulExpr = UnaryExpr { ("*" | "/" | "%") UnaryExpr}
UnaryExpr = [- | +] PowerExpr
PowerExpr = FactExpr {"^" PowerExpr}
FactExpr = Number {!}

```

## Version 6: Parenthesis
Add the Parenthesis expression.

```
Arithmetic Expression (AE) = AddExpr
AddExpr = mulExpr { ("+" | "-" ) mulExpr}
MulExpr = UnaryExpr { ("*" | "/" | "%") UnaryExpr}
UnaryExpr = [- | +] PowerExpr
PowerExpr = FactExpr {"^" PowerExpr}
FactExpr = Primary {!}
Primary = Number | "(" AE ")"

```

## Lexical Grammar
```
LeftParen = "("
RightParen = ")"
Terminal = "+"| "-"| "*" | "/" | "%" | "^" | "!" | "(" | ")" 
AddOp = "+" | "-"
MultOp = "*" | "/" | "%"
PowerOp = "^"
FacOp = "!"
Number = Digit {Digit}
Digit = "0" |...| "9"
```