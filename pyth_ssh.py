import paramiko

# ipv4 = input("IPv4: ")
# user = input("username: ")
# password = input("password: ")

p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect("192.168.1.66", port=22, username="pi", password="raspialak")
# p.connect(ipv4, port=22, username=user, password=password)

while True:
    commando = input("cmd: ")
    if commando == "spadam":
        break
    stdin, stdout, stderr = p.exec_command(commando)
    stdout.channel.recv_exit_status()
    opt = stdout.readlines()
    opt = "".join(opt)
    print(opt)
    # opt = stdin.readlines()
    # opt = "".join(opt)
    # print(opt)

