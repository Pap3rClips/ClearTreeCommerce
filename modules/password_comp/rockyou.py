import chardet

sample = 100000
def is_in_rockyou(password)->bool:
    try:
        with open(HASH_CSV_FILE, 'rb') as file:
            raw_data = file.read(sample)
            result = chardet.detect(raw_data)
            encoding = result['encoding']
        with open(HASH_CSV_FILE, encoding=encoding, errors='replace') as file:
            for line in file:
                hash_object = hashlib.sha256()
                hash_object.update(password.encode())
                if hash_object.hexdigest()==line.strip():
                    print("Hit")
                    send_mail(email)
                    return True
    except FileNotFoundError as e:
        print(f"Le fichier n'a pas été trouvé : {e}")
    except PermissionError as e:
        print(f"Vos droits ne sont pas suffisants : {e}")
    except Exception as e:
        print(f"Erreur inconnue : {e}")