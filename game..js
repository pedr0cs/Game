document.addEventListener('keydown', function(e) {
    let dx = 0, dy = 0;
    if (e.key === 'ArrowLeft' || e.key === 'a') dx = -10;
    if (e.key === 'ArrowRight' || e.key === 'd') dx = 10;
    if (e.key === 'ArrowUp' || e.key === 'w') dy = -10;
    if (e.key === 'ArrowDown' || e.key === 's') dy = 10;

    if (dx !== 0 || dy !== 0) {
        fetch(`http://localhost:5000/move/${dx}/${dy}`)
            .then(res => res.json())
            .then(pos => {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.fillRect(pos.x, pos.y, 30, 30);
            });
    }
});g
