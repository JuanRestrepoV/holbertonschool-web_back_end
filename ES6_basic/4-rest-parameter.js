export default function returnHowManyArguments(...Args) {
    let numberOfParameters = 0
    for (const arg of Args) {
        numberOfParameters += 1;
    }
    return numberOfParameters;
    console.log(numberOfParameters)
}