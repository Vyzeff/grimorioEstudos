//Never Changing Contants
const HOURHAND = document.querySelector("#hour");
const MINUTEHAND = document.querySelector("#minute");
const SECONDHAND = document.querySelector("#second");
const TEXTIME = document.querySelector(".textime");

//Basic Time and Date stuff
var date = new Date();
console.log(date);
var hr = date.getHours();
var min = date.getMinutes();
var sec = date.getSeconds();

//Time Test
console.log("Hour: " + hr + " Minute: " + min + " Second: " + sec)

//Fancy math for rotation
let hrPosition = (hr*360/12)+(min*(360/60)/12);
let minPosition = (min*360/60)+(sec*(360/60)/60);
let secPosition = (sec*360/60);       // +(sec*(360/60)/60)

//Fancy 00 for single digits
function leadingZero(time) {
  if (time <= 9) {
    time = "0" + time;
  }
  return time
}

//Fancy text time
function runTheText() {

  let textDate = new Date()
  let textHr = textDate.getHours();
  let textMin = textDate.getMinutes();
  let textSec = textDate.getSeconds();
  let dateArray = [textHr,textMin,textSec]
  // console.log(dateArray)
  TEXTIME.innerHTML = leadingZero(dateArray[0]) + "|" + leadingZero(dateArray[1]) + "|" + leadingZero(dateArray[2])

}

//Fancy analog clock
function runTheClock() {

  hrPosition = hrPosition+(3/360)
  minPosition = minPosition+(6/60)
  secPosition = secPosition+6

  HOURHAND.style.transform = "rotate(" + hrPosition + "deg)";
  MINUTEHAND.style.transform = "rotate(" + minPosition + "deg)";
  SECONDHAND.style.transform = "rotate(" + secPosition + "deg)";
}

//Actually run the functions
var firstInterval = setInterval(runTheClock, 1000);

var secondInterval = setInterval(runTheText, 1000);
