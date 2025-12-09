#Union adalah tipe data khusus yang memungkinkan beberapa variabel berbeda berbagi lokasi memori yang sama.

from typing import Union

def cetak_data(value: Union[int, float, str]):
    print(value)

cetak_data(23)
cetak_data(3.088)
cetak_data("haii")
