

// search.addEventListener('input', e =>{
//   console.log(e.input.value)
// })


// function search(e){
//   e.preventDefault();
//   var searchForm = document.getElementById('searchForm')
//   var form = new FormData(searchForm);
// console.log(searchForm)

// calling the data from api
function search(event){
  event.preventDefault();
  var searchForm = document.getElementById('searchForm');
  var form = new FormData(searchForm);

  fetch('http://127.0.0.1:5000/call_api', {method: 'POST', body: form})
   .then(res => {
    return res.json()
  })
   .then(data => {
    searchData(data);
})
.catch(err => {
  console.log('something went wrong')
  console.log(err)
})
}

function searchData(data) {


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

      // SETTING PROTIEN IN THE API==============

      const pro = Math.ceil(data.hints[0].food.nutrients.PROCNT);

      let proPerServing = pro * servings.value;

      let protien = document.querySelector('#protien')
      protien.value = `${proPerServing}`


// ============ Carb ================
      const carb = Math.floor(data.hints[0].food.nutrients.CHOCDF);

      let carbPerServing = carb * servings.value;

      let carbs = document.querySelector('#carbs')
      carbs.value = `${carbPerServing}`

// =========== date to string ==============
      const date = new Date();
      document.querySelector('#date').innerHTML = date.toDateString();



    }



// Notes
function addShadow(element) {
  element.classList.add("shadow");
}

function removeShadow(element) {
  element.classList.remove("shadow");
}


// Chart Js ==========================
const ctx = document.getElementById('myChart');

// id for first chart in goal page
let chartGoal = document.getElementById('goalCalChart');
let currCal = document.getElementById('caloriesCountChart');
let remCal = document.getElementById('remainingChart');
let chartText = document.getElementById('textChart');
let btnChart = document.getElementById('chartBtn');




if(chartGoal.innerHTML == 0){
  currCal.innerHTML = 0;
  remCal.innerHTML = 0;
  chartText.innerHTML = "Create A Goal"
}else {
  btnChart.remove()
} 

if(remCal.innerHTML < 0 ){
  chartText.innerHTML = "Better Luck Next time"
}


  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ["Today's Goal", 'Current Calorie Count', 'Remaining Calories'],
      datasets: [{
        label: 'Goal Calorie Tracker',
        labels: ["Today's Goal", 'Current Calorie Count', 'Remaining Calories'],
        data: [chartGoal.innerHTML, currCal.innerHTML, remCal.innerHTML],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });





// // ==============api key ================
// let url = "https://api.edamam.com/api/food-database/v2/parser?app_id=YOUR_APP_ID&app_key=YOUR_APP_KEY&ingr=" + ingr.value + "%20" + servings.value + "&nutrition-type=logging";