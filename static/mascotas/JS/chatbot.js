 // === REFERENCIAS A ELEMENTOS DEL DOM ===
    const chatToggle = document.getElementById("chatToggle");
    const chatContainer = document.getElementById("chatContainer");
    const closeChat = document.getElementById("closeChat");
    const messages = document.getElementById("messages");
    const userInput = document.getElementById("userInput");
    const sendBtn = document.getElementById("sendBtn");

    /* === FUNCIÓN: agregar mensaje al área === */
    function addMessage(text, sender) {
      const div = document.createElement("div");
      div.classList.add("message", sender);
      div.innerHTML = text.replace(/\n/g, '<br>');  // ← Esta línea mágica
      messages.appendChild(div);
      messages.scrollTop = messages.scrollHeight;
    }

    /* === RESPUESTAS SIMPLES DEL BOT === */
    function botResponse(input) {
      const pregunta = String(input).toLowerCase().trim();
      
      if (pregunta.includes("objetivo") || pregunta === "1") {
        return "El objetivo del Family Pets es ayudar a encontrar un segundo hogar a esas mascotas que no tuvieron mucha fortuna encontrando un hogar y ayudar a las fundaciones a financiar gastos para animales rescatados. 🏠🐾";
        
      } else if (pregunta.includes("tecnologias") || pregunta.includes("tecnologías") || pregunta === "2") {
        return "En tecnologías incluimos:\n• Django + Python (backend)\n• HTML/CSS/JS (frontend)\n• Registro y formularios para solicitudes de mascotas y ayudas\n• Base de datos SQL para gestionar usuarios y mascotas";
        
      } else if (pregunta.includes("integracion") || pregunta.includes("integración") || pregunta === "3") {
        return "Combinamos integraciones de:\n• JS, HTML y CSS para uso intuitivo\n• Django templates con {% include %} para reutilizar componentes\n• Archivos estáticos (CSS/JS) con {% static %}\n• URLs y vistas Django para navegación fluida";
        
      } else if (pregunta.includes("adoptar") || pregunta === "4") {
        return "Para la adopción debes seguir los siguientes pasos:\n\n" +
              "1. Si no estás registrado, hazlo en LOGIN / REGISTER\n" +
              "2. Dirígete a VER MASCOTAS para explorar\n" +
              "3. Elige tu mascota y haz clic en ADOPTAR\n" +
              "4. Diligencia el formulario\n" +
              "5. Espera contacto de la fundación 🐶";
              
      } else if (pregunta.includes("salir") || pregunta === "0") {
        return "¡Gracias por conversar! Éxitos en tu proyecto Family Pets. 👋🐾";
        
      } else {
        return "Escribe: \"objetivo\" (1), \"tecnologías\" (2), \"integración\" (3), \"adoptar\" (4) o \"salir\" (0)";
      }
    }


    /* === FUNCIÓN: enviar mensaje del usuario === */
    function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    // DEBUG SIMPLE
    console.log('Usuario escribió:', `'${text}'`);

    addMessage(text, "user");
    userInput.value = "";
    
    const respuesta = botResponse(text);
    console.log('Bot responde:', respuesta);  // ← Esto te dice qué está pasando
    setTimeout(() => addMessage(respuesta, "bot"), 400);
  }


    /* === EVENTOS === */

    // Abrir / cerrar chatbot al hacer clic en la burbuja
    chatToggle.addEventListener("click", () => {
      chatContainer.classList.add("active");
      userInput.focus();
    });

    // Cerrar chatbot y limpiar historial de mensajes
    closeChat.addEventListener("click", () => {
      chatContainer.classList.remove("active");
      messages.innerHTML = ""; // limpia mensajes automáticamente
    });

    // Botón enviar
    sendBtn.addEventListener("click", sendMessage);

    // Enviar con tecla Enter
    userInput.addEventListener("keypress", (e) => {
      if (e.key === "Enter") sendMessage();
    });
    /*************************************************************************
     * Inicialización: añadir mensaje de bienvenida (opcional)
     *************************************************************************/
    (function init() {
      // Mensaje inicial del bot - multi-línea y contextual
      addMessage('¡Hola! 🐾 Soy el asistente de Family Pets', 'bot');
      addMessage('Escoge una opcion o escribe la palabra para ayudarte', 'bot');
      addMessage('1 "objetivo" - ¿Qué es Family Pets?', 'bot');
      addMessage('2 "tecnologías" - Stack técnico usado', 'bot');
      addMessage('3 "integración" - Cómo funciona el proyecto', 'bot');
      addMessage('4 "adoptar" - Proceso de adopción', 'bot');
      addMessage('¿En qué te ayudo primero? 😊', 'bot');
    })();