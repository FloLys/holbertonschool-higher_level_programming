#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as op
    a = 10
    b = 5
    print(f"{a} + {b} = {op.add(a, b)}")
    print(f"{a} - {b} = {op.sub(a, b)}")
    print(f"{a} * {b} = {op.mul(a, b)}")
    print(f"{a} / {b} = {op.div(a, b)}")
