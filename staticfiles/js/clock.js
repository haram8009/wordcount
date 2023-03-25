console.log("clock.js");

var clock = document.querySelector(".clock");

const getTime = () => {
  console.log("getTime");

  const time = new Date();
  const months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];

  const month = months[time.getMonth()];
  const date = time.getDate();
  const hour = time.getHours();
  const minutes = time.getMinutes();
  const seconds = time.getSeconds();

  // clock.innerHTML = `${month} ${date} ${hour < 10 ? `0${hour}` : hour}:${
  //   minutes < 10 ? `0${minutes}` : minutes
  // }:${seconds < 10 ? `0${seconds}` : seconds}`;
  clock.innerHTML = `${month} ${date} ${hour < 10 ? `0${hour}` : hour}:${
    minutes < 10 ? `0${minutes}` : minutes
  }`;
};
function init() {
  getTime();
  setInterval(getTime, 1000);
}

init();
