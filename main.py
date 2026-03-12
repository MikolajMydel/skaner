from scanner import scan_expression

PREDEFINIOWANE = [
    "2+3*(76+8/3)+ 3*(9-3)",
    "abc + 12 * (x1 - y2)",
    "10 / 2 + @5",
    "  (  3 + 2  ) * 7  ",
    "hello##world",
]

if __name__ == "__main__":
    for expr in PREDEFINIOWANE:
        scan_expression(expr)
        print()

    while True:
        expr = input("Wyrażenie (lub koniec): ")
        if expr.strip().lower() == "koniec":
            break
        scan_expression(expr)
        print()
