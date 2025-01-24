# main.py

from src.lexer import Lexer
from rich.table import Table
from rich.console import Console

from rich.console import Console

def generate_table(tokens, output_file="tokens_output.txt"):
    """Generates a table of tokens and writes it to a text file."""
    from rich.table import Table

    # Create the table
    table = Table(title="Lexical Analysis")
    table.add_column("Token Type", style="cyan", justify="center")
    table.add_column("Lexeme", style="green", justify="center")
    table.add_column("Line", style="magenta", justify="center")
    table.add_column("Column", style="yellow", justify="center")

    # Fill the table with tokens
    for token in tokens:
        table.add_row(token.type, token.value, str(token.line), str(token.column))

    # Create a console object to render to a file
    console = Console(record=True)
    console.print(table)

    # Save rendered output to a text file with UTF-8 encoding
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(console.export_text())


def main():
    # Read input source code
    with open('input/sample_code.txt', 'r') as file:
        code = file.read()

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    # Generate tokens table
    output_file = "tokens_output.txt"
    generate_table(tokens, output_file)
    print(f"Tokens written to {output_file}")

if __name__ == "__main__":
    main()
