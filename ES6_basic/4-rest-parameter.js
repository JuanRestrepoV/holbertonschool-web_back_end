export default function returnHowManyArguments(...Args) {
  let numberOfParameters = 0;
  /* eslint-disable */
  for (const arg of Args) {
    numberOfParameters += 1;
  }
  /* eslint-disable */
  return numberOfParameters;
  console.log(numberOfParameters)
}
