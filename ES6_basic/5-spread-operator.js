export default function concatArrays(array1, array2, string) {
    const ListaFinal = [...array1, ...array2, ...string];
    return ListaFinal
}