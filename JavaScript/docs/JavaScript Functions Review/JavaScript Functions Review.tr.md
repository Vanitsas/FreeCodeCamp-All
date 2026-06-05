JavaScript Fonksiyonları İncelemesi
JavaScript Fonksiyonları
Fonksiyonlar, belirli bir görevi yerine getiren, yeniden kullanılabilir kod bloklarıdır.
functionFonksiyonlar , anahtar kelimeyi takiben bir isim, parametre listesi ve görevi gerçekleştiren bir kod bloğu kullanılarak tanımlanabilir .
function addNumbers(x, y, z) {
  return x + y + z;
}

console.log(addNumbers(5, 3, 8)); // Output: 16
Argümanlar, bir fonksiyon çağrıldığında ona iletilen değerlerdir.
Bir fonksiyon çağrısı, bir programda fonksiyonun adını parantez içinde belirterek ve isteğe bağlı olarak parantez içine argümanlar ekleyerek fonksiyonu çalıştırma işlemidir.
Bir fonksiyon yürütme işlemini tamamladığında, her zaman bir değer döndürür.
Varsayılan olarak, bir fonksiyonun dönüş değeri şudur undefined: .
Bu returnanahtar kelime, fonksiyondan döndürülecek değeri belirtmek ve fonksiyonun yürütülmesini sonlandırmak için kullanılır.
Varsayılan parametreler, fonksiyonların çağrıldığında bir argüman sağlanmadığında kullanılacak önceden tanımlanmış değerlere sahip olmasını sağlar. Bu, fonksiyonları daha esnek hale getirir ve belirli argümanların atlanabileceği durumlarda hataları önler.
const calculateTotal = (amount, taxRate = 0.05) => {
  return amount + (amount * taxRate);
};

console.log(calculateTotal(100)); // Output: 105
Anonim fonksiyonlar, değişkenlere atanabilen, adı olmayan fonksiyonlardır. Bu fonksiyonları değişkenlere atayarak, değişkenin erişilebilir olduğu her yerde yeniden kullanabilirsiniz.
const multiplyNumbers = function(firstNumber, secondNumber) {
  return firstNumber * secondNumber;
};

console.log(multiplyNumbers(4, 5)); // Output: 20
Ok Fonksiyonları
Ok fonksiyonları, JavaScript'te fonksiyon yazmanın daha özlü bir yoludur.
const calculateArea = (length, width) => {
  const area = length * width;
  return `The area of the rectangle is ${area} square units.`;
};

console.log(calculateArea(5, 10)); // Output: "The area of the rectangle is 50 square units."
Ok fonksiyonu tanımlarken anahtar kelimeye ihtiyacınız yoktur function.
Tek bir parametre kullanıyorsanız, parametre listesinin etrafındaki parantezleri kaldırabilirsiniz.
const cube = x => {
  return x * x * x;
};

console.log(cube(3)); // Output: 27
Fonksiyon gövdesi tek bir ifadeden oluşuyorsa, süslü parantezleri ve anahtar kelimeyi atlayabilirsiniz return.
const square = number => number * number;

console.log(square(5)); // Output: 25
Programlamada Kapsam
Küresel kapsam : Bu, JavaScript'teki en dış kapsamdır. Küresel kapsamda tanımlanan değişkenlere kodun herhangi bir yerinden erişilebilir ve bu değişkenlere küresel değişkenler denir.
Yerel kapsam : Bu, bir fonksiyon içinde tanımlanan değişkenleri ifade eder. Bu değişkenlere yalnızca tanımlandıkları fonksiyon içinde erişilebilir ve yerel değişkenler olarak adlandırılırlar.
Blok kapsamı : Bir blok , ifadeler veya döngüler {}gibi süslü parantezler içine alınmış bir dizi ifadedir .if
Blok kapsamlama let, constdeğişken erişilebilirliği üzerinde daha da hassas kontrol sağlayarak hataları önlemeye ve kodunuzu daha öngörülebilir hale getirmeye yardımcı olur.