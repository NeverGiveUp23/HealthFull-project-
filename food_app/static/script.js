

// search.addEventListener('input', e =>{
//   console.log(e.input.value)
// })

import API_KEY from "./apikey";


// function search(e){
//   e.preventDefault();
//   var searchForm = document.getElementById('searchForm')
//   var form = new FormData(searchForm);
// console.log(searchForm)

function search() {
  let ingr = document.querySelector("#foodSearch");
  let servings = document.querySelector('#servings');
  // if(amount.value.length < 1){
  fetch(`https://api.edamam.com/api/food-database/v2/parser?app_id=${API_TOKEN}&app_key=${API_KEY}&ingr=${ingr.value}%20${servings.value}&nutrition-type=logging`)

    .then(res => {
      return res.json();
    })
    .then(data => {

      // setting result  for ID FOOD in HTML//
      var food = document.querySelector('#food')
      food.value = `${data.hints[0].food.label}`;

      console.log(food.value)


      var amount = document.querySelector('#amount')
      amount.value = `${data.parsed[0].quantity}`;
      console.log(amount.value)
      // ========== END OF FOOD VALUE ===========

      // SETTING CALORIES FOR THE P TAG IN HTML
      let calories = document.querySelector('#calories');

      // Assigning cal to the API results
      const cal = Math.floor(data.hints[0].food.nutrients.ENERC_KCAL);
      // multiply the cal with the serving servings value to populate the serving result
      let calPerServing = cal * servings.value;

      // ACCESSING THE DATA IN THE API TO GET CALORIES

      calories.value = `${calPerServing}`;

      console.log(data)
      //========  END OF CALORIES DATA ===========

      // SETTING PROTIEN IN THE API

      const pro = Math.ceil(data.hints[0].food.nutrients.PROCNT);

      let proPerServing = pro * servings.value;

      let protien = document.querySelector('#protien')
      protien.value = `${proPerServing}`



      const carb = Math.floor(data.hints[0].food.nutrients.CHOCDF);

      let carbPerServing = carb * servings.value;

      let carbs = document.querySelector('#carbs')
      carbs.value = `${carbPerServing}`


      const date = new Date();
      document.querySelector('#date').innerHTML = date.toDateString();






    })
    .catch(err => {
      console.log('Error');
      console.log(err);
    })


}


// Notes
function addShadow(element) {
  element.classList.add("shadow");
}

function removeShadow(element) {
  element.classList.remove("shadow");
}




// let dayCal = document.querySelector('#dayCal');
// let totCal = document.querySelector('#totCal');
// let remCal = document.querySelector('#remCal');

// let counter = 0
// setInterval(() => {
// if(counter === dayCal.innerHTML - totCal.innerHTML){
//     clearInterval();
//   }
//   else if(){

//   }
//   else {
//     counter++;
//     remCal.innerHTML = counter;
//   }
// }, 20);
// console.log(remCal)

