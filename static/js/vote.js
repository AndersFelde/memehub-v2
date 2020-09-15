function vote(uploadId, btn) {
    if (btn.id.includes("d")) {
        btnType = 0;
    } else {
        btnType = 1;
    }
    convertActive(btn, btnType)

    $.post("/api/voter", {
        "uploadId": uploadId,
        "btnType": btnType
    }, function (data) {
        if (data["Error"]) {
            btn.classList.remove("active")
        }
    });
}

function convertActive(clickedBtn, btnType) {
    idBtn = clickedBtn.id;
    if (btnType == 0) {
        otherBtn = document.getElementById(idBtn.replace("d", "u"));
    } else {
        otherBtn = document.getElementById(idBtn.replace("u", "d"));
    }


    if (clickedBtn.classList.contains("active")) {
        clickedBtn.classList.remove("active");
    } else {
        clickedBtn.classList.add("active");
        if (otherBtn.classList.contains("active")) {
            otherBtn.classList.remove("active");
        }
    }
}