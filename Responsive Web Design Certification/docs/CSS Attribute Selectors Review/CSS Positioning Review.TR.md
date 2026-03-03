CSS Nitelik Seçicileri İncelemesi
Farklı Nitelik Seçiciler ve Bağlantılarla Çalışmak
Tanım : Seçici, `<title>` veya ` <title> attribute` gibi özniteliklerine göre HTML öğelerini hedeflemenizi sağlar .hreftitle
<link rel="stylesheet" href="styles.css">
<a href="https://www.freecodecamp.org">Link with href</a>
<a>No href</a>
a[href] {
  color: blue;
  text-decoration: underline;
}
titleÖzellik : Bu özellik, bir öğe hakkında ek bilgi sağlar. Bağlantıları bu özellik ile nasıl hedefleyebileceğiniz aşağıda açıklanmıştır title:
<link rel="stylesheet" href="styles.css">
<a href="#" title="Tooltip">Link with title</a>
<a href="#">Normal link</a>
a[title] {
  font-weight: bold;
  text-decoration: none;
}
hrefHem " ve" hem de title"özniteliklerine" sahip bağlantıları eşleştirmek için seçicileri birleştirin : Birden fazla öznitelik seçiciyi birleştirir.
<link rel="stylesheet" href="styles.css">
<a href="#" title="Info">Href + Title</a>
<a href="#">Only href</a>
a[href][title] {
  color: green;
}
Boşlukla ayrılmış listedeki tek bir kelimeyle eşleştirme : Belirli bir sınıf kelimesine sahip bağlantıları hedefler.
<link rel="stylesheet" href="styles.css">
<a class="link primary">Primary link</a>
<a class="link secondary">Secondary link</a>
a[class~="primary"] {
  color: red;
  font-weight: bold;
}
Belirli bir önekle başlayan değerleri eşleştir : . ile başlayan bağlantıları hedefler https://.
<link rel="stylesheet" href="styles.css">
<a href="https://www.freecodecamp.org">HTTPS link</a>
<a href="http://www.freecodecamp.org">HTTP link</a>
a[href^="https://"] {
  color: green;
  text-decoration: underline;
}
Belirli bir sonekle biten değerlerle eşleş : . ile biten bağlantıları hedefler .jpg.
<link rel="stylesheet" href="styles.css">
<a href="photo.jpg">Image link</a>
<a href="index.html">HTML link</a>
a[href$=".jpg"] {
  color: darkgreen;
  text-decoration: underline dotted;
}
Değerin herhangi bir yerinde bir alt dize içeren değerleri eşleştirhttps : Değerin herhangi bir yerinde bu alt dizeyi içeren bağlantıları hedefler .
<link rel="stylesheet" href="styles.css">
<a href="https://www.freecodecamp.org">Secure link</a>
<a href="page.html">Local link</a>
a[href*="https"] {
  color: teal;
}
Özet : Bu kalıplar, bağlantıları niteliklerine ve değerlerine göre tutarlı bir şekilde biçimlendirmeyi kolaylaştırır.
lang" and" data-langözniteliğiyle öğeleri hedefleme
langÖznitelik : Bu öznitelik, HTML'de bir öğenin içeriğinin dilini belirtmek için kullanılır. Özellikle çok dilli bir web sitesinde, öğeleri yazıldıkları dile göre farklı şekilde biçimlendirmek isteyebilirsiniz.
<link rel="stylesheet" href="styles.css">
<p lang="en">English text</p>
<p lang="fr">French text</p>
p[lang="en"] {
  font-style: italic;
}
data-langÖzellik : Özellik gibi özel veri özellikleri, data-langgenellikle öğelerde ek bilgiler depolamak için kullanılır; örneğin, belirli bir metin bölümünde kullanılan dili belirtmek gibi. İşte bu özelliğe göre öğeleri nasıl biçimlendirebileceğiniz data-lang:
<link rel="stylesheet" href="styles.css">
<div data-lang="fr">French content</div>
<div data-lang="en">English content</div>
div[data-lang="fr"] {
  color: blue;
}
Öznitelik Seçici, Sıralı Liste Öğeleri ve typeÖznitelik ile Çalışmak
typeÖznitelik : HTML'de sıralı listelerle çalışırken, bu typeöznitelik sayısal, alfabetik veya Roma rakamları gibi kullanılan numaralandırma stilini belirtmenize olanak tanır.
<link rel="stylesheet" href="styles.css">
<ol type="A">
  <li>Alpha</li>
  <li>Beta</li>
</ol>

<ol type="i">
  <li>One</li>
  <li>Two</li>
</ol>
/*Example targeting uppercase alphabetical numbering*/
ol[type="A"] {
  color: purple;
  font-weight: bold;
}

/*Example targeting lowercase Roman numerals*/
ol[type="i"] {
  color: green;
}