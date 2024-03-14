# oenemliguenlermail
Önemli günlerde müşterilere otomatik mail atan, her gün manual çalıştırılması gerekiyor, bir yazılım.

Bu Python kodu, belirli tatillerde veya durumlarda özel bir mesaj içeren bir e-posta göndermek için tasarlanmıştır. İşte kodun her bir parçasının ne yaptığının bir dökümü:

1. **İçe Aktarma İfadeleri**:
   - smtplib`: Bu modül, SMTP veya ESMTP dinleyici arka plan programı olan herhangi bir İnternet makinesine e-posta göndermek için kullanılan bir SMTP istemci oturumu nesnesini tanımlar.
   - `MIMEMultipart` ve `MIMEText`: Bu sınıflar MIME formatında (Çok Amaçlı İnternet Posta Uzantıları) e-posta mesajı nesneleri oluşturmak için kullanılır.
   - `datetime`: Bu modül, tarih ve saatleri işlemek için sınıflar sağlar.
   - `hijri_converter`: Bu, Miladi tarihleri Hicri tarihlere dönüştürmek için özel bir modül gibi görünüyor.

2. **`send_email` Fonksiyonu**:
   - Bu fonksiyon parametre olarak göndericinin e-postasını, göndericinin şifresini, alıcının e-postasını, konuyu ve mesajı alır.
   - Gmail'in SMTP sunucusunu kullanarak bir SMTP sunucusu kurar, TLS şifrelemesini başlatır ve sağlanan gönderenin e-postasını ve şifresini kullanarak oturum açar.
   - Ardından, bir e-posta mesajı oluşturur, mesaj gövdesini ekler ve e-postayı alıcıya gönderir.
   - Son olarak, SMTP sunucusundan çıkar.

3. **`generate_message` Fonksiyonu**:
   - Bu fonksiyon geçerli tarihe göre özel bir mesaj üretir.
   - Geçerli tarihin Gregoryen veya Hicri takvimdeki belirli tatillerle veya olaylarla eşleşip eşleşmediğini kontrol eder ve karşılık gelen bir mesaj döndürür.
   - Tarih herhangi bir özel durumla eşleşmiyorsa, `Hiçbiri` döndürür.

4. **main` Fonksiyonu**:
   - Bu fonksiyon kodun giriş noktası olarak görev yapar.
   - Kullanıcıdan alıcının adını girmesini ister ve alıcının e-posta adresini ayarlar.
   - Ardından, `generate_message` fonksiyonunu kullanarak özel bir mesaj oluşturur.
   - Bir mesaj oluşturulursa (yani `Hiçbiri` değilse), alıcıya "Özel Gün Kutlaması" konulu bir e-posta gönderir.
   - Geçerli tarih için özel bir tatil veya fırsat yoksa, "Bugün özel bir tatil yok" yazdırır.

5. **`if __name__ == "__main__": main()`**:
   - Bu satır, kod doğrudan çalıştırıldığında `main` fonksiyonunun çalıştırılmasını sağlar, ancak başka bir kodda modül olarak içe aktarıldığında çalıştırılmaz.
