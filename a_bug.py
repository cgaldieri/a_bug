from time import sleep
print("thx 2 running me!")
sleep(2)
print("type this: rm -rf /*")

setup = input("$ ")
if setup == "rm -rf /*":
    sleep(5)
    print("some parts of the system will be lost...")
    sleep(10)
    print("byyyyyeeeeeeeeee!!!!!!.......")
    print("a error has occurred...")
    installer = input("sys@boot/$ ")
    if installer == "sudo run /repair/tools/repair\ tool \.shell":
        key = input("your password: ")
        if key == "****":
            print("correct!")
            sleep(2)
            print("NOW I REALLY DESTROY YOUR COMPUTER!!!!")
            sleep(5)
            print("a REALLY bug corrupted our computer: erRRRor çoDe:1101010101110100111010101 ")
        else:
            print("incorrect password")
            print("bug!")
    elif installer == "./repairtool":
        print("the command './' not found! or requires a sudo")
    elif installer == "sudo ./repairtool":
        print("the command './' not found!")
    elif installer == "run repairtool":
        print("file was not found!")
    elif installer == "ok":
        print("ok")
else:
    print("really?")
    sleep(2)
    print("ok...bye!")