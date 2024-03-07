function estimate() {
    // Récupérer les valeurs des champs du formulaire
    var Gender = document.getElementById("gender").value;
    var Married = document.getElementById("Married").value;
    var Education = document.getElementById("Education").value;
    var Applicant_Income = parseFloat(document.getElementById("ApplicantIncome").value);
    var Credit_History = parseInt(document.getElementById("Credit_History").value);

    // Envoyer les données au serveur Flask pour prédiction
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            Gender: Gender,
            Married: Married,
            Education: Education,
            Applicant_Income: Applicant_Income,
            Credit_History: Credit_History,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Afficher le résultat au client
        document.getElementById("estimation").textContent = 'The Estimation : ' + data.estimation ;
        document.getElementById("result").style.display = 'block';

        // Réinitialiser les champs du formulaire
        document.getElementById("gender").value = '';
        document.getElementById("Married").value = '';
        document.getElementById("Education").value = '';
        document.getElementById("ApplicantIncome").value = '';
        document.getElementById("sim_type").value = '';
        document.getElementById("Credit_History").value = '';
    })
    .catch(error => console.error("Erreur lors de l'estimation :", error));
}
