JavaScript Dizeleri İncelemesi
String Temelleri
Tanım : Bir dize, tek tırnak, çift tırnak veya ters tırnak içine alınmış bir karakter dizisidir. Dizeler temel veri türleridir ve değiştirilemezdir. Değiştirilemezlik, bir dize oluşturulduktan sonra değiştirilemeyeceği anlamına gelir.
Bir Diziden Karakterlere Erişim : Bir diziden bir karaktere erişmek için köşeli parantez gösterimini kullanabilir ve dizin numarasını belirtebilirsiniz. Dizin, bir karakterin dizi içindeki konumunu gösterir ve sıfırdan başlar.
const developer = "Jessica";
console.log(developer[0]); // J
\n(Yeni Satır Karakteri) : Yeni satır karakterini kullanarak bir dizede yeni bir satır oluşturabilirsiniz \n.
const poem = "Roses are red,\nViolets are blue,\nJavaScript is fun,\nAnd so are you.";
console.log(poem);
Dizelerden Kaçınma\ : Bir dizedeki karakterlerden kaçınmak için tırnak işaretlerinin önüne ters eğik çizgi ( ) koyabilirsiniz .
const statement = "She said, \"Hello!\"";
console.log(statement); // She said, "Hello!"
Şablon Sabitleri (Şablon Dizeleri) ve Dize İnterpolasyonu
Tanım : Şablon değişmezleri ters tırnak işaretleri (`) ile tanımlanır. Bunlar, değişkenleri doğrudan bir dizenin içine yerleştirme de dahil olmak üzere, dize manipülasyonunu kolaylaştırır; bu özellik dize enterpolasyonu olarak bilinir.
const name = "Jessica";
const greeting = `Hello, ${name}!`; 
console.log(greeting); // "Hello, Jessica!"
ASCII, charCodeAt()Yöntem ve fromCharCode()Yöntem
ASCII : ASCII (American Standard Code for Information Interchange), temel İngilizce karakterleri sayısal değerler kullanarak temsil etmek için kullanılan bir karakter kodlama standardıdır. Önceki derslerde ASCII örnekleri tanıtılmış charCodeAt()ve kullanılmıştır.fromCharCode()
Unicode : JavaScript dizeleri dahili olarak Unicode kullanır, özellikle UTF-16 kodlamasını. İlk 128 karakter (temel Latin harfleri, rakamlar ve yaygın semboller) için Unicode değerleri ASCII kodlarıyla eşleşir. Bu nedenle ASCII tabanlı örnekler JavaScript'te çalışmaya devam eder.
Yöntem : Bu charCodeAt()yöntem , belirtilen dizindeki karakterin UTF-16 kod birimini döndürür. Temel Latin karakterleri için bu değer ASCII koduna karşılık gelir.
const letter = "A";
console.log(letter.charCodeAt(0));  // 65
Yöntem : Bu yöntem fromCharCode(), bir ASCII kodunu karşılık gelen karaktere dönüştürür.
const char = String.fromCharCode(65);
console.log(char);  // A
Diğer Yaygın Dize Yöntemleri
Yöntem : Bu indexOfyöntem , bir dize içinde bir alt dize aramak için kullanılır. Alt dize bulunursa, indexOfo alt dizenin ilk geçtiği yerin dizinini (veya konumunu) döndürür. Alt dize bulunamazsa, indexOfaramanın başarısız olduğunu gösteren -1 değerini döndürür.
const text = "The quick brown fox jumps over the lazy dog.";
console.log(text.indexOf("fox")); // 16
console.log(text.indexOf("cat")); // -1
Yöntem : Bu includes()yöntem , bir dizenin belirli bir alt dizeyi içerip içermediğini kontrol etmek için kullanılır. Alt dize dize içinde bulunursa, yöntem true değerini döndürür. Aksi takdirde, false değerini döndürür.
const text = "The quick brown fox jumps over the lazy dog.";
console.log(text.includes("fox")); // true
console.log(text.includes("cat")); // false
Yöntem : Bu slice()yöntem , bir dizenin bir bölümünü ayıklayarak orijinal dizeyi değiştirmeden yeni bir dize döndürür. İki parametre alır: başlangıç ​​dizini ve isteğe bağlı bitiş dizini.
const text = "freeCodeCamp";
console.log(text.slice(0, 4));  // "free"
console.log(text.slice(4, 8));  // "Code"
console.log(text.slice(8, 12)); // "Camp"
Yöntem : Bu toUpperCase()yöntem tüm karakterleri büyük harflere dönüştürür ve tamamı büyük harflerden oluşan yeni bir dize döndürür.
const text = "Hello, world!";
console.log(text.toUpperCase()); // "HELLO, WORLD!"
Yöntem : Bu toLowerCase()yöntem , bir dizedeki tüm karakterleri küçük harfe dönüştürür.
const text = "HELLO, WORLD!"
console.log(text.toLowerCase()); // "hello, world!"
Bu replace()yöntem , bir dizede belirtilen bir değeri (örneğin bir kelime veya karakter) bulmanıza ve onu başka bir değerle değiştirmenize olanak tanır. JavaScript dizeleri değiştirilemez olduğundan, yöntem orijinal dizeyi olduğu gibi bırakarak, değiştirme işlemiyle birlikte yeni bir dize döndürür.
const text = "I like cats";
console.log(text.replace("cats", "dogs")); // "I like dogs"
Yöntem : Bu replaceAll()yöntem , bir dizede belirtilen bir değerin (bir kelime, karakter veya desen) tüm tekrarlarını bulmanıza ve bunları başka bir değerle değiştirmenize olanak tanır. gibi çalışır replace(), ancak ilk eşleşmeden sonra durmak yerine, dizede bulunan her eşleşmeyi günceller.
const text = "I love cats and cats are so much fun!";
console.log(text.replaceAll("cats", "dogs")); // "I love dogs and dogs are so much fun!"
Yöntem : Bu yöntem repeat(), bir metin dizisini belirtilen sayıda tekrarlamak için kullanılır.
const text = "Hello";
console.log(text.repeat(3)); // "HelloHelloHello"
Yöntem : Bu trim()yöntem , bir metin dizisinin hem başındaki hem de sonundaki boşlukları kaldırmak için kullanılır.
const text = "  Hello, world!  ";
console.log(text.trim()); // "Hello, world!"
Yöntem : Bu trimStart()yöntem , dizenin başındaki (veya "başlangıcındaki") boşlukları kaldırır.
const text = "  Hello, world!  ";
console.log(text.trimStart()); // "Hello, world!  "
Yöntem : Bu trimEnd()yöntem , dizenin sonundaki boşlukları kaldırır.
const text = " Hello, world! ";
console.log(text.trimEnd()); // "  Hello, world!"
Yöntemprompt() : Bu yöntem, birwindow iletişim kutusu aracılığıyla kullanıcıdan bilgi almak için kullanılır. Bu yöntem iki argüman alır. Birinci argüman, iletişim kutusunun içinde görünecek olan ve genellikle kullanıcıdan bilgi girmesini isteyen mesajdır. İkinci argüman ise isteğe bağlı olan ve giriş alanını başlangıçta dolduracak varsayılan değerdir.
const answer = window.prompt("What's your favorite animal?"); // This will change depending on what the user answers