// estilos/circulo.js

function drawCirculo(ctx, analyser, dataArray, canvas, colorPicker, colorMode) {
    const cx = canvas.width / 2;
    const cy = canvas.height / 2;
    const radius = 150;
    const bars = dataArray.length;

    // Círculo base
    ctx.beginPath();
    ctx.arc(cx, cy, radius, 0, 2 * Math.PI);
    ctx.strokeStyle = '#3a3560';
    ctx.lineWidth = 2;
    ctx.stroke();

    for (let i = 0; i < bars * 2; i++) {
        const index = i < bars ? i : (bars * 2 - 1) - i;
        const angle = (i / (bars * 2)) * (2 * Math.PI) - Math.PI / 2;
        const barLength = Math.max(dataArray[Math.abs(index)] * 0.8, 3);

        const x1 = cx + Math.cos(angle) * radius;
        const y1 = cy + Math.sin(angle) * radius;
        const x2 = cx + Math.cos(angle) * (radius + barLength);
        const y2 = cy + Math.sin(angle) * (radius + barLength);

        let color;
        if (colorMode.value === 'solid') {
            color = colorPicker.value;
        } else if (colorMode.value === 'multicolor') {
            const hue = (i / (bars * 2)) * 360;
            color = `hsl(${hue}, 80%, 60%)`;
        } else if (colorMode.value === 'intensidad') {
            const valor = dataArray[Math.abs(index)];
            const hue = Math.round((valor / 255) * 260);
            color = `hsl(${hue}, 90%, 55%)`;
        }

        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.stroke();
    }
}