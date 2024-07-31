import mysql.connector 
import matplotlib.pyplot as plt 
import pandas as pd 

  

# MySQL bağlantısı kurma 

mydb = mysql.connector.connect( 

  host="localhost", 
  user="root", 
  password="", 
  database="inf"  

) 

  

# Veritabanı bağlantısı kontrolü 

if mydb.is_connected(): 

    print("MySQL veritabanına bağlantı başarılı.") 

  

# Kullanıcı kayıt olma fonksiyonu 

def register_user(): 
    cursor = mydb.cursor() 
    username = input("Kullanıcı adınızı giriniz: ").upper() 
    password = input("Şifrenizi giriniz: ").upper() 


    # Kullanıcı adının veritabanında olup olmadığını kontrol et 
    cursor.execute("SELECT * FROM user WHERE username = %s", (username,)) 
    result = cursor.fetchone() 

  

    if result: 

        print("Bu kullanıcı adı zaten mevcut. Lütfen farklı bir kullanıcı adı seçin.") 

    else: 
        # Kullanıcıyı veritabanına ekle 
        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password)) 
        mydb.commit() 
        print("Kayıt işlemi başarıyla tamamlandı.") 

  

    cursor.close() 

  

# Kullanıcı giriş yapma fonksiyonu 

def login_user(): 
    cursor = mydb.cursor() 
    username = input("Kullanıcı adınızı giriniz: ").upper() 
    password = input("Şifrenizi giriniz: ").upper() 


    # Kullanıcı bilgilerini kontrol et 
    cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password)) 
    result = cursor.fetchone() 

  

    if result: 
        print("Giriş başarılı. Hoş geldiniz,", username) 
        return True 
    else: 
        print("Kullanıcı adı veya şifre hatalı. Tekrar deneyin.") 
        return False 


    cursor.close() 

  

# Çıkış işlemi 
def logout(): 
    print("Çıkış yapılıyor. Hoşçakalın.") 

  
# Ana menüyü gösterme fonksiyonu 

def interface_menu(): 
    while True: 
        print("\n .....HOŞGELDİNİZ.....:") 
        print("1- Kullanıcı Kayıt Ol") 
        print("2- Giriş Yap") 
        print("4- Çıkış") 
        choice = input("Lütfen yapmak istediğiniz işlemi seçiniz: ") 
        if choice == '1': 
            register_user() 
        elif choice == '2': 
            if login_user(): 
                # Kullanıcı giriş yaptıktan sonra diğer işlemlere geç 
                database_operations_menu()                 
        elif choice == '4': 
            logout() 
            break 
        else: 
            print("Geçersiz seçenek. Tekrar deneyin.") 

  
# Veritabanı işlemleri menüsü 

def database_operations_menu(): 
    while True: 
        print("\nVeritabanı İşlemleri Menüsü:") 
        print("1- Veri Ekleme") 
        print("2- Veri Silme") 
        print("3- Veri Güncelleme") 
        print("4- Veri Listeleme") 
        print("5- Ana Menü") 
        choice = input("Lütfen yapmak istediğiniz işlemi seçiniz: ") 

        if choice == '1': 
            data_insertion() 
        elif choice == '2': 
            data_deletion() 
        elif choice == '3': 
            data_update() 
        elif choice == '4': 
            data_listing() 
        elif choice == '5': 
            break 
        else: 

            print("Geçersiz seçenek. Tekrar deneyin.") 

  

# Veri ekleme işlemi 

def data_insertion(): 
    cursor = mydb.cursor() 
    count = int(input("Kaç adet veri eklemek istiyorsunuz?: ")) 
  
    for i in range(count): 
        driver_name_surname = input("Araç sahibinin adı soyadı: ").upper() 
        car_plate = input("Araç plakası: ").upper() 
        car_brand = input("Araç markası: ").upper() 
        car_model = input("Araç modeli: ").upper() 
        driver_sex = input("Sürücü cinsiyeti: ").upper() 
        driver_age = int(input("Sürücü yaş: ")) 

        # Veritabanında aynı plaka numarasının olup olmadığını kontrol et 

        cursor.execute("SELECT * FROM car_park WHERE car_plate = %s", (car_plate,)) 
        existing_record = cursor.fetchone() 

        if existing_record: 
            print(f"{car_plate} plakalı araç zaten kayıtlı. Eklenemedi.") 
        else: 
            # Veriyi veritabanına ekle 
            cursor.execute("INSERT INTO car_park (driver_name_surname, car_plate, car_brand, car_model, driver_sex, driver_age) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (driver_name_surname, car_plate, car_brand, car_model, driver_sex, driver_age)) 
            mydb.commit() 
            print(f"{car_plate} plakalı araç başarıyla eklendi.") 
    cursor.close() 

    # Veri silme işlemi 

def data_deletion(): 
    cursor = mydb.cursor() 
    print("Kayıtlı veriler:") 
    cursor.execute("SELECT * FROM car_park") 
    records = cursor.fetchall() 

    for record in records: 
        print(f"ID: {record[0]}, Ad Soyad: {record[1]}, Plaka: {record[2]}, Marka: {record[3]}, Model: {record[4]}") 
    choice = input("Hangi kritere göre silme işlemi yapmak istersiniz?\n" 
                   "1- ID'ye göre sil\n" 
                   "2- Plakaya göre sil\n" 
                   "3- İsme göre sil\n" 
                   "4- Bir modeli komple sil\n" 
                   "5- Bir markayı komple sil\n" 
                   "Seçiminiz: ") 

    if choice == '1': 
        delete_by_id(cursor) 
    elif choice == '2': 
        delete_by_plate(cursor) 
    elif choice == '3': 
        delete_by_name(cursor) 
    elif choice == '4': 
        delete_by_model(cursor) 
    elif choice == '5': 
        delete_by_brand(cursor) 
    else: 
        print("Geçersiz seçenek.") 
    cursor.close() 

def delete_by_id(cursor): 
    id_to_delete = int(input("Silmek istediğiniz kaydın ID'sini giriniz: ")) 
    confirm = input("Emin misiniz? (1-Evet, 2-Hayır): ") 

    if confirm == '1': 
        cursor.execute("DELETE FROM car_park WHERE car_id = %s", (id_to_delete,)) 
        mydb.commit() 
        print("Kayıt başarıyla silindi.") 
    else: 
        print("Silme işlemi iptal edildi.") 


def delete_by_plate(cursor): 
    plate_to_delete = input("Silmek istediğiniz aracın plakasını giriniz: ") 
    confirm = input("Emin misiniz? (1-Evet, 2-Hayır): ") 

    if confirm == '1': 
        cursor.execute("DELETE FROM car_park WHERE car_plate = %s", (plate_to_delete,)) 
        mydb.commit() 
        print("Kayıt başarıyla silindi.") 
    else: 
        print("Silme işlemi iptal edildi.") 
  

def delete_by_name(cursor): 
    name_to_delete = input("Silmek istediğiniz kişinin adını ve soyadını giriniz: ").upper() 
    confirm = input("Emin misiniz? (1-Evet, 2-Hayır): ") 

    if confirm == '1': 
        cursor.execute("DELETE FROM car_park WHERE driver_name_surname = %s", (name_to_delete,)) 
        mydb.commit() 
        print("Kayıt başarıyla silindi.") 
    else: 
        print("Silme işlemi iptal edildi.") 


def delete_by_model(cursor): 
    model_to_delete = input("Silmek istediğiniz aracın modelini giriniz: ").upper() 
    confirm = input("Emin misiniz? (1-Evet, 2-Hayır): ") 

    if confirm == '1': 
        cursor.execute("DELETE FROM car_park WHERE car_model = %s", (model_to_delete,)) 
        mydb.commit() 
        print("Kayıt başarıyla silindi.") 
    else: 
        print("Silme işlemi iptal edildi.") 

  
def delete_by_brand(cursor): 
    brand_to_delete = input("Silmek istediğiniz aracın markasını giriniz: ").upper() 
    confirm = input("Emin misiniz? (1-Evet, 2-Hayır): ") 

    if confirm == '1': 
        cursor.execute("DELETE FROM car_park WHERE car_brand = %s", (brand_to_delete,)) 
        mydb.commit() 
        print("Kayıt başarıyla silindi.") 
    else: 
        print("Silme işlemi iptal edildi.") 

# Veri güncelleme işlemi 
def data_update(): 
    cursor = mydb.cursor() 

    print("Kayıtlı veriler:") 
    cursor.execute("SELECT * FROM car_park") 
    records = cursor.fetchall() 


    for record in records: 
        print(f"ID: {record[0]}, Ad Soyad: {record[1]}, Plaka: {record[2]}, Marka: {record[3]}, Model: {record[4]}")
        
    id_to_update = input("Güncellemek istediğiniz kaydın ID'sini giriniz: ") 
    confirm = input("Emin misiniz? (1-Evet, 2-Hayır): ") 


    if confirm == '1': 
        choice = input("Hangi alanı güncellemek istiyorsunuz?\n" 
                       "1- Araç sahibinin adı soyadı\n" 
                       "2- Araç plakası\n" 
                       "3- Araç markası\n" 
                       "4- Araç modeli\n" 
                       "Seçiminiz: ") 


        if choice == '1': 
            new_name = input("Yeni adı soyadı giriniz: ").upper() 
            cursor.execute("UPDATE car_park SET driver_name_surname = %s WHERE car_id = %s", (new_name, id_to_update)) 
            mydb.commit() 
            print("Veri başarıyla güncellendi.") 
        elif choice == '2': 
            new_plate = input("Yeni plakayı giriniz: ").upper() 
            cursor.execute("UPDATE car_park SET car_plate = %s WHERE car_id = %s", (new_plate, id_to_update)) 
            mydb.commit() 
            print("Veri başarıyla güncellendi.") 
        elif choice == '3': 
            new_brand = input("Yeni markayı giriniz: ").upper() 
            cursor.execute("UPDATE car_park SET car_brand = %s WHERE car_id = %s", (new_brand, id_to_update)) 
            mydb.commit() 
            print("Veri başarıyla güncellendi.") 
        elif choice == '4': 
            new_model = input("Yeni modeli giriniz: ").upper() 
            cursor.execute("UPDATE car_park SET car_model = %s WHERE car_id = %s", (new_model, id_to_update)) 
            mydb.commit() 
            print("Veri başarıyla güncellendi.") 
        else: 
            print("Geçersiz seçenek.") 
    else: 
        print("Güncelleme işlemi iptal edildi.") 

    cursor.close() 

  

# Veri listeleme işlemi 
def data_listing(): 
    cursor = mydb.cursor() 

    print("\nVeri Listeleme Seçenekleri:") 
    print("1- Plakaya göre listele") 
    print("2- İsme göre listele") 
    print("3- Modele göre listele") 
    print("4- Tüm verileri listele") 
    print("5- Ana Menü") 
    choice = input("Lütfen yapmak istediğiniz işlemi seçiniz: ") 

    if choice == '1': 
        plate = input("Listelemek istediğiniz aracın plakasını giriniz: ").upper() 
        cursor.execute("SELECT * FROM car_park WHERE car_plate = %s", (plate,)) 
        records = cursor.fetchall() 
        print_records(records) 
    elif choice == '2': 
        name = input("Listelemek istediğiniz kişinin adını soyadını giriniz: ").upper() 
        cursor.execute("SELECT * FROM car_park WHERE driver_name_surname = %s", (name,)) 
        records = cursor.fetchall() 
        print_records(records) 
    elif choice == '3': 
        model = input("Listelemek istediğiniz aracın modelini giriniz: ").upper() 
        cursor.execute("SELECT * FROM car_park WHERE car_model = %s", (model,)) 
        records = cursor.fetchall() 
        print_records(records) 
    elif choice == '4': 
        cursor.execute("SELECT * FROM car_park") 
        records = cursor.fetchall() 
        print_records(records) 
    elif choice == '5': 
        pass
    else: 
        print("Geçersiz seçenek.") 

    cursor.close() 

 
def print_records(records): 
    if not records: 
        print("Kayıt bulunamadı.") 
    else: 
        for record in records: 
            print(f"ID: {record[0]}, Ad Soyad: {record[1]}, Plaka: {record[2]}, Marka: {record[3]}, Model: {record[4]}") 

  

# Grafik işlemleri menüsü 

def graph_operations_menu(): 
    while True: 
        print("\nGrafik İşlemleri Menüsü:") 
        print("1- Pasta Grafiği (Araç markalarına göre dağılım)") 
        print("2- Histogram (Sürücü yaş dağılımı)") 
        print("3- Saçılma Grafiği (Sürücü yaşına göre araba markası)") 
        print("4- Ana Menü") 
        choice = input("Hangi grafiği oluşturmak istersiniz? (1-4): ") 


        if choice == '1': 
            create_pie_chart() 
        elif choice == '2': 
            create_histogram() 

        elif choice == '3': 
            create_scatter_plot() 
        elif choice == '4': 
            break 
        else: 
            print("Geçersiz seçenek. Tekrar deneyin.") 

  

def create_pie_chart(): 
    cursor = mydb.cursor() 
    cursor.execute("SELECT car_brand, COUNT(*) AS count FROM car_park GROUP BY car_brand") 
    records = cursor.fetchall() 

    labels = [record[0] for record in records] 
    sizes = [record[1] for record in records] 

    plt.figure(figsize=(8, 6)) 
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140) 
    plt.title("Araç Markalarına Göre Dağılım") 
    plt.axis('equal') 
    plt.show() 
    
    cursor.close() 

  

def create_histogram(): 
    cursor = mydb.cursor() 
    cursor.execute("SELECT driver_age FROM car_park") 
    ages = [record[0] for record in cursor.fetchall()] 

  
    plt.figure(figsize=(8, 6)) 
    plt.hist(ages, bins=20, edgecolor='black') 
    plt.title("Sürücü Yaş Dağılımı") 
    plt.xlabel("Yaş") 
    plt.ylabel("Frekans") 
    plt.grid(True) 
    plt.show()

    cursor.close() 

  

def create_scatter_plot(): 
    cursor = mydb.cursor() 
    cursor.execute("SELECT driver_age, car_brand FROM car_park") 
    data = cursor.fetchall() 


    ages = [record[0] for record in data] 
    brands = [record[1] for record in data] 


    plt.figure(figsize=(10, 6)) 
    plt.scatter(ages, brands, alpha=0.5) 
    plt.title("Sürücü Yaşına Göre Araba Markası") 
    plt.xlabel("Yaş") 
    plt.ylabel("Marka") 
    plt.grid(True) 
    plt.show() 

    cursor.close() 

  

# Excel dosyalarıyla işlemler menüsü 

def excel_operations_menu(): 
    while True: 
        print("\nExcel Dosyaları İşlemleri Menüsü:") 
        print("1- Excel dosyasından veri okuma") 
        print("2- Excel dosyasından veri listeleme") 
        print("3- Excel dosyasındaki verileri veritabanına kaydetme") 
        print("4- Ana Menü") 
        choice = input("Lütfen yapmak istediğiniz işlemi seçiniz: ") 
        if choice == '1': 
            read_from_excel() 
        elif choice == '2': 
            list_from_excel() 
        elif choice == '3': 
            save_to_database_from_excel() 
        elif choice == '4': 
            break 
        else:
            print("Geçersiz seçenek. Tekrar deneyin.") 
  

def read_from_excel(): 
    file_path = input("Okunacak Excel dosyasının yolunu giriniz: ") 
    try: 
        df = pd.read_excel(file_path) 
        print("Excel dosyası başarıyla okundu:") 
        print(df.head()) 
    except FileNotFoundError: 
        print("Belirtilen dosya bulunamadı.") 
    except Exception as e: 
        print("Hata:", e) 

def list_from_excel(): 
    file_path = input("Listelenecek Excel dosyasının yolunu giriniz: ") 
    
    try: 
        df = pd.read_excel(file_path) 
        print("Excel dosyası içeriği:") 
        print(df)
    except FileNotFoundError: 
        print("Belirtilen dosya bulunamadı.") 
    except Exception as e: 
        print("Hata:", e) 

  

def save_to_database_from_excel(): 
    file_path = input("Veritabanına kaydedilecek Excel dosyasının yolunu giriniz: ") 

    try: 
        df = pd.read_excel(file_path) 
        cursor = mydb.cursor()
  
        for index, row in df.iterrows(): 
            driver_name_surname = str(row['driver_name_surname']).upper() 
            car_plate = str(row['car_plate']).upper() 
            car_brand = str(row['car_brand']).upper() 
            car_model = str(row['car_model']).upper() 
            driver_sex = str(row['driver_sex']).upper() 
            driver_age = row['driver_age'] 

            cursor.execute("SELECT COUNT(*) FROM car_park WHERE car_plate = %s", (car_plate,)) 
            result = cursor.fetchone()    

            if result[0] == 0: 
                cursor.execute("INSERT INTO car_park (driver_name_surname, car_plate, car_brand, car_model, driver_sex, driver_age) VALUES (%s, %s, %s, %s, %s, %s)", 
                               (driver_name_surname, car_plate, car_brand, car_model, driver_sex, driver_age)) 
                mydb.commit() 

        print("Excel dosyasındaki verilerden veritabanında bulunmayan plakalı araçlar başarıyla veritabanına kaydedildi.") 
        cursor.close() 

    except FileNotFoundError: 
        print("Belirtilen dosya bulunamadı.") 
    except Exception as e: 
        print("Hata:", e) 

     

  

# Ana menüyü başlat 

if __name__ == "__main__": 
    while True: 
        print("\n .....HOŞGELDİNİZ.....:") 
        print("1- Kullanıcı Kayıt Ol") 
        print("2- Giriş Yap") 
        print("4- Çıkış") 
        choice = input("Lütfen yapmak istediğiniz işlemi seçiniz: ") 

        if choice == '1': 
            register_user() 
        elif choice == '2': 
            if login_user(): 
                # Kullanıcı giriş yaptıktan sonra diğer işlemlere geç 
                while True: 
                    print("\nAna Menü:") 
                    print("1- Veritabanı İşlemleri") 
                    print("2- Grafik İşlemleri") 
                    print("3- Dosyalama (Excel) İşlemleri") 
                    print("4- Çıkış") 
                    choice = input("Lütfen yapmak istediğiniz işlemi seçiniz: ") 

                    if choice == '1': 
                        database_operations_menu() 
                    elif choice == '2': 
                        graph_operations_menu() 
                    elif choice == '3': 
                        excel_operations_menu() 
                    elif choice == '4': 
                        logout() 
                        break 
                    else: 
                        print("Geçersiz seçenek. Tekrar deneyin.")                  
        elif choice == '4': 
            logout() 
            break 
        else: 
            print("Geçersiz seçenek. Tekrar deneyin.") 
