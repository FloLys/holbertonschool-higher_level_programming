#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    lista = dir(hidden_4)
    for i in lista:
        if i[:2] != "__":
            print(f"{i}")
