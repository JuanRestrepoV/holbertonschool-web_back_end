export default function taskBlock(trueOrFalse) {
    var task = false;
    var task2 = true;
  
    if (trueOrFalse) {
      /* eslint-disable */
      const task = true;
      const task2 = false;
      /* eslint-disable */
    }
  
    return [task, task2];
  }
  