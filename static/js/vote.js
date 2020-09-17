function vote(uploadId, btn) {
    if (btn.id.includes("d")) {
        btnType = 0;
        btnLetter = "d";
        otherBtnLetter = "u";
    } else {
        btnType = 1;
        btnLetter = "u";
        otherBtnLetter = "d";
    }
    convertActive(btn, btnType, btnLetter, uploadId)

    $.post("/api/voter", {
        "uploadId": uploadId,
        "btnType": btnType
    }, function (data) {
        if (data["Error"]) {
            btn.classList.remove("active-vote");
        }
    });
}

function convertActive(clickedBtn, btnType, btnLetter, uploadId) {
    idBtn = clickedBtn.id;
    if (btnType == 0) {
        otherBtn = document.getElementById(idBtn.replace("d", "u"));
    } else {
        otherBtn = document.getElementById(idBtn.replace("u", "d"));
    }


    if (clickedBtn.classList.contains("active-vote")) {
        clickedBtn.classList.remove("active-vote");
        clickedDiv = document.getElementById(btnLetter + "Count-" + uploadId)
        clickedDiv.innerHTML = parseInt(clickedDiv.innerHTML) - 1;
    } else {
        clickedBtn.classList.add("active-vote");
        clickedDiv = document.getElementById(btnLetter + "Count-" + uploadId)
        clickedDiv.innerHTML = parseInt(clickedDiv.innerHTML) + 1;
        if (otherBtn.classList.contains("active-vote")) {
            otherDiv = document.getElementById(otherBtnLetter + "Count-" + uploadId)
            otherDiv.innerHTML = parseInt(otherDiv.innerHTML) - 1;
            otherBtn.classList.remove("active-vote");
        }
    }
}