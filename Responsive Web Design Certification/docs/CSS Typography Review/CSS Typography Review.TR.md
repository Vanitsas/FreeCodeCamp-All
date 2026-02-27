CSS Tipografi İncelemesi
Tipografiye Giriş
Tanım : Tipografi, metni görsel olarak çekici ve okunması kolay hale getirmek için doğru yazı tiplerini ve biçimini seçme sanatıdır. "Tip", tek tek karakterlerin nasıl tasarlandığını ve düzenlendiğini ifade eder.

Yazı Tipi Tanımı : Yazı tipi, bir karakter, sayı ve sembol kümesinin genel tasarımı ve stilidir. Bir yazı tipi ailesinin taslağı gibidir.

Yazı Tipi Tanımı : Yazı tipi, boyut, kalınlık, stil ve genişlik gibi belirli özelliklere sahip bir yazı karakterinin özel bir varyasyonudur.

Serif Yazı Tipi : Bu yazı tipi, karakterlerin sonunda küçük çizgiler bulunan klasik bir stile sahiptir. Serif yazı tipleri genellikle kitap gibi basılı materyallerde kullanılır.

Sans Serif Yazı Tipi : Bu yazı tipi, karakterlerin sonundaki küçük çizgiler olmadan daha modern bir görünüme sahiptir. Sans Serif yazı tipleri, ekranda okunması kolay oldukları için dijital tasarımda yaygın olarak kullanılır. Helvetica, Arial ve Roboto gibi yazı tipleri buna örnek verilebilir.

Yazı Tipi Kalınlığı : Bu, karakterlerin kalınlığını ifade eder ve açık, normal, kalın ve siyah seçenekleri içerir.

Yazı Tipi Stili : Bu, karakterlerin eğimi ve yönüdür; örneğin italik ve eğik yazı tipi gibi.

Yazı Tipi Genişliği : Bu, karakterlerin yatay olarak kapladığı alandır; örneğin daraltılmış ve genişletilmiş yazı tipleri gibi.

Temel çizgi : Bu, karakterlerin çoğunun üzerinde durduğu hayali çizgidir.

Büyük Harf Yüksekliği : Bu, büyük harflerin taban çizgisinden tepesine kadar ölçülen yüksekliğidir.

X-yüksekliği : Bu, üst ve alt uzantılar hariç, küçük harflerin ortalama yüksekliğidir.

Yükselenler : Bunlar, küçük harflerin x yüksekliğinin üzerine uzanan kısımlarıdır; örneğin 'h', 'b', 'd' ve 'f' harflerinin üst kısımları.

Alt uzantılar : Bunlar, küçük harflerin taban çizgisinin altına uzanan kısımlarıdır; örneğin 'y', 'g', 'p' ve 'q' harflerinin kuyrukları.

Harf aralığı ayarı (Kerning) : Bu, okunabilirliği ve estetiği iyileştirmek için belirli karakter çiftleri arasındaki boşluğun nasıl ayarlandığıdır. Örneğin, A ve V harfleri arasındaki boşluğun azaltılması.

Karakter Aralığı : Bu, bir metin bloğundaki tüm karakterler arasındaki boşluğun nasıl ayarlandığını belirler. Esasen karakterler arasındaki mesafedir. Metnin ne kadar yoğun ve açık olacağını etkiler.

Satır Aralığı : Bu, metin satırları arasındaki dikey boşluktur. Bir satırın taban çizgisinden bir sonraki satırın taban çizgisine kadar ölçülür.

Tipografiyle İlgili En İyi Uygulamalar : Tasarımlarınızın anlaşılmasını kolaylaştırmak için net ve basit yazı tipleri seçmelisiniz. Bu, özellikle web sitenizin ana metni için önemlidir. Yazı tipi kolay okunabilirse, kullanıcıların içeriğinizle etkileşime girme olasılığı daha yüksektir. Görsel tutarlılık oluşturmak için en fazla iki veya üç yazı tipi kullanmalısınız. Çok fazla yazı tipi kullanmak, metni okumayı zorlaştırabilir ve markanızın kimliğini zayıflatabilir. Bu ayrıca web sitesinin yüklenme süresini artırarak kullanıcı deneyimini de etkileyebilir. Başlıklar, alt başlıklar, paragraflar ve diğer öğeler için görsel bir hiyerarşi oluşturmak için yazı tipi boyutunu kullanabilirsiniz. Örneğin, bir web sayfasındaki ana başlık daha büyük bir yazı tipine sahip olmalı, ardından daha küçük yazı tipi boyutlarına sahip alt başlıklar gelmelidir. Bu, hiyerarşideki her öğeye, kullanıcıların yapıda görsel olarak gezinmesine yardımcı olan belirli bir yazı tipi boyutu verecektir.

CSS font-familyÖzelliği
Tanım : Bir yazı tipi ailesi, ortak bir tasarıma sahip yazı tipleri grubudur. Aynı aileye ait tüm yazı tipleri aynı temel yazı tipine dayanır, ancak stil, kalınlık ve genişlik açısından da farklılıklar gösterirler. Birden fazla yazı tipi ailesini, en yüksekten en düşüğe doğru öncelik sırasına göre virgülle ayırarak belirtebilirsiniz. Bu alternatif yazı tipleri, yedek seçenekler olarak işlev görecektir. Yazı tipi ailesi listesinin sonuna her zaman genel bir yazı tipi ailesi eklemelisiniz.
font-family: Arial, Lato;
Yaygın Yazı Tipi Aileleri : İşte CSS'de kullanılan bazı yaygın yazı tipi aileleri: serif, sans-serif, monospace, cursive, fantasy
Web Güvenli Yazı Tipleri
Tanım : Bu yazı tipleri, bir bilgisayarda veya cihazda yüklü olma olasılığı çok yüksek olan yazı tiplerinin bir alt kümesidir. Tarayıcı bir yazı tipini işlemek zorunda kaldığında, kullanıcının sisteminde yazı tipi dosyasını bulmaya çalışır. Ancak yazı tipi bulunamazsa, genellikle varsayılan sistem yazı tipine geri döner.

Web Güvenli Yazı Tipleri :

Sans-serif yazı tipleri, karakterlerin sonunda küçük "ayaklar" veya çizgiler bulunmadığı için ekranda okunması kolay olduğundan web geliştirme alanında yaygın olarak kullanılır. Web için güvenli sans-serif yazı tiplerine örnek olarak Arial, Verdana ve Trebuchet MS verilebilir.
Buna karşılık, serif yazı tiplerinin karakterlerin sonunda küçük "ayakları" vardır, bu nedenle genellikle geleneksel baskıda kullanılırlar. Web için güvenli serif yazı tipleri şunlardır: Times New Roman ve Georgia.
At kuralları ve @font-faceAt kuralı
Tanım : `@` kuralları, tarayıcıya talimatlar veren ifadelerdir. Bunları, medya sorguları, anahtar kareler, yazı tipleri ve daha fazlası gibi stil sayfasının çeşitli yönlerini tanımlamak için kullanabilirsiniz.
@font-faceBu, yazı tipi dosyasını, biçimini ve ağırlık ve stil gibi diğer önemli özellikleri belirterek özel bir yazı tipi tanımlamanıza olanak tanır. Kuralın @font-facegeçerli olması için özelliği de belirtmeniz gerekir src. Bu özellik, yazı tipi kaynaklarına referanslar içerir.
@font-face {
  font-family: "MyCustomFont"; 
  src: url("path/to/font.woff2"),
       url("path/to/font.woff"),
       url("path/to/font.otf");
}
Yazı Tipi Biçimleri : Her yazı tipi kaynağı için biçimi de belirtebilirsiniz. Bu isteğe bağlıdır. Tarayıcıya yazı tipi biçimi hakkında bir ipucu verir. Biçim belirtilmezse, kaynak indirilir ve indirildikten sonra biçim algılanır. Biçim geçersizse, kaynak indirilmez. Olası yazı tipi biçimleri şunlardır collection: embedded-opentype, opentype, svg, truetype, woff, ve woff2.
@font-face {
  font-family: "MyCustomFont"; 
  src: url("path/to/font.woff2") format("woff2"),
       url("path/to/font.otf") format("opentype"),
       url("path/to/font.woff") format("woff");
}
woffvewoff2 : woff"Web Açık Yazı Tipi Formatı" anlamına gelir. Mozilla tarafından Type Supply, LettError ve diğer kuruluşlarla işbirliği içinde geliştirilen, yaygın olarak kullanılan bir yazı tipi formatıdır. woffve arasındaki fark, woff2verileri sıkıştırmak için kullanılan algoritmadır.
OpenType : Microsoft ve Adobe tarafından geliştirilen, ölçeklenebilir bilgisayar yazı tipleri için bir formattır ve kullanıcıların bir yazı tipindeki ek özelliklere erişmesine olanak tanır. Başlıca işletim sistemlerinde yaygın olarak kullanılır.
tech()Bu, yazı tipi kaynağının teknolojisini belirtmek için kullanılır. İsteğe bağlıdır.
@font-face {
  font-family: "MyCustomFont"; 
  src: url("path/to/font.woff2") format("woff2"),
       url("path/to/font.otf") format("opentype") tech(color-COLRv1),
       url("path/to/font.woff") format("woff");
}
Harici Yazı Tipleriyle Çalışmak
Tanım : Harici yazı tipi, proje dosyalarınıza doğrudan dahil edilmeyen bir yazı tipi dosyasıdır. Genellikle ayrı bir sunucuda barındırılırlar. Bu harici yazı tiplerini projenize dahil etmek için CSS'nizde bir link`<font>` öğesi veya ` <font>` ifadesi kullanabilirsiniz .@import
Google Fonts : Bu, Google'ın sunduğu ve çoğu özellikle web geliştirme için tasarlanmış yazı tiplerinden oluşan bir koleksiyondur.
İşte bu linköğeyi kullanan bir örnek:

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
.roboto-thin {
  font-family: "Roboto", sans-serif;
  font-weight: 100;
  font-style: normal;
}
İşte bu @importifadeyi kullanan bir örnek:

@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');
Font Squirrel : Bu, projelerinize özel harici yazı tipleri eklemek için kullanabileceğiniz bir diğer popüler kaynaktır.
text-shadowMülk
Tanım : Bu özellik metne gölge uygulamak için kullanılır. Gölgenin metinden yatay ve dikey mesafesini temsil eden X ve Y ofset değerlerini belirtmeniz gerekir. Bu değerler zorunludur. X ofsetinin pozitif değerleri gölgeyi sırasıyla sağa ve aşağıya doğru hareket ettirirken, negatif değerler gölgeyi sola ve yukarıya doğru hareket ettirir.
<link rel="stylesheet" href="styles.css">
<p>Typography Shadow</p>
  p {
    text-shadow: 3px 2px;
  }
Gölge Rengi : Bu değeri ofsetten önce veya sonra belirterek gölgenin rengini de özelleştirebilirsiniz. Renk belirtilmezse, tarayıcı rengi otomatik olarak belirleyecektir, bu nedenle genellikle açıkça belirtmek en iyisidir.
<link rel="stylesheet" href="styles.css">
<p>Colored Shadow</p>
p {
  text-shadow: 3px 2px #00ffc3;
}
Bulanıklık Yarıçapı : Bulanıklık yarıçapı isteğe bağlıdır ancak gölgenin çok daha pürüzsüz ve daha incelikli görünmesini sağlar. Bulanıklık yarıçapının varsayılan değeri sıfırdır. Değer ne kadar yüksek olursa, bulanıklık o kadar büyük olur, bu da gölgenin daha açık hale gelmesi anlamına gelir.
<link rel="stylesheet" href="styles.css">
<p>Blurred Shadow</p>
p {
  text-shadow: 3px 2px 3px #00ffc3;
}
Birden Fazla Metin Gölgesi Uygulama : Metnin birden fazla gölgesi olabilir. Gölgeler, önden arkaya doğru, ilk gölge en üstte olacak şekilde katmanlar halinde uygulanacaktır.
<link rel="stylesheet" href="styles.css">
<p>Multiple Shadows</p>
p {
  text-shadow:
    3px 2px 3px #00ffc3,
    -3px -2px 3px #0077ff,
    5px 4px 3px #dee7e5;
}