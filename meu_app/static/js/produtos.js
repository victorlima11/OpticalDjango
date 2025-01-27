document.addEventListener('DOMContentLoaded', function() {
    
    const tipoSelect = document.getElementById('filtro-tipo');
    const marcaSelect = document.getElementById('filtro-marca');
    const generoSelect = document.getElementById('filtro-genero');
    const produtos = document.querySelectorAll('.produto-card');

    
    function aplicarFiltro() {
        const tipoFiltro = tipoSelect.value.trim().toLowerCase();
        const marcaFiltro = marcaSelect.value.trim().toLowerCase();
        const generoFiltro = generoSelect.value.trim().toLowerCase();

        
        produtos.forEach(produto => {
            const tipo = produto.dataset.tipo ? produto.dataset.tipo.trim().toLowerCase() : "";
            const marca = produto.dataset.marca ? produto.dataset.marca.trim().toLowerCase() : "";
            const genero = produto.dataset.genero ? produto.dataset.genero.trim().toLowerCase() : "";

            
            const tipoMatch = !tipoFiltro || tipo === tipoFiltro;
            const marcaMatch = !marcaFiltro || marca === marcaFiltro;
            const generoMatch = !generoFiltro || genero === generoFiltro;

            
            if (tipoMatch && marcaMatch && generoMatch) {
                produto.style.display = "block"; 
            } else {
                produto.style.display = "none"; 
            }
        });
    }

    
    tipoSelect.addEventListener('change', aplicarFiltro);
    marcaSelect.addEventListener('change', aplicarFiltro);
    generoSelect.addEventListener('change', aplicarFiltro);

    
    aplicarFiltro();
});
