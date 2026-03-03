Duyarlı Web Tasarımı İncelemesi
Duyarlı Web Tasarımı
Tanım : Duyarlı tasarımın temel prensibi uyarlanabilirliktir; yani bir web sitesinin, görüntülendiği cihazın ekran boyutuna ve özelliklerine göre düzenini ve içeriğini ayarlayabilme yeteneğidir.
Esnek ızgaralar : Bunlar, piksel gibi sabit birimler yerine yüzde gibi göreceli birimler kullanır; bu da içeriğin ekran boyutuna göre yeniden boyutlandırılmasına ve yeniden düzenlenmesine olanak tanır.
Esnek resimler : Bunlar, içerdikleri öğeler içinde yeniden boyutlandırılacak şekilde ayarlanmıştır ve böylece daha küçük ekranlarda kapsayıcılarından taşmamaları sağlanır.
Medya Soruları
Tanım : Bu özellik, geliştiricilerin cihazın özelliklerine, özellikle de görüntü alanı genişliğine bağlı olarak farklı stiller uygulamasına olanak tanır.
<link rel="stylesheet" href="styles.css">
<p class="mq-example">The background of this paragraph will change when the viewport is at least 768px wide.</p>
.mq-example {
  padding: 10px;
  border: 1px solid #ccc;
  background-color: lightyellow;
}

@media screen and (min-width: 768px) {
  /* Styles for screens at least 768px wide */
  .mq-example {
    background-color: lightblue;
  }
}
allMedya Türü : Bu, tüm cihazlar için uygundur. Medya türü belirtilmediğinde varsayılan değerdir.
printMedya Türleri : Bu özellik, sayfalandırılmış materyaller ve baskı önizleme modunda ekranda görüntülenen belgeler için tasarlanmıştır.
screenMedya Türleri : Bu öncelikle ekranlar için tasarlanmıştır.
aspect-ratioBu, görüntüleme alanının genişliği ve yüksekliği arasındaki oranı tanımlar.
@media screen and (aspect-ratio: 16/9) {
  /* Styles for screens with a 16:9 aspect ratio */
}
orientationBu, cihazın yatay mı yoksa dikey mi konumda olduğunu belirtmek için kullanılır.
<link rel="stylesheet" href="styles.css">
<p class="orientation-example">This paragraph's background will change in landscape orientation.</p>
.orientation-example {
  padding: 10px;
  border: 1px solid #ccc;
  background-color: lightyellow;
}

@media screen and (orientation: landscape) {
  /* Styles for landscape orientation */
  .orientation-example {
    background-color: lightgreen;
  }
}
resolutionBu, çıkış aygıtının çözünürlüğünü inç başına nokta (dpi) veya santimetre başına nokta (dpcm) cinsinden tanımlamak için kullanılır.
@media screen and (min-resolution: 300dpi) {
  /* Styles for high-resolution screens */
}
hoverBu, birincil giriş mekanizmasının öğelerin üzerine gelip gelemeyeceğini test etmek için kullanılır.
<link rel="stylesheet" href="styles.css">
<button>Hover over me</button>
button {
  padding: 10px 20px;
  font-size: 1rem;
  background-color: lightgray;
  border: 1px solid #999;
  cursor: pointer;
}

@media (hover: hover) {
  /* Styles for devices that support hover */
  button:hover {
    background-color: yellow;
  }
}
prefers-color-schemeBu, kullanıcının açık veya koyu renk teması isteyip istemediğini tespit etmek için kullanılır.
Medya Sorguları ve Mantıksal Operatörler : andOperatör, birden fazla medya özelliğini birleştirmek için kullanılırken, notve onlyoperatörleri medya sorgularını olumsuzlamak veya izole etmek için kullanılabilir.
<link rel="stylesheet" href="styles.css">
<p class="logical-example">This paragraph's background will change when the screen is at least 768px wide AND in landscape orientation.</p>
.logical-example {
  padding: 10px;
  border: 1px solid #ccc;
  background-color: lightyellow;
}

@media screen and (min-width: 768px) and (orientation: landscape) {
  /* Styles for landscape screens at least 768px wide */
  .logical-example {
    background-color: lightcoral;
  }
}
Ortak Medya Kırılma Noktaları
Tanım : Medya kırılma noktaları, bir web sitesinin tasarımında düzenin ve içeriğin farklı ekran boyutlarına uyum sağlamak için ayarlandığı belirli noktalardır. Telefonları, tabletleri ve masaüstü ekranlarını hedeflemek için kullanabileceğiniz bazı genel kırılma noktaları vardır. Ancak farklı cihazlar için olası her ekran boyutunu tek tek takip etmeye çalışmak akıllıca değildir.
<link rel="stylesheet" href="styles.css">
<p class="breakpoint-example">This text will change size when the viewport width is at least 768px.</p>
.breakpoint-example {
  font-size: 1rem;
  padding: 10px;
  border: 1px solid #ccc;
}

/* Styles for screens wider than 768px */
@media screen and (min-width: 768px) {
  .breakpoint-example {
    font-size: 1.125rem;
    background-color: lightblue;
  }
}
Küçük boyutlu cihazlar (akıllı telefonlar) : 640 piksele kadar
Orta Boy Cihazlar (tabletler) : 641px - 1024px
Büyük Cihazlar (masaüstü bilgisayarlar) : 1025 piksel ve üzeri
Mobil öncelikli yaklaşım
Tanım : Mobil öncelikli yaklaşım, duyarlı web tasarımında, daha büyük ekranlar için tasarım yapmadan önce web sitelerini mobil cihazlar için oluşturmaya öncelik veren bir tasarım felsefesi ve geliştirme stratejisidir.
<link rel="stylesheet" href="styles.css">
<div class="container">
  <p>The width of this container changes based on the viewport size.</p>
</div>
/* Base styles for mobile */
.container {
  width: 100%;
  padding: 10px;
  background-color: lightblue;
}

/* Styles for larger screens */
@media screen and (min-width: 768px) {
  .container {
    width: 750px;
    margin: 0 auto;
    padding: 20px;
  }
}

@media screen and (min-width: 1024px) {
  .container {
    width: 960px;
  }
}