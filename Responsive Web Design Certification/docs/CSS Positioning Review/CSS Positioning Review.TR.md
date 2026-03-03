CSS Konumlandırma İncelemesi
Şamandıralarla Çalışmak
Tanım : Float özelliği, bir öğeyi sayfadaki normal akışından çıkarıp, kapsayıcısının sol veya sağ tarafına konumlandırmak için kullanılır. Bu gerçekleştiğinde, metin float özelliğiyle çevrelenmiş içeriğin etrafına sarılır.
float: left;
float: right;
Kaydırma Öğelerini Temizleme : Bu clearözellik, bir öğenin kaydırılmış içeriğin altına taşınması gerekip gerekmediğini belirlemek için kullanılır. Birbirine bitişik birden fazla kaydırılmış öğeniz olduğunda, düzenlerde çakışma ve daralma sorunları olabilir. Bu nedenle, clearfixbu sorunu çözmek için bir yöntem geliştirildi.
<link rel="stylesheet" href="styles.css">
<div class="clearfix">
  <div class="box left">Left</div>
  <div class="box right">Right</div>
</div>
.box {
  width: 100px;
  height: 60px;
  color: white;
  text-align: center;
  line-height: 60px;
}

.left {
  float: left;
  background: teal;
}

.right {
  float: right;
  background: purple;
}

.clearfix::after {
  content: "";
  display: block;
  clear: both;
}
Statik, Göreceli ve Mutlak Konumlandırma
Statik Konumlandırma : Bu, belgenin normal akışıdır. Öğeler yukarıdan aşağıya ve soldan sağa doğru birbiri ardına konumlandırılır.
Göreceli Konumlandırmatop : Bu özellik, öğeyi normal belge akışı içinde konumlandırmak için `<position> `, left`<position>` rightve `<position>` özelliklerini kullanmanıza olanak tanır bottom. Ayrıca, öğelerin sayfadaki diğer öğelerle üst üste gelmesini sağlamak için de göreceli konumlandırma kullanabilirsiniz.
<link rel="stylesheet" href="styles.css">
<div class="relative">Relative Element</div>
.relative {
    position: relative;
    top: 30px;
    left: 30px;
}
Mutlak Konumlandırma : Bu özellik, bir öğeyi normal belge akışından çıkarmanıza ve diğer öğelerden bağımsız olarak davranmasını sağlamanıza olanak tanır.
<link rel="stylesheet" href="styles.css">
<div class="parent">
  Parent
  <div class="positioned">Absolute</div>
</div>
.parent {
  position: relative;
  height: 120px;
  background: #eee;
}

.positioned {
  position: absolute;
  top: 30px;
  left: 30px;
  background-color: coral;
}
Sabit ve Yapışkan Konumlandırma
Sabit Konumlandırma : Bir öğe sabit konumlandırma ile konumlandırıldığında position: fixed, normal belge akışından çıkarılır ve görünüm alanına göre yerleştirilir; bu, kullanıcının kaydırma yapması durumunda bile aynı konumda kalacağı anlamına gelir. Bu genellikle her zaman görünür kalması gereken başlıklar veya gezinme çubukları gibi öğeler için kullanılır.
<link rel="stylesheet" href="styles.css">
<div class="navbar">Fixed Navbar</div>
<div style="height: 600px;"></div>
.navbar {
  position: fixed; 
  top: 0; 
  width: 100%;
  background: #0077ff;
  color: white;
  padding: 8px; 
}
Yapışkan Konumlandırma : Bu konumlandırma türü, göreceli ve sabit konumlandırma arasında bir hibrit görevi görür. Başlangıçta, öğe belgenin akışı içinde kalarak göreceli olarak konumlandırılmış gibi davranır. Ancak, kullanıcı öğeyi belirli bir noktanın ötesine kaydırdığında, görünüm alanına (genellikle üst kısma) "yapışır" ve sabitmiş gibi davranır. Bu, kullanıcının belirli bir konuma kaydırdığı anda sabit hale gelen yapışkan gezinme çubukları gibi öğeler oluşturmak için idealdir.
<link rel="stylesheet" href="styles.css">
<p>Scroll down</p>
<div class="positioned">Sticky Element</div>
<div style="height: 500px;"></div>
.positioned {
  position: sticky;
  top: 30px;
  left: 30px;
  background: #4caf50;
  color: white;
  padding: 6px;
}
z-indexMülkle Çalışmak
Tanım : z-indexCSS'deki bu özellik, sayfada üst üste gelen konumlandırılmış öğelerin dikey sıralama düzenini kontrol etmek için kullanılır.
<link rel="stylesheet" href="styles.css">
<div class="container">
  <div class="box box1">1</div>
  <div class="box box2">2</div>
</div>
.container {
  position: relative;
  width: 300px;
  height: 300px;
  border: 1px solid black;
}

.box {
  position: absolute;
  width: 100px;
  height: 100px;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}

.box1 {
  background: lightcoral;
  top: 20px;
  left: 20px;
  z-index: 1;
}

.box2 {
  background: steelblue;
  top: 40px;
  left: 40px;
  z-index: 2;
}