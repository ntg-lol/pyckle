import help
import echo

print("pyckle v0.1.0")
print("type help for help, or exit to exit")

while True:
    cmd = input("→ ")
    split_cmd = cmd.split()
    match split_cmd[0]:
        case "exit":
            break
        case "help":
            help.help()
        case "echo":
            try:
                echo.echo(split_cmd[1])
            except IndexError:
                print("not enough arguments →", split_cmd) # prints split_cmd for now, will fix later
        case _:
            print("invalid command →", split_cmd[0])
