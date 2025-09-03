document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll(".card-title").forEach(function(el) {
    let text = el.textContent || el.innerText;

    text = text.replace(/\s+/g, " ").trim();

    let noSpaces = text.replace(/\s/g, "");
    if (noSpaces.length > 30) {
      let count = 0;
      let result = "";
      for (let char of text) {
        if (char !== " ") count++;
        result += char;
        if (count >= 30) break;
      }
      text = result.trim() + "…";
    }

    el.textContent = text;
  });
});