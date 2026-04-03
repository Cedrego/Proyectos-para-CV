// estilos/barras.js

function drawBarras(ctx, analyser, dataArray, canvas, colorPicker, colorMode) {
    const bars = dataArray.length;
    const barWidth = canvas.width / bars;

    for (let i = 0; i < bars; i++) {
        const barHeight = dataArray[i] * 1.5;
        const x = i * barWidth;
        const y = canvas.height - barHeight;

        let color;
        if (colorMode.value === 'solid') {
            color = colorPicker.value;
        } else if (colorMode.value === 'multicolor') {
            const hue = (i / bars) * 360;
            color = `hsl(${hue}, 80%, 60%)`;
        } else if (colorMode.value === 'intensidad') {
            const hue = Math.round((dataArray[i] / 255) * 260);
            color = `hsl(${hue}, 90%, 55%)`;
        }

        ctx.fillStyle = color;
        ctx.fillRect(x, y, barWidth - 1, barHeight);
    }
}