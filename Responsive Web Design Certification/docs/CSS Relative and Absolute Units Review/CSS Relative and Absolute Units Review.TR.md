CSS Göreceli ve Mutlak Birimler İncelemesi
Mutlak Birimler
px(Piksel) : Bu mutlak birim, CSS'de sabit boyutlu bir ölçü birimidir. En yaygın kullanılan mutlak birimdir ve boyutlar üzerinde hassas kontrol sağlar. 1pxHer zaman inçin 1/96'sına eşittir.
in(İnç) : Bu mutlak birim 96 piksele eşittir.
cm(Santimetre) : Bu mutlak birim, bir inçin 25,2/64'üne eşittir.
mm(Milimetre) : Bu mutlak birim, bir santimetrenin 1/10'una eşittir.
q(Çeyrek Milimetre) : Bu mutlak birim, bir santimetrenin 1/40'ına eşittir.
pc(Pika) : Bu mutlak birim, inçin 1/6'sına eşittir.
pt(Puan) : Bu mutlak birim, inçin 1/72'sine eşittir.
<link rel="stylesheet" href="styles.css">
<div class="units">
  <div class="unit px">px</div>
  <div class="unit inch">in</div>
  <div class="unit cm">cm</div>
  <div class="unit mm">mm</div>
  <div class="unit q">q</div>
  <div class="unit pc">pc</div>
  <div class="unit pt">pt</div>
</div>
.units {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  align-items: flex-end;
}

.unit {
  background: steelblue;
  color: white;
  text-align: center;
  padding: 4px;
}

.px {
  width: 40px;
  height: 40px;
}

.inch {
  width: 0.5in;
  height: 0.5in;
}

.cm {
  width: 1cm;
  height: 1cm;
}

.mm {
  width: 10mm;
  height: 10mm;
}

.q {
  width: 40q;
  height: 40q;
}

.pc {
  width: 6pc;
  height: 6pc;
}

.pt {
  width: 36pt;
  height: 36pt;
}
Göreceli Birimler
Yüzdeler : Bu göreceli birimler, boyutları, ölçüleri ve diğer özellikleri üst öğelerinin bir oranı olarak tanımlamanıza olanak tanır. Örneğin, width: 50%;bir öğeye yüzde değeri atarsanız, üst kapsayıcısının genişliğinin yarısını kaplayacaktır.
emBirimems : Bu birimler, öğenin yazı tipi boyutuna göre belirlenir. Özellik için kullanıyorsanız font-size, metnin boyutu üst öğenin yazı tipi boyutuna göre belirlenir.
remBirim : Bu birimler, kök öğenin yani htmlöğenin yazı tipi boyutuna göre belirlenir.
vhBirim : Görüntü alanının yüksekliğinin %1'ini vhtemsil eder "viewport height"ve ona eşittir.1vh
vwBirim : Görüntü alanının genişliğinin %1'ini vwtemsil eder "viewport width"ve ona eşittir.1vw
<link rel="stylesheet" href="styles.css">
<div class="parent">
  <div class="box percent">50%</div>
  <div class="box em">2em</div>
  <div class="box rem">2rem</div>
  <div class="box vh">10vh</div>
  <div class="box vw">10vw</div>
</div>
html {
  font-size: 16px;
}

.parent {
  width: 200px;
  font-size: 20px;
  border: 2px dashed #555;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.box {
  background: seagreen;
  color: white;
  text-align: center;
  padding: 6px;
}

.percent {
  width: 50%;
}

.em {
  font-size: 2em;
}

.rem {
  font-size: 2rem;
}

.vh {
  height: 10vh;
}

.vw {
  width: 10vw;
}
calcİşlev
calc()Fonksiyon : Bu fonksiyon sayesinde calc(), özellik değerlerini dinamik olarak belirlemek için doğrudan stil sayfalarınızda hesaplamalar yapabilirsiniz. Bu, görünüm alanı boyutuna veya diğer öğelere bağlı olarak boyutları hesaplayarak esnek ve duyarlı kullanıcı arayüzleri oluşturabileceğiniz anlamına gelir.
<link rel="stylesheet" href="styles.css">
<div class="calc-box">calc()</div>
.calc-box {
  width: calc(100% - 40px);
  padding: 10px;
  background: steelblue;
  color: white;
  text-align: center;
  border: 2px solid black;
}