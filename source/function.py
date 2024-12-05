import pandas as pd

def basic_eda(df, name="DataFrame"):
    """
    Melakukan Exploratory Data Analysis (EDA) dasar pada DataFrame.
    
    Parameters:
    - df (pd.DataFrame): DataFrame yang akan dianalisis.
    - name (str): Nama DataFrame (opsional, untuk keperluan pelaporan).

    Returns:
    - None: Hasil EDA dicetak ke konsol.
    """
    print(f"\n=== EDA untuk {name} ===")
    
    # Dimensi data
    print(f"Dimensi data: {df.shape[0]} baris, {df.shape[1]} kolom\n")
    
    # Tipe data setiap kolom
    print("Tipe data setiap kolom:")
    print(df.dtypes)
    print("\n")
    
    # Cek duplikasi
    duplicates = df.duplicated().sum()
    print(f"Jumlah baris duplikat: {duplicates}")
    
    # Nilai null
    print("\nJumlah nilai null per kolom:")
    print(df.isnull().sum())
    print("\n")
    
    # Statistik deskriptif (hanya kolom numerik)
    print("Statistik deskriptif (kolom numerik):")
    print(df.describe())
    print("\n")
    
    # Informasi tambahan
    print("Info tambahan:")
    print(df.info())
    print("\n")
