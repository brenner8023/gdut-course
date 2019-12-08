/* 
 * Gdut-Course
 * Created by brenner 2019-12-08
*/

let fs = require('fs'),
    fsPromises = fs.promises;

let baseDir = '../../public/',
    result = [];

fsPromises.readdir(baseDir)
    .then((data) => {
        data.forEach((item, idx) => {
            let data2 = fs.readdirSync(baseDir + item);
            result.push({name: item, children: data2});
        });
        return result;
    })
    .then((res) => {
        res = 
`
/* 
 * Gdut-Course
 * Created by brenner 2019-12-08
*/

;(function($) {
    $.data = ${JSON.stringify(res)};
})(new Function("return this")());
`;
        fsPromises.writeFile('./db.js', res).then(() => {
            console.log("success");
        }).catch((err) => {
            console.log(err);
        });
    });