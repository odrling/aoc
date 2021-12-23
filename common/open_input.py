import pathlib


def get_input(solution_file: str, n: int = 1) -> str:
    input_path = pathlib.Path(solution_file).parent / f"input_{n}"
    with open(input_path) as f:
        return f.read()
