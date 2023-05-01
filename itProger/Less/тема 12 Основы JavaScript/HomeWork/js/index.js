
// 1) Напишите программу на JavaScript,
// что будет высчитывать сумму
// чисел кратных 3 или 5.
// Числа должны быть до 1000.
var summ = 0
var summAll = 0;
var summ3 = 0;
var summ5 = 0;
// вот тут вопрос по заданию
// до 1000 это влючая 1000 или нет
//
for (i = 0; i <= 1000; i++) {
  if (i % 3 == 0 || i % 5 == 0) {
    summ = summ + i;
  }
  // далее прото так время скоротать
  // да можно было использовать и это,
  // и в итоге результат двух условий сложить
  if (i % 3 == 0) summ3 = summ3 + i;
  if (i % 5 == 0) summ5 = summ5 + i;

  summAll = summAll + i
}
document.getElementById('summ').innerText = summ;
document.getElementById('summ3').innerText = summ3;
document.getElementById('summ5').innerText = summ5;
document.getElementById('summAll').innerText = summAll;
console.log("Сумма чисел кратных 3, 5 до 1000: " + summ);


// 2) Создайте двумерный массив, в котором найдите
// минимальный элемент среди всех элементов в массиве.
// Важно учесть, что нахождение минимального элемента
// должно производиться при помощи циклов.
// Массив:
//
// var x = new Array(new Array(20, 34, 2),
//                   new Array(9, 12, 18),
//                   new Array(3, 4, 5));
var arr = new Array(new Array(20, 34, 2),
                  new Array(9, 12, 18),
                  new Array(3, 4, 5));
// var min = arr[00][0]; // можно начальное задать и таким способом
var min = Number.MAX_SAFE_INTEGER;
var max = Number.MIN_SAFE_INTEGER;
var countElement = 0;
var summElement = 0;

for (i = 0; i < arr.length; i++) {
  for (y = 0; y < arr[i].length; y++) {
    if (min > arr[i][y]) {
      min = arr[i][y];
    }
    if (max < arr[i][y]) {
      max = arr[i][y];
    }
    countElement++;
    summElement = summElement + arr[i][y];
  }
}
document.getElementById('minElement').innerText = min;
document.getElementById('maxElement').innerText = max;
document.getElementById('countElement').innerText = countElement;
document.getElementById('summElement').innerText = summElement;

console.log("Минимальное значение в представленном массиве: " + min);
