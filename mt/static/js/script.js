document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript подключен и работает!");

    // Подтверждение перед удалением брони
    let deleteButtons = document.querySelectorAll(".delete-btn");
    deleteButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            if (!confirm("Вы уверены, что хотите удалить эту бронь?")) {
                event.preventDefault();
            }
        });
    });

    // Фильтр доступных столиков по дате
    let dateInput = document.getElementById("date-filter");
    let tableRows = document.querySelectorAll(".table-row");

    if (dateInput) {
        dateInput.addEventListener("change", function () {
            let selectedDate = this.value;
            tableRows.forEach(row => {
                let reservationDate = row.getAttribute("data-date");
                if (reservationDate !== selectedDate) {
                    row.style.display = "none";
                } else {
                    row.style.display = "";
                }
            });
        });
    }
});
