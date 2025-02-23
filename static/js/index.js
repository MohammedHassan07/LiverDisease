document.getElementById("prediction-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    fetch("/predict", {
        method: "POST",
        body: JSON.stringify(data),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(result => {
        console.log(result)
        document.getElementById("prediction-result").textContent = result.prediction;
        
        // Set image based on prediction
        if (result.prediction === "Disease Detected") {
            document.getElementById("img").src = "/static/images/sad.png";
        } else {
            document.getElementById("img").src = "/static/images/happy.png";
        }

        // Show dialog
        document.getElementById("dialog").style.display = "block";
        document.getElementById("dialog-overlay").style.display = "block";
    });
});

// Close dialog
document.getElementById("close-btn").addEventListener("click", function() {
    document.getElementById("dialog").style.display = "none";
    document.getElementById("dialog-overlay").style.display = "none";
});