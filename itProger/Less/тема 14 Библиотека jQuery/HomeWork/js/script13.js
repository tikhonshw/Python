
function theme1() {
  var ttt  = 8;
  var iii = prompt('Введите число: ');
  while (ttt != iii) {
  	console.log("И еще раз..");
  	iii = prompt("Введите число:");
  }
  alert("Мое число угадано!! Поздравляю!!! И это число: " + iii);
  console.log("Мое число угадано!! Поздравляю!!! И это число: " + iii);
}

function resize() {
  windowWidth = window.innerWidth;
  windowHeight = window.innerHeight;
  document.getElementById('size').innerHTML = 'Задание 2: ' +
        ' высота экрана - ' + windowHeight +
        ' ширина экрана - ' + innerWidth;
}
window.onresize = function () {
  windowWidth = window.innerWidth;
  windowHeight = window.innerHeight;
  document.getElementById('size').innerHTML = 'Задание 2: ' +
        ' высота экрана - ' + windowHeight +
        ' ширина экрана - ' + innerWidth;
}


function boldTestInRed(selector) {
  var elements = document.querySelectorAll(selector);
  var index = 0, length = elements.length;
  for ( ; index < length; index++) {
    elements[index].style.color = '#ff0000';
  }
}
function boldTestInBlack(selector) {
  var elements = document.querySelectorAll(selector);
  var index = 0, length = elements.length;
  for ( ; index < length; index++) {
    elements[index].style.color = '#000';
  }
}


function getAttributes() {
  console.log('Значение атрибута href: ' + document.getElementById("link").href);
  console.log('Значение атрибута hreflang: ' + document.getElementById("link").hreflang);
  console.log('Значение атрибута rel: ' + document.getElementById("link").rel);
  console.log('Значение атрибута target: ' + document.getElementById("link").target);
  console.log('Значение атрибута type: ' + document.getElementById("link").type);
}
