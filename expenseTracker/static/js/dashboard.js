// SIDEBAR OPEN AND CLOSE IMPLEMENTATION
const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#hamburger");
const closeBtn = document.querySelector("#close-btn");

menuBtn.addEventListener("click", () => {
  sideMenu.style.left = "0";
});

closeBtn.addEventListener("click", () => {
  sideMenu.style.left = "-100%";
});


// SIDEBAR NAVLINKS ACTIVE IMPLEMENTATION
// var sidebarLinks = document.querySelectorAll('.sidebar a');

// sidebarLinks.forEach(function(link) {
//   link.addEventListener('click', function(e) {
//     e.preventDefault(); 

//     sidebarLinks.forEach(function(link) {
//       link.classList.remove('active');
//     });

//     this.classList.add('active');
//   });
// });




// INCOME DOUGHNUT CHART
const incomeChartData = {
    labels: ["Salary", "Sales Revenue", "Royalties", "Investment", "Other"],
    data: [300, 120, 100, 40, 22],
};

const myChart1 = document.querySelector('.chart1');

new Chart(myChart1, {
    type: "doughnut",
    data: {
        labels: incomeChartData.labels,
        datasets: [
            {
                label: "Income",
                data: incomeChartData.data,
            }
        ]
    },

    options: {
        borderWidth: 4,
        borderRadius: 1.5,
        hoverBorderWidth: 0,
        plugins: {
            legend: {
                display: false,
            }
        }
    }
});


// EXPENSES DOUGHNUT CHART
const expensesChartData = {
    labels: ["Payroll", "Supplies", "Insurance", "Utilities", "Research"],
    data: [95, 12, 100, 190, 20],
};

const myChart2 = document.querySelector('.chart2');

new Chart(myChart2, {
    type: "doughnut",
    data: {
        labels: expensesChartData.labels,
        datasets: [
            {
                label: "Income",
                data: expensesChartData.data,
            }
        ]
    },

    options: {
        borderWidth: 4,
        borderRadius: 1.5,
        hoverBorderWidth: 0,
        plugins: {
            legend: {
                display: false,
            }
        }
    }
});



// INCOME DOUGHNUT CHART
const walletChartData = {
    labels: ["Research Dept", "Managers", "Tech Dept", "Employees", "PR Team", "Staff"],
    data: [55, 33, 74, 82, 9, 63],
};

const myChart3 = document.querySelector('.chart3');

new Chart(myChart3, {
    type: "doughnut",
    data: {
        labels: walletChartData.labels,
        datasets: [
            {
                label: "Income",
                data: walletChartData.data,
            }
        ]
    },

    options: {
        borderWidth: 4,
        borderRadius: 1.5,
        hoverBorderWidth: 0,
        plugins: {
            legend: {
                display: false,
            }
        }
    }
});


// LINE GRAPH

var ctx2 = document.querySelector('.line-chart').getContext('2d');

var gradientStroke1 = ctx2.createLinearGradient(0, 230, 0, 50);

gradientStroke1.addColorStop(1, 'rgba(203,12,159,0.2)');
gradientStroke1.addColorStop(0.2, 'rgba(72,72,176,0.0)');
gradientStroke1.addColorStop(0, 'rgba(203,12,159,0)');

var gradientStroke2 = ctx2.createLinearGradient(0, 230, 0, 50);

gradientStroke2.addColorStop(1, 'rgba(20,23,39,0.2)');
gradientStroke2.addColorStop(0.2, 'rgba(72,72,176,0.0)');
gradientStroke2.addColorStop(0, 'rgba(20,23,39,0)');

    new Chart(ctx2, {
      type: "line",
      data: {
        labels: ["Apr", "May", "Jun", "Jul", "Aug", "Sep"],
        datasets: [{
            label: "Income",
            tension: 0.4,
            borderWidth: 0,
            pointRadius: 0,
            borderColor: "#cb0c9f",
            borderWidth: 3,
            backgroundColor: gradientStroke1,
            fill: true,
            data: [50, 40, 300, 220, 500, 250],
            maxBarThickness: 6

          },
          {
            label: "Expenses",
            tension: 0.4,
            borderWidth: 0,
            pointRadius: 0,
            borderColor: "#9381ff",
            borderWidth: 3,
            backgroundColor: gradientStroke2,
            fill: true,
            data: [30, 90, 40, 140, 290, 290, 340, 230, 400],
            maxBarThickness: 6
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        aspectRatio: 2,
        plugins: {
          legend: {
            display: false,
          }
        },
        interaction: {
          intersect: false,
          mode: 'index',
        },
        scales: {
          y: {
            grid: {
              drawBorder: false,
              display: true,
              drawOnChartArea: true,
              drawTicks: false,
              borderDash: [5, 5]
            },
            ticks: {
              display: true,
              padding: 10,
              color: '#b2b9bf',
              font: {
                size: 12,
                family: "poppins",
                style: 'normal',
                lineHeight: 2
              },
            }
          },
          x: {
            grid: {
              drawBorder: false,
              display: false,
              drawOnChartArea: false,
              drawTicks: false,
              borderDash: [5, 5]
            },
            ticks: {
              display: true,
              color: '#b2b9bf',
              padding: 20,
              font: {
                size: 12,
                family: "poppins",
                style: 'normal',
                lineHeight: 2
              },
            }
          },
        },
      },
    });