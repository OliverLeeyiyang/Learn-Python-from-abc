def add_until_end(init_value, end_value, step_value):
    current = init_value
    steps = 0
    for _ in range(1000000):  # large upper bound to ensure loop can finish
        current += step_value
        steps += 1
        if current >= end_value:
            break
    print(f"init_value: {init_value}, end_value: {end_value}, step_value: {step_value}")
    print(f"Number of steps: {steps}")

def main():
    add_until_end(0, 10, 2)

if __name__ == "__main__":
    main()