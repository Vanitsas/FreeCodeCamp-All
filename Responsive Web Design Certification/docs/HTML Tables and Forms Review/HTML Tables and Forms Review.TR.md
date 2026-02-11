HTML Tabloları ve Formları İncelemesi
HTML Form Elemanları ve Nitelikleri
form`<form>` öğesi : Kullanıcıdan girdi almak için HTML formu oluşturmak amacıyla kullanılır.
actionÖzellik : Form verilerinin gönderileceği URL'yi belirtmek için kullanılır.
methodÖznitelik : Form verilerini gönderirken kullanılacak HTTP yöntemini belirtmek için kullanılır. En yaygın yöntemler GETve yöntemleridir POST.
Örnek Kod
<form method="value-goes-here" action="url-goes-here">
  <!-- inputs go inside here -->
</form>
inputelement : Kullanıcı girişi için bir giriş alanı oluşturmak için kullanılır.
typeÖzellik : Giriş alanının türünü belirtmek için kullanılır. Örnek: text, email, number, radio, checkbox, vb.
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
Örnek Kod
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
Örnek Kod
<form action="">
  <label>
    Full Name:
    <input type="text" />
  </label>
</form>
Açık form ilişkilendirmesifor : Giriş alanları, öğe üzerindeki özniteliği kullanarak etiketlerle ilişkilendirilebilir label.
Örnek Kod
<form action="">
  <label for="email">Email Address: </label>
  <input type="email" id="email" />
</form>
button<button> öğesitype : Tıklanabilir bir düğme oluşturmak için kullanılır. Bir düğme ayrıca , etkinleştirildiğinde düğmenin davranışını kontrol etmek için kullanılan bir özniteliğe de sahip olabilir . Örnek: <button> submit, reset<button>, button<button>.
Örnek Kod
<button type="button">Show Form</button>
<button type="submit">Submit Form</button>
<button type="reset">Reset Form</button>
fieldsetElement : Birbiriyle ilişkili girdileri gruplandırmak için kullanılır.
legendelement : Giriş gruplarını tanımlamak için başlık eklemek amacıyla kullanılır.
Örnek Kod
<!-- Radio group -->
<fieldset>
  <legend>Was this your first time at our hotel?</legend>

  <label for="yes-option">Yes</label>
  <input id="yes-option" type="radio" name="hotel-stay" value="yes" />

  <label for="no-option">No</label>
  <input id="no-option" type="radio" name="hotel-stay" value="no" />
</fieldset>

<!-- Checkbox group -->
<fieldset>
  <legend>
    Why did you choose to stay at our hotel? (Check all that apply)
  </legend>

  <label for="location">Location</label>
  <input type="checkbox" id="location" name="location" value="location" />

  <label for="price">Price</label>
  <input type="checkbox" id="price" name="price" value="price" />
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
Örnek Kod
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
HTML Araçlarıyla Çalışmak
HTML doğrulayıcı : HTML kodunun sözdizimini kontrol ederek geçerli olup olmadığını doğrulayan bir araç.
DOM denetleyicisi : Bir web sayfasının HTML yapısını incelemenize ve değiştirmenize olanak sağlayan bir araç.
Geliştirici araçları : Web sayfalarında hata ayıklama, performans analizi ve performans incelemesi yapmanıza yardımcı olan, doğrudan tarayıcıya entegre edilmiş bir dizi web geliştirici aracı.