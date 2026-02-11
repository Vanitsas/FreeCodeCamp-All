Semantik HTML İncelemesi
Semantik HTML'nin Önemi
Başlık öğeleri için yapısal hiyerarşi : İçeriğin yapısal hiyerarşisini korumak için doğru başlık öğesini kullanmak önemlidir. öğesi h1en üst düzey başlığı, h6öğesi ise en alt düzey başlığı temsil eder.
Sunumsal HTML öğeleri : İçeriğin görünümünü tanımlayan öğeler. Örnek: Kullanımdan kaldırılmış olan `<style>` center, `<style>` bigve font`<style>` öğeleri.
Anlamsal HTML öğeleri : Anlam ve yapı taşıyan öğeler. Örnek: header, nav, figure.
Anlamsal HTML Öğeleri
Başlık öğesi : Bir belgenin veya bölümün başlığını tanımlamak için kullanılır.

<header>
  <h1>CatPhotoApp</h1>
  <p>Welcome to our cat gallery.</p>
</header>
Ana öğe : Web sayfasının ana içeriğini içermek için kullanılır.

<main>
  <section>
    <h2>Cat Photos</h2>
    <p>Browse adorable cat pictures.</p>
  </section>
</main>
Bölüm öğesi : İçeriği daha küçük bölümlere ayırmak için kullanılır.

<section>
  <h2>About Me</h2>
  <p>Hi, I am Jane Doe and I am a web developer.</p>
</section>
Gezinti Bölümü ( nav) öğesi : gezinme bağlantıları içeren bir bölümü temsil eder.

<nav>
  <ul>
    <li><a href="#photos">Photos</a></li>
    <li><a href="#videos">Videos</a></li>
  </ul>
</nav>
Şekil öğesi : Çizimler ve diyagramlar içermek için kullanılır.

<figure>
  <img
    src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"
    alt="Two tabby kittens sleeping together on a couch."
  />
  <figcaption>Cats <strong>hate</strong> other cats.</figcaption>
</figure>
Vurgu ( em) öğesi : vurgulu metni işaretler.

<p>
  Never give up on <em>your</em> dreams.
</p>
Deyimsel Metin ( i) öğesi : alternatif ses veya ruh halini, başka bir dilden deyimsel terimleri, teknik terimleri ve düşünceleri vurgulamak için kullanılır.

<p>
  There is a certain <i lang="fr">je ne sais quoi</i> in the air.
</p>
lang`<a>` etiketinin içindeki özellik , iiçeriğin dilini belirtmek için kullanılır. Bu durumda dil Fransızca olacaktır. Bu iöğe, metnin önemli olup olmadığını göstermez, yalnızca çevredeki metinden bir şekilde farklı olduğunu gösterir.

Güçlü Önem ( strong) öğesi : güçlü öneme sahip metni işaretler.

<p>
  <strong>Warning:</strong> This product may cause allergic reactions.
</p>
Dikkat Çekmek İçin ( b) Öğesi : İçeriğin anlamı için önemli olmayan metne dikkat çekmek için kullanılır. Genellikle özetlerde anahtar kelimeleri veya yorumlarda ürün adlarını vurgulamak için kullanılır.

<p>
  We tested several products, including the <b>SuperSound 3000</b> for audio quality, the <b>QuickCharge Pro</b> for fast charging, and the <b>Ecoclean Vacuum</b> for cleaning. The first two performed well, but the <b>Ecoclean Vacuum</b> did not meet expectations.
</p>
Açıklama Listesi ( dl) öğesi : terim-açıklama gruplarının listesini temsil etmek için kullanılır.

Tanım Terimi ( dt) öğesi : Tanımlanan terimi temsil etmek için kullanılır.

Açıklama Ayrıntıları ( dd) öğesi : terimin açıklamasını temsil etmek için kullanılır.

<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
</dl>
Blok Alıntı ( blockquote) öğesi : Başka bir kaynaktan alıntı yapılan bir bölümü temsil etmek için kullanılır. Bu öğenin bir citeözniteliği vardır. Özniteliğin değeri, citekaynağın URL'sidir.

<blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
  "Can you imagine what it would be like to be a successful developer? To have built software systems that people rely upon?"
</blockquote>
Alıntı ( cite) öğesi : Referans verilen eserin kaynağını görsel olarak belirtmek için kullanılır. Referansın başlığını vurgular.

<div>
  <blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
    "Can you imagine what it would be like to be a successful developer? To have built software systems that people rely upon?"
  </blockquote>
  <p>
    -Quincy Larson, <cite>How to learn to Code and Get a Developer Job [Full Book].</cite>
  </p>
</div>
Satır İçi Alıntı ( q) öğesi : kısa bir satır içi alıntıyı temsil etmek için kullanılır.

<p>
  As Quincy Larson said,
  <q cite="https://www.freecodecamp.org/news/learn-to-code-book/">
    Momentum is everything.
  </q>
</p>
Kısaltma ( abbr) öğesi : bir kısaltmayı veya akronimi temsil etmek için kullanılır. Kullanıcıların kısaltmanın veya akronimin ne olduğunu anlamalarına yardımcı olmak için, özniteliğiyle tam halini, insan tarafından okunabilir bir açıklamasını gösterebilirsiniz title.

<p>
  <abbr title="HyperText Markup Language">HTML</abbr> is the foundation of the web.
</p>
İletişim Adresi ( address) öğesi : iletişim bilgilerini temsil etmek için kullanılır.

(Tarih) Saat ( time) öğesi : tarih ve/veya saati temsil etmek için kullanılır. Bu datetimeöznitelik, tarih ve saatleri makine tarafından okunabilir bir biçime çevirmek için kullanılır.

<p>
  The reservations are for the <time datetime="20:00">20:00 </time>
</p>
ISO 8601 Tarih ( datetime) özniteliği : Tarih ve saatleri makine tarafından okunabilir bir biçimde temsil etmek için kullanılır. Standart biçim YYYY-MM-DDThh:mm:ss, büyük harf Ttarih ve saat arasında ayırıcı görevi görür.

Üst simge ( sup) öğesi : Üst simge metni temsil etmek için kullanılır. Bu supöğenin yaygın kullanım alanları arasında üsler, üst yazı ve sıra sayıları bulunur.

<p>
  2<sup>2</sup> (2 squared) is 4.
</p>
Alt simge ( sub) öğesi : Alt simge metnini temsil etmek için kullanılır. Alt simge öğesinin yaygın kullanım alanları arasında kimyasal formüller, dipnotlar ve değişken alt simgeler bulunur.

<p>
  CO<sub>2</sub>
</p>
Satır İçi Kod ( code) öğesi : bilgisayar kodunun bir parçasını temsil etmek için kullanılır.

Önceden Biçimlendirilmiş Metin ( pre) öğesi : önceden biçimlendirilmiş metni temsil eder.

<pre>
  <code>
    body {
      color: red;
    }
  </code>
</pre>
Eklemlenmemiş Açıklama ( u) öğesi : Metin dışı bir açıklamaya sahip olduğunu gösteren bir şekilde işlenmesi gereken satır içi metin bölümünü temsil etmek için kullanılır.

<p>
  You can use the unarticulated annotation element to highlight
  <u>inccccort</u> <u>spling</u> <u>issses</u>.
</p>
Ruby Annotation ( ruby) elementi : Metne telaffuz veya anlam açıklamaları eklemek için kullanılır. Örnek bir kullanım alanı Doğu Asya tipografisidir.

Ruby yedek parantez ( rp) öğesi : Ruby ek açıklamalarını görüntüleme desteği olmayan tarayıcılar için yedek olarak kullanılır.

Ruby metin ( rt) öğesi : Ruby ek açıklaması için metni belirtmek amacıyla kullanılır. Genellikle Doğu Asya tipografisinde telaffuz veya çeviri ayrıntıları için kullanılır.

<ruby>
  明日 <rp>(</rp><rt>Ashita</rt><rp>)</rp>
</ruby>
Üstü çizili ( s) öğe : Artık doğru veya geçerli olmayan içeriği temsil etmek için kullanılır.

<p>
  <s>Tomorrow's hike will be meeting at noon.</s>
</p>
<p>
  Due to unforeseen weather conditions, the hike has been canceled.
</p>
Dahili bağlantılarhref="#id" : Bir aöğeye `<script>` etiketi ekleyerek ve hedef öğeye aynı etiketi vererek sayfanın başka bir bölümüne bağlantı vermek için kullanılır id. Bu genellikle atlama bağlantıları, içindekiler tablosu veya birden fazla bölümden oluşan uzun sayfalar için kullanılır.

<a href="#about-section">Go to About Section</a>

<section id="about-section">
  <h2>About</h2>
  <p>This is the about section of the page.</p>
</section>