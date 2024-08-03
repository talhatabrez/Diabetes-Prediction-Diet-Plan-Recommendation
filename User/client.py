import socket
import cv2

def client_program():
    host = socket.gethostname()
    port = 5000

    diet = ""

    filedata = ""
    with open("data/users.txt", "r", errors='ignore') as file:
       for line in file:
          line = line.strip('\n')
          filedata += line + " "

    with open("img/plan.txt", "r", errors='ignore') as file:
       for line in file:
          diet += line + " "
          
    file = filedata.split(" ")
    length = len(file)
    print(length)
    i = 0
    j = 0
    while i < length:
        client_socket = socket.socket()
        try:
            client_socket.connect((host, port))
        except ConnectionRefusedError:
            print("Connection refused. Ensure the server is running.")
            return
        message = str(file[i])
        print(message)
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)
        client_socket.close()
        if j == 0 and data == 'Abnormal Values. Disease predicted as type 2 diabetes':
            img = cv2.imread("img/1.jpg")
            cv2.imshow("Diet Plan Img", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        i += 1
    print("Ended")


if __name__ == '__main__':
    client_program()
