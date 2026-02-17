CSS Renkleri İncelemesi
Renk Teorisi
Renk Teorisi Tanımı : Bu, renklerin birbirleriyle nasıl etkileşimde bulunduğunu ve algımızı nasıl etkilediğini inceleyen bilim dalıdır. Renk ilişkilerini, renk uyumunu ve rengin psikolojik etkisini kapsar.
Ana Renkler : Sarı, mavi ve kırmızı olan bu renkler, diğer tüm renklerin türetildiği temel tonlardır.
İkincil Renkler : Bu renkler, iki ana rengin eşit miktarlarda karıştırılmasıyla elde edilir. Yeşil, turuncu ve mor, ikincil renklere örneklerdir.
Üçüncül Renkler : Bu renkler, birincil bir rengin komşu bir ikincil renkle birleştirilmesiyle elde edilir. Sarı-yeşil, mavi-yeşil ve mavi-mor, üçüncül renklere örneklerdir.
Sıcak Renkler : Kırmızı, turuncu ve sarı gibi renkler rahatlık, sıcaklık ve huzur duyguları uyandırır.
Soğuk Renkler : Mavi, yeşil ve mor gibi renkler sakinlik, huzur ve profesyonellik duyguları uyandırır.
Renk Çemberi : Renk çemberi, renklerin birbirleriyle nasıl ilişkili olduğunu gösteren dairesel bir şemadır. Tasarımcılar için renk kombinasyonlarını seçmelerine yardımcı olduğu için önemli bir araçtır.
Benzer Renk Şemaları : Bu renk şemaları, uyumlu ve sakinleştirici deneyimler yaratır. Renk çemberinde birbirine bitişik olan benzer renkleri içerirler.
Tamamlayıcı Renk Şemaları : Bu renk şemaları yüksek kontrast ve görsel etki yaratır. Renkleri, birbirlerine göre renk çemberinin zıt uçlarında yer alır.
Üçlü Renk Şeması : Bu renk şeması canlı renklere sahiptir. Renkler, birbirlerinden yaklaşık olarak eşit uzaklıkta olan renklerden oluşur. Birbirlerine bağlandıklarında, renk çemberinde eşkenar üçgen oluştururlar.
Tek Renkli Renk Şeması : Bu renk şemasında, tüm renkler aynı temel renkten, açıklık, koyuluk ve doygunluk ayarları yapılarak elde edilir. Bu, kontrast yaratırken aynı zamanda birlik ve uyum duygusu uyandırır.
CSS'te Renklerle Çalışmanın Farklı Yolları
Adlandırılmış Renkler : Bu renkler, tarayıcılar tarafından tanınan önceden tanımlanmış renk adlarıdır. Örnekler arasında blue, darkred, bulunur lightgreen.
rgb()Fonksiyon : RGB, ışığın ana renkleri olan Kırmızı, Yeşil ve Mavi'nin kısaltmasıdır. Bu üç renk, geniş bir renk yelpazesi oluşturmak için farklı yoğunluklarda birleştirilir. Bu rgb()fonksiyon, RGB renk modelini kullanarak renkleri tanımlamanıza olanak tanır.
<link rel="stylesheet" href="styles.css">
<p>RGB Color</p>
p {
  color: rgb(255, 0, 0);
}
rgba()Fonksiyon : Bu fonksiyon, rengin şeffaflığını kontrol eden dördüncü bir değer olan alfa değerini ekler. Alfa değeri belirtilmezse, varsayılan değer boş bırakılır 1.
<link rel="stylesheet" href="styles.css">
<div>RGBA Background</div>
div {
  background-color: rgba(0, 0, 255, 0.5);
}
hsl()İşlev : HSL, Renk Tonu, Doygunluk ve Parlaklık anlamına gelir; bunlar bir rengi tanımlayan üç temel bileşendir.
<link rel="stylesheet" href="styles.css">
<p>HSL Color</p>
p {
  color: hsl(120, 100%, 50%);
}
hsla()Fonksiyon : Bu fonksiyon, rengin saydamlığını kontrol eden dördüncü bir değer olan alfa değerini ekler.
<link rel="stylesheet" href="styles.css">
<div>HSLA Background</div>
div {
  background-color: hsla(0, 100%, 50%, 0.5);
}
Onaltılık (Hexadecimal ): Onaltılık kod (hexadecimal code'un kısaltması), RGB renk modelinde renkleri temsil etmek için kullanılan altı karakterlik bir dizedir. "Hex" terimi, 0'dan 9'a kadar rakamlar ve A'dan F'ye kadar harfler kullanan 16 tabanlı sayı sistemini ifade eder.
<link rel="stylesheet" href="styles.css">
<h3 class="hex-text">Hex Text</h3>
<p class="hex-bg">Hex Background</p>
h1 {
  color: #FF5733; /* A reddish-orange color */
}

p {
  background-color: #4CAF50; /* A shade of green */
}
Doğrusal ve Radyal Gradyanlar
Doğrusal Gradyanlar : Bu gradyanlar, düz bir çizgi boyunca renkler arasında kademeli bir geçiş oluşturur. Bu çizginin yönünü to top, to right, gibi anahtar kelimeler to bottom rightveya gibi açılar kullanarak kontrol edebilirsiniz 45deg. İstediğiniz herhangi bir geçerli CSS rengini ve istediğiniz kadar renk durağını kullanabilirsiniz.
<link rel="stylesheet" href="styles.css">
<div class="linear-gradient">Linear Gradient</div>
.linear-gradient {
  background: linear-gradient(45deg, red, #33FF11, rgba(100, 100, 255, 0.5));
  height: 40vh;
}
Radyal Gradyanlar : Bu gradyanlar, merkezi bir noktadan yayılan dairesel veya elips şeklinde gradyanlar oluşturur.
<link rel="stylesheet" href="styles.css">
<div class="radial-gradient">Radial Gradient</div>
.radial-gradient {
  background: radial-gradient(circle, red, blue);
  height: 40vh;
}