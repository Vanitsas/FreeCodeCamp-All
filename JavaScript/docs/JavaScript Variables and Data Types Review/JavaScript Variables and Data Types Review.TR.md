JavaScript Değişkenleri ve Veri Tipleri İncelemesi
HTML, CSS ve JavaScript ile çalışma
HTML ve CSS web sitelerine yapı sağlarken, JavaScript ise kullanıcı girdilerini işleme, öğeleri canlandırma ve hatta tam teşekküllü web uygulamaları oluşturma gibi karmaşık işlevleri mümkün kılarak web sitelerine etkileşim kazandırır.

JavaScript'te Veri Tipleri
Veri türleri, programın üzerinde çalıştığı verinin türünü (sayı, metin veya başka bir şey) anlamasına yardımcı olur.

Sayı : Bir sayı hem tam sayıları hem de ondalık sayıları temsil eder. Tam sayılara örnek olarak 7, 19 ve 90 verilebilir.
Ondalıklı sayı : Ondalıklı sayı, ondalık noktası olan bir sayıdır. Örnekler arasında 3,14, 0,5 ve 0,0001 bulunur.
Dize : Dize, tırnak işaretleri içine alınmış karakter veya metin dizisidir. "I like coding"ve 'JavaScript is fun'dizelere örnektir.
Mantıksal Değer (Boolean ): Mantıksal değer, iki olası değerden birini temsil eder: trueveya false. Mantıksal değeri, gibi bir koşulu temsil etmek için kullanabilirsiniz isLoggedIn = true.
Tanımlanmamış ve Null : Bir undefineddeğer, tanımlanmış ancak bir değer atanmamış bir değişkendir. Bir nulldeğer, boş bir değer veya kasıtlı olarak bir değer atanmış bir değişkendir null.
Nesne : Bir nesne, anahtar-değer çiftlerinden oluşan bir koleksiyondur. Anahtar, özellik adıdır ve değer, özellik değeridir.
Burada, petnesnenin üç özelliği veya anahtarı vardır: name, age, ve type. Değerler sırasıyla Fluffy, 3, ve dog'dir.

let pet = {
  name: "Fluffy",
  age: 3,
  type: "dog"
};
Sembol : Sembol veri türü, nesne özelliklerini tanımlamak için kullanılabilen benzersiz ve değiştirilemez bir değerdir.
Aşağıdaki örnekte, aynı açıklamaya sahip iki sembol oluşturulmuştur, ancak bunlar birbirine eşit değildir.

const crypticKey1= Symbol("saltNpepper");
const crypticKey2= Symbol("saltNpepper");
console.log(crypticKey1 === crypticKey2); // false
BigInt : Sayı, Numberveri türü için çok büyük olduğunda, keyfi uzunluktaki tamsayıları temsil etmek için BigInt veri türünü kullanabilirsiniz.
nSayının sonuna bir ekleyerek BigInt oluşturabilirsiniz.

const veryBigNumber = 1234567890123456789012345678901234567890n;
JavaScript'te Değişkenler
Değişkenler, `value` anahtar kelimesi kullanılarak tanımlanabilir let.
let cityName;
Bir değişkene değer atamak için atama operatörünü kullanabilirsiniz =.
cityName = "New York";
`@` kullanılarak tanımlanan değişkenlere letyeni bir değer atanabilir.
let cityName = "New York";
cityName = "Los Angeles";
console.log(cityName); // Los Angeles
Bunun dışında , bir değişkeni tanımlamak için `std:` ifadesini letde kullanabilirsiniz . Ancak, bir değişkene yeni bir değer atanamaz.constconst
const cityName = "New York";
cityName = "Los Angeles"; // TypeError: Assignment to constant variable.
`find` kullanılarak tanımlanan değişkenler const, kod boyunca değiştirilmesine izin verilmeyen sabitleri tanımlamak için kullanılır; örneğin `int` veya PI`int` gibi MAX_SIZE.
Değişken Adlandırma Kuralları
Değişken adları açıklayıcı ve anlamlı olmalıdır.
cityNameDeğişken adları , isLoggedIn, ve gibi camelCase formatında olmalıdır veryBigNumber.
Değişken adları bir rakamla başlamamalıdır. Bir harf, virgül _veya nokta ile başlamalıdırlar $.
_Değişken adları, ve karakterleri dışında boşluk veya özel karakter içermemelidir $.
Değişken adları, ayrılmış anahtar kelimeler olmamalıdır.
Değişken adları büyük/küçük harf duyarlıdır. ageve Agefarklı değişkenlerdir.
JavaScript'te Dizeler ve Dizelerin Değişmezliği
Dizeler, tırnak işaretleri içine alınmış karakter dizileridir. Tek tırnak ve çift tırnak kullanılarak oluşturulabilirler.
let correctWay = 'This is a string';
let alsoCorrect = "This is also a string";
JavaScript'te dizeler değiştirilemezdir. Bu, bir dize oluşturulduktan sonra, dizenin içindeki karakterleri değiştiremeyeceğiniz anlamına gelir. Ancak, dizelere yeni bir değer atayabilirsiniz.
let firstName = "John";
firstName = "Jane"; // Reassigning the string to a new value
JavaScript'te Dize Birleştirme
Birleştirme, birden fazla dizeyi birleştirme veya metin içeren değişkenlerle dizeleri bir araya getirme işlemidir. `concatenation` +operatörü, dizeleri birleştirmek için en basit ve en sık kullanılan yöntemlerden biridir.
let studentName = "Asad";
let studentAge = 25;
let studentInfo = studentName + " is " + studentAge + " years old.";
console.log(studentInfo); // Asad is 25 years old.
Mevcut bir dizeye ekleme veya uzatma yapmanız gerekiyorsa, bu +=operatörü kullanabilirsiniz. Bu, zaman içinde bir dizeye daha fazla metin ekleyerek onu geliştirmek istediğinizde faydalıdır.
let message = "Welcome to programming, ";
message += "Asad!";
console.log(message); // Welcome to programming, Asad!
Dizeleri birleştirmenin bir başka yolu da `replace` yöntemini kullanmaktır concat(). Bu yöntem, iki veya daha fazla dizeyi bir araya getirir.
let firstName = "John";
let lastName = "Doe";
let fullName = firstName.concat(" ", lastName);
console.log(fullName); // John Doe
Mesajları Kaydetmeconsole.log()
Bu console.log()yöntem, konsola mesaj kaydetmek için kullanılır. Kodunuzda hata ayıklama ve test etme için faydalı bir araçtır.
console.log("Hello, World!");
// Output: Hello, World!
JavaScript'te noktalı virgüller
Noktalı virgüller öncelikle bir ifadenin sonunu işaretlemek için kullanılır. Bu, JavaScript motorunun ayrı ayrı talimatların ayrımını anlamasına yardımcı olur ki bu da doğru yürütme için çok önemlidir.
let message = "Hello, World!"; // first statement ends here
let number = 42; // second statement starts here
Noktalı virgüller, kod yürütülmesindeki belirsizlikleri önlemeye ve ifadelerin doğru şekilde sonlandırılmasını sağlamaya yardımcı olur.
JavaScript'te Yorumlar
Yorum satırı haline getirilmiş herhangi bir kod satırı JavaScript motoru tarafından göz ardı edilir. Yorumlar, kodu açıklamak, not almak veya kodu geçici olarak devre dışı bırakmak için kullanılır.
Tek satırlık yorumlar . kullanılarak oluşturulur //.
// This is a single-line comment and will be ignored by the JavaScript engine
/*Çok satırlı yorumlar, yoruma başlamak için `<p>` ve */yorumu bitirmek için `<p>` etiketleri kullanılarak oluşturulur .
/*
This is a multi-line comment.
It can span multiple lines.
*/
Dinamik Tip Tanımlı Bir Dil Olarak JavaScript
JavaScript, dinamik olarak tiplendirilmiş bir dildir; bu, bir değişkeni tanımlarken veri türünü belirtmenize gerek olmadığı anlamına gelir. JavaScript motoru, değişkene atanan değere göre veri türünü otomatik olarak belirler.
let error = 404; // JavaScript treats error as a number
error = "Not Found"; // JavaScript now treats error as a string
C# gibi dinamik olarak tiplendirilmemiş diğer diller ise hataya neden olur:
int error = 404; // value must always be an integer
error = "Not Found"; // This would cause an error in C#
typeofOperatörü Kullanma
Bu typeofoperatör, bir değişkenin veri türünü kontrol etmek için kullanılır. Değişkenin türünü belirten bir dize döndürür.
let age = 25;
console.log(typeof age); // "number"

let isLoggedIn = true;
console.log(typeof isLoggedIn); // "boolean"
Ancak JavaScript'te `.` operatörüyle ilgili bilinen bir tuhaflık var null. `.` operatörü `.` değerleri için `.` typeofdöndürür ."object"null
let user = null;
console.log(typeof user); // "object"