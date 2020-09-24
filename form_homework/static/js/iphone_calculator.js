var decimalBtn = document.getElementById("calc-decimal");
var clearBtn = document.getElementById("calc-clear");
var backspaceBtn = document.getElementById("calc-backspace");

var displayValElement = document.getElementById("calc-display-val");

var displayVal = "0";
var pendingVal;
var evalStringArray = [];

var calcNumBtns = document.getElementsByClassName("calc-btn-num");
var calcOperatorBtns = document.getElementsByClassName("calc-btn-operator");

var updateDisplayVal = (clickObj) => {
  var btnText = clickObj.target.innerText;

  if (displayVal === "0")
    //first emplty that '0'
    displayVal = "";
  // if displayVal is not '0' You concatenate the new clicked number
  displayVal += btnText;
  //Display in the html
  displayValElement.innerText = displayVal;
};

//create events listener to execute updateDisplayVal function each calc-btn-num
for (let i = 0; i < calcNumBtns.length; i++) {
  calcNumBtns[i].addEventListener("click", updateDisplayVal, false);
}

var performOperation = (clickObj) => {
  var operator = clickObj.target.innerText;
  // switch is used to perform different actions based on different conditions
  switch (operator) {
    case "+":
      // use  pendingval to keep the displayval
      pendingVal = displayVal;
      // clear the displayval
      displayVal = "0";
      displayValElement.innerHTML = displayVal;
      // push the pendingval to the evalstringarray
      evalStringArray.push(pendingVal);
      //push + to the evalstringarray
      evalStringArray.push("+");
      break;

    case "-":
      pendingVal = displayVal;
      displayVal = "0";
      displayValElement.innerHTML = displayVal;
      evalStringArray.push(pendingVal);
      evalStringArray.push("-");

      break;

    case "x":
      pendingVal = displayVal;
      displayVal = "0";
      displayValElement.innerHTML = displayVal;
      evalStringArray.push(pendingVal);
      evalStringArray.push("*");
      break;

    case "÷":
      pendingVal = displayVal;
      displayVal = "0";
      displayValElement.innerHTML = displayVal;
      evalStringArray.push(pendingVal);
      evalStringArray.push("/");
      break;

    case "=":
      //console.log(displayVal);
      evalStringArray.push(displayVal);

      console.log(displayVal);
      console.log(pendingVal);
      console.log(evalStringArray);

      var evaluation = eval(evalStringArray.join(" "));

      displayVal = evaluation;
      //display the result back to the html
      displayValElement.innerHTML = displayVal;
      //clear the array
      evalStringArray = [];
      break;
  }
};

// for each of the elements in the [calc-btn-operator] execcute performOperator
for (let i = 0; i < calcOperatorBtns.length; i++) {
  calcOperatorBtns[i].addEventListener("click", performOperation, false);
}

clearBtn.onclick = () => {
  displayVal = "0";
  pendingVal = undefined;
  evalStringArray = [];
  displayValElement.innerHTML = displayVal;
};

backspaceBtn.onclick = () => {
  //let is the block scope variable
  let lengthOfDisplayVal = displayVal.length;
  //use  the slice function to get the substring starting at [ , )
  displayVal = displayVal.slice(0, lengthOfDisplayVal - 1);

  if (displayVal === "") displayVal = "0";
  displayValElement.innerText = displayVal;
};

decimalBtn.onclick = () => {
  if (!displayVal.includes(".")) displayVal += ".";

  displayValElement.innerText = displayVal;
};
