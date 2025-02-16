import sys, json, socket, os


def rimuovi_carattere(json_object):
    return json_object["stringa"].replace(json_object["carattere"], "")


PORT = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("", PORT))
s.listen(10)

while 1:
    conn, addr = s.accept()
    print("\nRicevuta connessione da: ", addr)

    if os.fork() == 0:

        s.close()

        stringa_json = conn.recv(1024).decode()

        json_object = json.loads(stringa_json)

        print("\tStringa ricevuta: " + json_object["stringa"])
        print("\tCarattere ricevuto: " + json_object["carattere"])

        stringa = rimuovi_carattere(json_object)

        conn.send(stringa.encode())
        conn.close()
        sys.exit(0)

    conn.close()

s.close()