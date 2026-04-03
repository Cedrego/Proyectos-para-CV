function drawOla(ctx, analyser, dataArray, canvas, colorPicker, colorMode) {
    const { width, height } = canvas;
    const NUMBER_OF_NODES = 24;

    // Fade en vez de clearRect
    ctx.globalAlpha = 0.15;
    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, width, height);
    ctx.globalAlpha = 1;

    const w = width / NUMBER_OF_NODES;
    const escala = 0.5; // ← controla qué tan alto llegan las olas

    // Colores según el modo
    let colorIzq, colorDer;
    if (colorMode.value === 'solid') {
        colorIzq = colorPicker.value;
        colorDer = colorPicker.value;
    } else if (colorMode.value === 'multicolor') {
        colorIzq = '#FD12EA';
        colorDer = '#FD9413';
    } else if (colorMode.value === 'intensidad') {
        const avg = dataArray.reduce((a, b) => a + b, 0) / dataArray.length;
        const hue = Math.round((avg / 255) * 260);
        colorIzq = `hsl(${hue}, 90%, 55%)`;
        colorDer = `hsl(${hue + 40}, 90%, 55%)`;
    }

    // --- Ola izquierda ---
    ctx.beginPath();
    ctx.moveTo(-20, height);
    for (let i = 0; i < NUMBER_OF_NODES; i += 2) {
        const x1 = i * w;
        const y1 = height - height * escala * (dataArray[i] / 255);
        const x2 = (i + 1) * w;
        const y2 = height - height * escala * (dataArray[i + 1] / 255);
        ctx.quadraticCurveTo(x1, y1, x2, y2);
    }
    ctx.lineTo(width + 20, height);
    ctx.closePath();
    ctx.fillStyle = colorIzq;
    ctx.strokeStyle = colorIzq;
    ctx.lineWidth = 3;
    ctx.globalAlpha = 0.2;
    ctx.fill();
    ctx.globalAlpha = 0.8;
    ctx.stroke();

    // --- Ola derecha espejada ---
    ctx.beginPath();
    ctx.moveTo(width + 20, height);
    for (let i = 0; i < NUMBER_OF_NODES; i += 2) {
        const x1 = width - i * w;
        const y1 = height - height * escala * (dataArray[i] / 255);
        const x2 = width - (i + 1) * w;
        const y2 = height - height * escala * (dataArray[i + 1] / 255);
        ctx.quadraticCurveTo(x1, y1, x2, y2);
    }
    ctx.lineTo(-20, height);
    ctx.closePath();
    ctx.fillStyle = colorDer;
    ctx.strokeStyle = colorDer;
    ctx.lineWidth = 3;
    ctx.globalAlpha = 0.2;
    ctx.fill();
    ctx.globalAlpha = 0.8;
    ctx.stroke();

    ctx.globalAlpha = 1;
}