JavaScript Matematik İncelemesi
Sayı Veri Türüyle Çalışmak
Tanım : JavaScript'in Numberveri tipleri arasında tamsayılar, ondalık sayılar Infinityve sayısal değerler bulunur NaN. Ondalık sayılar, ondalık noktası olan sayılardır. Pozitif sayılar Infinity, diğer tüm sayılardan büyük olan sayıları, negatif sayılar ise -Infinitydiğer tüm sayılardan küçük olan sayıları temsil eder. NaN( Not a Number) geçersiz bir sayısal değeri temsil eder, örneğin "boş" dizesi gibi "Jessica".
Yaygın Aritmetik İşlemler
Toplama Operatörü : Bu operatör ( +) iki veya daha fazla sayının toplamını hesaplamak için kullanılır.
Çıkarma Operatörü : Bu operatör ( -) iki sayı arasındaki farkı hesaplamak için kullanılır.
Çarpma İşlemi : Bu işlem ( *) iki veya daha fazla sayının çarpımını hesaplamak için kullanılır.
Bölme Operatörü : Bu operatör ( /) iki sayı arasındaki bölümü hesaplamak için kullanılır.
Sıfıra Bölme : Sıfıra bölmeye çalışırsanız, JavaScript . değerini döndürür Infinity.
Kalan Operatörü : Bu operatör ( %) bir bölme işleminden kalanını döndürür.
Üs Alma Operatörü : Bu operatör ( **) bir sayıyı başka bir sayının kuvvetine yükseltir.
Sayılar ve Dizelerle Hesaplamalar
Açıklama : `or` operatörünü bir sayı ve bir dizeyle kullandığınızda +, JavaScript sayıyı bir dizeye dönüştürür ve iki değeri birleştirir. `or` -, *`or` /operatörlerini bir dize ve sayıyla kullandığınızda, JavaScript dizeyi bir sayıya dönüştürür ve sonuç bir sayı olur. ` nullor` ve ` or` için undefinedJavaScript, matematiksel işlemlerdeki nullgibi `or`'u 0 ve `or`'u tanımsız olarak kabul eder.NaN
const result = 5 + '10';

console.log(result); // "510"
console.log(typeof result); // string

const subtractionResult = '10' - 5;
console.log(subtractionResult); // 5
console.log(typeof subtractionResult); // number

const multiplicationResult = '10' * 2;
console.log(multiplicationResult); // 20
console.log(typeof multiplicationResult); // number

const divisionResult = '20' / 2;
console.log(divisionResult); // 10
console.log(typeof divisionResult); // number

const result1 = null + 5;
console.log(result1); // 5
console.log(typeof result1); // number

const result2 = undefined + 5;
console.log(result2); // NaN
console.log(typeof result2); // number
Operatör Önceliği
Tanım : Operatör önceliği, bir ifadede işlemlerin değerlendirilme sırasını belirler. Daha yüksek önceliğe sahip operatörler, daha düşük önceliğe sahip operatörlerden önce değerlendirilir. Parantez içindeki değerler önce değerlendirilir ve çarpma/bölme işlemleri toplama/çıkarma işlemlerinden daha yüksek önceliğe sahip olur. Operatörlerin aynı önceliğe sahip olması durumunda, JavaScript ilişkilendirme özelliğini kullanır.
const result = (2 + 3) * 4;

console.log(result); // 20

const result2 = 10 - 2 + 3;

console.log(result2); // 11

const result3 = 2 ** 3 ** 2;

console.log(result3); // 512
Tanım : İlişkilendirme, aynı türden birden fazla operatör bulunduğunda bir ifadenin hangi yönde değerlendirileceğini bize bildirir. İfadenin soldan sağa ( left-associative) veya sağdan sola ( right-associative) değerlendirilmesi gerekip gerekmediğini tanımlar. Örneğin, üs alma operatörü de sağdan sola ilişkilidir:
const result4 = 5 ** 4 ** 1; 

console.log(result4); // 625
Artırma ve Azaltma Operatörleri
Artırma Operatörü : Bu operatör, değeri bir artırmak için kullanılır. Önek gösterimi ++numönce değişkenin değerini artırır, ardından yeni bir değer döndürür. Sonek gösterimi ise num++önce değişkenin mevcut değerini döndürür, ardından artırır.
let x = 5;

console.log(++x); // 6
console.log(x); // 6


let y = 5;

console.log(y++); // 5
console.log(y); // 6
Azaltma Operatörü : Bu operatör, değeri bir azaltmak için kullanılır. Önek gösterimi ve sonek gösterimi, artırma operatöründe olduğu gibi aynı şekilde çalışır.
let num = 5;

console.log(--num); // 4
console.log(num--); // 4
console.log(num); // 3
Bileşik Atama Operatörleri
Toplama Atama ( +=) Operatörü : Bu operatör, değerler üzerinde toplama işlemi gerçekleştirir ve sonucu değişkene atar.
Çıkarma Atama -=Operatörü ( ) : Bu operatör, değerler üzerinde çıkarma işlemi gerçekleştirir ve sonucu değişkene atar.
Çarpma Atama *=Operatörü ( ) : Bu operatör değerler üzerinde çarpma işlemi gerçekleştirir ve sonucu değişkene atar.
Bölme Atama /=Operatörü ( ) : Bu operatör, değerler üzerinde bölme işlemi gerçekleştirir ve sonucu değişkene atar.
Kalan Atama ( %=) Operatörü : Bu operatör, bir değişkeni belirtilen sayıya böler ve kalanı değişkene atar.
Üs Alma Atama **=Operatörü ( ) : Bu operatör, bir değişkeni belirtilen sayının kuvvetine yükseltir ve sonucu değişkene yeniden atar.
Mantıksal Değerler ve Eşitlik
Mantıksal (Boolean) Tanımı : Mantıksal (boolean) yalnızca iki değer alabilen bir veri türüdür: trueveya false.
Eşitlik ( ==) Operatörü : Bu operatör, değerlerin eşit olup olmadığını kontrol etmeden önce tür dönüştürme işlemini kullanır.
console.log(5 == '5'); // true
Kesin Eşitlik ( ===) Operatörü : Bu operatör tür dönüştürme işlemi yapmaz ve hem türlerin hem de değerlerin eşit olup olmadığını kontrol eder.
console.log(5 === '5'); // false
Eşitsizlik ( !=) Operatörü : Bu operatör, değerlerin eşit olup olmadığını kontrol etmeden önce tür dönüştürme kullanır.
Kesin Eşitsizlik ( !==) Operatörü : Bu operatör tür dönüştürme işlemi yapmaz ve hem türlerin hem de değerlerin eşit olup olmadığını kontrol eder.
Karşılaştırma Operatörleri
Büyüktür ( >) Operatörü : Bu operatör, soldaki değerin sağdaki değerden büyük olup olmadığını kontrol eder.
Büyüktür ( >=) veya Eşittir Operatörü : Bu operatör, soldaki değerin sağdaki değerden büyük veya eşit olup olmadığını kontrol eder.
Küçüktür ( <) Operatörü : Bu operatör, soldaki değerin sağdaki değerden küçük olup olmadığını kontrol eder.
Küçüktür ( <=) veya Eşittir Operatörü : Bu operatör, soldaki değerin sağdaki değerden küçük veya eşit olup olmadığını kontrol eder.
Tekli Operatörler
Tekli Artı Operatörü : Bu operatör, işlenenini bir sayıya dönüştürür. İşlenen zaten bir sayı ise, değişmeden kalır.
const str = '42';
const num = +str;

console.log(num); // 42
console.log(typeof num); // number
Tekli Olumsuzlama ( -) Operatörü : Bu operatör, işlenen ifadeyi olumsuzlar.
const num = 4;
console.log(-num); // -4
Mantıksal DEĞİL ( !) Operatörü : Bu operatör, işleneninin mantıksal değerini tersine çevirir. Yani, işlenen ise trueolur falseve ise falseolur true. 
Bit düzeyinde Operatörler
Bit düzeyinde VE ( &) Operatörü : Bu operatör, her iki işlenenin karşılık gelen bitlerinin 1 olduğu her bit konumunda 1 değerini döndürür.
Bit düzeyinde VE atama &=operatörü ( ) : Bu operatör, bitwise ANDbelirtilen sayı ile bir işlem gerçekleştirir ve sonucu değişkene yeniden atar.
Bit düzeyinde VEYA ( |) Operatörü : Bu operatör, işlenenlerden birinin veya her ikisinin karşılık gelen bitleri 1 olan her bit konumunda 1 değerini döndürür.
Bit düzeyinde VEYA atama |=operatörü ( ) : Bu operatör, bitwise ORbelirtilen sayı ile bir işlem gerçekleştirir ve sonucu değişkene yeniden atar.
Bit düzeyinde XOR ( ^) Operatörü : Bu operatör, işlenenlerden yalnızca birinin (ama ikisinin birden değil) karşılık gelen bitlerinin 1 olduğu her bit konumunda 1 değerini döndürür.
Bit düzeyinde DEĞİL ( ~) Operatörü : Bu operatör, bir sayının ikili gösterimini tersine çevirir.
Sol Kaydırma ( <<) Operatörü : Bu operatör, tüm bitleri belirtilen sayıda pozisyon kadar sola kaydırır.
Sağ Kaydırma ( >>) Operatörü : Bu operatör tüm bitleri sağa kaydırır.
Koşullu İfadeler, Doğru Değerler, Yanlış Değerler ve Üçlü Operatör
if/else if/elseBir ififade, bir koşul alır ve bu koşul sağlandığında bir kod bloğunu çalıştırır truthy. Koşul yanlışsa false, bir sonraki bloğa geçer else if. Bu koşulların hiçbiri yanlış değilse true, yan tümceyi yürütür else. Değerler, bir ifade gibi Boolean bir bağlamda değerlendirildiğinde Truthydoğru sonuç veren herhangi bir değerdir . Değerler, Boolean bir bağlamda yanlış olarak değerlendirilen değerlerdir .trueifFalsyfalse
const score = 87;

if (score >= 90) {
 console.log('You got an A'); 
} else if (score >= 80) {
 console.log('You got a B'); // You got a B
} else if (score >= 70) {
 console.log('You got a C');
} else {
 console.log('You failed! You need to study more!');
}
Üçlü Operatörif else : Bu operatör genellikle ifadeleri daha kısa yazmanın bir yolu olarak kullanılır .
const temperature = 30;
const weather = temperature > 25 ? 'sunny' : 'cool';

console.log(`It's a ${weather} day!`); // It's a sunny day!
İkili Mantıksal Operatörler
Mantıksal VE ( &&) Operatörü : Bu operatör, her iki işlenenin de boş olup olmadığını kontrol eder true. Her ikisi de boşsa true, ikinci değeri döndürür. İşlenenlerden biri boşsa falsy, boş değeri döndürür falsy. Her iki işlenen de boşsa falsy, birinci değeri döndürür falsy.
const result = true && 'hello';

console.log(result); // hello
Mantıksal VEYA ( ||) Operatörü : Bu operatör, işlenenlerden en az birinin doğru olup olmadığını kontrol eder. 
Nullish Coalescing ( ??) Operatörünull : Bu operatör yalnızca ilk değer veya ise bir değer döndürür undefined.
const userSettings = {
 theme: null,
 volume: 0,
 notifications: false,
};

let theme = userSettings.theme ?? 'light';
console.log(theme); // light
NesneMath​
Yöntem : Bu Math.random()yöntem , 0 (dahil) ile 1 (hariç) arasında rastgele bir ondalık sayı üretir. Bu, olası çıktının 0 olabileceği, ancak asla 1'e ulaşmayacağı anlamına gelir.
Yöntem : Bu Math.max()yöntem , bir sayı kümesi alır ve en büyük değeri döndürür.
Yöntem : Bu Math.min()yöntem , bir sayı kümesi alır ve en küçük değeri döndürür.
Yöntem : Bu Math.ceil()yöntem , bir değeri en yakın tam sayıya yuvarlar.
Yöntem : Bu Math.floor()yöntem , bir değeri en yakın tam sayıya yuvarlar.
Yöntem : Bu Math.round()yöntem , bir değeri en yakın tam sayıya yuvarlar.
console.log(Math.round(2.3)); // 2
console.log(Math.round(4.5)); // 5
console.log(Math.round(4.8)); // 5
Yöntem : Bu Math.trunc()yöntem , bir sayının ondalık kısmını kaldırır ve yuvarlama yapmadan yalnızca tam sayı kısmını döndürür.
Yöntem : Bu yöntem Math.sqrt(), bir sayının karekökünü döndürür.
Yöntem : Bu yöntem Math.cbrt(), bir sayının küp kökünü döndürür.
Yöntem : Bu Math.abs()yöntem , bir sayının mutlak değerini döndürür.
Yöntem : Bu Math.pow()yöntem iki sayı alır ve birincisini ikincisinin kuvvetine yükseltir.
Yaygın Sayı Yöntemleri
isNaN(): NaN"Sayı Değil" anlamına gelir. Temsil edilemeyen veya tanımlanmamış sayısal bir sonucu temsil eden özel bir değerdir. isNaN()Fonksiyon özelliği, bir değerin sayı olup olmadığını belirlemek için kullanılır NaN. Özellikle tür dönüştürmenin genel fonksiyonla beklenmedik sonuçlara yol açabileceği durumlarda, değerleri Number.isNaN()kontrol etmek için daha güvenilir bir yol sağlar .NaNisNaN()
console.log(isNaN(NaN));       // true
console.log(isNaN(undefined)); // true
console.log(isNaN({}));        // true

console.log(isNaN(true));      // false
console.log(isNaN(null));      // false
console.log(isNaN(37));        // false


console.log(Number.isNaN(NaN));        // true
console.log(Number.isNaN(Number.NaN)); // true
console.log(Number.isNaN(0 / 0));      // true

console.log(Number.isNaN("NaN"));      // false
console.log(Number.isNaN(undefined));  // false
Yöntem : Bu parseFloat()yöntem , bir dize bağımsız değişkenini ayrıştırır ve kayan noktalı bir sayı döndürür. Dizenin daha sonra sayısal olmayan karakterler içermesi durumunda bile, dizenin başından bir sayı çıkarmak için tasarlanmıştır.
Yöntem : Bu parseInt()yöntem , bir dize argümanını ayrıştırır ve bir tamsayı döndürür. parseInt()Karşılaştığı ilk rakam olmayan karakterde ayrıştırmayı durdurur. Ondalık sayılar için yalnızca tamsayı kısmını döndürür. Dizinin başında geçerli bir tamsayı bulamazsa, boş değer döndürür NaN.
Bu toFixed()yöntem , bir sayı üzerinde çağrılır ve isteğe bağlı olarak ondalık noktasından sonra görünecek basamak sayısını belirten bir argüman alır. Belirtilen ondalık basamak sayısına sahip sayının dize temsilini döndürür.