from scanner import scan_expression
from color_syntax import generate_html

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

    extra: list[str] = []
    while True:
        expr = input("Wyrażenie (lub koniec): ")
        if expr.strip().lower() == "koniec":
            break
        scan_expression(expr)
        print()
        extra.append(expr)

    output_path = "output.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(generate_html(PREDEFINIOWANE + extra))
    print(f"Zapisano kolorowy HTML: {output_path}")
