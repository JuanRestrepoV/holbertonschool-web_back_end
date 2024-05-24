export default function createEmployeesObject(departmentName, employees) {
  const employe = {};
  employe[departmentName] = employees;
  return employe;
}