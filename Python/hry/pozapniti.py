import os
import shutil
from datetime import date
from pathlib import Path

# Získání cesty k ploše uživatele
desktop_path = Path(os.path.expanduser("~/Desktop"))

# Zjistění aktuálního data
today = date.today()

# Vytvoření názvu složky obsahující datum
folder_name = today.strftime("%Y-%m-%d")

# Cesta k umístění složky na ploše uživatele
path = desktop_path / folder_name

# Vytvoření složky, pokud neexistuje
if not path.exists():
    path.mkdir()

# Přesunutí složky na plochu uživatele
user_name = os.getlogin()
shutil.move(str(path), f"C:/Users/{user_name}/Desktop/Visualstudio/prace")

