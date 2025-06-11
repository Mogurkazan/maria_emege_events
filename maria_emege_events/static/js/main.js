document.addEventListener("DOMContentLoaded", () => {
  const fadeIns = document.querySelectorAll(".fade-in");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target); // para que no se reanime
        }
      });
    },
    {
      threshold: 0.1,
    }
  );

  fadeIns.forEach((el) => observer.observe(el));
});
