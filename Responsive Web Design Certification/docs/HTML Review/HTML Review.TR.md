HTML İncelemesi
Yaklaşan hazırlık sınavına hazırlanmak için aşağıdaki kavramları gözden geçirin.

HTML Temelleri
HTML'in Rolü : HTML (Hypertext Markup Language), web yapısının temelidir ve bir web sayfasının öğelerini tanımlar.
HTML Öğeleri : Sayfadaki içeriği temsil etmek için kullanılırlar. Çoğu, bir açılış ve bir kapanış etiketinden oluşur (örneğin, `<p>`, <h1></h1>`<h1> <p></p>`).
HTML Yapısı : HTML, meta verilerin, stillerin ve içeriğin yapılandırıldığı bir head<style> ve <style> etiketinden oluşur.body
Yaygın HTML Öğeleri : Başlıklar ( <h1>- <h6>), paragraflar ( <p>) ve div kapsayıcıları ( <div>).
div`<element>` : ` div<element>`, herhangi bir anlamsal anlam taşımayan genel bir HTML öğesidir. Diğer HTML öğelerini barındırmak için genel bir kapsayıcı olarak kullanılır.
Boşluk Öğeleri<img> : Kapanış etiketi (örneğin, ) içermezler .
Özellikler : Öğelere meta veri ve davranış ekleme.
Tanımlayıcılar ve Gruplandırma
Kimlikler (ID'ler) : Benzersiz öğe tanımlayıcıları.
Sınıflar : Stil ve davranış için öğeleri gruplandırma.
Özel Karakterler ve Bağlantılar
HTML varlıkları&amp; : ve gibi özel karakterler kullanılarak &lt;.
linkelement : Harici stil sayfalarına bağlantı.
scriptelement : Harici JavaScript dosyalarının yerleştirilmesi.
Şablon ve Kodlama
HTML şablonuDOCTYPE : `<head>` , `<head> html`, head`<head>` ve `<head>` öğelerini içeren bir web sayfasının temel yapısıdır body. Bir HTML belgesi için başlangıç ​​noktası olarak kullanılmalıdır.
UTF-8 karakter kodlaması : Evrensel karakter görüntülemeyi sağlar.
SEO ve Sosyal Paylaşım
Meta etiketleri ( description) : Web sayfası için kısa bir açıklama sağlar ve SEO'yu etkiler.
Open Graph etiketleri : Sosyal medya paylaşımını geliştirme.
Medya Öğeleri ve Optimizasyon
Değiştirilen öğeler : Gömülü içerik (örneğin, resimler, iframe'ler).
Medya optimizasyonu : Medya performansını iyileştirmeye yönelik teknikler.
Görüntü formatları ve lisansları : Kullanım haklarını ve türlerini anlamak.
SVG'ler : Keskin görseller için ölçeklenebilir vektör grafikler.
Multimedya Entegrasyonu
HTML ses ve video öğeleri : Multimedya öğelerinin yerleştirilmesi.
Gömme işlemi<iframe> : Harici video içeriğinin entegrasyonu.
Yollar ve Bağlantı Davranışı
Hedef özellik türleri : Bağlantı davranışını kontrol etme.
Mutlak yollar ve göreceli yollar : Dizinlerde gezinme.
Yol sözdizimi : Dosya navigasyonu için /, ./, işaretlerinin anlaşılması.../
Bağlantı durumları : Farklı bağlantı etkileşimlerini yönetme (fareyle üzerine gelme, aktif olma).
İç bağlantılarhref="#id" : Bir aöğe üzerinde `<title>` etiketi kullanarak ve hedef öğeye aynı `<title>` etiketini vererek sayfanın başka bir bölümüne bağlantı verme id.
Semantik HTML'nin Önemi
Başlık öğeleri için yapısal hiyerarşi : İçeriğin yapısal hiyerarşisini korumak için doğru başlık öğesini kullanmak önemlidir. öğesi h1en üst düzey başlığı, h6öğesi ise en alt düzey başlığı temsil eder.
Sunumsal HTML öğeleri : İçeriğin görünümünü tanımlayan öğeler, örneğin, kullanımdan kaldırılmış olan `<img>`, `<img>` centerve big` font<img>` öğeleri.
Anlamsal HTML öğeleri : Bu öğeler, içeriğin yapısına anlam kazandırır. Örnekler şunlardır:
<header>Giriş niteliğindeki içeriği temsil eder.
<nav>: Gezinme bağlantıları içerir.
<article>: Kendi başına bağımsız içeriği temsil eder.
<aside>Yan çubuklar veya ilgili içerikler için kullanılır.
<section>Belge içindeki ilgili içerikleri gruplandırır.
<footer>Bir bölüm veya belge için altbilgiyi tanımlar.
Anlamsal HTML Öğeleri
Vurgu ( em) öğesi : Vurgulu metni işaretler.
Deyimsel Metin ( i) öğesi : Alternatif ses veya ruh halini, başka bir dilden deyimsel terimleri, teknik terimleri ve düşünceleri vurgulamak için kullanılır.
Güçlü Önem ( strong) öğesi : Güçlü öneme sahip metni işaretler.
Dikkat Çekmek İçin Kullanılan bÖğe ( ) : İçeriğin anlamı için önemli olmayan metne dikkat çekmek için kullanılır.
Açıklama Listesi ( dl) öğesi : Terim-açıklama gruplarının listesini temsil etmek için kullanılır.
Açıklama Terimi ( dt) öğesi : Tanımlanan terimi temsil etmek için kullanılır.
Açıklama Ayrıntıları ( dd) öğesi : Terimin açıklamasını temsil etmek için kullanılır.
Blok Alıntı ( blockquote) öğesi : Başka bir kaynaktan alıntı yapılan bir bölümü temsil etmek için kullanılır.
Satır İçi Alıntı ( q) öğesi : Kısa bir satır içi alıntıyı temsil etmek için kullanılır.
Kısaltma ( abbr) öğesi : Bir kısaltmayı veya akronimi temsil etmek için kullanılır.
İletişim Adresi ( address) öğesi : İletişim bilgilerini temsil etmek için kullanılır.
(Tarih) Saat ( time) öğesi : Tarih ve/veya saati temsil etmek için kullanılır.
Üst simge ( sup) öğesi : Üst simge metni temsil etmek için kullanılır.
Alt simge ( sub) öğesi : Alt simge metni göstermek için kullanılır.
Satır İçi Kod ( code) öğesi : Bilgisayar kodunun bir parçasını temsil etmek için kullanılır.
Eklemlenmemiş Açıklama ( u) öğesi : Metin dışı bir açıklamaya sahip olduğunu gösteren bir şekilde işlenmesi gereken satır içi metin bölümünü temsil etmek için kullanılır.
Ruby Annotation ( ruby) elementi : Ruby annotation metnini temsil etmek için kullanılır.
Üstü çizili ( s) öğe : Artık doğru veya geçerli olmayan içeriği temsil etmek için kullanılır.
HTML Form Elemanları ve Nitelikleri
Formlar
formelement : Kullanıcıdan girdi almak için HTML formu oluşturmak amacıyla kullanılır.
Yaygın Giriş Türleri :
text, email, password, radio, checkbox, number, date.
actionÖzellik : Form verilerinin gönderileceği URL'yi belirtmek için kullanılır.
methodÖznitelik : Form verilerini gönderirken kullanılacak HTTP yöntemini belirtmek için kullanılır. En yaygın yöntemler GETve yöntemleridir POST.
<form method="value-goes-here" action="url-goes-here">
  <!-- inputs go inside here -->
</form>
inputelement : Kullanıcı girişi için bir giriş alanı oluşturmak için kullanılır.
typeÖzellik : Giriş alanının türünü belirtmek için kullanılır, örneğin, text, email, number, radio, checkbox.
placeholderÖzellik : Kullanıcıya giriş alanına ne girmesi gerektiğini gösteren bir ipucu vermek için kullanılır.
valueÖzellik : Giriş alanının değerini belirtmek için kullanılır. Giriş alanının bir buttontürü varsa, bu valueözellik düğme metnini ayarlamak için kullanılabilir.
nameÖzellik : Form verileri gönderildiğinde anahtar görevi gören bir giriş alanına ad atamak için kullanılır. Radyo düğmeleri için, bunlara aynı adı vermek, nameonları bir araya getirir, böylece gruptaki seçeneklerden yalnızca biri aynı anda seçilebilir.
sizeÖzellik : Kullanıcının giriş alanına yazarken görünür olması gereken karakter sayısını tanımlamak için kullanılır.
minÖzellik : Giriş türleriyle birlikte kullanılabilir; örneğin, numbergiriş alanında izin verilen minimum değeri belirtmek için.
maxÖzellik : Giriş türleriyle birlikte kullanılabilir; örneğin, numbergiriş alanında izin verilen maksimum değeri belirtmek için.
minlengthÖzellik : Giriş alanında gerekli olan minimum karakter sayısını belirtmek için kullanılır.
maxlengthÖzellik : Giriş alanında izin verilen maksimum karakter sayısını belirtmek için kullanılır.
requiredÖzellik : Formu göndermeden önce bir giriş alanının doldurulması gerektiğini belirtmek için kullanılır.
disabledÖzellik : Bir giriş alanının devre dışı bırakılması gerektiğini belirtmek için kullanılır.
readonlyÖzellik : Bir giriş alanının salt okunur olduğunu belirtmek için kullanılır.
<!-- Text input -->
<input 
  type="text"
  id="name"
  name="name"
  placeholder="e.g. Quincy Larson"
  size="20"
  minlength="5"
  maxlength="30"
  required
/>

<!-- Number input -->
<input 
  type="number"
  id="quantity"
  name="quantity"
  min="2"
  max="10"
  disabled
/>

<!-- Button -->
<input type="button" value="Show Alert" />
labelelement : giriş alanı için etiket oluşturmak amacıyla kullanılır.
forÖzellik : Etiketin hangi giriş alanı için olduğunu belirtmek için kullanılır.
Örtük form ilişkilendirmesi : Giriş alanları, giriş alanını bir öğenin içine alarak etiketlerle ilişkilendirilebilir label.
<form action="">
  <label>
    Full Name:
    <input type="text" />
  </label>
</form>
Açık form ilişkilendirmesifor : Giriş alanları, öğe üzerindeki özniteliği kullanarak etiketlerle ilişkilendirilebilir label.
<form action="">
  <label for="email">Email Address: </label>
  <input type="email" id="email" />
</form>
button<button> öğesitype : tıklanabilir bir düğme oluşturmak için kullanılır. Bir düğme ayrıca , etkinleştirildiğinde düğmenin davranışını kontrol eden bir özniteliğe de sahip olabilir , örneğin <button>, <button> submit, reset<button> button.
<button type="button">Show Form</button>
<button type="submit">Submit Form</button>
<button type="reset">Reset Form</button>
fieldsetElement : Birbiriyle ilişkili girdileri gruplandırmak için kullanılır.
legendelement : Giriş gruplarını tanımlamak için başlık eklemek amacıyla kullanılır.
<!-- Radio group -->
<fieldset>
  <legend>Was this your first time at our hotel?</legend>

  <input id="yes-option" type="radio" name="hotel-stay" value="yes" />
  <label for="yes-option">Yes</label>

  <input id="no-option" type="radio" name="hotel-stay" value="no" />
  <label for="no-option">No</label>
</fieldset>

<!-- Checkbox group -->
<fieldset>
  <legend>
    Why did you choose to stay at our hotel? (Check all that apply)
  </legend>

  <input type="checkbox" id="location" name="location" value="location" />
  <label for="location">Location</label>

  <input type="checkbox" id="price" name="price" value="price" />
  <label for="price">Price</label>
</fieldset>
Odaklanmış durum : Bu, bir giriş alanının kullanıcı tarafından seçildiği durumdur.
HTML Tablo Öğeleri ve Nitelikleriyle Çalışmak
Tablo öğesi : HTML tablosu oluşturmak için kullanılır.
Tablo Başlığı ( thead) öğesi : HTML tablosunda başlık içeriğini gruplandırmak için kullanılır.
Tablo Satırı ( tr) öğesi : HTML tablosunda bir satır oluşturmak için kullanılır.
Tablo Başlığı ( th) öğesi : HTML tablosunda başlık hücresi oluşturmak için kullanılır.
Tablo gövdesi ( tbody) öğesi : HTML tablosunda gövde içeriğini gruplandırmak için kullanılır.
Tablo Veri Hücresi ( td) öğesi : HTML tablosunda veri hücresi oluşturmak için kullanılır.
Tablo Altbilgisi ( tfoot) öğesi : HTML tablosunda altbilgi içeriğini gruplandırmak için kullanılır.
caption`<element>` : HTML tablosuna başlık eklemek için kullanılır.
colspanÖzellik : Bir tablo hücresinin kaç sütunu kapsaması gerektiğini belirtmek için kullanılır.
<table>
  <caption>Exam Grades</caption>

  <thead>
    <tr>
      <th>Last Name</th>
      <th>First Name</th>
      <th>Grade</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Davis</td>
      <td>Alex</td>
      <td>54</td>
    </tr>

    <tr>
      <td>Doe</td>
      <td>Samantha</td>
      <td>92</td>
    </tr>

    <tr>
      <td>Rodriguez</td>
      <td>Marcus</td>
      <td>88</td>
    </tr>
  </tbody>

  <tfoot>
    <tr>
      <td colspan="2">Average Grade</td>
      <td>78</td>
    </tr>
  </tfoot>
</table>
HTML Araçları
HTML doğrulayıcı : HTML kodunun sözdizimini kontrol ederek geçerli olup olmadığını doğrulayan bir araç.
DOM denetleyicisi : Bir web sayfasının HTML yapısını incelemenize ve değiştirmenize olanak sağlayan bir araç.
Geliştirici Araçları : Web sayfalarında hata ayıklama, performans analizi ve performans incelemesi yapmanıza yardımcı olan, doğrudan tarayıcıya entegre edilmiş bir dizi web geliştirici aracı.
Erişilebilirliğe Giriş
Web İçeriği Erişilebilirlik Yönergeleri : Web İçeriği Erişilebilirlik Yönergeleri (WCAG), web içeriğini engelli kişiler için daha erişilebilir hale getirmeye yönelik bir dizi yönergedir. WCAG'nin dört ilkesi, Algılanabilir, İşletilebilir, Anlaşılabilir ve Sağlam anlamına gelen POUR'dur.
Erişilebilirlik için Yardımcı Teknoloji
Ekran okuyucular : Bilgisayar ekranındaki içeriği sesli olarak okuyan yazılım programlarıdır. Görme engelli veya görme bozukluğu olan kişiler tarafından internete erişmek için kullanılırlar.
Büyük yazı tipi veya Braille klavyeler : Görme engelli kişilerin internete erişmesi için kullanılır.
Ekran büyütücüler : Bilgisayar ekranının içeriğini büyüten yazılım programlarıdır. Görme engelli kişilerin internete erişimi için kullanılırlar.
Alternatif işaretleme aygıtları : Hareket kısıtlılığı olan kişilerin internete erişmek için kullandığı aygıtlar. Bunlara joystick, trackball ve dokunmatik yüzey gibi aygıtlar dahildir.
Ses tanıma : Hareket kısıtlılığı olan kişilerin internete erişimi için kullanılır. Kullanıcıların bilgisayarı seslerini kullanarak kontrol etmelerini sağlar.
Erişilebilirlik Denetleme Araçları
Yaygın Erişilebilirlik Araçları : Google Lighthouse, Wave, IBM Equal Accessibility Checker ve axe DevTools, bir web sitesinin erişilebilirliğini denetlemek için kullanılan yaygın erişilebilirlik araçlarından bazılarıdır.
Erişilebilirlik En İyi Uygulamaları
Doğru başlık düzeyi yapısı : İçeriğiniz için mantıklı bir yapı oluşturmak üzere doğru başlık düzeylerini kullanmalısınız. Bu, yardımcı teknolojilerin web sitenizin içeriğini anlamasına yardımcı olur.
Erişilebilirlik ve Tablolarth : Tablo kullanırken, başlık hücrelerini tanımlamak için `<table>` öğesini ve veri hücrelerini tanımlamak için `<table>` öğesini kullanmalısınız td. Bu, yardımcı teknolojilerin tablonun yapısını anlamasına yardımcı olur.
Giriş alanlarının etiketle ilişkilendirilmesinin önemi : Form giriş alanlarıyla etiket ilişkilendirmek için `<tag>` öğesini kullanmalısınız label. Bu, yardımcı teknolojilerin giriş alanının amacını anlamasına yardımcı olur.
altİyi metnin önemi : Görseller için metin alternatifi sağlamak amacıyla bu özelliği kullanmalısınız alt. Bu, yardımcı teknolojilerin görselin içeriğini anlamasına yardımcı olur.
İyi bir bağlantı metninin önemi : Kullanıcıların bağlantının amacını anlamalarına yardımcı olmak için açıklayıcı bağlantı metni kullanmalısınız.
Sesli ve görüntülü içerikleri erişilebilir hale getirmenin en iyi uygulamaları : İşitme engelliler için erişilebilir hale getirmek amacıyla sesli ve görüntülü içeriklere altyazı ve metin dökümü sağlamalısınız. Ayrıca, görme engelliler için erişilebilir hale getirmek amacıyla video içeriklerine sesli açıklamalar da sağlamalısınız.
tabindexBu özellik , öğeleri odaklanabilir hale getirmek ve klavye kullanılarak gezinmeleri gereken göreceli sırayı tanımlamak için kullanılır. Bu özelliği asla 0'dan büyük bir değerle kullanmamak önemlidir. tabindexBunun yerine, 0 veya -1 değerini kullanmalısınız.
accesskeyÖzellik : Bir öğe için klavye kısayolu tanımlamak için kullanılır. Bu, hareket kısıtlılığı olan kullanıcıların web sitesinde daha kolay gezinmelerine yardımcı olabilir.
WAI-ARIA, Roller ve Nitelikler
WAI-ARIA : Web Erişilebilirlik Girişimi - Erişilebilir Zengin İnternet Uygulamaları anlamına gelir. Erişilebilirliği artırmak için HTML öğelerine eklenebilen bir dizi özelliktir. Yardımcı teknolojilere içeriğin amacı ve yapısı hakkında ek bilgi sağlar.
ARIA rolleri : HTML öğelerine eklenebilen ve amaçlarını tanımlayan önceden tanımlanmış bir rol kümesidir. Bu, yardımcı teknolojilerin web sitesinin içeriğini anlamasına yardımcı olur. Örnekler arasında role="tab", role="menu", ve bulunur role="alert".
aria-labelve aria-labelledbyöznitelikler : Bu öznitelikler, bir öğeye programatik (veya erişilebilir) bir ad vermek için kullanılır; bu da yardımcı teknolojilerin (ekran okuyucular gibi) öğenin amacını anlamasına yardımcı olur. Genellikle bir öğenin görsel etiketi metin yerine bir resim veya sembol olduğunda kullanılırlar. aria-labelözniteliğinde adı doğrudan tanımlamanıza olanak tanırken, aria-labelledbysayfadaki mevcut metne referans vermenize olanak tanır.
aria-hiddenÖzellik : Ekran okuyucular gibi yardımcı teknolojilerden bir öğeyi gizlemek için kullanılır. Örneğin, anlamlı bir içerik sağlamayan dekoratif resimleri gizlemek için kullanılabilir.
aria-describedbyÖzellik : Bir öğe hakkında ek bilgi sağlamak için, o öğeyi bilgiyi içeren başka bir öğeyle ilişkilendirmek amacıyla kullanılır. Bu, yardımcı teknolojilerin öğenin amacını anlamasına yardımcı olur.