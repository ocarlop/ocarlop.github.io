function createObserver() {
  let observer;
  observer = new IntersectionObserver(entries => {
      entries.forEach((entry) => {
        const player = entry.target.querySelector('.playlist-card');
        console.log(player);
        if (entry.isIntersecting) {
          player.classList.add('player-animation');
        return;
        }
        player.classList.remove('player-animation');
      })
  });
  observer.observe(element);
}

window.addEventListener("DOMContentLoaded", (event) => {
  element = document.querySelector("#playerContainer");
  createObserver();
}, false);