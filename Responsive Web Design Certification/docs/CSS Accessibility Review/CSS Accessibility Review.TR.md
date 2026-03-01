CSS Erişilebilirlik İncelemesi
Renk Kontrastı Araçları
WebAIM Renk Kontrastı Denetleyicisi : Bu çevrimiçi araç, tasarımınızın ön plan ve arka plan renklerini girmenize ve bunların Web İçeriği Erişilebilirlik Yönergeleri (WCAG) standartlarına uygun olup olmadığını anında görmenize olanak tanır.
TPGi Renk Kontrastı Analiz Aracı : Bu ücretsiz renk kontrastı denetleyicisi, web sitelerinizin ve uygulamalarınızın Web İçeriği Erişilebilirlik Yönergeleri (WCAG) standartlarını karşılayıp karşılamadığını kontrol etmenizi sağlar. Bu araç ayrıca, renk körlüğü sorunu olan kişiler için web sitenizin veya uygulamanızın nasıl göründüğünü görmenizi sağlayan bir Renk Körlüğü Simülatörü özelliği de içerir.
Erişilebilirlik Ağacı
Erişilebilirlik ağacı, ekran okuyucular gibi yardımcı teknolojilerin bir web sayfasındaki içeriği yorumlamak ve onunla etkileşim kurmak için kullandığı bir yapıdır.

max()İşlev
Bu max()fonksiyon, virgülle ayrılmış değerler kümesinin en büyüğünü döndürür:

<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <img src="https://cdn.freecodecamp.org/curriculum/css-photo-gallery/9.jpg" alt="A cat sitting on a table">
</body>
img {
  width: max(250px, 25vw);
}
Yukarıdaki örnekte, görüntü alanı genişliği 1000 pikselden az ise resmin genişliği 250 piksel olacaktır. Görüntü alanı genişliği 1000 pikselden büyükse, resmin genişliği 25vw olacaktır. Bunun nedeni, 25vw'nin görüntü alanı genişliğinin %25'ine eşit olmasıdır.

CSS ve Erişilebilirlik ile İlgili En İyi Uygulamalar
display: none;Bu yöntemi kullanmak, display: none;ekran okuyucuların ve diğer yardımcı teknolojilerin bu içeriğe erişemeyeceği anlamına gelir, çünkü bu içerik erişilebilirlik ağacına dahil edilmemiştir. Bu nedenle, bu yöntemi yalnızca içeriği hem görsel sunumdan hem de erişilebilirlikten tamamen kaldırmak istediğinizde kullanmanız önemlidir.
visibility: hidden;Bu özellik ve değer, içeriği görsel olarak gizler ancak belge akışında tutar, yani sayfada yer kaplamaya devam eder. Bu öğeler, erişilebilirlik ağacından kaldırıldıkları için artık ekran okuyucular tarafından okunmayacaktır.
.sr-onlyCSS sınıfı : Bu, içeriği görsel olarak gizlerken ekran okuyucular için erişilebilirliğini korumak için kullanılan yaygın bir tekniktir.
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <span>This span element can be read</span>
  <span class="sr-only">This span element can only be read by screen readers</span>
  <p style="display: none">
    This text is hidden with display: none and is NOT accessible to screen readers.
  </p>
  <p style="visibility: hidden">
    This text is hidden with visibility: hidden and is NOT read by screen readers,
    but it still takes up space.
  </p>
</body>

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

scroll-behavior: smooth;Bu özellik ve değer, sorunsuz bir kaydırma davranışı sağlar.
prefers-reduced-motionÖzellik : Bu, kullanıcının animasyon tercihini tespit etmek için kullanılabilen bir medya özelliğidir.
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Clicking these links should result in smooth scrolling 
 if the user has not set a preference for reduced motion -->
  <nav>
    <a href="#section1">Section 1</a>
    <a href="#section2">Section 2</a>
    <a href="#section3">Section 3</a>
  </nav>

  <section id="section1">
    <h2>Section 1</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ligula dui, venenatis quis ligula ac, gravida pellentesque orci. Phasellus feugiat tortor ut vehicula porttitor. Proin vehicula scelerisque purus sit amet porttitor. Suspendisse egestas congue nibh auctor auctor. Pellentesque interdum, urna eget rhoncus tincidunt, mi urna sodales ex, quis tincidunt ante purus et erat. Quisque lacinia sapien a nibh porta semper. Pellentesque vitae enim non elit euismod gravida. Etiam eu orci pulvinar, malesuada est non, molestie ex. Etiam massa ante, malesuada quis lorem ut, aliquet aliquam libero. Etiam arcu nunc, suscipit sit amet leo eu, pharetra viverra nibh.
    </p>
  </section>

  <section id="section2">
    <h2>Section 2</h2>
    <p>Mauris vel arcu enim. Nunc bibendum tincidunt dapibus. Nulla bibendum diam eget rutrum commodo. Quisque congue, erat eu tempus tincidunt, lacus ligula condimentum mi, ut luctus nisl erat at ipsum. In id mi sit amet purus laoreet commodo. Nunc facilisis sem diam, quis gravida nibh vulputate tempor. Praesent quam est, rhoncus ac volutpat non, sollicitudin quis tellus. Integer et velit sit amet ante tristique lobortis id eu nunc. Cras odio magna, malesuada nec eros sit amet, tincidunt tincidunt orci. Nam sit amet quam id urna tempus porttitor. Phasellus felis ligula, egestas non fringilla id, egestas vel erat. Ut semper est non bibendum facilisis. Ut ullamcorper tempor imperdiet.
    </p>
  </section>

  <section id="section3">
    <h2>Section 3</h2>
    <p>Praesent sed finibus lectus, vel ultricies sem. Nam nec suscipit turpis. Duis vehicula posuere magna, sed laoreet leo scelerisque id. Suspendisse iaculis vulputate nisl id porttitor. Praesent aliquam blandit ex, porta ultricies enim fermentum tristique. Morbi ac imperdiet diam, sit amet suscipit massa. Proin sed nisl a ex ultrices interdum. Nullam vitae diam eget odio iaculis tristique.
    </p>
  </section>
</body>

@media (prefers-reduced-motion: no-preference) {
  * {
    scroll-behavior: smooth;
  }
}
Yukarıdaki örnekte, kullanıcının cihazında animasyon tercihi ayarlanmamışsa, yumuşak kaydırma etkinleştirilir.

HTML Nitelikleriyle İçeriği Gizleme
aria-hiddenÖzellik : Ekran okuyucular gibi yardımcı teknolojiler kullanan kişilerden bir öğeyi gizlemek için kullanılır. Örneğin, anlamlı bir içerik sağlamayan dekoratif resimleri gizlemek için kullanılabilir.
hiddenÖzellik : Bu özellik çoğu modern tarayıcı tarafından desteklenir ve içeriği hem görsel olarak hem de erişilebilirlik ağacından gizler. JavaScript ile kolayca açılıp kapatılabilir.
<p aria-hidden>This paragraph is visible for sighted users, but is hidden from assistive technology.</p>
<p hidden>This paragraph is hidden from both sighted users and assistive technology.</p>
<p>This is a normal paragraph</p>

placeholderÖzelliğin Erişilebilirlik Sorunu
Yer tutucu metin kullanmak erişilebilirlik açısından pek iyi değil. Kullanıcılar çok sık yer tutucu metni gerçek bir giriş değeriyle karıştırıyorlar; giriş alanında zaten bir değer olduğunu düşünüyorlar.