// Estilos/particulas.js

// Las partículas se crean una sola vez y se reusan
let particles = null;

function initParticulas(canvas) {
    particles = [];
    for (let i = 0; i < 100; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            radius: Math.random() * 5 + 2,
            speedX: Math.random() * 2 - 1,
            speedY: Math.random() * 2 - 1,
        });
    }
}

function drawParticulas(ctx, analyser, dataArray, canvas, colorPicker, colorMode) {
    const { width, height } = canvas;

    // Inicializa las partículas la primera vez
    if (!particles) initParticulas(canvas);

    // Fade en vez de clearRect
    ctx.fillStyle = 'rgba(13, 13, 13, 0.2)';
    ctx.fillRect(0, 0, width, height);

    analyser.getByteFrequencyData(dataArray);

    const avgVolume = dataArray.reduce((acc, val) => acc + val, 0) / dataArray.length;
    const volumeNorm = avgVolume / 255;
    const baseSize = 5 + volumeNorm * 50;

    particles.forEach(p => {
        // Movimiento
        p.x += p.speedX;
        p.y += p.speedY;

        // Rebote en los bordes
        if (p.x < 0 || p.x > width)  p.speedX *= -1;
        if (p.y < 0 || p.y > height) p.speedY *= -1;

        // Reactividad al audio
        const audioIndex = Math.floor((p.x / width) * dataArray.length);
        const audioValue = dataArray[audioIndex] / 255;
        p.radius = baseSize * audioValue * 2;

        // Color según el modo
        let color;
        if (colorMode.value === 'solid') {
            color = colorPicker.value;
        } else if (colorMode.value === 'multicolor') {
            color = `hsl(${audioValue * 360}, 100%, 50%)`;
        } else if (colorMode.value === 'intensidad') {
            const hue = Math.round((audioValue) * 260);
            color = `hsl(${hue}, 90%, 55%)`;
        }

        ctx.beginPath();
        ctx.fillStyle = color;
        ctx.globalAlpha = audioValue * 0.8;
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();
    });

    ctx.globalAlpha = 1;
}