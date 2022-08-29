const form = document.getElementById('formulario');
const codeSelector = document.getElementById('codigo')

const selectOptions = {
    CADS: libros[0],
    ECNTQLE: libros[1],
    HP: libros[2],
    ERDG: libros[3],
    DQM: libros[4],
    EP: libros[5],
    EMMDO: libros[6],
    LTH: libros [7]
}

codeSelector.addEventListener('change', () =>{
    if(selectOptions[codeSelector.value]){
        const tituloForm = document.getElementById('titulo');
        const autorForm = document.getElementById('autor');
        const estanteForm = document.getElementById('estante');

        const { autor, titulo, estante } = selectOptions[codeSelector.value];

        tituloForm.value = titulo
        autorForm.value = autor
        estanteForm.value = estante

        window.localStorage.clear()
    }
    else{
        const tituloForm = document.getElementById('titulo');
        const autorForm = document.getElementById('autor');
        const estanteForm = document.getElementById('estante');


        tituloForm.value = ''
        autorForm.value = ''
        estanteForm.value = ''
    }
})

form.addEventListener('submit', (e)=>{
    e.preventDefault()
})