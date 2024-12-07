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

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def UVA_numeric(data, var_group, bins=None, labels=None):
    '''
    mengambil sekelompok variabel (INTEGER dan FLOAT) dan memplot/mencetak semua deskriptif dan properti bersama dengan Boxplot, Histogram, dan Count Plot.

    Parameter
    data: DataFrame yang berisi data.
    var_group: Daftar variabel yang akan dianalisis.
    bins: (Opsional) Daftar tbin
    labels: (Opsional) Daftar label
    '''

    size = len(var_group)
    plt.figure(figsize=(14, 6*size), dpi=100)


    for j, i in enumerate(var_group):


        mini = data[i].min()
        maxi = data[i].max()
        ran = data[i].max() - data[i].min()
        mean = data[i].mean()
        median = data[i].median()
        st_dev = data[i].std()
        skew = data[i].skew()
        kurt = data[i].kurtosis()

        points = mean - st_dev, mean + st_dev


        plt.subplot(size, 3, 3*j + 1)
        sns.boxplot(y=data[i])
        plt.title(f'Boxplot of {i}\nRange: {round(mini, 2)} to {round(maxi, 2)}\nSkew: {round(skew, 2)}')


        plt.subplot(size, 3, 3*j + 2)
        sns.histplot(data[i], kde=True)
        plt.axvline(mean, color='red', linestyle='--', label='Mean')
        plt.axvline(median, color='blue', linestyle='-', label='Median')
        plt.axvline(points[0], color='black', linestyle='--', label='-1 std dev')
        plt.axvline(points[1], color='black', linestyle='--', label='+1 std dev')
        plt.title(f'Histogram of {i}\nMean: {round(mean, 2)}, Median: {round(median, 2)}, Kurtosis: {round(kurt, 2)}')
        plt.legend()


        plt.subplot(size, 3, 3*j + 3)
        if bins is not None and labels is not None:

            if len(labels) == len(bins) - 1:

                binned_data = pd.cut(data[i], bins=bins, labels=labels, include_lowest=True)
                sns.countplot(x=binned_data)
                plt.title(f'Count Plot of {i} (Binned)')
            else:
                raise ValueError("Bin labels must be one fewer than the number of bin edges")
        else:

            sns.countplot(x=data[i])
            plt.title(f'Count Plot of {i}')

    plt.tight_layout()
    plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def UVA_category(data, var_group, bins=None, labels=None):
    '''

    mengambil sekelompok variabel kategorikal dan memplot semua visualisasi yang relevan seperti Count Plot dan Pie Chart.

    Parameter
    data: DataFrame yang berisi data.
    var_group: Daftar variabel yang akan dianalisis.
    bins: (Opsional)
    labels: (Opsional)


    '''

    size = len(var_group)
    plt.figure(figsize=(14, 6*size), dpi=100)


    for j, i in enumerate(var_group):


        mode = data[i].mode()[0]
        value_counts = data[i].value_counts()
        top_category = value_counts.idxmax()
        top_count = value_counts.max()
        unique_categories = data[i].nunique()


        plt.subplot(size, 2, 2*j + 1)

        if bins is not None and labels is not None:

            if len(labels) == len(bins) - 1:

                binned_data = pd.cut(data[i], bins=bins, labels=labels, include_lowest=True)
                sns.countplot(x=binned_data)
                plt.title(f'Count Plot of {i}')
            else:
                raise ValueError("Bin labels must be one fewer than the number of bin edges")
        else:

            sns.countplot(x=data[i], order=value_counts.index)
            plt.title(f'Count Plot of {i}\nMode: {mode}, Top Category: {top_category} ({top_count})\nUnique Categories: {unique_categories}')

        plt.xticks(rotation=45)

        plt.subplot(size, 2, 2*j + 2)

        if bins is not None and labels is not None:

            if len(labels) == len(bins) - 1:

                binned_data = pd.cut(data[i], bins=bins, labels=labels, include_lowest=True)
                binned_counts = binned_data.value_counts()
                plt.pie(binned_counts, labels=binned_counts.index, autopct='%1.1f%%', startangle=140)
                plt.title(f'Pie Chart of {i}')
            else:
                raise ValueError("Bin labels must be one fewer than the number of bin edges")
        else:

            plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140)
            plt.title(f'Pie Chart of {i}')

    plt.tight_layout()
    plt.show()
def detect_outliers(data, var_group):

    outliers_info = {}

    for column in var_group:
        # Calculate Q1 (25th percentile) and Q3 (75th percentile)
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1

        # Define outlier bounds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Identify outliers
        outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)][column]

        # Store the results
        outliers_info[column] = {
            'count': outliers.count(),
            'proportion': outliers.count() / len(data),
            'outliers': outliers.tolist()
        }

    return outliers_info

