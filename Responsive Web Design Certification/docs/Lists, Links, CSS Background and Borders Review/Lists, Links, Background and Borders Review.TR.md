Listeler, Bağlantılar, Arka Plan ve Sınırlar İncelemesi
Stil Listeleri
line-heightÖzellik : Bu özellik, metin satırları arasında boşluk oluşturmak için kullanılır. Kabul edilen line-heightdeğerler arasında anahtar kelime normal, sayılar, yüzdeler ve uzunluk birimleri (örneğin ' emd') bulunur.
list-style-typeÖzellik : Bu özellik, liste öğesi için işaretleyici belirtmek için kullanılır. Kabul edilebilir değerler arasında daire, disk veya ondalık sayı bulunabilir.
İşte list-style-typemadde işaretinin stilini değiştirmek için bir örnek:

<link rel="stylesheet" href="styles.css">
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
ul {
  list-style-type: square;
}
list-style-positionÖzellik : Bu özellik, liste işaretçisinin konumunu ayarlamak için kullanılır. Kabul edilebilir yalnızca iki değer vardır: inside ve outside.
İşte insideve arasındaki farkı gösteren bir örnek outside:

<link rel="stylesheet" href="styles.css">
<ul class="inside-list">
  <li>Item with inside position</li>
  <li>Item with inside position</li>
</ul>
<ul class="outside-list">
  <li>Item with outside position</li>
  <li>Item with outside position</li>
</ul>
.inside-list {
  list-style-position: inside;
}

.outside-list {
  list-style-position: outside;
}
list-style-imageÖzellikurl : Bu özellik, liste öğesi işaretleyicisi için bir resim kullanmak amacıyla kullanılır. Yaygın bir kullanım örneği , geçerli bir resim konumuna ayarlanmış bir değerle işlevi kullanmaktır .
Liste öğeleri arasında boşluk bırakmamargin
Bunun yanı sıra line-height, CSS'de kenar boşlukları liste öğelerinin aralığını ve okunabilirliğini artırmak için de kullanılabilir.
Kenar boşlukları, her öğenin dışında boşluk oluşturarak liliste öğeleri arasındaki boşluğu kontrol etmeyi sağlar.
margin-bottomBu, her liste öğesinin altına boşluk oluşturmak için kullanılır. Örneğin, margin-bottom: 10px;her liste öğesinin altına 10 piksellik bir boşluk oluşturacaktır.
İşte margin-bottomliste öğeleri arasında boşluk bırakmaya yönelik bir örnek:

<link rel="stylesheet" href="styles.css">
<ul class="list">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
.list li {
  margin-bottom: 20px;
}
Stil Bağlantıları
pseudo-classBu, belirli bir duruma bağlı olarak öğeleri seçmenizi sağlayan, seçiciye eklenen bir anahtar kelimedir. Yaygın durumlar arasında :hover, :visitedve :focusdurumları bulunur.
:link pseudo-classBu sözde sınıf, kullanıcı tarafından ziyaret edilmemiş bağlantıları biçimlendirmek için kullanılır.
İşte :linksözde sınıfın kullanıldığı bir örnek:

<link rel="stylesheet" href="styles.css">
<a href="/">Example link</a>
a:link {
  color: red;
}
:visited pseudo-classBu sözde sınıf, kullanıcının daha önce ziyaret ettiği bağlantıları biçimlendirmek için kullanılır.
:hover pseudo-classBu sözde sınıf, kullanıcının fareyle üzerine geldiği öğeleri biçimlendirmek için kullanılır.
İşte :hoversözde sınıfın kullanıldığı bir örnek:

<link rel="stylesheet" href="styles.css">
<a href="/">Hover over me!</a>
a:hover {
  color: green;
  text-decoration: underline;
}
:focus pseudo-classBu sözde sınıf, bir öğeye odaklanıldığında ona stil vermek için kullanılır. Örnek olarak, inputtıklama selectveya sekme hareketiyle öğeye odaklanılan öğeler verilebilir.
İşte :focussözde sınıfın kullanıldığı bir örnek:

<link rel="stylesheet" href="styles.css">
<a href="/">Example link</a>
a:focus {
  outline: 2px solid orange;
}
:active pseudo-classBu sözde sınıf, kullanıcı tarafından etkinleştirilen bir öğeyi biçimlendirmek için kullanılır. Yaygın bir örnek, kullanıcının bir düğmeye tıklamasıdır.
İşte :activesözde sınıfın kullanıldığı bir örnek:

<link rel="stylesheet" href="styles.css">
<a href="/">Click me!</a>
a:active {
  color: pink;
}
Arka Planlar ve Sınırlarla Çalışmak
background-sizeÖzellik : Bu özellik, bir öğenin arka plan boyutunu ayarlamak için kullanılır. Yaygın değerler arasında coverarka plan resminin tüm öğeyi kaplaması ve containarka plan resminin öğenin içine sığması yer alır.
İşte bir örnek background-size: contain:

<style>
  body {
    background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    min-height: 100px;
  }
</style>
background-repeatÖzellik : Bu özellik, arka plan resimlerinin yatay ve dikey eksenler boyunca nasıl tekrarlanacağını belirlemek için kullanılır. Varsayılan değer, resmin hem yatay hem de dikey olarak tekrarlanacağı anlamına background-repeatgelir repeat. Ayrıca, bu özelliği kullanarak tekrar olmamasını da belirtebilirsiniz no-repeat.
İşte bir örnek background-repeat: no-repeat:

<style>
  body {
    background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
    background-size: contain;
    background-repeat: no-repeat;
    min-height: 100px;
  }
</style>
background-positionÖzelliktop : Bu özellik, arka plan resminin konumunu belirtmek için kullanılır. Belirli bir uzunluğa, yüzdeye veya , bottom, left, right, ve gibi anahtar kelime değerlerine ayarlanabilir center.
İşte bir örnek background-position:

<style>
  body {
    background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center top;
    min-height: 100px;
  }
</style>
background-attachmentÖzellik : Bu özellik, arka plan resminin içerikle birlikte kaydırılıp kaydırılmayacağını veya sabit kalıp kalmayacağını belirtmek için kullanılır. Başlıca değerler scroll(varsayılan), arka plan resminin içerikle birlikte kaydırıldığı ve fixedarka plan resminin ekranda aynı konumda kaldığı durumlardır.
background-imageÖzellik : Bu özellik, bir öğenin arka plan resmini ayarlamak için kullanılır. Aynı anda birden fazla arka plan resmi ayarlayabilir ve değer olarak url, radial-gradientveya linear-gradientişlevlerini kullanabilirsiniz.
İşte bir örnek background-image:

<style>
  body {
    background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
    min-height: 100px;
  }
</style>
backgroundÖzellik : Bu, tüm arka plan özelliklerini tek bir bildirimde ayarlamak için kullanılan kısaltılmış özelliktir. İşte arka plan resmini ayarlama ve tekrar etmemeyi ayarlama örneği:background: no-repeat url("example-url-goes-here");
İşte backgroundkısaltma özelliğini kullanan bir örnek:

<style>
  body {
    background: center top no-repeat url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
    min-height: 100px;
  }
</style>
Arka Plan ve Ön Plan Renkleri İçin İyi Kontrast : Metnin okunabilirliğini sağlamak için arka plan ve ön plan renklerinin iyi bir kontrasta sahip olması önemlidir. Web İçeriği Erişilebilirlik Yönergeleri (WCAG), normal metin için minimum 4,5:1 ve büyük metin için 3:1 kontrast oranını önermektedir.
Sınırlar
border-topÖzellik : Bu özellik, bir öğenin üst kenarlığı için stilleri ayarlamak için kullanılır. border-top: 3px solid blue;Öğenin üst tarafına 3 piksel genişliğinde düz mavi bir kenarlık uygular.
border-rightÖzellik : Bu özellik, bir öğenin sağ kenarlığı için stilleri ayarlamak için kullanılır. border-right: 2px solid red;Öğenin sağ tarafına 2 piksel genişliğinde düz kırmızı bir kenarlık uygular.
border-bottomÖzellik : Bu özellik, bir öğenin alt kenarlığının stillerini ayarlamak için kullanılır. border-bottom: 1px dashed green;Öğenin alt tarafına 1 piksel genişliğinde kesik çizgili yeşil bir kenarlık ekler.
border-leftÖzellik : Bu özellik, bir öğenin sol kenarlığı için stilleri ayarlamak için kullanılır. border-left: 4px dotted orange;Öğenin sol tarafına 4 piksel genişliğinde noktalı turuncu bir kenarlık ekler.
İşte ayrı ayrı kenar özelliklerini kullanan bir örnek:

<link rel="stylesheet" href="styles.css">
<div class="bordered-box">Box with different borders</div>
.bordered-box {
  border-top: 3px solid blue;
  border-right: 2px solid red;
  border-bottom: 1px dashed green;
  border-left: 4px dotted orange;
  padding: 20px;
}
borderÖzellik : Bu, bir öğenin kenarlığının genişliğini, stilini ve rengini ayarlamak için kullanılan kısaltılmış özelliktir. border: 1px solid black;1 piksel genişliğinde düz siyah bir kenarlık ayarlar.
İşte borderkısaltma özelliğini kullanan bir örnek:

<link rel="stylesheet" href="styles.css">
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="A cute cat lying on its back.">
img {
  border: 2px solid red;
}
border-radiusÖzellik : Bu özellik, bir öğenin kenarlığına yuvarlak köşeler oluşturmak için kullanılır.
İşte bir örnek border-radius:

<link rel="stylesheet" href="styles.css">
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="A cute cat lying on its back.">
img {
  border: 2px solid black;
  border-radius: 10px;
}
border-styleÖzellik : Bu özellik, bir öğenin kenarlığının stilini ayarlamak için kullanılır. Kabul edilen bazı değerler şunlardır: solid, dashed, dotted, ve double.
İşte farklı border-styledeğerler kullanan bir örnek:

<link rel="stylesheet" href="styles.css">
<div class="solid-border">Solid border</div>
<div class="dashed-border">Dashed border</div>
<div class="dotted-border">Dotted border</div>
.solid-border {
  border: 3px solid blue;
  margin-bottom: 10px;
  padding: 10px;
}

.dashed-border {
  border: 3px dashed red;
  margin-bottom: 10px;
  padding: 10px;
}

.dotted-border {
  border: 3px dotted green;
  padding: 10px;
}
Eğimler
linear-gradient()Fonksiyon : Bu CSS fonksiyonu, düz bir çizgi boyunca birden fazla renk arasında geçiş oluşturmak için kullanılır.
İşte bir örnek linear-gradient():

<link rel="stylesheet" href="styles.css">
<div class="linear-gradient"></div>
.linear-gradient {
  background: linear-gradient(to right, red, blue);
  height: 40vh;
}
radial-gradient()Fonksiyon : Bu CSS fonksiyonu, bir daire veya elips gibi belirli bir noktadan yayılan ve kademeli olarak birden fazla renk arasında geçiş yapan bir görüntü oluşturur.
İşte bir örnek radial-gradient():

<link rel="stylesheet" href="styles.css">
<div class="radial-gradient"></div>
.radial-gradient {
  background: radial-gradient(circle, red, blue);
  height: 40vh;
}