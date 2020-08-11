import sys

print_beej = 1
halt = 2

memory = [
    print_beej,
    print_beej,
    print_beej,
    print_beej,
    print_beej,
    halt

]

pc = 0
running = True

while running:
    command = memory[pc]

    if command == print_beej:
        print('Beej')

    elif command == halt:
        running = False

    else:
        print(f'unknown instruction: {command}')
        sys.exit(1)

    pc += 1
