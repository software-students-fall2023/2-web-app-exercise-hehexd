const themeSwitch = document.getElementById("themeSwitch");

themeSwitch.addEventListener("change", () => {
    document.body.classList.toggle("night-mode", themeSwitch.checked);
    localStorage.setItem("theme", themeSwitch.checked ? "night" : "day");
});

const savedTheme = localStorage.getItem("theme");
if (savedTheme) {
    document.body.classList.toggle("night-mode", savedTheme === "night");
    themeSwitch.checked = savedTheme === "night";
}