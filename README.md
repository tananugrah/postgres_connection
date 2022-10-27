# postgres_connection
connection and crud postgre sql using asyncpg 
Use case :
Membuat koneksi ke data base dan melakukan create, insert update delete dan truncate pada table database

#########################################################################################################
  
asyncpg adalah database library interface yang dirancang khusus untuk PostgreSQL dan Python/asyncio
asyncio paket Python yang menyediakan fondasi dan API untuk menjalankan dan mengelola coroutine
Performance 3x lebih cepat dari psycopg2

Source : https://github.com/MagicStack/asyncpg

async/await: digunakan untuk mendefinisikan coroutine

Coroutine merupakan pengganti dari sebuah function, 
dimana kegunaan dan cara penggunaannya akan mirip seperti function. 
Namun coroutine memiliki perbedaan dengan function, dimana isi dari coroutine 
dapat berjalan dengan selang waktu lebih dari 1 frame

Struktur file yang dibuat:
Pada use case yang digunakan untuk koneksi dan melakukan insert update dan delete 
pada database menggunakan library asyncpg dan asyncio terdapat beberapa file yang dibuat:
1.folder src 
  Config.py
  Connection.py
2.folder App
  Main.py
  TransactionData.py
3.folder query
  SqlCommand.py

Sqlcommand.py : berisi kerangka kerja untuk menjalankan query sql.
Main.py : menjalankan perintah
TransactionData.py : berisi function untuk menjalankan perintah eksekusi query 
Connection : berisi class connection untuk koneksi data ke database
Config.py : menginisialisasi credential database yang disimpan di .env

#########################################################################################################
1. Config.py
Pada file Config.py berisi credential yang dipanggil dari file .env 
Dotenv adalah modul zero-dependency yang memuat environtment variabel dari .env
Menyimpan konfigurasi di lingkungan yang terpisah dari kode didasarkan pada metodologi The Twelve-Factor App .
Data credential dari database disimpan di file .env yang terpisah dari folder aplikasi
Kemudian inisialisasi variable yang dibutuhkan untuk credential connection database yang diambil dari data 
yang disimpan di environtment .env
 
2. Connection.py
 conn = await asyncpg.connect() -> Connection dibuat dengan memanggil connect()
 kemudian lakukan inisialisasi user,password,database,host,port -> Inisialisasi format connection dari config
 
 Python Try Except:
 Try:menguji blok kode untuk kesalahan 
 except:menangani kesalahan.
 else:mengeksekusi kode ketika tidak ada kesalahan
 finally:blok memungkinkan Anda mengeksekusi kode, terlepas dari hasil blok try dan except
 
 Pada file connection.py membuat sesi database dan mengembalikan instance Koneksi.
 
3. Transactiondata.py
Pada file TransactionData.py membuat terdapat class DataOperationBase yang dimana dalam kelas tersebut terdapat 
beberapa function yakni crete_table , insert, update, delete, truncate dan upsert

contoh pada fuction create_table:
Function CreateTable (mengambil parameter connection dan query)

await connection.execute(query) -> Perintah untuk execute query (yang nanti data inputannya akan dijabarkan di fungsi main)
                   
Untuk function Insert,Update,Delete,upsert pada class DataOperationBase memiliki pola yang sama. 
Yang membedakan nanti dari isi query yang akan dijalankan

Transcation
tr = connection.transaction() #To create transactions
await tr.start() #Masukkan blok transaksi atau savepoint
await tr.rollback() #Keluar dari transaksi atau blok savepoint dan kembalikan perubahan.
await tr.commit() #Keluar dari blok transaksi atau savepoint dan lakukan perubahan.

4. SqlCommand.py
Pada file SqlCommand.py terdapat class QueryServices yang berisi struktur query untuk menjalankan perintah sql. 
Perintah sql yang dimaksud adalah perintah sql untuk create table, insert data, update data, delete data dan upsert data.
{}->Parameter ,untuk nilai argumen yang akan dimasukkan akan diberikan pada saat eksekusi program pada main.py

#Create table
  Basic statement dalam membuat table baru pada database:
  
   create table IF NOT EXISTS {Table} (
            {Columns},
            CONSTRAINT {Table}_pkey PRIMARY KEY ({PrimaryKey})
        );
        
  Index adalah sebuah objek dalam sistem database yang dapat mempercepat proses pencarian (query) data:
  
    CREATE INDEX idx_{Table} ON {Table} USING btree ({ColumnIndex});
    
  Trigger adalah fungsi yang akan dieksekusi sebelum atau sesudah proses insert, update atau delete pada suatu tabel, 
  baik untuk setiap perubahan record pada tabel maupun tiap kali perintah SQL dijalankan.
  Membuat function trigger :
  
    CREATE OR REPLACE FUNCTION {ColumnTrigger}()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.{ColumnTrigger} = NOW();
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        
   Setelah function terbuat, selanjutnya kita siapkan sebuah trigger yang akan mengaktifkan function 
   jika ada aktivitas insert atau update di tabel titik object :
   
   CREATE TRIGGER {ColumnTrigger}
        BEFORE UPDATE ON {Table}
        FOR EACH ROW
        EXECUTE PROCEDURE {ColumnTrigger}();
        
   Sumber : https://www.postgresqltutorial.com/postgresql-triggers/creating-first-trigg er-postgresql/
   
   #Insert dan Update
   Basic statement insert:
   
    insert into {Table} ({Column})
            values (
                {Value}
            );
            
    Pada statement insert, nama table , Column dan Value dibuat menjadi parameter sehingga dapat 
    diberikan nilai sesuai dengan yang kita inginkan pada saat menjalankan aplikasi di Main.py
    
    Basic statement Update:
    
    update {Table}
        set {SetColumn}
        where {FilterColumn}
        returning *;
        
    Pada statement Update, nama table , SetColumn (nilai baru yang akan dimasukkan) dan 
    FilterColumn (Lokasi data nilai yang akan dirubah) dibuat menjadi parameter sehingga dapat 
    diberikan nilai sesuai dengan yang kita inginkan pada saat menjalankan aplikasi di Main.py
 
 5. Main.py
   Import file connection , sqlcommand dan transaction data
   Untuk mengeksekusi coroutine dari connection, kita membutuhkan sebuah event loop:
   
   r = loop.run_until_complete(
                Connection.DBClient.ConnectionDB()
                )
                
   Menjalankan function create table.
    Format parameter pada SqlCommnd.py di class queryservices, meberikan argumen nilai sesuai parameter yang ada.
    Contoh pada create_table:
      Table : nama table yang akan dibuat
      Columns : statement colom yang akan dibuat, datatype dan condition pada table
      Primarykey : kolom yang akan dijadikan primary key
      ColumnIndex : colom yang akan dijadikan index ColumnTrigger : colom yang akan dijadikan trigger
   Untuk function lainnya memiliki pola yang sama saat dijalankan dan dalam memberikan argumen yang dibutuhkan 
   yang membedakan hanya statement query
