// Funciones globales para la aplicación

function mostrarFeedback(mensaje, tipo) {
    const modalHtml = `
        <div class="modal fade" id="feedbackGlobalModal" tabindex="-1">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">${tipo === 'success' ? '¡Bien!' : 'Información'}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <div class="alert alert-${tipo}">${mensaje}</div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                    </div>
                </div>
            </div>
        </div>
    `;
    const modalContainer = document.createElement('div');
    modalContainer.innerHTML = modalHtml;
    document.body.appendChild(modalContainer);
    const modal = new bootstrap.Modal(modalContainer.querySelector('.modal'));
    modal.show();
    modalContainer.addEventListener('hidden.bs.modal', () => modalContainer.remove());
}

function normalizarTexto(texto) {
    return texto.toLowerCase().trim().replace(/[¿?¡!]/g, '').replace(/\s+/g, ' ');
}

function cargarProgresoFlashcards() {
    const progreso = localStorage.getItem('progresoFlashcards');
    return progreso ? JSON.parse(progreso) : { vistas: {}, dominadas: {}, dificiles: {} };
}

function guardarProgresoFlashcards(progreso) {
    localStorage.setItem('progresoFlashcards', JSON.stringify(progreso));
}

function cargarProgresoEjercicios() {
    const progreso = localStorage.getItem('progresoEjercicios');
    return progreso ? JSON.parse(progreso) : {};
}

function guardarProgresoEjercicios(progreso) {
    localStorage.setItem('progresoEjercicios', JSON.stringify(progreso));
}

window.mostrarFeedback = mostrarFeedback;
window.normalizarTexto = normalizarTexto;
window.cargarProgresoFlashcards = cargarProgresoFlashcards;
window.guardarProgresoFlashcards = guardarProgresoFlashcards;
window.cargarProgresoEjercicios = cargarProgresoEjercicios;
window.guardarProgresoEjercicios = guardarProgresoEjercicios;
