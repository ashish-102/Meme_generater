const imagefile = document.getElementById("up-img");
const canvas = document.getElementById("canvas-page");
const toptext = document.getElementById("text-1");
const centertext = document.getElementById("text-2");
const bottomtext = document.getElementById("text-3");
const topcolor = document.getElementById("color1");
const centercolor = document.getElementById("color2");
const bottomcolor = document.getElementById("color3");

let image;

imagefile.addEventListener("change", (e) => {
    const imageurl = URL.createObjectURL(e.target.files[0])

    image = new Image();
    image.src = imageurl;

    image.addEventListener(
        "load",
        () => {
            updatecanvaspage(canvas, image, toptext.value, centertext.value, bottomtext.value, topcolor.value, centercolor.value, bottomcolor.value);
        },
        { once: true }
    );
});



toptext.addEventListener("change", () => {
    updatecanvaspage(canvas, image, toptext.value, centertext.value, bottomtext.value, topcolor.value, centercolor.value, bottomcolor.value);
});

topcolor.addEventListener("change", () => {
    updatecanvaspage(canvas, image, toptext.value, centertext.value, bottomtext.value, topcolor.value, centercolor.value, bottomcolor.value);
});



centertext.addEventListener("change", () => {
    updatecanvaspage(canvas, image, toptext.value, centertext.value, bottomtext.value, topcolor.value, centercolor.value, bottomcolor.value);
});

centercolor.addEventListener("change", () => {
    updatecanvaspage(canvas, image, toptext.value, centertext.value, bottomtext.value, topcolor.value, centercolor.value, bottomcolor.value);
});



bottomtext.addEventListener("change", () => {
    updatecanvaspage(canvas, image, toptext.value, centertext.value, bottomtext.value, topcolor.value, centercolor.value, bottomcolor.value);
});

bottomcolor.addEventListener("change", () => {
    updatecanvaspage(canvas, image, toptext.value, centertext.value, bottomtext.value, topcolor.value, centercolor.value, bottomcolor.value);
});


function updatecanvaspage(canvas, image, top, center, bottom, colortop, colorcenter, colorbottom) {
    const ctx = canvas.getContext("2d");
    const width = image.width;
    const height = image.height;
    const fontSize = Math.floor(width / 12)
    const yOffset = height / 25;


    // update image on canvas
    canvas.width = width;
    canvas.height = height;
    ctx.drawImage(image, 0, 0)

    // text config
    ctx.strokeStyle = "black";
    // ctx.lineWidth = Math.floor(fontSize / 10)
    // ctx.fillStyle = colortop;
    ctx.textAlign = "center";
    ctx.lineJoin = "round";
    ctx.font = `${fontSize}px sans-serif`;


    // Add top text
    ctx.textBaseline = "top";
    ctx.strokeText(top, width / 2, yOffset);
    ctx.fillStyle = colortop;
    ctx.fillText(top, width / 2, yOffset);


    // Add bottom text
    ctx.textBaseline = "center";
    ctx.strokeText(center, width / 2, height / 2);
    ctx.fillStyle = colorcenter;
    ctx.fillText(center, width / 2, height / 2);

    // Add bottom text
    ctx.textBaseline = "bottom";
    ctx.strokeText(bottom, width / 2, height - yOffset);
    ctx.fillStyle = colorbottom;
    ctx.fillText(bottom, width / 2, height - yOffset);

}





function save() {
    document.getElementById('imageData').value = canvas.toDataURL();
    document.forms["memeform"].submit();
}