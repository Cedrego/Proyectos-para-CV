//----------------------------------------------------------------------//
//Variables
const fileInput = document.getElementById('fileInput');
const audioPlayer = document.getElementById('audioPlayer');
const canvas = document.getElementById('canvas');
//Apartado para los controles de reproducción y volumen
const playButton = document.getElementById('playButton');
const pauseButton = document.getElementById('pauseButton');
const stopButton = document.getElementById('stopButton');
const volumeSlider = document.getElementById('volumeSlider');
const colorPicker = document.getElementById('colorPicker');
const colorMode = document.getElementById('colorMode');
const estiloSelector = document.getElementById('estiloSelector');
    // Medidas del canvas
    canvas.width = 800;
    canvas.height = 800;
    const ctx = canvas.getContext('2d');

    // Centro del círculo
    const cx = canvas.width / 2;
    const cy = canvas.height / 2;
    const radius = 150; // radio del círculo base
    // Con "let" para poder reasignarlas después
    let audioCtx = null;
    let analyser = null;
    let source = null;
    let dataArray = null;
    let sourceCreated = false;
    // Botones deshabilitados hasta que haya canción
    playButton.disabled = true;
    pauseButton.disabled = true;
    stopButton.disabled = true;

    // input que esté escuchando el evento change, es decir, que ejecute la función cada vez que el usuario selecciona un archivo
fileInput.addEventListener('change', function(e) {
    const file = e.target.files[0];
    //Si por alguna razón no hay archivo
    if (!file) return;
    //Crea una URL temporal en memoria del navegador que apunta al archivo
    const url = URL.createObjectURL(file);
    //Le asigna esa URL al elemento <audio> del HTML
    audioPlayer.src = url;
    if (!audioCtx) {
        // Solo se crea la primera vez

        // Asignamos el contexto de audio (el motor que analiza el sonido)
        audioCtx = new AudioContext();
        // Asignamos el analizador
        analyser = audioCtx.createAnalyser();
        analyser.fftSize = 256; // 256 / 2 = 128 barras de frecuencia

        // Conectamos el audio al analizador y el analizador a la salida (parlantes)
        source = audioCtx.createMediaElementSource(audioPlayer);
        source.connect(analyser);
        analyser.connect(audioCtx.destination);

        // Array donde se guardan los datos de frecuencia en cada frame
        dataArray = new Uint8Array(analyser.frequencyBinCount);
        draw();
    } else {
        // Las siguientes veces solo reanudamos el contexto
        audioCtx.resume();
    }
    //Reproduce el audio.
    audioPlayer.play();

    playButton.disabled = false;
    pauseButton.disabled = false;
    stopButton.disabled = false;

    draw();
});
// Play
    playButton.addEventListener('click', function() {
        if (audioPlayer.src) {
            audioCtx.resume(); // reactiva el contexto si estaba suspendido
            audioPlayer.play();
        }
    });

    // Pausa
    pauseButton.addEventListener('click', function() {
        audioPlayer.pause();
    });

    // Stop — pausa y vuelve al inicio
    stopButton.addEventListener('click', function() {
        audioPlayer.pause();
        audioPlayer.currentTime = 0;
    });

    // Volumen
    volumeSlider.addEventListener('input', function() {
        audioPlayer.volume = volumeSlider.value;
    });

    function draw() {
    requestAnimationFrame(draw);
    if (!analyser) return;

    analyser.getByteFrequencyData(dataArray);
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Llama al estilo activo
    const estilo = estiloSelector.value;
    if (estilo === 'circulo') drawCirculo(ctx, analyser, dataArray, canvas, colorPicker, colorMode);
    if (estilo === 'barras')  drawBarras(ctx, analyser, dataArray, canvas, colorPicker, colorMode);
    if (estilo === 'ola')    drawOla(ctx, analyser, dataArray, canvas, colorPicker, colorMode);
    if (estilo === 'particulas') drawParticulas(ctx, analyser, dataArray, canvas, colorPicker, colorMode);
}

