CSS Temelleri İncelemesi
CSS Temelleri
CSS nedir? : Basamaklı Stil Sayfaları (CSS), HTML öğelerine stil uygulamak için kullanılan bir işaretleme dilidir. CSS, renkler, arka plan resimleri, düzenler ve daha fazlası için kullanılır.
CSS Kuralının Temel Anatomisi : Bir CSS kuralı iki ana bölümden oluşur: bir seçici ve bir bildirim bloğu. Seçici, CSS'de belirli HTML öğelerini tanımlamak ve stillendirmek için kullanılan bir kalıptır. Bildirim bloğu, belirli bir seçici veya seçiciler için bir dizi stil uygular.
İşte bir CSS kuralının genel sözdizimi:

selector {
    property: value;
}
meta name="viewport"Element : Bu metaelement, tarayıcıya sayfanın boyutlarını ve ölçeklendirmesini farklı cihazlarda, özellikle cep telefonlarında ve tabletlerde nasıl kontrol edeceğine dair talimatlar verir.
Varsayılan Tarayıcı Stilleri : Her HTML öğesine varsayılan tarayıcı stilleri uygulanır. Bu genellikle varsayılan kenar boşlukları ve dolgular gibi öğeleri içerir.
Satır İçi, Dahili ve Harici CSS
Satır İçi CSS : Bu stiller, `<style>` özniteliği kullanılarak doğrudan bir HTML öğesinin içine yazılır style. Çoğu zaman, sorumlulukların ayrılması nedeniyle satır içi CSS kullanmayacaksınız.
İşte satır içi CSS örneği:

12
<link rel="stylesheet" href="styles.css">
<p style="color: red;">This is a red paragraph.</p>

Açık Kum Havuzu
Dahili CSS<style> : Bu stiller, bir HTML belgesinin <head> bölümündeki <head> etiketlerinin içine yazılır head. Bu, kısa kod örnekleri oluşturmak için yararlı olabilir, ancak genellikle dahili CSS kullanmanıza gerek kalmaz.
Harici CSS : Bu stiller ayrı bir CSS dosyasında yazılır ve `<head>` linkbölümündeki `<style>` öğesi kullanılarak HTML belgesine bağlanır head. Çoğu proje için, dahili veya satır içi CSS yerine harici bir CSS dosyası kullanacaksınız.
widthve heightMülklerle Çalışmak
widthÖzellik : Bu özellik, bir öğenin genişliğini belirtir. Genişlik belirtmezseniz, varsayılan değer boş bırakılır auto. Bu, tarayıcının öğenin genişliğini içeriğine, üst öğesine ve görüntü türüne göre belirlemesine olanak tanır.
min-widthÖzellik : Bu özellik, bir öğenin minimum genişliğini belirtir.
max-widthÖzellik : Bu özellik, bir öğenin maksimum genişliğini belirtir.
heightÖzellik : Bu özellik, bir öğenin yüksekliğini belirtir. autoVarsayılan olarak yükseklik sabittir, yani içindeki içeriğe göre kendini ayarlar.
min-heightÖzellik : Bu özellik, bir öğe için minimum yüksekliği belirtir.
max-heightÖzellik : Bu özellik, bir öğenin maksimum yüksekliğini belirtir.
Farklı CSS Kombinatör Türleri
Alt Öğe Birleştirici : Bu birleştirici, belirtilen bir üst öğenin alt öğelerini hedeflemek için kullanılır. Aşağıdaki örnek, öğelerin liiçindeki tüm öğeleri hedefleyecektir ul.
index.html
styles.css
123456
<link rel="stylesheet" href="styles.css">
<ul>
    <li>Example item one</li>
    <li>Example item two</li>
    <li>Example item three</li>
</ul>

Açık Kum Havuzu
Çocuk Birleştirici ( >)p : Bu birleştirici, belirtilen bir üst öğenin doğrudan çocukları olan öğeleri seçmek için kullanılır. Aşağıdaki örnek , sınıfın doğrudan çocukları olan tüm öğeleri hedefleyecektir container.
index.html
styles.css
12345678
<link rel="stylesheet" href="styles.css">
<div class="container">
  <p>This will get styled.</p>

  <div>
    <p>This will not get styled.</p>
  </div>
</div>

Açık Kum Havuzu
Sonraki Kardeş Öğeyi Birleştirici ( +) : Bu birleştirici, belirtilen kardeş öğeyi hemen takip eden bir öğeyi seçer. Aşağıdaki örnek, öğeyi hemen takip eden paragraf öğesini seçecektir h2.
index.html
styles.css
1234
<link rel="stylesheet" href="styles.css">
<h2>I am a sub heading</h2>

<p>This paragraph element will get a red background.</p>

Açık Kum Havuzu
Sonraki Kardeş Birleştirici ( ~) : Bu birleştirici, belirtilen bir öğenin kendisinden sonra gelen tüm kardeş öğelerini seçer. Aşağıdaki örnek, yalnızca ikinci paragraf öğesini biçimlendirecektir çünkü bu öğenin tek kardeşidir ulve aynı üst öğeyi paylaşır.
index.html
styles.css
1234567891011
<link rel="stylesheet" href="styles.css">
<div class="container">
  <p>This will not get styled.</p>
  <ul>
    <li>Example item one</li>
    <li>Example item two</li>
    <li>Example item three</li>
  </ul>
  <p>This will get styled.</p>
</div>


Açık Kum Havuzu
Satır İçi, Blok ve Satır İçi-Blok Seviye Elemanları
Satır İçi Öğeler : Satır içi öğeler yalnızca ihtiyaç duydukları kadar genişlik kaplar ve yeni bir satırda başlamazlar. Bu öğeler içerik içinde akar ve metnin ve diğer satır içi öğelerin yanlarında görünmesine olanak tanır. Yaygın satır içi öğeler arasında span, anchor, ve imgöğeleri bulunur.
Blok Düzeyindeki Öğeler : Blok düzeyindeki öğeler yeni bir satırda başlar ve varsayılan olarak kendilerine ayrılan tam genişliği kaplayarak kapsayıcılarının genişliği boyunca uzanır. Bazı yaygın blok düzeyindeki öğeler div, paragraph, ve sectionöğeleridir.
Satır İçi Blok Düzeyi Öğelerinline-block : Bir öğeyi, özelliği kullanarak bu şekilde ayarlayabilirsiniz . Bu öğeler satır içi öğeler gibi davranır, ancak blok düzeyi öğeleri gibi bir ve özelliğine displaysahip olabilirler .widthheight
Kenar boşluğu ve dolgu
marginÖzellik : Bu özellik, öğenin kenarı ile çevreleyen öğeler arasında, öğenin dışına boşluk uygulamak için kullanılır.
paddingÖzellik : Bu özellik, öğenin içeriği ile kenarlığı arasına boşluk eklemek için kullanılır.
marginKısaltma : Kenar boşluklarını ayarlamak için 1-4 değer belirtebilirsiniz. Bir değer dört kenarın tamamına uygulanır; iki değer topve değerlerini bottom, ardından rightve değerlerini ayarlar left; üç değer topyatay ( rightve left) değerini, ardından değerini ayarlar bottom; dört değer ise top, right, bottom, değerlerini ayarlar left.
paddingKısaltma : Kenar boşluklarını ayarlamak için 1-4 değer belirtebilirsiniz. Bir değer dört kenarın tamamına uygulanır; iki değer topve değerlerini bottom, ardından rightve değerlerini ayarlar left; üç değer topyatay ( rightve left) değerini, ardından değerini ayarlar bottom; dört değer ise top, right, bottom, değerlerini ayarlar left.
CSS Özgüllüğü
Satır İçi CSS Özgüllüğü : Satır içi CSS, doğrudan öğeye uygulandığı için en yüksek özgüllüğe sahiptir. Dahili veya harici herhangi bir CSS'yi geçersiz kılar. Satır içi stiller için özgüllük değeri (1, 0, 0, 0)'dır.
Dahili CSS Özgüllüğü : Dahili CSS, HTML belgesinin style<head> bölümündeki bir <head> öğesi içinde tanımlanır . Satır içi stillere göre daha düşük özgüllüğe sahiptir ancak harici stilleri geçersiz kılabilir.head
Harici CSS Özgüllüğülink : Harici CSS, `<head>` bölümündeki bir `<head>` öğesi aracılığıyla bağlanır headve ayrı dosyalarda yazılır .css. En düşük özgüllüğe sahiptir ancak daha büyük projeler için en iyi bakım kolaylığını sağlar.
Evrensel Seçici ( *) : Belgedeki herhangi bir öğeyle eşleşen özel bir CSS seçici türüdür. Genellikle sayfadaki tüm öğelere stil uygulamak için kullanılır; bu, farklı tarayıcılarda stilleri sıfırlamak veya normalleştirmek için yararlı olabilir. Evrensel seçici, herhangi bir seçicinin en düşük özgüllük değerine sahiptir. Özgüllük değerinin tüm bölümlerine 0 katkıda bulunur (0, 0, 0, 0).
Tür Seçiciler : Bu seçiciler, etiket adlarına göre öğeleri hedefler. Tür seçicilerin özgüllüğü diğer seçicilere göre nispeten düşüktür. Bir tür seçicinin özgüllük değeri (0, 0, 0, 1)'dir.
Sınıf Seçiciler : Bu seçiciler, nokta ( ) ve ardından sınıf adıyla tanımlanır .. Bir sınıf seçicinin özgüllük değeri (0, 0, 1, 0)'dır. Bu, sınıf seçicilerin tür seçicileri geçersiz kılabileceği, ancak kimlik seçiciler ve satır içi stiller tarafından da geçersiz kılınabileceği anlamına gelir.
Kimlik Seçiciler : Kimlik seçiciler, bir karma sembolü ( ) ve ardından kimlik adıyla tanımlanır #. Kimlik seçicilerin özgüllüğü çok yüksektir; tür seçicilerden ve sınıf seçicilerden daha yüksek, ancak satır içi stillerden daha düşüktür. Bir kimlik seçicinin özgüllük değeri (0, 1, 0, 0)'dır.
!importantAnahtar kelime : Bir stil kuralına en yüksek önceliği vermek ve bir özellik için diğer tüm bildirimleri geçersiz kılmasını sağlamak için kullanılır. Kullanıldığında, diğer seçicilerin özgüllüğünden bağımsız olarak, tarayıcının belirtilen stili uygulamasına neden olur. Kullanırken dikkatli olmalısınız !importantçünkü CSS'nizin bakımını ve hata ayıklamasını zorlaştırabilir.
Basamaklı Algoritma : Aynı öğeyi hedefleyen birden fazla stil olduğunda hangi CSS kurallarının uygulanacağına karar vermek için kullanılan bir algoritmadır. İyi tanımlanmış bir dizi kurala dayanarak en uygun stillerin kullanılmasını sağlar.
CSS Kalıtımı : Stillerin üst öğelerden alt öğelere aktarılma sürecidir. Kalıtım, belge ağacında daha yüksek bir seviyede stil tanımlamanıza ve bu stilleri her bir öğe için açıkça belirtmeden birden fazla öğeye uygulamanıza olanak tanır.