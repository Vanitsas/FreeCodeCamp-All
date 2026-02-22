CSS Düzenleri ve Efektleri İncelemesi
CSS Taşma Özelliği
Tanım : Taşma (overflow), öğelerin, kapsayıcı öğenin boyutunu aşan veya "taşan" içeriği ele alma biçimini ifade eder. Taşma iki boyutludur.
overflow-xX ekseni yatay taşmayı belirler.
overflow-yY ekseni dikey taşmayı belirler.
overflowoverflow-x: ve için kısaltılmış özellik overflow-y. Tek bir değer verilirse, her iki taşma da bu değeri kullanır. İki değer verilirse, overflow-xilki kullanılır ve overflow-yikincisi kullanılır.
<link rel="stylesheet" href="styles.css">
<div class="overflow-box">
  This is very long content that will overflow horizontally and vertically.
  <br />
  This is very long content that will overflow horizontally and vertically.
  <br />
  This is very long content that will overflow horizontally and vertically.
  <br />
  This is very long content that will overflow horizontally and vertically.
  <br />
  This is very long content that will overflow horizontally and vertically.
  <br />
  This is very long content that will overflow horizontally and vertically.
</div>
.overflow-box {
  width: 140px;
  height: 70px;
  border: 2px solid black;
  overflow-x: auto;
  overflow-y: auto;
  white-space:nowrap;
}
CSS Dönüştürme Özelliği
Tanım : Bu özellik, öğelere 2 boyutlu veya 3 boyutlu uzayda döndürme, ölçeklendirme, eğme veya öteleme (hareket ettirme) gibi çeşitli dönüşümler uygulamanıza olanak tanır.
translate()Fonksiyon : Bu fonksiyon, bir öğeyi mevcut konumundan hareket ettirmek için kullanılır.
scale()Fonksiyon : Bu fonksiyon, bir öğenin boyutunu değiştirmenize olanak tanır.
rotate()Fonksiyon : Bu fonksiyon, bir öğeyi döndürmenizi sağlar.
skew()Fonksiyon : Bu fonksiyon, bir öğeyi eğmenizi sağlar.
Dönüşümler ve Erişilebilirlik : İçeriği gizlemek veya göstermek için dönüşüm kullanıyorsanız, içeriğin ekran okuyucular ve klavye navigasyonu için hala erişilebilir olduğundan emin olun. Gizlenen içerik, yalnızca görsel olarak ekrandan çıkarılmak yerine, display: noneveya gibi yöntemler kullanılarak gerçekten gizlenmelidir.visibility: hidden
<link rel="stylesheet" href="styles.css">
<div class="container">
  <div class="transform-box translate">Translate</div>
  <div class="transform-box scale">Scale</div>
  <div class="transform-box rotate">Rotate</div>
  <div class="transform-box skew">Skew</div>
</div>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.transform-box {
  width: 100px;
  height: 100px;
  background: coral;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* translate() */
.translate {
  transform: translateX(20px);
}

/* scale() */
.scale {
  transform: scale(1.2);
}

/* rotate() */
.rotate {
  transform: rotate(15deg);
}

/* skew() */
.skew {
  transform: skew(10deg, 5deg);
}
Kutu Modeli
Tanım : CSS kutu modelinde, her öğe bir kutu ile çevrilidir. Bu kutu dört bileşenden oluşur: içerik alanı, `<div>` padding, ` border<div>`, `<div> margin`.
İçerik Alanı : İçerik alanı, kutunun en iç kısmıdır. Metin veya resim gibi bir öğenin gerçek içeriğini barındıran alandır.
paddingDolgu (padding), içerik alanının hemen ardından gelen alandır. İçerik alanı ile bir öğenin kenarlığı arasındaki boşluktur.
borderKenarlık, CSS kutu modelinde bir öğenin dış kenarı veya dış çizgisidir. Öğenin görsel sınırıdır.
marginKenar boşluğu, bir öğenin sınırının dışındaki alandır. Bir öğe ile etrafındaki diğer öğeler arasındaki mesafeyi belirler.
<link rel="stylesheet" href="styles.css">
<div class="box-model">Content</div>
.box-model {
  width: 120px;
  background: lightblue;
  padding: 16px;
  border: 4px solid teal;
  margin: 20px;
  text-align: center;
}
Kenar Çökmesi
Tanım : Bu davranış, bitişik öğelerin dikey kenar boşluklarının üst üste gelmesi ve iki kenar boşluğundan daha büyük olanına eşit tek bir kenar boşluğu oluşması durumunda ortaya çıkar. Bu davranış yalnızca dikey kenar boşlukları (üst ve alt) için geçerlidir, yatay kenar boşlukları (sol ve sağ) için geçerli değildir.
content-boxve Gayrimenkul border-boxDeğerleri
box-sizingÖzellikwidth : Bu özellik, bir HTML öğesi için nihai ve değerlerinin nasıl heighthesaplanacağını belirlemek için kullanılır .
content-boxDeğer : Modelde content-box, bir öğe için belirlediğiniz widthve değerleri içerik alanının boyutlarını belirler, ancak , , veya heightdeğerlerini içermez .paddingbordermargin
border-boxDeğer : ile border-box, bir öğenin widthve heightözellikleri içerik alanını, paddingve öğelerini içerir border, ancak öğesini içermez margin.
<link rel="stylesheet" href="styles.css">
<div class="sizing-box content-box">Content-box</div>
<div class="sizing-box border-box">Border-box</div>
.sizing-box {
  width: 150px;
  padding: 10px;
  border: 4px solid teal;
  margin-bottom: 10px;
  background: peachpuff;
  text-align: center;
}

.content-box {
  box-sizing: content-box;  
}

.border-box {
  box-sizing: border-box;
  background: lightgreen;
}
CSS Sıfırlama
Tanım : CSS sıfırlama, web tarayıcılarının HTML öğelerine uyguladığı varsayılan biçimlendirmenin tamamını veya bir kısmını kaldıran bir stil sayfasıdır. CSS sıfırlama için üçüncü taraf seçenekler arasında sanitize.cssve bulunur normalize.css.
CSS Filtre Özelliği
Tanım : Bu özellik, bulanıklık, renk kaydırma ve kontrast ayarlama gibi çeşitli efektler oluşturmak için kullanılabilir.
blur()Fonksiyon : Bu fonksiyon, öğeye Gauss bulanıklığı uygular. Miktar piksel cinsinden tanımlanır ve bulanıklığın yarıçapını temsil eder.
brightness()Fonksiyon : Bu fonksiyon, öğenin parlaklığını ayarlar. %0 değeri öğeyi tamamen siyah yaparken, %100'ün üzerindeki değerler parlaklığı artırır.
contrast()Fonksiyon : Bu fonksiyon, öğenin kontrastını ayarlar. %0 değeri öğeyi tamamen gri yapar, %100 değeri öğenin normal görünmesini sağlar ve %100'den büyük değerler kontrastı artırır.
grayscale()Fonksiyon : Bu fonksiyon, öğeyi gri tonlamaya dönüştürür. Oran yüzde olarak tanımlanır; %100 tamamen gri tonlama, %0 ise görüntüyü değiştirmeden bırakır.
sepia()Fonksiyon : Bu fonksiyon, öğeye sepya tonu uygular. Gri tonlama gibi, yüzde değeri kullanır.
hue-rotate()Fonksiyon : Bu fonksiyon, öğeye renk tonu döndürme işlemi uygular. Değer derece cinsinden tanımlanır ve renk çemberi etrafındaki bir döndürmeyi temsil eder.
<link rel="stylesheet" href="styles.css">
<div class="container">
  <img class="filter blur" src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="Blur" />
  <img class="filter brightness" src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="Brightness" />
  <img class="filter contrast" src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="Contrast" />
  <img class="filter grayscale" src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="Grayscale" />
  <img class="filter sepia" src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="Sepia" />
  <img class="filter hue" src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="Hue Rotate" />
</div>
.container {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.filter {
  width: 120px;
}

/* blur() */
.blur {
  filter: blur(3px);
}

/* brightness() */
.brightness {
  filter: brightness(130%);
}

/* contrast() */
.contrast {
  filter: contrast(150%);
}

/* grayscale() */
.grayscale {
  filter: grayscale(100%);
}

/* sepia() */
.sepia {
  filter: sepia(100%);
}

/* hue-rotate() */
.hue {
  filter: hue-rotate(90deg);
}