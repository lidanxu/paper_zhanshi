
$(function () {
var chart = c3.generate({
    bindto: '#combine-chart',
    data: {
        columns: [
            ['data1', 1617, 1607, 1565, 1565, 1392, 1333,1554],
            ['data2', 7448, 7560, 7073, 7397, 7174, 7278,8160],
            ['data3', 9065,9167,8638,8962,8566,8611,9714],
        ],
        types: {
            data1: 'bar',
            data2: 'bar',
            data3: 'spline',
           
        },
    },
    axis: {
        x: {
            type: 'categorized'
        }
    }
});

});
 
