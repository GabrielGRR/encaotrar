// Função para alternar entre os cards "lost" e "found"
function toggleCards(category) {
    // Oculta todos os cards de ambas as categorias
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => card.classList.add('hidden'));
    
    // Exibe apenas os cards da categoria selecionada
    const selectedCards = document.querySelectorAll(`.${category}`);
    selectedCards.forEach(card => card.classList.remove('hidden'));
}