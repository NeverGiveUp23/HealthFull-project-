// id's for chart in dashboard page
const ctx2 = document.getElementById('myChart2');
let calGroup = document.getElementById('groupCal').innerHTML;
let carbGroup = document.getElementById('groupCarb').innerHTML;
let proGroup = document.getElementById('groupPro').innerHTML;
let servGroup = document.getElementById('groupServ').innerHTML;

  new Chart(ctx2, {
    type: 'doughnut',
    data: {
      labels: ['Total Servings', "Total Calories", 'Total Carbs', 'Total Protien'],
      datasets: [{
        label: 'Goal Calorie Tracker',
        labels: ["Total Servings", 'Total Calories', 'Total Protien', 'Total Carbs'],
        data: [servGroup,calGroup, carbGroup, proGroup],
        borderWidth: 1,
        hoverOffset: 15
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
// Retrieve the numbers representing the months and the total number of calories for each month from the 

// id's for chart in dashboard page
const ctx3 = document.getElementById('myChart3');
let calMonth = document.querySelectorAll('.monthDate');
let calTotalMonth = document.querySelectorAll('.monthCal');

  let labels = getMonth();
  function getMonth(){
    let labels = []
    for(let i = 0; i < calMonth.length; i++){
      labels.push(calMonth[i].innerHTML);
    }
    return labels;
  }


  let data = getCalorie();
  function getCalorie(){
    let data = []
    for(let j = 0; j < calTotalMonth.length; j++){
      data.push(calTotalMonth[j].innerHTML);
    }
    return data;
  }


  new Chart(ctx3, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Monthly Calorie Amount',
        labels: ["Total Calories"],
        data: data,
        borderWidth: 1,
        hoverOffset: 15
      }]
    },
    options: {
      indexAxis : 'y',
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

