/* ==== FUNCIÓN PARA MOSTRAR / OCULTAR CAMPOS ==== */

// Capturamos elementos del DOM
const tipoUsuario = document.getElementById("tipo");     // Selector
const fundacionExtra = document.getElementById("fundacionExtra"); // Campo extra

// Escuchamos el cambio en el selector
tipoUsuario.addEventListener("change", function() {
  if (tipoUsuario.value === "fundacion") {
    // Si selecciona fundación, mostramos el campo
    fundacionExtra.style.display = "block";
  } else {
    // Si selecciona usuario normal, lo ocultamos
    fundacionExtra.style.display = "none";
  }
});
