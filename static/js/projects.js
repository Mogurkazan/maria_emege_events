document.addEventListener("DOMContentLoaded", function () {
  console.log("✅ Swiper JS está corriendo y el DOM ya está cargado");

  const swiper = new Swiper("#main-swiper", {
    slidesPerView: 1.1,
    spaceBetween: 20,
    centeredSlides: true,
    loop: true,
    grabCursor: true,

    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    scrollbar: {
      el: ".swiper-scrollbar",
    },
    effect: "coverflow",
    coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 100,
      modifier: 2.5,
      slideShadows: false,
    },
    breakpoints: {
      768: {
        slidesPerView: "auto",
      },
    },
  });
});
