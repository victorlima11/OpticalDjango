document.addEventListener('DOMContentLoaded', function() {
    // Obter os elementos de filtro
    const tipoSelect = document.getElementById('filtro-tipo');
    const marcaSelect = document.getElementById('filtro-marca');
    const generoSelect = document.getElementById('filtro-genero');
    const produtos = document.querySelectorAll('.produto-card');

    // Função de filtro
    function aplicarFiltro() {
        const tipoFiltro = tipoSelect.value.trim().toLowerCase();
        const marcaFiltro = marcaSelect.value.trim().toLowerCase();
        const generoFiltro = generoSelect.value.trim().toLowerCase();

        // Filtrando os produtos
        produtos.forEach(produto => {
            const tipo = produto.dataset.tipo ? produto.dataset.tipo.trim().toLowerCase() : "";
            const marca = produto.dataset.marca ? produto.dataset.marca.trim().toLowerCase() : "";
            const genero = produto.dataset.genero ? produto.dataset.genero.trim().toLowerCase() : "";

            // Verificar se o produto corresponde aos filtros
            const tipoMatch = !tipoFiltro || tipo === tipoFiltro;
            const marcaMatch = !marcaFiltro || marca === marcaFiltro;
            const generoMatch = !generoFiltro || genero === generoFiltro;

            // Mostrar ou esconder o produto
            if (tipoMatch && marcaMatch && generoMatch) {
                produto.style.display = "block"; // Exibe o produto
            } else {
                produto.style.display = "none"; // Esconde o produto
            }
        });
    }

    // Adicionar eventos de mudança nos selects
    tipoSelect.addEventListener('change', aplicarFiltro);
    marcaSelect.addEventListener('change', aplicarFiltro);
    generoSelect.addEventListener('change', aplicarFiltro);

    // Inicializar o filtro ao carregar a página
    aplicarFiltro();
});
