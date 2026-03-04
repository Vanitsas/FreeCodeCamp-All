CSS Değişkenleri İncelemesi
CSS Özel Özellikleri (CSS Değişkenleri)
Tanım : CSS özel özellikleri, diğer adıyla CSS değişkenleri, CSS yazarları tarafından tanımlanan ve bir belge boyunca yeniden kullanılacak belirli değerler içeren varlıklardır. Daha verimli, bakımı kolay ve esnek stil sayfaları oluşturmaya olanak tanıyan güçlü bir özelliktir. Özel özellikler, özellikle temaya uygun tasarımlar oluşturmada kullanışlıdır. Farklı temalar için bir dizi özellik tanımlayabilirsiniz:
:root {
  --bg-color: white;
  --text-color: black;
}

.dark-theme {
  --bg-color: #333;
  --text-color: white;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
}
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
@propertyKural Kullanarak Gradyan Örneği : Bu örnek, öğenin üzerine gelindiğinde yumuşak bir şekilde hareket eden bir gradyan oluşturur.
<link rel="stylesheet" href="styles.css">

<div class="gradient-box"></div>
@property --gradient-angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.gradient-box {
  width: 100px;
  height: 100px;
  background: linear-gradient(var(--gradient-angle), red, blue);
  transition: --gradient-angle 0.5s;
}

.gradient-box:hover {
  --gradient-angle: 90deg;
}
Yedek Değerlervar() : Özel özelliği kullanırken, standart özel özelliklerde olduğu gibi, bir yedek değer sağlamak için şu işlevi kullanabilirsiniz :
.button {
  background-color: var(--main-color, #3498db);
}