# IPC allows processes to communicate with each other.
from multiprocessing import Process, Pipe

def send_msg(conn):
    conn.send("Hello from Process 1")
    conn.close()

if __name__ == "__main__":

    parent_conn, child_conn = Pipe()

    p = Process(target=send_msg, args=(child_conn,))
    p.start()

    print(parent_conn.recv())

    p.join()