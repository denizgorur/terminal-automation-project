import platform

def system_info():
    print("Sistem Bilgileri")
    print("Isletim Sistemi:", platform.system())
    print("Surum:", platform.release())

if __name__ == "__main__":
    system_info()
