let obj = {
  1: 1,
  2: 2,
  3: 3,
};

let len = Object.keys(obj).length;
obj.g = "HHH";
let len2 = Object.keys(obj).length;
console.log(len2, "OBJ LEN");
