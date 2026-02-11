HTML Erişilebilirlik İncelemesi
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
Uygun başlık düzeyi yapısı : İçeriğiniz için mantıklı bir yapı oluşturmak üzere uygun başlık düzeyleri kullanmalısınız. Bu, yardımcı teknolojileri kullanan kişilerin web sitenizin içeriğini anlamasına yardımcı olur.
Erişilebilirlik ve Tablolarth : Tablo kullanırken, başlık hücrelerini tanımlamak için `<title>` öğesini ve veri hücrelerini tanımlamak için `<title>` öğesini kullanmalısınız td. Bu, yardımcı teknolojileri kullanan kişilerin tablonun yapısını anlamalarına yardımcı olur. `<title>` öğesiyle , tablonun başlığını (veya açıklamasını) yazabilirsiniz, böylece kullanıcılar, özellikle yardımcı teknolojileri kullananlar, tablonun amacını ve içeriğini hızlı bir şekilde anlayabilirler. `<title>` öğesini `<title>` öğesinin açılış etiketinden hemen sonra captionyerleştirmelisiniz . Bu şekilde, ekran okuyucular ve diğer yardımcı teknolojiler, içeriği okumadan önce açıklamayı duyurarak daha fazla bağlam sağlayabilir.captiontable
Giriş alanlarının etiketle ilişkilendirilmesinin önemi : Form giriş alanlarıyla etiket ilişkilendirmek için `<tag>` öğesini kullanmalısınız label. Bu, yardımcı teknolojileri kullanan kişilerin giriş alanının amacını anlamalarına yardımcı olur.
altİyi metnin önemi : Görseller için metin alternatifi sağlamak amacıyla bu özelliği kullanmalısınız alt. Bu, yardımcı teknolojileri kullanan kişilerin görselin içeriğini anlamalarına yardımcı olur.
İyi bir bağlantı metninin önemi : Kullanıcıların bağlantının amacını anlamalarına yardımcı olmak için açıklayıcı bağlantı metni kullanmalısınız. Bu, yardımcı teknolojileri kullanan kişilerin bağlantının amacını anlamalarına yardımcı olur.
Sesli ve görüntülü içerikleri erişilebilir hale getirmenin en iyi uygulamaları : İşitme engelliler için erişilebilir hale getirmek amacıyla sesli ve görüntülü içeriklere altyazı ve metin dökümü sağlamalısınız. Ayrıca, görme engelliler için erişilebilir hale getirmek amacıyla video içeriklerine sesli açıklamalar da sağlamalısınız.
tabindexBu özellik , öğeleri odaklanabilir hale getirmek ve klavye kullanılarak gezinmeleri gereken göreceli sırayı tanımlamak için kullanılır. Bu özelliği asla 0'dan büyük bir değerle kullanmamak önemlidir. tabindexBunun yerine, 0 veya -1 değerini kullanmalısınız.
<p tabindex="-1">Sorry, there was an error with your submission.</p>
accesskeyÖzellik : Bir öğe için klavye kısayolu tanımlamak için kullanılır. Bu, hareket kısıtlılığı olan kullanıcıların web sitesinde daha kolay gezinmelerine yardımcı olabilir.
<button accesskey="s">Save</button>
<button accesskey="c">Cancel</button>
<a href="index.html" accesskey="h">Home</a>
WAI-ARIA, Roller ve Nitelikler
WAI-ARIA : Web Erişilebilirlik Girişimi - Erişilebilir Zengin İnternet Uygulamaları anlamına gelir. Erişilebilirliği artırmak için HTML öğelerine eklenebilen bir dizi özelliktir. Yardımcı teknolojilere içeriğin amacı ve yapısı hakkında ek bilgi sağlar.
ARIA rolleri : HTML öğelerine eklenebilen ve amaçlarını tanımlayan önceden tanımlanmış bir rol kümesidir. Bu, yardımcı teknolojileri kullanan kişilerin web sitesinin içeriğini anlamalarına yardımcı olur. Örnekler arasında role="tab", role="menu", ve bulunur role="alert".
ARIA'da altı ana rol kategorisi bulunmaktadır:

Belge yapısı rolleri : Bu roller, web sayfasının genel yapısını tanımlar. Bu roller sayesinde, yardımcı teknolojiler farklı bölümler arasındaki ilişkileri anlayabilir ve kullanıcıların içeriğe erişmesine yardımcı olabilir.

Widget rolleri : Bu roller, kaydırma çubukları gibi etkileşimli öğelerin amacını ve işlevselliğini tanımlar.

Önemli bölüm rolleri : Bu roller, bir web sayfasının temel bölümlerini sınıflandırır ve etiketler. Ekran okuyucular, sayfanın önemli bölümlerine kolay gezinme sağlamak için bunları kullanır.

Canlı bölge rolleri : Bu roller, içeriği dinamik olarak değişecek öğeleri tanımlar. Bu sayede, ekran okuyucular ve diğer yardımcı teknolojiler, görme engelli kullanıcılara değişiklikleri duyurabilir.

Pencere rolleri : Bu roller, açılır iletişim kutuları gibi alt pencereleri tanımlar. Bu roller arasında alertdialogve bulunur dialog.

Soyut roller : Bu roller belgeyi düzenlemeye yardımcı olur. Yalnızca tarayıcı tarafından dahili olarak kullanılmak üzere tasarlanmıştır, geliştiriciler tarafından değil; bu nedenle var olduklarını bilmelisiniz ancak web sitelerinizde veya web uygulamalarınızda kullanmamalısınız.

aria-labelve aria-labelledbyöznitelikler : Bu öznitelikler, bir öğeye programatik (veya erişilebilir) bir ad vermek için kullanılır; bu da yardımcı teknoloji (ekran okuyucular gibi) kullanan kişilerin öğenin amacını anlamalarına yardımcı olur. Genellikle bir öğenin görsel etiketi metin yerine bir resim veya sembol olduğunda kullanılırlar. aria-labelözniteliğinde adı doğrudan tanımlamanıza olanak tanırken, aria-labelledbysayfadaki mevcut metne referans vermenize olanak tanır.

<button aria-label="Search">
    <i class="fas fa-search"></i>
</button>
<input type="text" aria-labelledby="search-btn">
<button type="button" id="search-btn">Search</button>
aria-hiddenÖzellik : Ekran okuyucular gibi yardımcı teknolojilerden bir öğeyi gizlemek için kullanılır. Örneğin, anlamlı bir içerik sağlamayan dekoratif resimleri gizlemek için kullanılabilir.
<button>
    <i class="fa-solid fa-gear" aria-hidden="true"></i>
    <span class="label">Settings</span>
</button>
aria-describedbyÖznitelik : Bir öğeye ek bilgi sağlamak için, bu bilgiyi içeren başka bir öğeyle ilişkilendirmek amacıyla kullanılır. Bu, ekran okuyucu kullanan kişilerin öğeye gittiklerinde ek bilgilere anında erişmelerini sağlar. Yaygın kullanım örnekleri arasında, metin girişine biçimlendirme talimatları veya geçersiz form gönderiminden sonra bir hata mesajı eklemek yer alır.
<form>
    <label for="password">Password:</label>
    <input type="password" id="password" aria-describedby="password-help" />
    <p id="password-help">Your password must be at least 8 characters long.</p>
</form>