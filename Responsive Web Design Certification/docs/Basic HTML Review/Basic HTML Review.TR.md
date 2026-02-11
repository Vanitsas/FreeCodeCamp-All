HTML Temelleri
HTML'nin Rolü : HTML, web sayfasının içeriğini ve yapısını temsil eder.
HTML Öğeleri : Öğeler, bir HTML belgesinin yapı taşlarıdır. Başlıkları, paragrafları, bağlantıları, resimleri ve daha fazlasını temsil ederler. Çoğu HTML öğesi bir açılış etiketi (<h1> <elementName>) ve bir kapanış etiketi (<h2> </elementName>) içerir.
İşte temel sözdizimi:

Örnek Kod
<elementName>Content goes here</elementName>
Boş Öğeler : Boş öğeler herhangi bir içeriğe sahip olamaz ve yalnızca bir başlangıç ​​etiketi içerir. Örnekler arasında imgve metaöğeleri bulunur.
Örnek Kod
<img>
<meta>
/Bazı kod tabanlarında `void` elementi içinde eğik çizgi (/) görmek yaygındır . Her iki kullanım da kabul edilebilir:

Örnek Kod
<img>
<img/>
Özellikler : Bir özellik, bir HTML öğesinin açılış etiketine yerleştirilen bir değerdir. Özellikler, öğe hakkında ek bilgi sağlar veya öğenin nasıl davranması gerektiğini belirtir. İşte bir özellik için temel sözdizimi:
Örnek Kod
<element attribute="value"></element>
Mantıksal (boolean) öznitelik, bir HTML etiketinde ya var olabilen ya da olmayabilen bir özniteliktir. Var ise değeri true, aksi takdirde false'tur. Mantıksal özniteliklere örnek olarak `<p>` disabled, readonly`<input>` ve ` <input>` verilebilir required.

Yorumlar : Yorumlar, programlamada kodunuzda kendiniz ve diğer geliştiriciler için notlar bırakmak amacıyla kullanılır. İşte HTML'de bir yorumun sözdizimi:
Örnek Kod
<!--This is an HTML comment.-->
Yaygın HTML öğeleri
Başlık Öğeleri : HTML'de altı başlık öğesi bulunur. h1Başlık h6öğeleri, altlarındaki içeriğin önemini belirtmek için kullanılır. Sayı ne kadar düşükse, önem o kadar yüksektir; bu nedenle, h2öğelerin önemi öğelerin öneminden daha azdır h1.
Örnek Kod
<h1>most important heading element</h1>
<h2>second most important heading element</h2>
<h3>third most important heading element</h3>
<h4>fourth most important heading element</h4>
<h5>fifth most important heading element</h5>
<h6>least important heading element</h6>
Paragraf Öğeleri : Bu, bir web sayfasındaki paragraflar için kullanılır.
Örnek Kod
<p>This is a paragraph element.</p>
imgÖğeler : Öğeler, imgweb sayfasına resim eklemek için kullanılır. `<img>` özniteliği, srcresmin konumunu belirtmek için kullanılır. Resim öğeleri için, `<img>` özniteliği adı verilen başka bir öznitelik eklemek iyi bir uygulamadır . İşte `<img>` ve `<img> ` özniteliklerine sahip altbir öğe örneği :imgsrcalt
Örnek Kod
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg" alt="A slice of lasagna on a plate.">
bodyElement : Bu element, HTML belgesinin içeriğini temsil etmek için kullanılır.
Örnek Kod
<body>
  <h1>CatPhotoApp</h1>
  <p>This is a paragraph element.</p>
</body>    
sectionÖğeler : Bu öğe, içeriği daha küçük bölümlere ayırmak için kullanılır.
Örnek Kod
<section>
  <h2>About Me</h2>
  <p>Hi, I am Jane Doe and I am a web developer.</p>
</section>
divÖğeler : Bu öğe, herhangi bir anlamsal anlam taşımayan genel bir HTML öğesidir. Diğer HTML öğelerini barındırmak için genel bir kapsayıcı olarak kullanılır.
Örnek Kod
<div>
  <h1>I am a heading</h1>
  <p>I am a paragraph</p>
</div>
Çapa ( a) Öğeleri : Bu öğeler, bir web sayfasına bağlantı eklemek için kullanılır. `<link>` özniteliği, hrefkullanıcının bağlantıya tıkladığında bağlantının nereye yönlendirilmesi gerektiğini belirtmek için kullanılır.
Örnek Kod
<a href="https://cdn.freecodecamp.org/curriculum/cat-photo-app/running-cats.jpg">cute cats</a>
Sırasız ( ul) ve Sıralı ( ol) Liste Öğeleriul : Madde işaretli bir liste oluşturmak için, içine bir veya daha fazla liöğe yerleştirilmiş şu şekilde bir öğe kullanmalısınız :
Örnek Kod
<ul>
  <li>catnip</li>
  <li>laser pointers</li>
  <li>lasagna</li>
</ul>
Öğelerin sıralı bir listesini oluşturmak için şu öğeyi kullanmalısınız ol:

Örnek Kod
<ol>
  <li>flea treatment</li>
  <li>thunder</li>
  <li>other cats</li>
</ol>
Vurgu ( em) Öğesi : Bu, bir metin parçasını vurgulamak için kullanılır.
Örnek Kod
<p>Cats <em>love</em> lasagna.</p>  
Güçlü Önem ( strong) Öğesi : Bu öğe, metne aciliyet ve ciddiyet duygusu vermek için güçlü bir vurgu yapmak amacıyla kullanılır.
Örnek Kod
<p>
  <strong>Important:</strong> Before proceeding, make sure to wear your safety goggles. 
</p>
figureve figcaptionÖğeler : figureöğesi, resimler ve diyagramlar gibi içerikleri gruplandırmak için kullanılır. figcaptionöğesi, bu öğe içindeki içeriğe bir başlık eklemek için kullanılır figure.
Örnek Kod
<figure>
  <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Two tabby kittens sleeping together on a couch.">
  <figcaption>Cats <strong>hate</strong> other cats.</figcaption>  
</figure>
mainElement : Bu element, bir web sayfasının ana içeriğini temsil etmek için kullanılır.
footer<title> öğesi : Bu öğe HTML belgesinin en altına yerleştirilir ve genellikle telif hakkı bilgilerini ve diğer önemli sayfa bağlantılarını içerir.
Örnek Kod
<footer>
  <p>
    No Copyright - <a href="https://www.freecodecamp.org">freeCodeCamp.org</a>
  </p>
</footer>
Tanımlayıcılar ve Gruplandırma
Kimlikler (ID'ler) : HTML öğeleri için benzersiz öğe tanımlayıcıları. Kimlik adları, bir HTML belgesinde yalnızca bir kez kullanılmalıdır.
Örnek Kod
<h1 id="title">Movie Review Page</h1>
Kimlik adlarında boşluk bulunamaz. Kimlik adınız birden fazla kelime içeriyorsa, kelimeler arasına tire koyabilirsiniz, örneğin:

Örnek Kod
<div id="red-box"></div>
Sınıflar : Sınıflar, öğeleri stil ve davranış açısından gruplandırmak için kullanılır.
Örnek Kod
<div class="box"></div>
Kimlik numaralarının aksine, aynı sınıf adını HTML belgesi boyunca tekrar kullanabilirsiniz. classDeğerde şu şekilde boşluklar da bulunabilir:

Örnek Kod
<div class="box red-box"></div>
<div class="box blue-box"></div>
Özel Karakterler ve Bağlantılar
HTML varlıkları : Bir HTML varlığı veya karakter referansı, HTML'de ayrılmış bir karakteri temsil etmek için kullanılan bir karakter kümesidir. Örnekler arasında ampersand (& &amp;) sembolü ve küçüktür (< &lt;) sembolü bulunur.
Örnek Kod
<p>This is an &lt;img /&gt; element</p>
linkElementlink : Bu element, stil sayfaları ve site simgeleri gibi harici kaynaklara bağlantı vermek için kullanılır. Harici bir CSS dosyası için elementi kullanmanın temel sözdizimi şöyledir :
Örnek Kod
<link rel="stylesheet" href="./styles.css" />
Bu relözellik, bağlantılı kaynak ile HTML belgesi arasındaki ilişkiyi belirtmek için kullanılır. Bu hrefözellik, harici kaynağın URL'sinin konumunu belirtmek için kullanılır.

scriptElement : Bu element, çalıştırılabilir kodu yerleştirmek için kullanılır.
Örnek Kod
<body>
  <script>
    alert("Welcome to freeCodeCamp");
  </script>
</body>
Teknik olarak tüm JavaScript kodunuzu `<script>` etiketlerinin içine yazabilirsiniz script, ancak bunun yerine harici bir JavaScript dosyasına bağlantı vermek en iyi uygulama olarak kabul edilir. İşte scriptharici bir JavaScript dosyasına bağlantı vermek için `<script>` öğesinin kullanımına bir örnek:

Örnek Kod
<script src="path-to-javascript-file.js"></script>
Bu srcözellik, harici JavaScript dosyasının konumunu belirtmek için kullanılır.

Şablon ve Kodlama
HTML şablonu : Bu, her HTML belgesinin ihtiyaç duyduğu temel yapıyı ve önemli öğeleri içeren bir şablondur.
Örnek Kod
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>freeCodeCamp</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <!--Headings, paragraphs, images, etc. go inside here-->
  </body>
</html>
DOCTYPEBu, tarayıcılara hangi HTML sürümünü kullandığınızı bildirmek için kullanılır.
htmlElement : Bu, bir HTML belgesinin en üst düzey öğesini veya kökünü temsil eder. Belge için dil belirtmek için `<div>` özniteliğini kullanmalısınız lang.
headElement : Bu headbölüm, tarayıcılar ve arama motorları için gerekli olan arka plandaki önemli meta verileri içerir.
metaÖğeler : Bu öğeler sitenizin meta verilerini temsil eder. Bu öğeler, karakter kodlaması ve Twitter gibi web sitelerinin sayfanızın bağlantısını nasıl önizlemesi gerektiği gibi detaylar içerir.
titleElement : Bu element, tarayıcı sekmesinde veya penceresinde görünen metni ayarlamak için kullanılır.
UTF-8 karakter kodlaması : UTF-8 veya UCS Dönüştürme Biçimi 8, web'de yaygın olarak kullanılan standartlaştırılmış bir karakter kodlamasıdır. Karakter kodlaması, bilgisayarların karakterleri veri olarak depolamak için kullandığı yöntemdir. Bu öznitelik , karakter kodlamasını UTF-8 olarak ayarlamak için charsetbir `<script>` öğesinin içinde kullanılır .meta
SEO ve Sosyal Paylaşım
SEO : Arama Motoru Optimizasyonu, web sayfalarının arama motorlarında daha görünür hale gelmesi ve daha üst sıralarda yer alması için optimize edilmesi uygulamasıdır.
Meta ( description) Öğesi : Bu, web sayfası için kısa bir açıklama sağlamak ve SEO'yu etkilemek için kullanılır.
Örnek Kod
<meta
  name="description"
  content="Discover expert tips and techniques for gardening in small spaces, choosing the right plants, and maintaining a thriving garden."
/>
Open Graph etiketleri : Open Graph protokolü, web sitenizin içeriğinin Facebook, LinkedIn ve daha birçok sosyal medya platformunda nasıl görüneceğini kontrol etmenizi sağlar.
metaBu OpenGraph özelliklerini ayarlayarak, kullanıcıları içeriğinize tıklamaya ve etkileşime geçmeye teşvik edebilirsiniz. Bu özellikleri HTML bölümünüzdeki bir dizi öğe aracılığıyla ayarlayabilirsiniz head.

og:titleÖzellik : Bu özellik, sosyal medya gönderilerinde görüntülenecek başlığı ayarlamak için kullanılır.
Örnek Kod
<meta content="freeCodeCamp.org" property="og:title" />
og:typeÖzellik : Bu typeözellik, sosyal medyada paylaşılan içerik türünü temsil etmek için kullanılır. Bu içeriğe örnek olarak makaleler, web siteleri, videolar veya müzik verilebilir.
Örnek Kod
<meta property="og:type" content="website" />
og:imageÖzellik : Bu özellik, sosyal medya paylaşımlarında gösterilecek resmi ayarlamak için kullanılır.
Örnek Kod
<meta
  content="https://cdn.freecodecamp.org/platform/universal/fcc_meta_1920X1080-indigo.png"
  property="og:image"
/>
og:urlÖzellik : Bu özellik, kullanıcıların sosyal medya gönderilerine tıklamak için kullanacakları URL'yi ayarlamak için kullanılır.
Örnek Kod
<meta property="og:url" content="https://www.freecodecamp.org" />
Medya Öğeleri ve Optimizasyon
Değiştirilen öğeler : Değiştirilen öğe, içeriği CSS'nin kendisi yerine harici bir kaynak tarafından belirlenen bir öğedir. Örnek olarak bir `<p>` iframeöğesi verilebilir. iframe`<p>` ise satır içi çerçeve anlamına gelir. Diğer HTML içeriğini doğrudan HTML sayfasına yerleştirmek için kullanılan bir satır içi öğedir.
Örnek Kod
<iframe src="https://www.example.com" title="Example Site"></iframe>
allowfullscreenKullanıcının iframe'i tam ekran modunda görüntülemesine olanak tanıyan özelliği ekleyebilirsiniz .

Örnek Kod
<iframe
  src="video-url"
  width="width-value"
  height="height-value"
  allowfullscreen
></iframe>
Bir videoyu bir etiketinize yerleştirmek için iframe, YouTube ve Vimeo gibi popüler video servislerinden doğrudan kopyalayabilir veya srcvideo URL'sine işaret eden özniteliği kullanarak kendiniz tanımlayabilirsiniz. İşte YouTube'dan popüler bir freeCodeCamp kursunu yerleştirmenin bir örneği:

Örnek Kod
<h1>A freeCodeCamp YouTube Video Embedded with the iframe Element</h1>

<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/PkZNo7MFNFg?si=-UBVIUNM3csdeiWF"
  title="YouTube video player"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
video, ve gibi başka değiştirilmiş öğeler de vardır embed. Ve bazı öğeler belirli koşullar altında değiştirilmiş öğeler gibi davranır. İşte özniteliği inputolarak ayarlanmış bir öğeye örnek :typeimage

Örnek Kod
<input type="image" alt="Descriptive text goes here" src="example-img-url">
Medya optimizasyonu : Web sayfalarınızda resimler gibi medya öğeleri kullanırken dikkate almanız gereken üç araç vardır: boyut, biçim ve sıkıştırma. Sıkıştırma algoritması, dosyaların veya verilerin boyutunu küçültmek için kullanılır.
Görüntü formatları : En yaygın dosya formatlarından ikisi PNG ve JPG'dir, ancak bunlar artık görüntü sunmak için en ideal formatlar değildir. Eski tarayıcılar için desteğe ihtiyacınız yoksa, WEBP veya AVIF gibi daha optimize edilmiş bir format kullanmayı düşünmelisiniz.
Görsel Lisansları : Kamu malı statüsündeki bir görselin telif hakkı yoktur ve herhangi bir kısıtlama olmaksızın kullanılabilir. Özellikle Creative Commons 0 lisansı altında lisanslanan görseller kamu malı olarak kabul edilir. Bazı görseller, Creative Commons lisansı veya freeCodeCamp'in kullandığı BSD lisansı gibi izin verici bir lisans altında yayınlanabilir.
SVG'ler : Ölçeklenebilir Vektör Grafikleri, noktaları, çizgileri ve eğrileri çizmek için yollara ve denklemlere dayalı verileri izler. Bunun gerçek anlamı, bir SVG gibi bir vektör grafiğinin kalitesini etkilemeden herhangi bir boyuta ölçeklendirilebileceğidir.
Multimedya Entegrasyonu
audio`<audio> ` ve ` video<video>` öğeleri : `<audio> audio` ve `<video>` videoöğeleri, HTML belgelerinize ses ve video içeriği eklemenizi sağlar. ` audio<audio>` öğesi mp3, wav ve ogg gibi popüler ses formatlarını destekler. ` video<audio>` öğesi ise mp4, ogg ve webm formatlarını destekler.
Örnek Kod
<audio src="CrystalizeThatInnerChild.mp3"></audio>
Sayfada ses oynatıcısını görmek istiyorsanız, şu özniteliğe audiosahip öğeyi ekleyebilirsiniz controls:

Örnek Kod
<audio src="CrystalizeThatInnerChild.mp3" controls></audio>
Bu controlsözellik, kullanıcıların ses oynatımını yönetmelerini sağlar; buna ses seviyesini ayarlama, oynatımı duraklatma veya devam ettirme dahildir. Bu controlsözellik, yerleşik oynatım kontrollerini etkinleştirmek için bir öğeye eklenebilen bir boolean özelliğidir. Atlanırsa, hiçbir kontrol gösterilmez.

loopÖzellik : Bu loopözellik, sesin sürekli olarak tekrar oynatılmasını sağlayan bir boolean özelliğidir.
Örnek Kod
<audio
  src="https://cdn.freecodecamp.org/curriculum/js-music-player/can't-stay-down.mp3"
  loop
  controls
></audio>
mutedÖzellik : Öğede bulunduğunda audio, mutedboolean özellik sesi sessiz modda başlatır.
Örnek Kod
<audio
  src="https://cdn.freecodecamp.org/curriculum/js-music-player/can't-stay-down.mp3"
  loop
  controls
  muted
></audio>
sourceÖğesource : Ses dosyası türleri söz konusu olduğunda, hangi tarayıcıların hangi türü desteklediği konusunda farklılıklar vardır. Bunu gidermek için, öğesinin içine öğeleri kullanabilirsiniz audiove tarayıcı anladığı ilk kaynağı seçecektir. İşte bir öğesi sourceiçin birden fazla öğe kullanmanın bir örneği:audio
Örnek Kod
<audio controls>
  <source src="audio.ogg" type="audio/ogg" />
  <source src="audio.wav" type="audio/wav" />
  <source src="audio.mp3" type="audio/mpeg" />
</audio>
Şimdiye kadar öğrendiğimiz tüm özellikler, öğesinde de desteklenmektedir video. İşte , , ve özelliklerine videosahip bir öğesinin kullanımına bir örnek :loopcontrolsmuted

Örnek Kod
<video
  src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
  loop
  controls
  muted
></video>
posterÖzellik : Video indirilirken bir resim görüntülemek istiyorsanız, bu posterözelliği kullanabilirsiniz. Bu özellik, öğeler için kullanılamaz audiove yalnızca öğeye özgüdür video.
Örnek Kod
<video
  src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
  loop
  controls
  muted
  poster="https://peach.blender.org/wp-content/uploads/title_anouncement.jpg?x11217"
  width="620"
></video>
Hedef özellik türleri
targetÖznitelik : Bu öznitelik, tarayıcıya bağlantı öğesinin URL'sini nerede açacağını söyler. Bu öznitelik için dört önemli olası değer vardır: _self, _blank, _parentve . Şu anda deneysel API için kullanılan _topbeşinci bir değer de vardır . Muhtemelen henüz bunu kullanmanız için bir nedeniniz olmayacaktır._unfencedTopFencedFrame
_selfDeğer : Bu, öznitelik için varsayılan değerdir target. Bu, bağlantıyı geçerli tarama bağlamında açar. Çoğu durumda, bu geçerli sekme veya pencere olacaktır.
Örnek Kod
<a href="https://freecodecamp.org" target="_self">Visit freeCodeCamp</a>
_blankDeğer : Bu, bağlantıyı yeni bir tarama bağlamında açar. Genellikle yeni bir sekmede açılır. Ancak bazı kullanıcılar tarayıcılarını bunun yerine yeni bir pencere açacak şekilde yapılandırabilir.
Örnek Kod
<a href="https://freecodecamp.org" target="_blank">Visit freeCodeCamp</a>
_parentDeğer : Bu, bağlantıyı geçerli bağlamın üst öğesinde açar. Örneğin, web sitenizde bir iframe varsa, _parentbu iframe'deki bir değer, gömülü çerçevede değil, web sitenizin sekmesinde/penceresinde açılır.
Örnek Kod
<a href="https://freecodecamp.org" target="_parent">Visit freeCodeCamp</a>
_topDeğer : Bu, bağlantıyı en üstteki tarama bağlamında açar - "ebeveynin ebeveyni" gibi düşünün. Bu, etiketine benzer _parent, ancak bağlantı, iç içe yerleştirilmiş çerçeveler için bile her zaman tam tarayıcı sekmesinde/penceresinde açılır.
Örnek Kod
<a href="https://freecodecamp.org" target="_top">Visit freeCodeCamp</a>
Mutlak ve Göreceli Yollar
Yol tanımı : Yol, bir dosya sisteminde bir dosyanın veya dizinin konumunu belirten bir dizedir. Web geliştirmede, yollar geliştiricilerin resimler, stil sayfaları, komut dosyaları ve diğer web sayfaları gibi kaynaklara bağlantı vermesini sağlar.
Yol Sözdizimi : Bilmeniz gereken üç temel sözdizimi vardır. Birincisi, işletim sisteminize bağlı olarak ters eğik çizgi ( \) veya düz eğik çizgi ( ) olabilen eğik çizgidir. İkincisi tek noktadır ( ). Ve son olarak, çift nokta ( ) vardır . Eğik çizgi "yol ayırıcı" olarak bilinir. Klasör veya dosya adları arasında metinde bir ayrım belirtmek için kullanılır. Tek nokta geçerli dizini, iki nokta ise üst dizini gösterir./...
Örnek Kod
public/index.html
./favicon.ico
../src/index.css
Mutlak Yol : Mutlak yol, bir kaynağa giden eksiksiz bir bağlantıdır. Kök dizinden başlar, diğer tüm dizinleri içerir ve son olarak dosya adını ve uzantısını kapsar. "Kök dizin", hiyerarşideki en üst düzey dizini veya klasörü ifade eder. Mutlak yol ayrıca protokolü (örneğin, , ve olabilir) ve kaynak web üzerindeyse alan adını da içerir http. httpsİşte filefreeCodeCamp logosuna bağlantı veren bir mutlak yol örneği:
Örnek Kod
<a href="https://design-style-guide.freecodecamp.org/img/fcc_secondary_small.svg">
  View fCC Logo
</a>
Göreceli Yol : Göreceli yol, bir dosyanın konumunu geçerli dosyanın bulunduğu dizine göre belirtir. Protokol veya alan adını içermez, bu da onu aynı web sitesi içindeki dahili bağlantılar için daha kısa ve daha esnek hale getirir. İşte aynı klasörde bulunan iki sayfadan about.htmldiğerine bağlantı verme örneği:contact.html
Örnek Kod
<p>
  Read more on the
  <a href="about.html">About Page</a>
</p>
Bağlantı durumları
:linkBu varsayılan durumdur. Bu durum, kullanıcının henüz ziyaret etmediği, tıklamadığı veya etkileşimde bulunmadığı bir bağlantıyı temsil eder. Bu durumu, sayfanızdaki tüm bağlantılar için temel stilleri sağlayan bir durum olarak düşünebilirsiniz. Diğer durumlar bunun üzerine inşa edilir.
:visitedBu, kullanıcının bağlantı verilen sayfayı daha önce ziyaret etmesi durumunda geçerlidir. Varsayılan olarak, bu bağlantıyı mor renge dönüştürür; ancak kullanıcıya farklı bir görsel gösterim sağlamak için CSS'den yararlanabilirsiniz.
:hoverBu durum, kullanıcı imlecini bir bağlantının üzerine getirdiğinde geçerlidir. Bu durum, bağlantıya ekstra dikkat çekmek ve kullanıcının gerçekten tıklamak isteyip istemediğinden emin olmak için faydalıdır.
:focusBu durum, bir bağlantıya odaklandığımızda geçerlidir.
:activeBu durum, kullanıcı tarafından etkinleştirilen bağlantılar için geçerlidir. Bu genellikle, çoğunlukla sol tıklama yoluyla birincil fare düğmesiyle bağlantıya tıklamak anlamına gelir.
Atama

Temel HTML konularını ve kavramlarını gözden geçirin.

