// Use Morris.Area instead of Morris.Line
Morris.Donut({
    element: 'graph-donut',
    data: [
        {value: 33.10, label: 'answer num=0', formatted: 'approx. 33.10%' },
        {value: 66.36, label: 'answer num~[1,99] ', formatted: 'approx. 66.36%' },
        {value: 0.47, label: 'answer num~[100,499] ', formatted: 'approx. 0.47%' },
        {value: 0.07, label: 'answer_num>=500', formatted: 'approx. 0.07%' }
    ],
    backgroundColor: false,
    labelColor: '#fff',
    colors: [
        '#6a8bc0','#4acacb','#fe8676','#5ab6df'
    ],
    formatter: function (x, data) { return data.formatted; }
});


$(function() {

    var d1 = [
        [0, 601],
        [1, 620],
        [2, 437],
        [3, 361],
        [4, 549],
        [5, 618],
        [6, 570],
        [7, 758],
        [8, 658],
        [9, 538],
        [10, 488]

    ];
    var d2 = [
        [0, 401],
        [1, 520],
        [2, 337],
        [3, 261],
        [4, 449],
        [5, 518],
        [6, 470],
        [7, 658],
        [8, 558],
        [9, 438],
        [10, 388]
    ];

    var data = ([{
        label: "New Visitors",
        data: d1,
        lines: {
            show: true,
            fill: true,
            fillColor: {
                colors: ["rgba(255,255,255,.4)", "rgba(183,236,240,.4)"]
            }
        }
    },
        {
            label: "Unique Visitors",
            data: d2,
            lines: {
                show: true,
                fill: true,
                fillColor: {
                    colors: ["rgba(255,255,255,.0)", "rgba(253,96,91,.7)"]
                }
            }
        }
    ]);

    var options = {
        grid: {
            backgroundColor:
            {
                colors: ["#ffffff", "#f4f4f6"]
            },
            hoverable: true,
            clickable: true,
            tickColor: "#eeeeee",
            borderWidth: 1,
            borderColor: "#eeeeee"
        },
        // Tooltip
        tooltip: true,
        tooltipOpts: {
            content: "%s X: %x Y: %y",
            shifts: {
                x: -60,
                y: 25
            },
            defaultTheme: false
        },
        legend: {
            labelBoxBorderColor: "#000000",
            container: $("#main-chart-legend"), //remove to show in the chart
            noColumns: 0
        },
        series: {
            stack: true,
            shadowSize: 0,
            highlightColor: 'rgba(000,000,000,.2)'
        },
//        lines: {
//            show: true,
//            fill: true
//
//        },
        points: {
            show: true,
            radius: 3,
            symbol: "circle"
        },
        colors: ["#5abcdf", "#ff8673"]
    };
    var plot = $.plot($("#main-chart #main-chart-container"), data, options);
});
