from typing import Union

def display_data(data: Union[int, str]):
    if isinstance(data, int):
        print(f"Angka: {data}")
    elif isinstance(data, str):
        print(f"Teks: {data}")

display_data(32)
display_data("Hello sisfo")
