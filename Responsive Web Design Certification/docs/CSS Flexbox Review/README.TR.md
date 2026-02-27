Mülkflex-direction​
Tanım : Bu özellik, ana eksenin yönünü belirler. Varsayılan değeri flex-direction, rowtüm esnek öğeleri aynı satıra, tarayıcınızın varsayılan dilinin yönünde (soldan sağa veya sağdan sola) yerleştirir.
flex-direction: row-reverse;Bu, satırdaki öğelerin sırasını değiştirir.
flex-direction: column;Bu işlem, esnek öğeleri yatay yerine dikey olarak hizalayacaktır.
flex-direction: column-reverse;Bu, esnek öğelerin dikey sırasını tersine çevirir.
<div class="container">
  <div class="box">1</div>
  <div class="box">2</div>
  <div class="box">3</div>
</div>
.container {
  display: flex;
  flex-direction: row;
  gap: 10px;
}

.box {
  background-color: lightblue;
  padding: 20px;
  text-align: center;
}
Mülkflex-wrap​
Tanım : Bu özellik, esnek öğelerin mevcut alana sığacak şekilde esnek bir kapsayıcı içinde nasıl sarılacağını belirler. flex-wrapÜç olası değer alabilir: nowrap, wrap, ve wrap-reverse.
flex-wrap: nowrap;Bu varsayılan değerdir. Esnek öğeler, genişlikleri kapsayıcının genişliğini aşsa bile yeni bir satıra geçirilmez.
flex-wrap: wrap;Bu özellik, öğeler bulundukları kabın genişliğini aştığında onları sarmalayacaktır.
flex-wrap: wrap-reverse;Bu özellik, esnek öğeleri ters sırada sarmalayacaktır.
flex-flowÖzellikflex-direction : Bu özellik, ve için kısaltılmış bir özelliktir flex-wrap.
<div class="container">
  <div class="box">1</div>
  <div class="box">2</div>
  <div class="box">3</div>
  <div class="box">4</div>
  <div class="box">5</div>
</div>
.container {
  display: flex;
  flex-wrap: wrap;
  width: 150px;
  background: #f0f0f0;
}

.box {
  width: 60px;
  padding: 10px;
  margin: 5px;
  background: skyblue;
  text-align: center;
}
Mülkjustify-content​
Tanım : Bu özellik, alt öğeleri esnek kapsayıcının ana ekseni boyunca hizalar.
justify-content: flex-start;Bu durumda, esnek öğeler ana eksenin başlangıcına hizalanacaktır. Bu, yatay veya dikey olabilir.
justify-content: flex-end;Bu durumda, esnek elemanlar ana eksenin ucuna yatay veya dikey olarak hizalanır.
justify-content: center;Bu, esnek öğeleri ana eksen boyunca ortalar.
justify-content: space-between;Bu işlem, elemanları ana eksen boyunca eşit olarak dağıtacaktır.
justify-content: space-around;Bu işlem, esnek öğeleri ana eksen içinde eşit olarak dağıtacak ve ilk öğeden önce ve son öğeden sonra bir boşluk ekleyecektir.
justify-content: space-evenly;Bu işlem, öğeleri ana eksen boyunca eşit olarak dağıtacaktır.
<div class="container">
  <div class="box">A</div>
  <div class="box">B</div>
  <div class="box">C</div>
</div>
.container {
  display: flex;
  justify-content: space-between;
  background: #eee;
}

.box {
  padding: 20px;
  background: salmon;
}
Mülkalign-items​
Tanım : Bu özellik, öğeleri çapraz eksen boyunca dağıtmak için kullanılır. Çapraz eksenin ana eksene dik olduğunu unutmayın.
align-items: center;Bu, öğeleri çapraz eksen boyunca ortalamak için kullanılır.
align-items: flex-start;Bu, öğeleri çapraz eksenin başlangıç ​​noktasına hizalar.
align-items: stretch;Bu, esnek parçaları çapraz eksen boyunca germek için kullanılır.
<div class="container">
  <div class="box tall">1</div>
  <div class="box">2</div>
  <div class="box">3</div>
</div>
.container {
  display: flex;
  align-items: center;
  height: 150px;
  background: #ddd;
}

.box {
  background: lightgreen;
  padding: 10px;
}

.tall {
  height: 100px;
}