CSS Sözde Sınıfları İncelemesi
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
<link rel="stylesheet" href="styles.css" />

<p class="example">This text will change color.</p>
<p>This text will not change color.</p>
<p>This text will not change color.</p>
<p class="this-works-too">This text will change color.</p>
p:is(.example, .this-works-too) {
    color: red;
}
:where()Sözde sınıf : Bu sözde sınıf, bir seçici listesi (örneğin, ol, ul) alır ve listedeki seçicilerden biriyle eşleşen bir öğeyi seçer. :isve arasındaki fark :where, ikincisinin özgüllüğünün 0 olmasıdır.
:where(h1, h2, h3) {
    margin: 0;
    padding: 0;
}
:has()Sözde sınıf : Bu sözde sınıf genellikle seçici olarak adlandırılır "parent"çünkü seçici listesinde belirtilen alt öğeleri içeren öğeleri biçimlendirmenize olanak tanır.
article:has(h2) {
    border: 2px solid hotpink;
}
:not()Sözde sınıf : Bu sözde sınıf, sağlanan seçiciyle eşleşmeyen öğeleri seçmek için kullanılır.
p:not(.example) {
  color: blue;
}
Sahte öğeler
::beforeSözde öğe : Bu sözde öğe, contentöğenin hemen önüne simgeler gibi görsel içerik eklemek için özelliği kullanır.
::afterSözde öğe : Bu sözde öğe, contentöğenin hemen ardından simgeler gibi görsel içerik eklemek için özelliği kullanır.
::first-letterSözde öğe : Bu sözde öğe, bir öğenin içeriğinin ilk harfini hedefleyerek ona stil vermenizi sağlar.
::markerSözde öğe : Bu sözde öğe, liste öğelerinin stilini belirlemek için işaretleyici (madde işareti veya numaralandırma) seçmenize olanak tanır.