CSS Temelleri
CSS nedir? : Basamaklı Stil Sayfaları (CSS), HTML öğelerine stil uygulamak için kullanılan bir işaretleme dilidir. CSS, renkler, arka plan resimleri, düzenler ve daha fazlası için kullanılır.
CSS Kuralının Temel Anatomisi : Bir CSS kuralı iki ana bölümden oluşur: bir seçici ve bir bildirim bloğu. Seçici, CSS'de belirli HTML öğelerini tanımlamak ve stillendirmek için kullanılan bir kalıptır. Bildirim bloğu, belirli bir seçici veya seçiciler için bir dizi stil uygular.
meta name="viewport"Element : Bu metaelement, tarayıcıya sayfanın boyutlarını ve ölçeklendirmesini farklı cihazlarda, özellikle cep telefonlarında ve tabletlerde nasıl kontrol edeceğine dair talimatlar verir.
Varsayılan Tarayıcı Stilleri : Her HTML öğesine varsayılan tarayıcı stilleri uygulanır. Bu genellikle varsayılan kenar boşlukları ve dolgular gibi öğeleri içerir.
Satır İçi, Dahili ve Harici CSS
Satır İçi CSS : Bu stiller, `<style>` özniteliği kullanılarak doğrudan bir HTML öğesinin içine yazılır style. Çoğu zaman, sorumlulukların ayrılması nedeniyle satır içi CSS kullanmayacaksınız.
Dahili CSS<style> : Bu stiller, bir HTML belgesinin <head> bölümündeki <head> etiketlerinin içine yazılır head. Bu, kısa kod örnekleri oluşturmak için yararlı olabilir, ancak genellikle dahili CSS kullanmazsınız.
Harici CSS : Bu stiller ayrı bir CSS dosyasında yazılır ve `<head>` linkbölümündeki `<style>` öğesi kullanılarak HTML belgesine bağlanır head. Çoğu proje için, dahili veya satır içi CSS yerine harici bir CSS dosyası kullanacaksınız.
widthve heightMülklerle Çalışmak
widthÖzellik : Bu özellik, bir öğenin genişliğini belirtir. Genişlik belirtmezseniz, varsayılan değer boş bırakılır auto. Bu, tarayıcının öğenin genişliğini içeriğine, üst öğesine ve görüntü türüne göre belirlemesine olanak tanır.
min-widthÖzellik : Bu özellik, bir öğenin minimum genişliğini belirtir.
max-widthÖzellik : Bu özellik, bir öğenin maksimum genişliğini belirtir.
heightÖzellik : Bu özellik, bir öğenin yüksekliğini belirtir. autoVarsayılan olarak yükseklik sabittir, yani içindeki içeriğe göre kendini ayarlar.
min-heightÖzellik : Bu özellik, bir öğe için minimum yüksekliği belirtir.
max-heightÖzellik : Bu özellik, bir öğenin maksimum yüksekliğini belirtir.
Farklı CSS Kombinatör Türleri
Soy Birleştirici ( ) *seçiciler arasında tek bir boşluk : Bu birleştirici, belirtilen bir üst öğenin soyundan gelen öğeleri hedeflemek için kullanılır.

Çocuk Birleştirici ( >) : Bu birleştirici, belirtilen bir üst öğenin doğrudan çocukları olan öğeleri seçmek için kullanılır.

Sonraki Kardeş Birleştirici ( +) : Bu birleştirici, belirtilen kardeş öğeyi hemen takip eden bir öğeyi seçer.

Sonraki Kardeş Birleştirici ( ~) : Bu birleştirici, belirtilen bir öğenin kendisinden sonra gelen tüm kardeşlerini seçer.

Satır İçi, Blok ve Satır İçi-Blok Seviye Elemanları
Satır İçi Öğeler : Satır içi öğeler yalnızca ihtiyaç duydukları kadar genişlik kaplar ve yeni bir satırda başlamazlar. Bu öğeler içerik içinde akar ve metnin ve diğer satır içi öğelerin yanlarında görünmesine olanak tanır. Yaygın satır içi öğeler arasında span, anchor, ve imgöğeleri bulunur.
Blok Düzeyindeki Öğeler : Blok düzeyindeki öğeler, varsayılan olarak kendilerine ayrılan tam genişliği kaplar ve kapsayıcılarının genişliği boyunca uzanır. Bazı yaygın blok düzeyindeki öğeler şunlardır: div, p, ve sectionöğeleri.
Satır İçi Blok Düzeyi Öğelerinline-block : Bir öğeyi, özelliği kullanarak bu şekilde ayarlayabilirsiniz . Bu öğeler satır içi öğeler gibi davranır, ancak blok düzeyi öğeler gibi bir ve özelliğine displaysahip olabilirler .widthheight
Kenar boşluğu ve dolgu
marginÖzellik : Bu özellik, öğenin kenarı ile çevreleyen öğeler arasında, öğenin dışına boşluk uygulamak için kullanılır.
marginKısaltma : Kenar boşluklarını ayarlamak için 1-4 değer belirtebilirsiniz. Bir değer dört kenarın tamamına uygulanır; iki değer topve değerlerini bottom, ardından rightve değerlerini ayarlar left; üç değer topyatay ( rightve left) değerini, ardından değerini ayarlar bottom; dört değer ise top, right, bottom, değerlerini ayarlar left.
paddingÖzellik : Bu özellik, öğenin içeriği ile kenarlığı arasına boşluk eklemek için kullanılır.
paddingKısaltma : Kenar boşluklarını ayarlamak için 1-4 değer belirtebilirsiniz. Bir değer dört kenarın tamamına uygulanır; iki değer topve değerlerini bottom, ardından rightve değerlerini ayarlar left; üç değer topyatay ( rightve left) değerini, ardından değerini ayarlar bottom; dört değer ise top, right, bottom, değerlerini ayarlar left.
CSS Özgüllüğü
Satır İçi CSS Özgüllüğü : Satır içi CSS, doğrudan öğeye uygulandığı için en yüksek özgüllüğe sahiptir. Dahili veya harici herhangi bir CSS'yi geçersiz kılar. Satır içi stiller için özgüllük değeri (1, 0, 0, 0)'dır.
Dahili CSS Özgüllüğü : Dahili CSS, HTML belgesinin style<head> bölümündeki bir <head> öğesi içinde tanımlanır . Satır içi stillere göre daha düşük özgüllüğe sahiptir ancak harici stilleri geçersiz kılabilir.head
Harici CSS Özgüllüğülink : Harici CSS, `<head>` bölümündeki bir `<head>` öğesi aracılığıyla bağlanır headve ayrı dosyalarda yazılır .css. En düşük özgüllüğe sahiptir ancak daha büyük projeler için en iyi bakım kolaylığını sağlar.
Evrensel Seçici ( *) : Bu, belgedeki herhangi bir öğeyle eşleşen özel bir CSS seçici türüdür. Genellikle sayfadaki tüm öğelere stil uygulamak için kullanılır; bu da farklı tarayıcılarda stilleri sıfırlamak veya normalleştirmek için yararlı olabilir. Evrensel seçici, herhangi bir seçicinin en düşük özgüllük değerine sahiptir. Özgüllük değerinin tüm bölümlerine 0 katkıda bulunur (0, 0, 0, 0).
Tür Seçiciler : Bu seçiciler, etiket adlarına göre öğeleri hedefler. Tür seçicilerin özgüllüğü diğer seçicilere göre nispeten düşüktür. Bir tür seçicinin özgüllük değeri (0, 0, 0, 1)'dir.
Sınıf Seçiciler : Bu seçiciler, nokta ( ) ve ardından sınıf adıyla tanımlanır .. Bir sınıf seçicinin özgüllük değeri (0, 0, 1, 0)'dır. Bu, sınıf seçicilerin tür seçicileri geçersiz kılabileceği, ancak kimlik seçiciler ve satır içi stiller tarafından da geçersiz kılınabileceği anlamına gelir.
Kimlik Seçiciler : Kimlik seçiciler, bir karma sembolü ( ) ve ardından kimlik adıyla tanımlanır #. Kimlik seçicilerin özgüllüğü çok yüksektir; tür seçicilerden ve sınıf seçicilerden daha yüksek, ancak satır içi stillerden daha düşüktür. Bir kimlik seçicinin özgüllük değeri (0, 1, 0, 0)'dır.
!importantAnahtar kelime : Bir stil kuralına en yüksek önceliği vermek ve bir özellik için diğer tüm bildirimleri geçersiz kılmasını sağlamak için kullanılır. Kullanıldığında, diğer seçicilerin özgüllüğünden bağımsız olarak, tarayıcının belirtilen stili uygulamasına neden olur. Kullanırken dikkatli olmalısınız !importantçünkü CSS'nizin bakımını ve hata ayıklamasını zorlaştırabilir.
Basamaklı Algoritma : Aynı öğeyi hedefleyen birden fazla stil olduğunda hangi CSS kurallarının uygulanacağına karar vermek için kullanılan bir algoritmadır. İyi tanımlanmış bir dizi kurala dayanarak en uygun stillerin kullanılmasını sağlar.
CSS Kalıtımı : Stillerin üst öğelerden alt öğelere aktarılma sürecidir. Kalıtım, belge ağacında daha yüksek bir seviyede stil tanımlamanıza ve bu stilleri her bir öğe için açıkça belirtmeden birden fazla öğeye uygulamanıza olanak tanır.
Tasarım Terminolojisi
Sayfa düzeni (Layout) : Görsel öğelerin bir mesajı iletmek için sayfada veya ekranda nasıl düzenlendiğidir. Bu öğeler metin, resimler ve boş alanları içerebilir.
Hizalama : Bu, öğelerin birbirlerine göre nasıl yerleştirildiğini ifade eder. Hizalamayı doğru kullanmak, tasarımın temiz ve düzenli görünmesine yardımcı olur.
Kompozisyon : Bu, uyumlu bir tasarım oluşturmak için unsurları düzenleme eylemidir. Görüntüler, metin ve şekiller gibi unsurların birbirleriyle nasıl ilişkili olduğunu ve tasarıma sanatsal bir şekilde nasıl katkıda bulunduğunu belirler.
Denge : Bu, bir kompozisyon içindeki görsel ağırlığın dağılımıdır. Tasarımcılar, simetrik veya asimetrik düzenlemeler yoluyla bir denge yaratmayı amaçlar.
Ölçek : Bu, bir öğenin boyutlarını veya büyüklüğünü başka bir öğenin boyutlarıyla karşılaştırmayı ifade eder.
Hiyerarşi : Bu, bir tasarımda öğelerin önem sırasını belirler. En önemli bilgilerin önce fark edilmesini sağlamakla ilgilidir.
Kontrast : Bu, öğeler arasında net ayrımlar oluşturma sürecidir. Bunu renk, boyut, şekil, doku veya diğer görsel özelliklerdeki farklılıklar yoluyla yapabilirsiniz. Güçlü kontrast, okunabilirliği artırmak için de faydalıdır.
Beyaz Alan (Negatif Alan) : Bu, bir tasarımda boş alandır. Öğeleri çevreleyen alandır.
Kullanıcı Arayüzü (UI) : Kullanıcı arayüzü, kullanıcıların ekranlarında görebilecekleri simgeler, resimler, metinler, menüler, bağlantılar ve düğmeler gibi görsel ve etkileşimli öğeleri içerir.
UX (Kullanıcı Deneyimi) : UX, kullanıcıların bir ürün veya hizmeti kullanırken nasıl hissettikleriyle ilgilidir. İyi tasarlanmış bir kullanıcı deneyimine sahip bir uygulama sezgisel, kullanımı kolay, verimli, erişilebilir ve keyifli olur.
Tasarım Özeti : Bu, bir projenin amaçlarını, hedeflerini ve gereksinimlerini özetleyen bir belgedir. Tasarım sürecine rehberlik eden ve nihai ürünün müşterinin ihtiyaçlarını karşılamasını sağlayan bir yol haritasıdır.
Vektör Tabanlı Tasarım : Bu, çizgileri, şekilleri ve renkleri tanımlamak için matematiksel formüller kullanarak dijital sanat eserleri oluşturmayı içerir.
Prototipleme : Bu, bir ürünün veya kullanıcı arayüzünün etkileşimli bir modelini oluşturma sürecini ifade eder.
Kullanıcı Arayüzü Tasarımının Temelleri
Arka Plan ve Ön Plan Renkleri İçin İyi Kontrast : Metnin okunabilirliğini sağlamak için arka plan ve ön plan renklerinin iyi bir kontrasta sahip olması önemlidir. Web İçeriği Erişilebilirlik Yönergeleri (WCAG), normal metin için minimum 4,5:1 ve büyük metin için 3:1 kontrast oranını önermektedir.
Tasarımda İyi Bir Görsel Hiyerarşi : Güçlü bir görsel hiyerarşi, gözün izleyeceği net bir yol sağlayarak, ilettiğiniz bilgilerin amaçladığınız sırayla algılanmasını sağlar.
Duyarlı Görseller : Duyarlı görseller, görüntülendikleri ekranın boyutuna uyacak şekilde ölçeklenen görsellerdir. Bu önemlidir çünkü görsellerinizin masaüstü bilgisayarlardan cep telefonlarına kadar tüm cihazlarda iyi görünmesini sağlar.
Aşamalı Geliştirme : Bu, tüm kullanıcıların, tarayıcı veya cihazdan bağımsız olarak, bir uygulamanın temel içeriğine ve işlevlerine erişebilmesini sağlayan bir tasarım yaklaşımıdır.
Kullanıcı Odaklı Tasarım : Bu yaklaşım, son kullanıcının ihtiyaçlarından tercihlerine ve sınırlamalarına kadar her şeyini önceliklendirir. Kullanıcı odaklı tasarımın amacı, sezgisel, verimli ve kullanıcılarınızın etkileşim kurmaktan keyif alacağı bir web sayfası oluşturmaktır.
Kullanıcı Araştırması : Bu, ürününüzü kullanan kişilerin sistematik olarak incelenmesidir. Amaç, kullanıcı ihtiyaçlarını, davranışlarını ve sorunlarını ölçmektir.
Kullanıcı Testi : Bu, kullanıcıların uygulamanızla etkileşim kurarken veri toplama uygulamasına verilen addır.
A/B Testi : Bu, yeni bir özelliği kullanıcı tabanınızın rastgele seçilmiş bir alt kümesine sunma sürecidir. Daha sonra, özelliğin faydalı olup olmadığını belirlemek için analiz verilerinden yararlanabilirsiniz.
Kullanıcı Gereksinimleri : Bu, uygulamanızın uyması gereken senaryoları veya kriterleri ifade eder. Kullanıcı gereksinimleri, kullanıcı araştırmaları veya sektör standartları tarafından tanımlanabilir. Hatta paydaş girdileriyle de tanımlanabilirler.
Aşamalı Bilgilendirme : Bu, kullanıcılara yalnızca mevcut etkinliklerine göre alakalı içerik göstermek ve geri kalanını gizlemek için kullanılan bir tasarım desenidir. Bu, bilişsel yükü azaltmak ve kullanıcı deneyimini daha sezgisel hale getirmek için yapılır.
Ertelenmiş/Tembel Kayıt : Bu, kullanıcıların kayıt olmaları gerekmeden uygulamanızda gezinmelerine ve etkileşimde bulunmalarına olanak tanıyan bir kullanıcı arayüzü tasarım desenidir.
Tasarımda En İyi Uygulamalar
Koyu Mod : Bu, web uygulamalarında varsayılan açık renk şemasını koyu renk şemasına değiştirebileceğiniz özel bir özelliktir. Koyu modda doygunluğu azaltılmış renkler kullanmalısınız. Doygunluğu azaltılmış renkler, daha az yoğun ve daha düşük doygunluk seviyesine sahip renklerdir.
Yol izleme (Breadcrumbs) : Bu, kullanıcının sitenin hiyerarşisinde nerede olduğunu gösteren bir gezinme aracıdır. Kullanıcıların kolayca bulabilmesi için yol izleme çubuklarını sayfanın en üstüne yerleştirmek en iyisidir. Ayrıca, yol izleme çubuklarının kolayca okunabilecek kadar büyük, ancak sayfada çok fazla yer kaplamayacak kadar küçük olduğundan emin olmalısınız.
Kart Bileşeni : Kart bileşeniniz tasarım olarak sade olmalı, görsel olarak karmaşık olmamalı veya çok fazla bilgi içermemelidir. Medya için, kullanıcı deneyimini geliştirmek amacıyla yüksek kaliteli resimler ve videolar seçtiğinizden emin olun.
Sonsuz Kaydırma : Bu, kullanıcının sayfayı aşağı kaydırdıkça daha fazla içerik yükleyen bir tasarım desenidir. Kullanıcıya daha fazla içerik görmek istediği zamanı kontrol etme olanağı sağladığı için "Daha Fazla Yükle" düğmesi kullanmayı düşünmelisiniz. Ayrıca, kullanıcıların en başa kadar kaydırmak zorunda kalmadan önceki sayfaya geri dönebilmeleri için bir geri düğmesi de ekleyebilirsiniz.
Modal Diyalog : Bu, mevcut sayfa içeriğinin üzerinde görüntülenen bir tür açılır penceredir. Genellikle arka plan içeriği, kullanıcının modal içeriğe daha iyi odaklanmasına yardımcı olmak için soluk bir renk katmanına sahip olur. Ayrıca, kullanıcının modalı kapatmak için dışına tıklamasına izin vermek her zaman iyi bir fikirdir. HTML dialogöğesini kullandığınızda, yerleşik birçok işlevsellik ve erişilebilirlik avantajından yararlanacaksınız.
Form Kaydı İçin İlerleme Göstergesi : Bu, kullanıcılara bir süreçte ne kadar ilerlediklerini göstermenin bir yoludur. Formlarda, kayıt ve kurulum süreçlerinde kullanılabilir. Tasarımınız basit, kolay bulunabilir olmalı ve önceki adımlara geri dönmeyi mümkün kılmalıdır.
Alışveriş Sepeti : Sepetler, kullanıcıların e-ticaret platformunda zaten seçtikleri ürünleri görebilecekleri bir yerdir. Sepetleriniz her zaman kullanıcı tarafından görülebilir olmalı, sepet, çanta veya kasa gibi yaygın bir simge kullanmalı ve kullanıcıların ödeme işlemine devam etmeleri için net bir harekete geçirici düğmeye sahip olmalıdır.
Ortak Tasarım Araçları
Figma : Bu bulut tabanlı araç, Kullanıcı Arayüzü ve Kullanıcı Deneyimi (UI/UX) tasarımında uzmanlaşmıştır. Tasarım ve geliştirme ekiplerinin her yerden iş birliği yapmasını sağlar ve vektör tabanlı tasarım, otomatik yerleşim, yorum ve geri bildirim sistemi gibi yerleşik özellikler sunar.
Sketch : Sezgisel arayüzü ve sadeliği sayesinde prototipleri hızlıca oluşturmak isteyen geliştiriciler için ideal olan popüler bir tasarım aracıdır. Ayrıca, kullanıcı arayüzleri, simgeler ve web düzenleri oluşturmak gibi görevler için tasarımcılar tarafından da yaygın olarak kullanılır.
Adobe XD : Bu, UI/UX tasarımı için vektör tabanlı bir tasarım ve prototipleme aracıdır ve Photoshop, Illustrator ve After Effects gibi diğer Adobe uygulamalarıyla sorunsuz entegrasyonuyla bilinir.
Canva : Bu araç, posterler, kapak fotoğrafları, sunumlar, kısa videolar ve daha fazlasını içeren çok çeşitli görsel içerik oluşturmanıza olanak tanır. Kullanıcı dostu ve basit tasarımı, onu yeni başlayanlar için ideal hale getirir.
Mutlak Birimler
px(Piksel) : Bu mutlak birim, CSS'de boyutlar üzerinde hassas kontrol sağlayan sabit boyutlu bir ölçü birimidir. Bu, 1 pikselin her zaman inçin 1/96'sına eşit olduğu anlamına gelir.
in(İnç) : Bu mutlak birim 96 piksele eşittir.
cm(Santimetre) : Bu mutlak birim, bir inçin 25,2/64'üne eşittir.
mm(Milimetre) : Bu mutlak birim, bir santimetrenin 1/10'una eşittir.
q(Çeyrek Milimetre) : Bu mutlak birim, bir santimetrenin 1/40'ına eşittir.
pc(Pika) : Bu mutlak birim, inçin 1/6'sına eşittir.
pt(Puan) : Bu mutlak birim, inçin 1/72'sine eşittir.
Göreceli Birimler
Yüzdeler : Bu göreceli birimler, boyutları, ölçüleri ve diğer özellikleri üst öğelerinin bir oranı olarak tanımlamanıza olanak tanır. Örneğin, width: 50%;bir öğeye yüzde değeri atarsanız, üst kapsayıcısının genişliğinin yarısını kaplayacaktır.
emBirimems : Bu birimler, öğenin yazı tipi boyutuna göre belirlenir. Özellik için kullanıyorsanız font-size, metnin boyutu üst öğenin yazı tipi boyutuna göre belirlenir.
remBirim : Bu birimler, kök öğenin yani htmlöğenin yazı tipi boyutuna göre belirlenir.
vhBirim : Görüntü alanının yüksekliğinin %1'ini vhtemsil eder "viewport height"ve ona eşittir.1vh
vwBirim : Görüntü alanının genişliğinin %1'ini vwtemsil eder "viewport width"ve ona eşittir.1vw
calcİşlev
calc()Fonksiyon : Bu fonksiyon sayesinde calc(), özellik değerlerini dinamik olarak belirlemek için doğrudan stil sayfalarınızda hesaplamalar yapabilirsiniz. Bu, görünüm alanı boyutuna veya diğer öğelere bağlı olarak boyutları hesaplayarak esnek ve duyarlı kullanıcı arayüzleri oluşturabileceğiniz anlamına gelir.
Kullanıcı Eylemi Sözde Sınıfları
Sözde Sınıfların Tanımı : Bunlar, bir öğeyi belirli durumuna veya konumuna göre seçmenize olanak tanıyan özel CSS anahtar kelimeleridir.
Kullanıcı Eylemi Sözde Sınıfları : Bunlar, kullanıcı etkileşimlerine bağlı olarak öğelerin görünümünü değiştirmenize ve genel kullanıcı deneyimini iyileştirmenize olanak tanıyan özel anahtar kelimelerdir.
:activeSözde sınıf : Bu sözde sınıf, bir öğenin etkin durumunu seçmenize olanak tanır; örneğin bir düğmeye tıklamak gibi.
:hoverSözde sınıf : Bu sözde sınıf, bir öğenin üzerine gelme durumunu tanımlar.
:focusSözde sınıf : Bu sözde sınıf, bir öğe odak kazandığında (genellikle klavye navigasyonu yoluyla veya kullanıcı bir form giriş alanına tıkladığında) stilleri uygular.
:focus-withinSözde sınıf : Bu sözde sınıf, bir öğeye veya onun alt öğelerinden herhangi birine odaklanıldığında stil uygulamak için kullanılır.
Giriş Sözde Sınıfları
Giriş Sözde Sınıflarıinput : Bu sözde sınıflar , kullanıcı etkileşiminden önce ve sonra bulundukları duruma göre HTML öğelerini hedeflemek için kullanılır .
:enabledSözde sınıf : Bu sözde sınıf, şu anda etkin olan form düğmelerini veya diğer öğeleri hedeflemek için kullanılır.
:disabledSözde sınıf : Bu sözde sınıf, etkileşimli bir öğeyi devre dışı bırakılmış modda biçimlendirmenizi sağlar.
:checkedSözde sınıf : Bu sözde sınıf, kullanıcının işaretli olduğunu anlamasını sağlamak için kullanılır.
:validSözde sınıf : Bu sözde sınıf, doğrulama kriterlerini karşılayan giriş alanlarını hedef alır.
:invalidSözde sınıf : Bu sözde sınıf, doğrulama kriterlerini karşılamayan giriş alanlarını hedef alır.
:in-rangeve :out-of-rangeSözde Sınıflar : Bu sözde sınıflar, değerlerinin belirtilen aralık kısıtlamaları içinde veya dışında olmasına bağlı olarak öğelere stil uygular.
:requiredSözde sınıf : Bu sözde sınıf, ilgili özniteliğe inputsahip öğeleri hedef alır required. Kullanıcıya formu göndermek için ilgili alanı doldurması gerektiğini bildirir.
:optionalSözde sınıf : Bu sözde sınıf, zorunlu olmayan ve boş bırakılabilen giriş öğelerine stil uygular.
:autofillSözde sınıf : Bu sözde sınıf, tarayıcının kaydedilmiş verilerle otomatik olarak doldurduğu giriş alanlarına stiller uygular.
Konum Sahte Sınıfları
Konum Sözde Sınıfları : Bu sözde sınıflar, geçerli belge içindeki bağlantıları ve öğeleri biçimlendirmek için kullanılır.
:any-linkSözde sınıf:link : Bu sözde sınıf , ve sözde sınıflarının birleşimidir :visited. Dolayısıyla, ziyaret edilip edilmemesine bakılmaksızın, href özniteliğine sahip herhangi bir bağlantı öğesiyle eşleşir.
:linkSözde sınıf : Bu sözde sınıf, bir web sayfasındaki henüz ziyaret edilmemiş tüm bağlantıları hedeflemenizi sağlar. Kullanıcı tıklamadan önce bağlantıları farklı şekilde biçimlendirmek için kullanabilirsiniz.
:local-linkSözde sınıf : Bu sözde sınıf, aynı belgeye işaret eden bağlantıları hedef alır. Dahili bağlantıları harici bağlantılardan ayırmak istediğinizde faydalı olabilir.
:visitedSözde sınıf : Bu sözde sınıf, kullanıcının ziyaret ettiği bir bağlantıyı hedef alır.
:targetSözde sınıf : Bu sözde sınıf, bir URL parçasının hedefi olan bir öğeye stil uygulamak için kullanılır.
Ağaç Yapısal Sözde Sınıflar
Ağaç Yapısal Sözde Sınıflar : Bu sözde sınıflar, öğeleri belge ağacındaki konumlarına göre hedeflemenize ve biçimlendirmenize olanak tanır.
:rootSözde sınıf : Bu sözde sınıf genellikle kök htmlöğedir. Belgedeki en üst seviyeyi hedeflemenize ve böylece tüm belgeye ortak bir stil uygulamanıza yardımcı olur. 
:emptySözde sınıf : Boş öğeler, yani boşluktan başka çocuğu olmayan öğeler de belge ağacına dahil edilir. Bu nedenle :emptyboş öğeleri hedeflemek için bir sözde sınıf vardır.
:nth-child(n)Sözde sınıf : Bu sözde sınıf, öğeleri bir üst öğe içindeki konumlarına göre seçmenize olanak tanır.
:nth-last-child(n)Sözde sınıf : Bu sözde sınıf, sondan sayarak öğeleri seçmenizi sağlar.
:first-childSözde sınıf : Bu sözde sınıf, üst öğedeki veya belgedeki ilk öğeyi seçer.
:last-childSözde sınıf : Bu sözde sınıf, üst öğedeki veya belgedeki son öğeyi seçer.
:only-childSözde sınıf : Bu sözde sınıf, üst öğedeki veya belgedeki tek öğeyi seçer.
:first-of-typeSözde sınıf : Bu sözde sınıf, üst öğesi içindeki belirli bir öğe türünün ilk örneğini seçer.
:last-of-typeSözde sınıf : Bu sözde sınıf, üst öğesi içindeki belirli bir öğe türünün son geçtiği yeri seçer.
:nth-of-type(n)Sözde sınıf : Bu sözde sınıf, aynı türdeki kardeş öğeler arasındaki konumuna bağlı olarak, üst öğesi içindeki belirli bir öğeyi seçmenize olanak tanır.
:only-of-typeSözde sınıf : Bu sözde sınıf, bir öğenin ebeveyni içinde o türden tek öğe olması durumunda o öğeyi seçer.
Fonksiyonel Sözde Sınıflar
Fonksiyonel Sözde Sınıflar : Fonksiyonel sözde sınıflar, daha karmaşık koşullara veya ilişkilere bağlı olarak öğeleri seçmenize olanak tanır. Bir duruma (örneğin, :hover, :focus) bağlı olarak öğeleri hedefleyen normal sözde sınıfların aksine, fonksiyonel sözde sınıflar argümanları kabul eder.
:is()Sözde sınıf : Bu sözde sınıf, bir seçici listesi (örneğin, ol, ul) alır ve listedeki seçicilerden biriyle eşleşen bir öğeyi seçer.
:where()Sözde sınıf : Bu sözde sınıf, bir seçici listesi (örneğin, ol, ul) alır ve listedeki seçicilerden biriyle eşleşen bir öğeyi seçer. :isve arasındaki fark :where, ikincisinin özgüllüğünün 0 olmasıdır.
:has()Sözde sınıf : Bu sözde sınıf genellikle seçici olarak adlandırılır "parent"çünkü seçici listesinde belirtilen alt öğeleri içeren öğeleri biçimlendirmenize olanak tanır.
Sahte öğeler
::beforeSözde öğe : Bu sözde öğe, contentöğenin hemen önüne simgeler gibi görsel içerik eklemek için özelliği kullanır.
::afterSözde öğe : Bu sözde öğe, contentöğenin hemen ardından simgeler gibi görsel içerik eklemek için özelliği kullanır.
::first-letterSözde öğe : Bu sözde öğe, bir öğenin içeriğinin ilk harfini hedefleyerek ona stil vermenizi sağlar.
::markerSözde öğe : Bu sözde öğe, liste öğelerinin stilini belirlemek için işaretleyici (madde işareti veya numaralandırma) seçmenize olanak tanır.
Renk Teorisi
Renk Teorisi Tanımı : Bu, renklerin birbirleriyle nasıl etkileşimde bulunduğunu ve algımızı nasıl etkilediğini inceleyen bilim dalıdır. Renk ilişkilerini, renk uyumunu ve rengin psikolojik etkisini kapsar.
Ana Renkler : Sarı, mavi ve kırmızı olan bu renkler, diğer tüm renklerin türetildiği temel tonlardır.
İkincil Renkler : Bu renkler, iki ana rengin eşit miktarlarda karıştırılmasıyla elde edilir. Yeşil, turuncu ve mor, ikincil renklere örneklerdir.
Üçüncül Renkler : Bu renkler, birincil bir rengin komşu bir ikincil renkle birleştirilmesiyle elde edilir. Sarı-yeşil, mavi-yeşil ve mavi-mor, üçüncül renklere örneklerdir.
Sıcak Renkler : Kırmızı, turuncu ve sarı gibi renkler rahatlık, sıcaklık ve huzur duyguları uyandırır.
Soğuk Renkler : Mavi, yeşil ve mor gibi renkler sakinlik, huzur ve profesyonellik duyguları uyandırır.
Renk Çemberi : Renk çemberi, renklerin birbirleriyle nasıl ilişkili olduğunu gösteren dairesel bir şemadır. Tasarımcılar için renk kombinasyonlarını seçmelerine yardımcı olduğu için önemli bir araçtır.
Benzer Renk Şemaları : Bu renk şemaları, uyumlu ve sakinleştirici deneyimler yaratır. Renk çemberinde birbirine bitişik olan benzer renkleri içerirler.
Tamamlayıcı Renk Şemaları : Bu renk şemaları yüksek kontrast ve görsel etki yaratır. Renkleri, birbirlerine göre renk çemberinin zıt uçlarında yer alır.
Üçlü Renk Şeması : Bu renk şeması canlı renklere sahiptir. Renkler, birbirlerinden yaklaşık olarak eşit uzaklıkta olan renklerden oluşur. Birbirlerine bağlandıklarında, renk çemberinde eşkenar üçgen oluştururlar.
Tek Renkli Renk Şeması : Bu renk şemasında, tüm renkler aynı temel renkten, açıklık, koyuluk ve doygunluk ayarları yapılarak elde edilir. Bu, kontrast yaratırken aynı zamanda birlik ve uyum duygusu uyandırır.
CSS'te Renklerle Çalışmanın Farklı Yolları
Adlandırılmış Renkler : Bu renkler, tarayıcılar tarafından tanınan önceden tanımlanmış renk adlarıdır. Örnekler arasında blue, darkred, bulunur lightgreen.
rgb()Fonksiyon : RGB, ışığın ana renkleri olan Kırmızı, Yeşil ve Mavi'nin kısaltmasıdır. Bu üç renk, geniş bir renk yelpazesi oluşturmak için farklı yoğunluklarda birleştirilir. Bu rgb()fonksiyon, RGB renk modelini kullanarak renkleri tanımlamanıza olanak tanır.
rgba()Fonksiyon : Bu fonksiyon, rengin saydamlığını kontrol eden dördüncü bir değer olan alfa değerini ekler.
hsl()İşlev : HSL, Renk Tonu, Doygunluk ve Parlaklık anlamına gelir; bunlar bir rengi tanımlayan üç temel bileşendir.
hsla()Fonksiyon : Bu fonksiyon, rengin saydamlığını kontrol eden dördüncü bir değer olan alfa değerini ekler.
Onaltılık (Hexadecimal ): Onaltılık kod (hexadecimal code'un kısaltması), RGB renk modelinde renkleri temsil etmek için kullanılan altı karakterlik bir dizedir. "Hex" terimi, 0'dan 9'a kadar rakamlar ve A'dan F'ye kadar harfler kullanan 16 tabanlı sayı sistemini ifade eder.
box-shadowMülk
Tanım : Bu box-shadowözellik, bir öğenin etrafına bir veya daha fazla gölge uygular.
Ofset Değerlerioffset-x : Yatay ( ) ve dikey ( offset-y) değerler belirtmelisiniz . Pozitif değerler offset-xgölgeyi sağa, negatif değerler ise sola doğru hareket ettirir. Pozitif değerler offset-ygölgeyi aşağı, negatif değerler ise yukarı doğru hareket ettirir. Değer ise 0, birim belirtmenize gerek yoktur.
Bulanıklık Yarıçapı : Bu isteğe bağlı değer, gölgenin ne kadar bulanık görüneceğini kontrol eder. Dahil edilmezse, varsayılan değer 0keskin kenarlar oluşturan 0 olur. Değer ne kadar yüksek olursa, gölge o kadar yumuşak olur.
Yayılma Yarıçapı : Bu isteğe bağlı değer, gölgenin ne kadar genişleyeceğini veya daralacağını kontrol eder. Dahil edilmezse, varsayılan değer boş bırakılır 0.
Gölge Rengi : Rengi adlandırılmış renkler, onaltılık rgb()değerler veya fonksiyonlar kullanarak belirtebilirsiniz .rgba()hsl()hsla()
insetAnahtar Kelime : Bu insetanahtar kelimeyi eklemek, gölgeyi öğenin dışına değil, içine yerleştirir.
Birden Çok Kutu Gölgesi Uygulama : Gölgeleri virgülle ayırarak birden çok gölge uygulayabilirsiniz. Gölgeler önden arkaya doğru katmanlanır.
Sözdizimi
box-shadow: offset-x offset-y blur-radius spread-radius color;
<div class="shadow-box">Shadow Example</div>

<style>
.shadow-box {
  width: 200px;
  padding: 20px;
  margin: 20px;
  background-color: lightblue;
  text-align: center;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.4);
}
</style>
Doğrusal ve Radyal Gradyanlar
Doğrusal Gradyanlar : Bu gradyanlar, düz bir çizgi boyunca renkler arasında kademeli bir geçiş oluşturur. Bu çizginin yönünü ve kullanılan renkleri kontrol edebilirsiniz.
Radyal Gradyanlar : Bu gradyanlar, merkezi bir noktadan yayılan dairesel veya elips şeklinde gradyanlar oluşturur.
Stil Girişleri İçin En İyi Uygulamalar
Giriş Alanlarının Stillendirilmesi : Tüm metin öğelerinde olduğu gibi, metin giriş alanlarına uyguladığınız stillerin erişilebilir olduğundan emin olmalısınız. Bu, yazı tipinin yeterli boyutta olması ve rengin arka planla yeterli kontrast oluşturması gerektiği anlamına gelir. Giriş öğeleri ayrıca odaklanabilir özelliktedir. Stillerinizi düzenlerken, öğenin odaklandığını gösteren belirgin bir göstergeyi (örneğin kalın bir kenarlık) korumaya özen göstermelisiniz.
appearance: noneGirişler için kullanılıyor
appearance: noneTarayıcılar birçok öğeye varsayılan stil uygular. appearance: noneCSS özelliği size stil üzerinde tam kontrol sağlar, ancak bazı sakıncaları da beraberinde getirir. Giriş öğeleri için özel stiller oluştururken, odaklanma ve hata göstergelerinin hala mevcut olduğundan emin olmanız gerekir.
Stil datetime-localve colorÖzelliklerle İlgili Sık Karşılaşılan Sorunlar
Sık Karşılaşılan Sorunlar : Bu özel giriş türleri, tarih ve renk seçiciler gibi öğeler oluşturmak için karmaşık sözde öğelere dayanır. Bu, bu girişlerin stillendirilmesi için önemli bir zorluk teşkil eder. Zorluklardan biri, varsayılan stilin tamamen tarayıcıya bağlı olmasıdır; bu nedenle, seçicinin istediğiniz gibi görünmesini sağlamak için yazdığınız CSS, başka bir tarayıcıda tamamen farklı olabilir.
CSS Taşma Özelliği
Tanım : Taşma (overflow), öğelerin, kapsayıcı öğenin boyutunu aşan veya "taşan" içeriği ele alma biçimini ifade eder. Taşma iki boyutludur.
overflow-xX ekseni yatay taşmayı belirler.
overflow-yY ekseni dikey taşmayı belirler.
CSS Dönüştürme Özelliği
Tanım : Bu özellik, öğelere 2 boyutlu veya 3 boyutlu uzayda döndürme, ölçeklendirme, eğme veya öteleme (hareket ettirme) gibi çeşitli dönüşümler uygulamanıza olanak tanır.
translate()Fonksiyon : Bu fonksiyon, bir öğeyi mevcut konumundan hareket ettirmek için kullanılır.
scale()Fonksiyon : Bu fonksiyon, bir öğenin boyutunu değiştirmenize olanak tanır.
Dönüşümler ve Erişilebilirlik : İçeriği gizlemek veya göstermek için dönüşüm kullanıyorsanız, içeriğin ekran okuyucular ve klavye navigasyonu için hala erişilebilir olduğundan emin olun. Gizlenen içerik, yalnızca görsel olarak ekrandan çıkarılmak yerine, display: noneveya gibi yöntemler kullanılarak gerçekten gizlenmelidir.visibility: hidden
Kutu Modeli
Tanım : CSS kutu modelinde, her öğe bir kutu ile çevrilidir. Bu kutu dört bileşenden oluşur: içerik alanı, `<div>` padding, ` border<div>`, `<div> margin`.
İçerik Alanı : İçerik alanı, kutunun en iç kısmıdır. Metin veya resim gibi bir öğenin gerçek içeriğini barındıran alandır.
paddingDolgu (padding), içerik alanının hemen ardından gelen alandır. İçerik alanı ile bir öğenin kenarlığı arasındaki boşluktur.
borderKenarlık, CSS kutu modelinde bir öğenin dış kenarı veya dış çizgisidir. Öğenin görsel sınırıdır.
marginKenar boşluğu, bir öğenin sınırının dışındaki alandır. Bir öğe ile etrafındaki diğer öğeler arasındaki mesafeyi belirler.
Kenar Çökmesi
Tanım : Bu davranış, bitişik öğelerin dikey kenar boşluklarının üst üste gelmesi ve iki kenar boşluğundan daha büyük olanına eşit tek bir kenar boşluğu oluşması durumunda ortaya çıkar. Bu davranış yalnızca dikey kenar boşlukları (üst ve alt) için geçerlidir, yatay kenar boşlukları (sol ve sağ) için geçerli değildir.
content-boxve Gayrimenkul border-boxDeğerleri
box-sizingÖzellikwidth : Bu özellik, bir HTML öğesi için nihai ve değerlerinin nasıl heighthesaplanacağını belirlemek için kullanılır .
content-boxDeğer : Modelde content-box, bir öğe için belirlediğiniz widthve değerleri içerik alanının boyutlarını belirler, ancak , , veya heightdeğerlerini içermez .paddingbordermargin
border-boxDeğer : ile border-box, bir öğenin widthve heightözellikleri içerik alanını, paddingve öğelerini içerir border, ancak öğesini içermez margin.
CSS Sıfırlama
Tanım : CSS sıfırlama, web tarayıcılarının HTML öğelerine uyguladığı varsayılan biçimlendirmenin tamamını veya bir kısmını kaldıran bir stil sayfasıdır. CSS sıfırlama için üçüncü taraf seçenekler arasında sanitize.cssve bulunur normalize.css.
CSS Filtre Özelliği
Tanım : Bu özellik, bulanıklık, renk kaydırma ve kontrast ayarlama gibi çeşitli efektler oluşturmak için kullanılabilir.
blur()Fonksiyon : Bu fonksiyon, öğeye Gauss bulanıklığı uygular. Miktar piksel cinsinden tanımlanır ve bulanıklığın yarıçapını temsil eder.
brightness()Fonksiyon : Bu fonksiyon, öğenin parlaklığını ayarlar. %0 değeri öğeyi tamamen siyah yaparken, %100'ün üzerindeki değerler parlaklığı artırır.
grayscale()Fonksiyon : Bu fonksiyon, öğeyi gri tonlamaya dönüştürür. Oran yüzde olarak tanımlanır; %100 tamamen gri tonlama, %0 ise görüntüyü değiştirmeden bırakır.
sepia()Fonksiyon : Bu fonksiyon, öğeye sepya tonu uygular. Gri tonlama gibi, yüzde değeri kullanır.
hue-rotate()Fonksiyon : Bu fonksiyon, öğeye renk tonu döndürme işlemi uygular. Değer derece cinsinden tanımlanır ve renk çemberi etrafındaki bir döndürmeyi temsil eder.
CSS Flexbox ve Flex Modeline Giriş
Tanım : CSS flexbox, bir kapsayıcı içindeki öğeleri satır ve sütunlar halinde düzenlemenizi sağlayan tek boyutlu bir düzen modelidir.
Esnek Model : Bu model, esnek öğelerin bir esnek kapsayıcı içinde nasıl düzenleneceğini tanımlar. Her esnek kapsayıcının iki ekseni vardır: ana eksen ve çapraz eksen.
Mülkflex-direction​
Tanım : Bu özellik, ana eksenin yönünü belirler. Varsayılan değeri flex-direction, rowtüm esnek öğeleri aynı satıra, tarayıcınızın varsayılan dilinin yönünde (soldan sağa veya sağdan sola) yerleştirir.
flex-direction: row-reverse;Bu, satırdaki öğelerin sırasını değiştirir.
flex-direction: column;Bu işlem, esnek öğeleri yatay yerine dikey olarak hizalayacaktır.
flex-direction: column-reverse;Bu, esnek öğelerin dikey sırasını tersine çevirir.
Mülkflex-wrap​
Tanım : Bu özellik, esnek öğelerin mevcut alana sığacak şekilde esnek bir kapsayıcı içinde nasıl sarılacağını belirler. flex-wrapÜç olası değer alabilir: nowrap, wrap, ve wrap-reverse.
flex-wrap: nowrap;Bu varsayılan değerdir. Esnek öğeler, genişlikleri kapsayıcının genişliğini aşsa bile yeni bir satıra geçirilmez.
flex-wrap: wrap;Bu özellik, öğeler bulundukları kabın genişliğini aştığında onları sarmalayacaktır.
flex-wrap: wrap-reverse;Bu özellik, esnek öğeleri ters sırada sarmalayacaktır.
flex-flowÖzellikflex-direction : Bu özellik, ve için kısaltılmış bir özelliktir flex-wrap.
Mülkjustify-content​
Tanım : Bu özellik, alt öğeleri esnek kapsayıcının ana ekseni boyunca hizalar.
justify-content: flex-start;Bu durumda, esnek öğeler ana eksenin başlangıcına hizalanacaktır. Bu, yatay veya dikey olabilir.
justify-content: flex-end;Bu durumda, esnek elemanlar ana eksenin ucuna yatay veya dikey olarak hizalanır.
justify-content: center;Bu, esnek öğeleri ana eksen boyunca ortalar.
justify-content: space-between;Bu işlem, elemanları ana eksen boyunca eşit olarak dağıtacaktır.
justify-content: space-around;Bu işlem, esnek öğeleri ana eksen içinde eşit olarak dağıtacak ve ilk öğeden önce ve son öğeden sonra bir boşluk ekleyecektir.
justify-content: space-evenly;Bu işlem, öğeleri ana eksen boyunca eşit olarak dağıtır.
Mülkalign-items​
Tanım : Bu özellik, öğeleri çapraz eksen boyunca dağıtmak için kullanılır. Çapraz eksenin ana eksene dik olduğunu unutmayın.
align-items: center;Bu, öğeleri çapraz eksen boyunca ortalamak için kullanılır.
align-items: flex-start;Bu, öğeleri çapraz eksenin başlangıç ​​noktasına hizalar.
align-items: stretch;Bu, esnek parçaları çapraz eksen boyunca germek için kullanılır.
Tipografiye Giriş
Tanım : Tipografi, metni görsel olarak çekici ve okunması kolay hale getirmek için doğru yazı tiplerini ve biçimini seçme sanatıdır. "Tip", tek tek karakterlerin nasıl tasarlandığını ve düzenlendiğini ifade eder.

Yazı Tipi Tanımı : Yazı tipi, bir karakter, sayı ve sembol kümesinin genel tasarımı ve stilidir. Bir yazı tipi ailesinin taslağı gibidir.

Yazı Tipi Tanımı : Yazı tipi, boyut, kalınlık, stil ve genişlik gibi belirli özelliklere sahip bir yazı karakterinin özel bir varyasyonudur.

Serif Yazı Tipi : Bu yazı tipi, karakterlerin sonunda küçük çizgiler bulunan klasik bir stile sahiptir. Serif yazı tipleri genellikle kitap gibi basılı materyallerde kullanılır.

Sans Serif Yazı Tipi : Bu yazı tipi, karakterlerin sonundaki küçük çizgiler olmadan daha modern bir görünüme sahiptir. Sans Serif yazı tipleri, ekranda okunması kolay oldukları için dijital tasarımda yaygın olarak kullanılır. Helvetica, Arial ve Roboto gibi yazı tipleri buna örnek verilebilir.

Yazı Tipi Kalınlığı : Bu, karakterlerin kalınlığını ifade eder ve açık, normal, kalın ve siyah seçenekleri içerir.

Yazı Tipi Stili : Bu, karakterlerin eğimi ve yönüdür; örneğin italik ve eğik yazı tipi gibi.

Yazı Tipi Genişliği : Bu, karakterlerin yatay olarak kapladığı alandır; örneğin daraltılmış ve genişletilmiş yazı tipleri gibi.

Temel çizgi : Bu, karakterlerin çoğunun üzerinde durduğu hayali çizgidir.

Büyük Harf Yüksekliği : Bu, büyük harflerin taban çizgisinden tepesine kadar ölçülen yüksekliğidir.

X-yüksekliği : Bu, üst ve alt uzantılar hariç, küçük harflerin ortalama yüksekliğidir.

Yükselen uzantılar : Bunlar, küçük harflerin x yüksekliğinin üzerine uzanan kısımlarıdır; örneğin 'h', 'b', 'd' ve 'f' harflerinin üst kısımları.

Alt uzantılar : Bunlar, küçük harflerin taban çizgisinin altına uzanan kısımlarıdır; örneğin 'y', 'g', 'p' ve 'q' harflerinin kuyrukları.

Harf aralığı ayarı (Kerning) : Bu, okunabilirliği ve estetiği iyileştirmek için belirli karakter çiftleri arasındaki boşluğun nasıl ayarlandığıdır. Örneğin, A ve V harfleri arasındaki boşluğun azaltılması.

Karakter Aralığı : Bu, bir metin bloğundaki tüm karakterler arasındaki boşluğun nasıl ayarlandığını belirler. Esasen karakterler arasındaki mesafedir. Metnin ne kadar yoğun ve açık olacağını etkiler.

Satır Aralığı : Bu, metin satırları arasındaki dikey boşluktur. Bir satırın taban çizgisinden bir sonraki satırın taban çizgisine kadar ölçülür.

Tipografiyle İlgili En İyi Uygulamalar : Tasarımlarınızın anlaşılmasını kolaylaştırmak için net ve basit yazı tipleri seçmelisiniz. Bu, özellikle web sitenizin ana metni için önemlidir. Yazı tipi kolay okunabilirse, kullanıcıların içeriğinizle etkileşime girme olasılığı daha yüksektir. Görsel tutarlılık oluşturmak için en fazla iki veya üç yazı tipi kullanmalısınız. Çok fazla yazı tipi kullanmak, metni okumayı zorlaştırabilir ve markanızın kimliğini zayıflatabilir. Bu ayrıca web sitesinin yüklenme süresini artırarak kullanıcı deneyimini de etkileyebilir. Başlıklar, alt başlıklar, paragraflar ve diğer öğeler için görsel bir hiyerarşi oluşturmak için yazı tipi boyutunu kullanabilirsiniz. Örneğin, bir web sayfasındaki ana başlık daha büyük bir yazı tipine sahip olmalı, ardından daha küçük yazı tipi boyutlarına sahip alt başlıklar gelmelidir. Bu, hiyerarşideki her öğeye, kullanıcıların yapıda görsel olarak gezinmesine yardımcı olan belirli bir yazı tipi boyutu verecektir.

CSS font-familyÖzelliği
Tanım : Bir yazı tipi ailesi, ortak bir tasarıma sahip yazı tipleri grubudur. Aynı aileye ait tüm yazı tipleri aynı temel yazı tipine dayanır, ancak stil, kalınlık ve genişlik açısından da farklılıklar gösterirler. Birden fazla yazı tipi ailesini, en yüksekten en düşüğe doğru öncelik sırasına göre virgülle ayırarak belirtebilirsiniz. Bu alternatif yazı tipleri, yedek seçenekler olarak işlev görecektir. Yazı tipi ailesi listesinin sonuna her zaman genel bir yazı tipi ailesi eklemelisiniz.
Yaygın Yazı Tipi Aileleri : İşte CSS'de kullanılan bazı yaygın yazı tipi aileleri: serif, sans-serif, monospace, cursive, fantasy
Web Güvenli Yazı Tipleri
Tanım : Bu yazı tipleri, bir bilgisayarda veya cihazda yüklü olma olasılığı çok yüksek olan yazı tiplerinin bir alt kümesidir. Tarayıcı bir yazı tipini işlemek zorunda kaldığında, kullanıcının sisteminde yazı tipi dosyasını bulmaya çalışır. Ancak yazı tipi bulunamazsa, genellikle varsayılan sistem yazı tipine geri döner.

Web Güvenli Yazı Tipleri :

Sans-serif yazı tipleri, karakterlerin sonunda küçük "ayaklar" veya çizgiler bulunmadığı için ekranda okunması kolay olduğundan web geliştirme alanında yaygın olarak kullanılır. Web için güvenli sans-serif yazı tiplerine örnek olarak Arial, Verdana ve Trebuchet MS verilebilir.
Buna karşılık, serif yazı tiplerinin karakterlerin sonunda küçük "ayakları" vardır, bu nedenle genellikle geleneksel baskıda kullanılırlar. Web için güvenli serif yazı tipleri şunlardır: Times New Roman ve Georgia.
At kuralları ve @font-faceAt kuralı
Tanım : `@` kuralları, tarayıcıya talimatlar veren ifadelerdir. Bunları, medya sorguları, anahtar kareler, yazı tipleri ve daha fazlası gibi stil sayfasının çeşitli yönlerini tanımlamak için kullanabilirsiniz.
@font-faceBu, yazı tipi dosyasını, biçimini ve ağırlık ve stil gibi diğer önemli özellikleri belirterek özel bir yazı tipi tanımlamanıza olanak tanır. Kuralın @font-facegeçerli olması için özelliği de belirtmeniz gerekir src. Bu özellik, yazı tipi kaynaklarına referanslar içerir.
Yazı Tipi Biçimleri : Her yazı tipi kaynağı için biçimi de belirtebilirsiniz. Bu isteğe bağlıdır. Tarayıcıya yazı tipi biçimi hakkında bir ipucu verir. Biçim belirtilmezse, kaynak indirilir ve indirildikten sonra biçim algılanır. Biçim geçersizse, kaynak indirilmez. Olası yazı tipi biçimleri şunlardır collection: embedded-opentype, opentype, svg, truetype, woff, ve woff2.
woffvewoff2 : woff"Web Açık Yazı Tipi Formatı" anlamına gelir. Mozilla tarafından Type Supply, LettError ve diğer kuruluşlarla işbirliği içinde geliştirilen, yaygın olarak kullanılan bir yazı tipi formatıdır. woffve arasındaki fark, woff2verileri sıkıştırmak için kullanılan algoritmadır.
OpenType : Microsoft ve Adobe tarafından geliştirilen, ölçeklenebilir bilgisayar yazı tipleri için bir formattır ve kullanıcıların bir yazı tipindeki ek özelliklere erişmesine olanak tanır. Başlıca işletim sistemlerinde yaygın olarak kullanılır.
tech()Bu, yazı tipi kaynağının teknolojisini belirtmek için kullanılır. İsteğe bağlıdır.
Harici Yazı Tipleriyle Çalışmak
Tanım : Harici yazı tipi, proje dosyalarınıza doğrudan dahil edilmeyen bir yazı tipi dosyasıdır. Genellikle ayrı bir sunucuda barındırılırlar. Bu harici yazı tiplerini projenize dahil etmek için CSS'nizde bir link`<font>` öğesi veya ` <font>` ifadesi kullanabilirsiniz .@import
Google Fonts : Bu, Google'ın sunduğu ve çoğu özellikle web geliştirme için tasarlanmış yazı tiplerinden oluşan bir koleksiyondur.
Font Squirrel : Bu, projelerinize özel harici yazı tipleri eklemek için kullanabileceğiniz bir diğer popüler kaynaktır.
text-shadowMülk
Tanım : Bu özellik metne gölge uygulamak için kullanılır. Gölgenin metinden yatay ve dikey mesafesini temsil eden X ve Y ofset değerlerini belirtmeniz gerekir. Bu değerler zorunludur. X ofsetinin pozitif değerleri gölgeyi sırasıyla sağa ve aşağıya doğru hareket ettirirken, negatif değerler gölgeyi sola ve yukarıya doğru hareket ettirir.
Gölge Rengi : Bu değeri ofsetten önce veya sonra belirterek gölgenin rengini de özelleştirebilirsiniz. Renk belirtilmezse, tarayıcı rengi otomatik olarak belirleyecektir, bu nedenle genellikle açıkça belirtmek en iyisidir.
Bulanıklık Yarıçapı : Bulanıklık yarıçapı isteğe bağlıdır ancak gölgenin çok daha pürüzsüz ve daha incelikli görünmesini sağlar. Bulanıklık yarıçapının varsayılan değeri sıfırdır. Değer ne kadar yüksek olursa, bulanıklık o kadar büyük olur, bu da gölgenin daha açık hale gelmesi anlamına gelir.
Birden Fazla Metin Gölgesi Uygulama : Metnin birden fazla gölgesi olabilir. Gölgeler, önden arkaya doğru, ilk gölge en üstte olacak şekilde katmanlar halinde uygulanacaktır.
Renk Kontrastı Araçları
WebAIM Renk Kontrastı Denetleyicisi : Bu çevrimiçi araç, tasarımınızın ön plan ve arka plan renklerini girmenize ve bunların Web İçeriği Erişilebilirlik Yönergeleri (WCAG) standartlarına uygun olup olmadığını anında görmenize olanak tanır.
TPGi Renk Kontrastı Analiz Aracı : Bu ücretsiz renk kontrastı denetleyicisi, web sitelerinizin ve uygulamalarınızın Web İçeriği Erişilebilirlik Yönergeleri (WCAG) standartlarını karşılayıp karşılamadığını kontrol etmenizi sağlar. Bu araç ayrıca, renk körlüğü sorunu olan kişiler için web sitenizin veya uygulamanızın nasıl göründüğünü görmenizi sağlayan bir Renk Körlüğü Simülatörü özelliği de içerir.
Erişilebilirlik Ağacı
Erişilebilirlik ağacı, ekran okuyucular gibi yardımcı teknolojilerin bir web sayfasındaki içeriği yorumlamak ve onunla etkileşim kurmak için kullandığı bir yapıdır.

max()İşlev
Bu max()fonksiyon, virgülle ayrılmış değerler kümesinin en büyüğünü döndürür:

img {
  width: max(250px, 25vw);
}
Yukarıdaki örnekte, görüntü alanı genişliği 1000 pikselden az ise resmin genişliği 250 piksel olacaktır (çünkü 250 piksel, görüntü alanı genişliğinin %25'inden büyüktür). Görüntü alanı genişliği 1000 pikselden büyükse, resmin genişliği 25vw olacaktır. Bunun nedeni, 25vw'nin görüntü alanı genişliğinin %25'ine eşit olmasıdır.

CSS ve Erişilebilirlik ile İlgili En İyi Uygulamalar
display: none;Bu yöntemi kullanmak, display: none;ekran okuyucuların ve diğer yardımcı teknolojilerin bu içeriğe erişemeyeceği anlamına gelir, çünkü bu içerik erişilebilirlik ağacına dahil edilmemiştir. Bu nedenle, bu yöntemi yalnızca içeriği hem görsel sunumdan hem de erişilebilirlikten tamamen kaldırmak istediğinizde kullanmanız önemlidir.
visibility: hidden;Bu özellik ve değer, içeriği görsel olarak gizler ancak belge akışında tutar, yani sayfada yer kaplamaya devam eder. Bu öğeler, erişilebilirlik ağacından kaldırıldıkları için artık ekran okuyucular tarafından okunmayacaktır.
.sr-onlyCSS sınıfı : Bu, içeriği görsel olarak gizlerken ekran okuyucular için erişilebilirliğini korumak için kullanılan yaygın bir tekniktir.
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
placeholderÖzelliğin Erişilebilirlik Sorunu
Yer tutucu metin kullanmak erişilebilirlik açısından pek iyi değil. Kullanıcılar çok sık yer tutucu metni gerçek bir giriş değeriyle karıştırıyorlar; giriş alanında zaten bir değer olduğunu düşünüyorlar.

Farklı Nitelik Seçiciler ve Bağlantılarla Çalışmak
Tanım : Seçici, `<title>` veya ` <title> attribute` gibi özniteliklerine göre HTML öğelerini hedeflemenizi sağlar .hreftitle
titleÖzellik : Bu özellik, bir öğe hakkında ek bilgi sağlar.
lang" and" data-langözniteliğiyle öğeleri hedefleme
langÖznitelik : Bu öznitelik, HTML'de bir öğenin içeriğinin dilini belirtmek için kullanılır. Özellikle çok dilli bir web sitesinde, öğeleri yazıldıkları dile göre farklı şekilde biçimlendirmek isteyebilirsiniz.
data-langÖzellik : Özellik gibi özel veri özellikleri, data-langmetnin belirli bir bölümünde kullanılan dili belirtmek gibi, öğelerde ek bilgiler depolamak için yaygın olarak kullanılır.
Öznitelik Seçici, Sıralı Liste Öğeleri ve typeÖznitelik ile Çalışmak
typeÖznitelik : HTML'de sıralı listelerle çalışırken, bu typeöznitelik sayısal, alfabetik veya Roma rakamları gibi kullanılan numaralandırma stilini belirtmenize olanak tanır.
Şamandıralarla Çalışmak
Tanım : Float özelliği, bir öğeyi sayfadaki normal akışından çıkarıp, kapsayıcısının sol veya sağ tarafına konumlandırmak için kullanılır. Bu gerçekleştiğinde, metin float özelliğiyle çevrelenmiş şekilde satır sonuna sarılır.
Kaydırma Öğelerini Temizleme : Bu clearözellik, bir öğenin kaydırılmış içeriğin altına taşınması gerekip gerekmediğini belirlemek için kullanılır. Birbirine bitişik birden fazla kaydırılmış öğeniz olduğunda, düzenlerde çakışma ve daralma sorunları olabilir. Bu nedenle, clearfixbu sorunu çözmek için bir yöntem geliştirildi.
Statik, Göreceli ve Mutlak Konumlandırma
Statik Konumlandırma : Bu, belgenin normal akışıdır. Öğeler yukarıdan aşağıya ve soldan sağa doğru birbiri ardına konumlandırılır.
Göreceli Konumlandırmatop : Bu özellik, öğeyi normal belge akışı içinde konumlandırmak için `<position> `, left`<position>` rightve `<position>` özelliklerini kullanmanıza olanak tanır bottom. Ayrıca, öğelerin sayfadaki diğer öğelerle üst üste gelmesini sağlamak için de göreceli konumlandırma kullanabilirsiniz.
Mutlak Konumlandırma : Bu özellik, bir öğeyi normal belge akışından çıkarmanıza ve diğer öğelerden bağımsız olarak davranmasını sağlamanıza olanak tanır.
Sabit ve Yapışkan Konumlandırma
Sabit Konumlandırma : Bir öğe sabit konumlandırma ile konumlandırıldığında position: fixed, normal belge akışından çıkarılır ve görünüm alanına göre yerleştirilir; bu, kullanıcının kaydırma yapması durumunda bile aynı konumda kalacağı anlamına gelir. Bu genellikle her zaman görünür kalması gereken başlıklar veya gezinme çubukları gibi öğeler için kullanılır.
Yapışkan Konumlandırma : Bu konumlandırma türü, göreceli ve sabit konumlandırma arasında bir hibrit görevi görür. Başlangıçta, öğe belgenin akışı içinde kalarak göreceli olarak konumlandırılmış gibi davranır. Ancak, kullanıcı öğeyi belirli bir noktanın ötesine kaydırdığında, görünüm alanına (genellikle üst kısma) "yapışır" ve sabitlenmiş gibi davranır. Bu, kullanıcının belirli bir konuma kaydırdığı anda sabit hale gelen yapışkan gezinme çubukları gibi öğeler oluşturmak için idealdir.
z-indexMülkle Çalışmak
Tanım : z-indexCSS'deki bu özellik, sayfada üst üste gelen konumlandırılmış öğelerin dikey sıralama düzenini kontrol etmek için kullanılır.
Duyarlı Web Tasarımı
Tanım : Duyarlı tasarımın temel prensibi uyarlanabilirliktir; yani bir web sitesinin, görüntülendiği cihazın ekran boyutuna ve özelliklerine göre düzenini ve içeriğini ayarlayabilme yeteneğidir.
Esnek ızgaralar : Bunlar, piksel gibi sabit birimler yerine yüzde gibi göreceli birimler kullanır; bu da içeriğin ekran boyutuna göre yeniden boyutlandırılmasına ve yeniden düzenlenmesine olanak tanır.
Esnek resimler : Bunlar, içerdikleri öğeler içinde yeniden boyutlandırılacak şekilde ayarlanmıştır ve böylece daha küçük ekranlarda kapsayıcılarından taşmamaları sağlanır.
Medya Soruları
Tanım : Bu özellik, geliştiricilerin cihazın özelliklerine, özellikle de görüntü alanı genişliğine bağlı olarak farklı stiller uygulamasına olanak tanır.
allMedya Türü : Bu, tüm cihazlar için uygundur. Medya türü belirtilmediğinde varsayılan değerdir.
printMedya Türleri : Bu özellik, sayfalandırılmış materyaller ve baskı önizleme modunda ekranda görüntülenen belgeler için tasarlanmıştır.
screenMedya Türleri : Bu öncelikle ekranlar için tasarlanmıştır.
aspect-ratioBu, görüntüleme alanının genişliği ve yüksekliği arasındaki oranı tanımlar.
orientationBu, cihazın yatay mı yoksa dikey mi konumda olduğunu belirtmek için kullanılır.
resolutionBu, çıkış aygıtının çözünürlüğünü inç başına nokta (dpi) veya santimetre başına nokta (dpcm) cinsinden tanımlamak için kullanılır.
hoverBu, birincil giriş mekanizmasının öğelerin üzerine gelip gelemeyeceğini test etmek için kullanılır.
prefers-color-schemeBu, kullanıcının açık veya koyu renk teması isteyip istemediğini tespit etmek için kullanılır.
Medya Sorguları ve Mantıksal Operatörler : andOperatör, birden fazla medya özelliğini birleştirmek için kullanılırken, notve onlyoperatörleri medya sorgularını olumsuzlamak veya izole etmek için kullanılabilir.
Ortak Medya Kırılma Noktaları
Tanım : Medya kırılma noktaları, bir web sitesinin tasarımında düzenin ve içeriğin farklı ekran boyutlarına uyum sağlamak için ayarlandığı belirli noktalardır. Telefonları, tabletleri ve masaüstü ekranlarını hedeflemek için kullanabileceğiniz bazı genel kırılma noktaları vardır. Ancak farklı cihazlar için olası her ekran boyutunu tek tek takip etmeye çalışmak akıllıca değildir.
Küçük boyutlu cihazlar (akıllı telefonlar) : 640 piksele kadar
Orta Boy Cihazlar (tabletler) : 641px - 1024px
Büyük Cihazlar (masaüstü bilgisayarlar) : 1025 piksel ve üzeri
Mobil öncelikli yaklaşım
Tanım : Mobil öncelikli yaklaşım, duyarlı web tasarımında, daha büyük ekranlar için tasarım yapmadan önce web sitelerini mobil cihazlar için oluşturmaya öncelik veren bir tasarım felsefesi ve geliştirme stratejisidir.
CSS Özel Özellikleri (CSS Değişkenleri)
Tanım : CSS özel özellikleri, diğer adıyla CSS değişkenleri, CSS yazarları tarafından tanımlanan ve bir belge boyunca yeniden kullanılacak belirli değerler içeren varlıklardır. Daha verimli, bakımı kolay ve esnek stil sayfaları oluşturmaya olanak tanıyan güçlü bir özelliktir. Özel özellikler, özellikle temaya uygun tasarımlar oluşturmada kullanışlıdır. Farklı temalar için bir dizi özellik tanımlayabilirsiniz.
Kural@property​
Tanım : Bu @propertykural, geliştiricilerin animasyonları ve başlangıç ​​değerleri de dahil olmak üzere davranışları üzerinde daha fazla kontrol sahibi olarak özel özellikler tanımlamalarına olanak tanıyan güçlü bir CSS özelliğidir.
@property --property-name {
  syntax: '<type>';
  inherits: true | false;
  initial-value: <value>;
}
--property-nameBu, tanımladığınız özel özelliğin adıdır. Tüm özel özellikler gibi, iki tire ile başlamalıdır.
syntaxBu, özelliğin türünü tanımlar; bu türler <color>, <length>, <number>, <percentage>, gibi şeyler veya daha karmaşık türler olabilir.

inheritsBu, özelliğin değerini üst öğesinden miras alıp almayacağını belirtir.
initial-valueBu, özelliğin varsayılan değerini belirler.
Yedek Değerlervar() : Özel özelliği kullanırken, standart özel özelliklerde olduğu gibi, bir yedek değer sağlamak için fonksiyonu kullanabilirsiniz .
CSS Grid Temelleri
Tanım : CSS Grid, web sayfalarında karmaşık düzenler oluşturmak için kullanılan iki boyutlu bir düzen sistemidir. Izgaralar, aralarında boşluklar bulunan satır ve sütunlardan oluşur. Bir ızgara düzeni tanımlamak için, özelliği `<grid>` displayolarak ayarlamanız gerekir grid.
fr(Kesirli) Birim :fr Bu birim, ızgara kabı içindeki alanın bir kesrini temsil eder. Bu birimi esnek ızgaralar oluşturmak için kullanabilirsiniz .
CSS grid'de izler arasında boşluk oluşturmanıncolumn-gap üç yolu vardır. Sütunlar arasında boşluk oluşturmak için `<port>` özelliğini kullanabilirsiniz. Satırlar arasında boşluk oluşturmak için `<port>` özelliğini kullanabilirsiniz. Veya hem satırlar hem de sütunlar arasında boşluk oluşturmak için kısaltılmış `<port>` özelliğini row-gapkullanabilirsiniz .gap
repeat()Fonksiyon : Bu fonksiyon, parça listesindeki bölümleri tekrarlamak için kullanılır. Yazmak yerine grid-template-columns: 1fr 1fr 1fr;bu fonksiyonu kullanabilirsiniz repeat().
Açık Izgaragrid-template-columns : veya özelliklerini kullanarak satır veya iz sayısını belirtebilirsiniz grid-template-rows.
Örtük Izgara : Öğeler ızgaranın dışına yerleştirildiğinde, bu dışarıdaki öğeler için otomatik olarak satırlar ve sütunlar oluşturulur.
minmax()Fonksiyon : Bu fonksiyon, bir pist için minimum ve maksimum boyutları ayarlamak için kullanılır.
Izgara Otomatik Yerleştirme : Tarayıcı, otomatik yerleştirme algoritmasını kullanarak öğeleri otomatik olarak yerleştirir. Bu özellik, yerleştirme yönünü ve boşlukların doldurulup doldurulmayacağını etkilemek için , , veya grid-auto-flowgibi değerler kullanarak bu davranışı kontrol eder .rowcolumndense
Çizgi Tabanlı Yerleştirmegrid-column-start : Tüm ızgaraların çizgileri vardır. Öğenin bir çizgi üzerinde nerede başladığını belirtmek için ve özelliklerini kullanabilirsiniz . Öğenin çizgi üzerinde nerede bittiğini belirtmek için ve özelliklerini grid-row-startkullanabilirsiniz . Bunun yerine veya kısaltma özelliklerini de kullanmayı tercih edebilirsiniz .grid-column-endgrid-row-endgrid-columngrid-row
grid-template-areasBu özellik, ızgaraya yerleştireceğiniz öğelere ad vermek için kullanılır.
Hizalama: Öğelerin ızgara alanlarında nasıl hizalanacağını kontrol etmek için justify-itemsve komutlarını kullanın . Kapsayıcıda ayarlanan hizalamayı geçersiz kılmak için tek tek ızgara öğelerinde ve komutlarını kullanın.align-itemsjustify-selfalign-self
CSS Animasyon Temelleri
Tanım : CSS animasyonları, JavaScript veya karmaşık programlama gerektirmeden web sayfalarında dinamik, görsel olarak ilgi çekici efektler oluşturmanıza olanak tanır. Belirli bir süre boyunca öğelerin farklı stiller arasında sorunsuz bir şekilde geçiş yapmasını sağlarlar.
Kural : Bu @keyframeskural , animasyonun aşamalarını ve stillerini tanımlar. Animasyon sırasında öğenin çeşitli noktalarda hangi stillere sahip olması gerektiğini belirtir.
animationÖzellik : Bu, animasyonları uygulamak için kullanılan kısaltılmış özelliktir.
animation-name@keyframesBu, kullanılacak kural için adı belirtir .
animation-durationBu, animasyonun tamamlanmasının ne kadar süreceğini belirler.
animation-timing-functionBu, animasyonun zaman içinde nasıl ilerleyeceğini tanımlar (örneğin, yumuşak geçiş, doğrusal geçiş, yumuşak giriş-çıkış).
animation-delayBu, animasyonun başlamasından önce ne kadar süre geçmesi gerektiğini belirtir.
animation-iteration-countBu, animasyonun kaç kez tekrarlanması gerektiğini belirler.
animation-directionBu, animasyonun ileriye, geriye veya dönüşümlü olarak oynatılıp oynatılmayacağını belirler.
animation-fill-modeBu, öğenin animasyondan önce ve sonra nasıl biçimlendirilmesi gerektiğini belirtir.
animation-play-stateBu özellik, animasyonu duraklatmanıza ve devam ettirmenize olanak tanır.
Erişilebilirlik ve prefers-reduced-motionMedya Sorgusu
Medya prefers-reduced-motionSorgusu : Animasyonlarla ilgili temel erişilebilirlik endişelerinden biri, bazı kullanıcılara rahatsızlık hatta fiziksel zarar verebilmeleridir. Vestibüler bozuklukları veya hareket hassasiyeti olan kişiler, ekrandaki belirli hareket türlerine maruz kaldıklarında baş dönmesi, mide bulantısı veya baş ağrısı yaşayabilirler. Medya prefers-reduced-motionsorgusu, web geliştiricilerinin kullanıcının sistem düzeyinde minimum animasyon veya hareket efektleri talep edip etmediğini tespit etmelerini sağlar.