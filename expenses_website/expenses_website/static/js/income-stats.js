let currentChartType = "doughnut";
let myChart;

const renderChart = (data, labels) => {
  const ctx = document.getElementById("myChart").getContext("2d");
  if (myChart) {
    myChart.destroy();
  }
  myChart = new Chart(ctx, {
    type: currentChartType,
    data: {
      labels: labels,
      datasets: [
        {
          label: "Last month's income",
          data: data,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      title: {
        display: true,
        text: "income per source",
      },
    },
  });
};

const getChartData = () => {
  console.log("fetching");
  fetch("/income/income_source_sumarry")
    .then((res) => res.json())
    .then((results) => {
      console.log("results", results);
      const source_data = results.income_source_data;
      const [labels, data] = [
        Object.keys(source_data),
        Object.values(source_data),
      ];

      renderChart(data, labels);
    })
    .catch((error) => console.error("Error fetching data:", error));
};

const toggleChartType = () => {
  const chartTypes = ["doughnut", "bar", "line", "pie"];
  let currentIndex = chartTypes.indexOf(currentChartType);
  currentIndex = (currentIndex + 1) % chartTypes.length;
  currentChartType = chartTypes[currentIndex];
  getChartData();
};

document.addEventListener("keydown", (event) => {
  if (event.code === "Space") {
    event.preventDefault();
    toggleChartType();
  }
});

document.addEventListener("DOMContentLoaded", getChartData);
