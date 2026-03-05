CSS Grid İncelemesi
CSS Grid Temelleri
Tanım : CSS Grid, web sayfalarında karmaşık düzenler oluşturmak için kullanılan iki boyutlu bir düzen sistemidir. Izgaralar, aralarında boşluklar bulunan satır ve sütunlardan oluşur. Bir ızgara düzeni tanımlamak için, özelliği `<grid>` displayolarak ayarlamanız gerekir grid.
.container {
  display: grid;
}
fr(Kesirli) Birim :fr Bu birim, ızgara kabı içindeki alanın bir kesrini temsil eder. Bu birimi esnek ızgaralar oluşturmak için kullanabilirsiniz .
CSS grid'de izler arasında boşluk oluşturmanıncolumn-gap üç yolu vardır. Sütunlar arasında boşluk oluşturmak için `<port>` özelliğini kullanabilirsiniz. Satırlar arasında boşluk oluşturmak için `<port>` özelliğini kullanabilirsiniz. Veya hem satırlar hem de sütunlar arasında boşluk oluşturmak için kısaltılmış `<port>` özelliğini row-gapkullanabilirsiniz .gap
grid-template-columnsBu, ızgara izleme sütunları için çizgi adlarını ve boyutlarını ayarlamak için kullanılır.
.container {
  display: grid;
  width: 100%;
  grid-template-columns: 30px 1fr;
}
grid-template-rowsBu, ızgara izleme satırları için satır adlarını ve boyutlarını ayarlamak için kullanılır.
grid-auto-flowBu, otomatik olarak yerleştirilen öğelerin ızgaraya nasıl sığacağını belirler.
.container {
  display: grid;
  width: 100%;
  grid-auto-flow: column;
}
grid-auto-columnsBu, örtük olarak oluşturulan sütunların boyutunu ayarlamak için kullanılır.
.container {
  display: grid;
  width: 100%;
  grid-auto-columns: auto;
}
place-itemsBu, hem blok hem de satır içi yönlerdeki öğeleri hizalamak için kullanılır.
align-itemsBu, bir tablo kapsayıcısındaki öğelerin hizalamasını ayarlamak için kullanılır.
repeat()Fonksiyon : Bu fonksiyon, parça listesindeki bölümleri tekrarlamak için kullanılır. Yazmak yerine grid-template-columns: 1fr 1fr 1fr;bu fonksiyonu kullanabilirsiniz repeat().
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
Açık Izgaragrid-template-columns : veya özelliklerini kullanarak satır veya iz sayısını belirtebilirsiniz grid-template-rows.
Örtük Izgara : Öğeler ızgaranın dışına yerleştirildiğinde, bu dışarıdaki öğeler için otomatik olarak satırlar ve sütunlar oluşturulur.
minmax()Fonksiyon : Bu fonksiyon, bir pist için minimum ve maksimum boyutları ayarlamak için kullanılır.
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(150px, auto);
}
Çizgi Tabanlı Yerleştirmegrid-column-start : Tüm ızgaraların çizgileri vardır. Öğenin bir çizgi üzerinde nerede başladığını belirtmek için ve özelliklerini kullanabilirsiniz . Öğenin çizgi üzerinde nerede bittiğini belirtmek için ve özelliklerini grid-row-startkullanabilirsiniz . Bunun yerine veya kısaltma özelliklerini de kullanmayı tercih edebilirsiniz .grid-column-endgrid-row-endgrid-columngrid-row
İşte grid-columnbir öğenin tüm sütunlara yayılmasını sağlamak için bu özelliğin kullanımına bir örnek.

.element {
  grid-column: 1 / -1;
}
grid-template-areasBu özellik, ızgaraya yerleştireceğiniz öğelere isim vermek için kullanılır.
<link rel="stylesheet" href="styles.css">

<div class="container">
  <div class="header">Header</div>
  <div class="sidebar">Sidebar</div>
  <div class="main">Main Content</div>
  <div class="footer">Footer</div>
</div>

.container {
  display: grid;
  grid-template-columns: 200px 1fr; 
  grid-template-rows: auto 1fr auto; 
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer"; 
  gap: 20px; 
}

.header {
  grid-area: header; 
  background-color: #4CAF50;
  padding: 10px;
  color: white;
}

.sidebar {
  grid-area: sidebar;
  background-color: #f4f4f4;
  padding: 10px;
}

.main {
  grid-area: main; 
  background-color: #e0e0e0;
  padding: 10px;
}

.footer {
  grid-area: footer; 
  background-color: #4CAF50;
  padding: 10px;
  color: white;
}
CSS'de Hata Ayıklama
Geliştirici Araçları (DevTools) : Geliştirici Araçları, CSS'inizi gerçek zamanlı olarak incelemenize ve değiştirmenize olanak tanır. Stiller bölmesi, miras alınan stiller de dahil olmak üzere seçilen öğeye uygulanan tüm CSS kurallarını gösterir. Tek tek özellikleri açıp kapatabilir, değerleri düzenleyebilir ve hatta doğrudan tarayıcıda yeni kurallar ekleyebilirsiniz. Bu anlık geri bildirim, kaynak kodunuzu değiştirmeden farklı stillerle deneme yapmak için inanılmaz derecede kullanışlıdır.
CSS Doğrulayıcıları : Doğrulayıcılar, CSS kodunuzu resmi spesifikasyonlara göre kontrol etmek ve hataları veya uyarıları bildirmek için kullanılır. Kullanabileceğiniz popüler bir doğrulayıcı W3C CSS Doğrulayıcısıdır.
Duyarlı Tasarımlarda Hata Ayıklama : Geliştirici Araçları, sitenizin çeşitli ekran boyutlarında ve cihazlarda nasıl görüneceğini simüle etmenize olanak tanıyan bir seçeneğe sahiptir. Bu, kırılma noktası sorunlarını veya farklı görüntüleme alanı boyutlarında iyi ölçeklenmeyen stilleri belirlemenize yardımcı olabilir.